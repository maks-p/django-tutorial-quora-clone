import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import About from "../views/About.vue";
import Question from "../views/Question.vue";
import QuestionEditor from "../views/QuestionEditor.vue";

Vue.use(VueRouter);

const routes = [
	{
		path: "/",
		name: "home",
		component: Home,
	},
	{
		path: "/about",
		name: "about",
		component: About,
	},
	{
		path: "/questions/:slug",
		name: "question",
		component: Question,
		props: true,
	},
	{
		path: "/ask",
		name: "question-editor",
		component: QuestionEditor,
	},
];

const router = new VueRouter({
	mode: "history",
	//base: process.env.BASE_URL,
	routes,
});

export default router;
