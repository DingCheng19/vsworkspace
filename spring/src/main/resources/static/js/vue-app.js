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
            // setTimeout(() => {
            //     this.answer = 'This is the answer to your question: ' + this.question;
            // }, 1000);
            const apiUrl = '/api/hello';
            const postData = {
                token: 'exampleUser',
                question: 'examplePassword',
            };

            // 创建 Request 对象
            const request = new Request(apiUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json', // 设置请求体类型为 JSON
                    // 可以添加其他的请求头，如认证信息等
                },
                body: JSON.stringify(postData), // 将 JavaScript 对象转换为 JSON 字符串
            });

            // 创建 Request 对象
            const request2 = new Request(apiUrl, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json', // 设置请求体类型为 JSON
                    // 可以添加其他的请求头，如认证信息等
                }
            });

            fetch(request2)
                .then(response => {
                    if (!response.ok) {
                        throw new Error(`HTTP error! Status: ${response.status}`);
                    }
                    return response.text(); // 返回的是一个 Promise
                })
                .then(data => {
                    // 处理 JSON 数据
                    console.log('JSON Data:', data);
                })
                .catch(error => {
                    // 处理错误
                    console.error('Error fetching data:', error);
                });
        }
    }
});