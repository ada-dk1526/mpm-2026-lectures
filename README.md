# Modern Programming Methods (MPM)

In this module you will acquire essential skills for developing software in a robust and professional manner. You will learn to compose software for sustainable and reproducible research, carry out test-driven software development and integration and develop software using a version control system. These skills will be developed through creating software using the Python programming language. Further, you will learn to distinguish different sources of errors in software and create tests for these errors. You will also be introduced to the foundations of language models (how modern AI tools generate text and code) and to cloud-based services for collaborative software development and continuous integration.

## Learning outcomes

On successful completion of this module, you will be able to:
1. Design software for sustainable and reproducible research.
2. Build software using test-driven development and continuous integration.
3. Develop software using a version control system.
4. Create software using the Python programming language.
5. Assess different sources of errors in science and engineering software and create tests for these errors.
6. Explain the use of cloud computing technologies for computational and data science.

## Module content

The module will cover the following topics:
1. **Software version control:** This is necessary to maintain a detailed record of software as it is developed, including how to work collaboratively. While the skills are portable across many software version control systems, this module will use git with GitHub.
2. **Software packaging, test-driven development and continuous integration:** Software is structured and packaged for reuse and distribution, development is planned around the tests that can be written to ensure correctness, and version control is integrated with automated testing, run on cloud-based services, to monitor software health on a continuous basis.
3. **Programming in Python:** You will be taught how to program in Python and how to use a range of Python modules to perform compute-intensive and data-intensive tasks.
4. **Introduction to language models:** Starting from the elementary notion of a function, you will build up the idea of a probabilistic model that predicts text, gaining a functional understanding of how large language models and AI coding assistants work, and a foundation for their effective and responsible use.

## Preparation

The pre-sessional material, which should be reviewed in preparation for this module and the ACSE MSc in general, can be found [here](https://ese-msc.github.io/preinduction/acse/markdown/ACSEIntro.html#before-the-course-starts). Instructions for configuring your computer for this module can be found [here](https://github.com/ese-ada-lovelace-2026/laptop-setup).

All of the lecture material runs in the `mpm2026` conda environment, which is defined by the `environment.yml` file in this repository. The laptop setup instructions walk you through creating it. In short, from the top level of this repository run
```
conda env create -f environment.yml
conda activate mpm2026
```
If the environment is updated during the module, rebuild your copy from scratch (the most reliable way to match the file exactly):
```
conda deactivate
conda env remove -n mpm2026 -y
conda env create -f environment.yml
```

You must also complete the College's online course "An Introduction to Generative AI for Students". It supports the responsible use of AI in academic work. Completing it is a mandatory requirement of this module, but it is not assessed and does not contribute to your grade.

## Lecture schedule

|Date                       | Lecture                                                | Instructor                  | Material                 |
|---------------------------|--------------------------------------------------------|-----------------------------|--------------------------|
|05-10-2026 Mon 9:00-12:00+ | GitHub and Python environments                         | Rhodri Nelson               | [Lecture01](Lecture01)   |
|06-10-2026 Tue 9:00-12:00  | NumPy and SciPy                                        | Rhodri Nelson               | [Lecture02](Lecture02)   |
|07-10-2026 Wed 9:00-12:00  | Code profiling and optimisation                        | Marijan Beg                 | [Lecture03](Lecture03)   |
|08-10-2026 Thu 9:00-12:00  | Debugging and testing                                  | Rhodri Nelson               | [Lecture04](Lecture04)   |
|09-10-2026 Fri 9:00-17:00  | Coding Without (and with) AI - Mock Coding Assignment (Unassessed)++ | Rhodri Nelson |                    |
|12-10-2026 Mon 9:00-12:00  | Python packaging and continuous integration            | Marijan Beg & Rhodri Nelson | [Lecture05](Lecture05)   |
|13-10-2026 Tue 9:00-12:00  | Introduction to small language models                  | Rhodri Nelson               | [Lecture06](Lecture06)   |
|14-10-2026 Wed 9:00-12:00  | Floating point arithmetic                              | Marijan Beg                 | [Lecture07](Lecture07)   |
|15-10-2026 Thu 9:00-12:00  | Pandas                                                 | Tom Davison                 | [Lecture08](Lecture08)   |
|16-10-2026 Fri             | No lecture - coursework submission (11:00) and consolidation test (14:00-15:30) | |                   |

+For the first lecture, it's probable that presentation of the material will continue into the afternoon session.

++Requirements of the Mock Coding Assignment will be discussed in detail at 09:00 on the Friday. This is designed to be a fun and informal day of coding to prepare you for the formal assessment the following week and also those of future courses! Submissions will be tested against a suite of in-house tests and a personal feedback report provided. To re-iterate, this will be an **unassessed** submission.

Morning sessions are lectures, and the afternoon sessions are practicals in which you work through the lecture's exercises and problem sheets. Each lecture also comes with a short multiple-choice self-check quiz covering its main points (`quiz.ipynb` in the lecture's folder; open it and click an option under each question). Complete it before you start the lecture's main problem sheet, or any part of the coursework that relies on that lecture's material. The answers, with explanations, are released afterwards so that you can check your own. The quizzes are formative (unassessed), but they are also good preparation for the multiple-choice part of the consolidation test.

## Assessment

Assessment consists of two linked components of equal weight:

|Component                          | Weighting | Release                             | Due / held                                   |
|-----------------------------------|-----------|-------------------------------------|----------------------------------------------|
|1. Package-development coursework  | 50%       | 13-10-2026 Tue, following the lecture | Code submission: 16-10-2026 Fri, 11:00     |
|2. Consolidation test              | 50%       |                                     | 16-10-2026 Fri, 14:00-15:30, rooms 1.51 and 301E |

Component 1 is an independent, unsupervised coding assignment on numerical package development. It will be distributed and submitted via GitHub.

Component 2 is a 90-minute, closed-book, in-class test that builds directly on your coursework. It consists of multiple-choice questions that apply the principles taught in the lectures to your own submission, and open-ended questions asking you to explain your implementation. Because the test refers back to your own coursework, its marking cannot be fully anonymous.

**The consolidation test will take place between 14:00 and 15:30 on Friday the 16th of October 2026. The class will be split between rooms 1.51 and 301E.**

Further details will be provided when the coursework is released.
