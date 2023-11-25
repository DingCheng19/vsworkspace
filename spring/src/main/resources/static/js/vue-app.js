// src/main/resources/static/js/vue-app.js

new Vue({
    el: '#app',
    data: {
        question: '',
        answer: ''
    },
    methods: {
        askQuestion: function () {
            // Simulate a backend API call (replace with actual API call)
            // In a real-world scenario, you would send an AJAX request to the server.
            // Here, we are just simulating it with a timeout.
            setTimeout(() => {
                this.answer = 'This is the answer to your question: ' + this.question;
            }, 1000);
        }
    }
});