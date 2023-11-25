package com.example.dc.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import com.example.dc.model.QuestionRequestEntity;

@RestController
@RequestMapping("/api")
public class HelloController {
    @GetMapping("/hello")
    public String hello() {
        return "Hello, World!";
    }

    @PostMapping("/create")
    public String create(@RequestBody QuestionRequestEntity questionRequest) {
        // Logic to handle POST request
        String token = questionRequest.getToken();
        String question = questionRequest.getQuestion();

        return "Object created successfully!";
    }
}
