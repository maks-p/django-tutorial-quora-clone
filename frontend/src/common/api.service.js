import { CSRF_TOKEN } from "./csrf_token.js";

const getJSON = async (response) => {
	if (response.status === 204) return "";
	return response.json();
};

const apiService = (endpoint, method, data) => {
	const config = {
		method: method || GET,
		body: data !== undefined ? JSON.stringify(data) : null,
		headers: {
			"content-type": "applicaiton/json",
			"X-CSRFTOKEN": CSRF_TOKEN,
		},
	};

	return fetch(endpoint, config)
		.then(getJSON)
		.catch((error) => console.log(error));
};

export { apiService };
