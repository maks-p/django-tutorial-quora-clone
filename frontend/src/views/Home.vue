<template>
  <div class="home">
    <div class="container">
        <div v-for="question in questions"
            :key="question.pk">
            <p class="mb-0">Posted by:
                <span class="question-author-name">{{ question.author }}</span>
            </p>
            <h2>
                <router-link
                    :to="{ name: 'question', params: { slug: question.slug } }"
                    class="question-link"
                >{{ question.content }}
                </router-link>
            </h2>
            <p>Answers: {{ question.answers_count }}</p>
            <hr>
        </div>
    </div>
  </div>
</template>

<script>
import { apiService } from '../common/api.service.js'

export default {
  name: "home",
  data() {
    return {
        questions: []
    }
  },
  methods: {
    getQuestions() {
        let endpoint = 'api/questions/';
        apiService(endpoint)
            .then(data => {
                this.questions.push(...data.results)
            })
    }
  },
  created() {
    this.getQuestions()
    document.title = "Quora Clone"
  }
};
</script>

<style scoped>
    .question-author-name {
        color: grey;
    }
    .question-link {
        font-weight: bold;
        color: teal;
    }
    .question-link:hover {
        color: rgb(98, 143, 143);
        text-decoration: none;
    }
</style>