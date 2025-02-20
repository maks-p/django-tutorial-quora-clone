<template>
  <div class="single-question mt-2">
    <div v-if="question" class="container">
      <h1>{{ question.content }}</h1>
      <QuestionActions v-if="isQuestionAuthor" :slug="question.slug" class="mt-2 mb-2" />
      <p class="mb-0">
        Posted by:
        <span class="author-name">{{ question.author }}</span>
      </p>
      <p class="mb-0">
        Created on:
        <span class="created-date">{{ question.created_at }}</span>
      </p>
      <hr />
      <div v-if="userHasAnswered">
        <p class="answer-added">You've answered this question!</p>
      </div>
      <div v-else-if="showForm">
        <form class="card" @submit.prevent="onSubmit">
          <div class="card-header px-3">
            <strong>Answer the Question</strong>
          </div>
          <div class="card-block">
            <textarea
              v-model="newAnswerBody"
              class="form-control"
              placeholder="Share your knowledge"
              row="7"
            ></textarea>
          </div>
          <div class="card-footer px-3">
            <button type="submit" class="btn btn-sm btn-success">Submit your Answer</button>
          </div>
        </form>
        <p v-if="error" class="error mt-2">{{ error }}</p>
      </div>
      <div v-else>
        <button class="btn btn-sm btn-success" @click="showForm = true">Answer the question</button>
      </div>
      <hr />
    </div>
    <div v-else>
      <h1 id="notfound">404 - Question Not Found</h1>
    </div>
    <div v-if="question" class="container">
      <AnswerComponent
        v-for="(answer, index) in answers"
        :answer="answer"
        :requestUser="requestUser"
        :key="index"
        @delete-answer="deleteAnswer"
      />
      <div class="my-4">
        <p v-show="loadingAnswers">...loading...</p>
        <button
          v-show="next"
          @click="getQuestionAnswers"
          class="btn btn-sm load-more"
        >Load More Answers</button>
      </div>
    </div>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
import AnswerComponent from "@/components/Answer.vue";
import QuestionActions from "@/components/QuestionActions.vue";

export default {
  name: "Question",
  props: {
    slug: {
      type: String,
      required: true
    }
  },
  components: {
    AnswerComponent,
    QuestionActions
  },
  data() {
    return {
      question: {},
      answers: [],
      next: null,
      loadingAnswers: false,
      newAnswerBody: null,
      error: null,
      userHasAnswered: false,
      showForm: false,
      requestUser: null
    };
  },
  computed: {
    isQuestionAuthor() {
      return this.question.author === this.requestUser;
    }
  },
  methods: {
    setPageTitle(title) {
      document.title = title;
    },

    setRequestUser() {
      this.requestUser = window.localStorage.getItem("username");
    },

    getQuestionData() {
      let endpoint = `/api/questions/${this.slug}/`;
      apiService(endpoint).then(data => {
        if (data) {
          this.question = data;
          this.userHasAnswered = data.user_has_answered;
          this.setPageTitle(data.content);
        } else {
          this.question = null;
          this.setPageTitle("404 - Page Not Found");
        }
      });
    },

    getQuestionAnswers() {
      let endpoint = `/api/questions/${this.slug}/answers/`;
      if (this.next) {
        endpoint = this.next;
      }
      this.loadingAnswers = true;
      apiService(endpoint).then(data => {
        this.answers.push(...data.results);
        this.loadingAnswers = false;
        if (data.next) {
          this.next = data.next;
        } else {
          this.next = null;
        }
      });
    },

    onSubmit() {
      if (this.newAnswerBody) {
        let endpoint = `/api/questions/${this.slug}/answer/`;
        apiService(endpoint, "POST", { body: this.newAnswerBody }).then(
          data => {
            this.answers.unshift(data);
          }
        );
        this.newAnswerBody = null;
        this.showForm = false;
        this.userHasAnswered = true;
        if (this.error) {
          this.error = null;
        }
      } else {
        this.error = "You can't send an empty answer!";
      }
    },

    async deleteAnswer(answer) {
      let endpoint = `/api/answers/${answer.id}/`;
      try {
        await apiService(endpoint, "DELETE");
        this.$delete(this.answers, this.answers.indexOf(answer));
        this.userHasAnswered = false;
      } catch (err) {
        console.log(err);
      }
    }
  },
  created() {
    this.getQuestionData();
    this.getQuestionAnswers();
    this.setRequestUser();
  }
};
</script>

<style scoped>
.author-name {
  color: grey;
}
.created-date {
  color: grey;
}
.answer-add {
  font-weight: bold;
  color: teal;
}
.btn-success {
  background-color: white;
  border: 2px solid teal;
  color: teal;
  font-weight: bold;
}
.error {
  font-weight: bold;
  color: red;
}

.answer-added {
  color: teal;
}
</style>