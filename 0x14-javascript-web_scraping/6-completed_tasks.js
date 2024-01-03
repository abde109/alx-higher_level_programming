#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function(err, response, body) {
    if(err){
        console.error(err);
    }else if (response.statusCode === 200){
        const todos = JSON.parse(body);
        const completed = {};
        todos.forEach(todo => {
            if (todo.completed === true) {
                if (completed[todo.userId] === undefined) {
                    completed[todo.userId] = 1;
                } else {
                    completed[todo.userId] += 1;
                }
            }
        });
        console.log(completed);
}});
