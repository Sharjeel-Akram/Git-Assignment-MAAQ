# Git-Assignment-MAAQ
**GitFlow Process:**<br>
Gitflow is a widely recognized and popular branching model and workflow that provides a structured approach to managing the development of software projects. Gitflow is built on top of the Git version control system, which allows multiple developers to work on a project concurrently while maintaining a clean and organized codebase. This workflow defines a set of branching strategies and guidelines, making it easier for teams to manage different aspects of software development, such as feature development, bug fixes, and release management. <br>

**Steps to follow:**<br>

1. First, I have initialized an empty local repository using command **git init**
2. Secondly, I added a remote repository with it so that whatever I do, I can push it to my remote repository using **git remote add origin https://github.com/Sharjeel-Akram/Git-Assignment-MAAQ.git/**
3. Third, I made a pull request so that I can make changes to repository and branches using **git pull -v origin main**
4. After this, to check in which branch I am working, I used the command **git branch -a**. I was in the master branch, and there was another branch, remotes/origin/main, which was not being used till now, and it was the main branch where all other branches would be merged.
5. After that, I made a branch named Development Branch.<br> ![image](https://github.com/Sharjeel-Akram/Git-Assignment-MAAQ/assets/65490295/915ce01f-f63d-45be-8458-55fdd2fb8530)
6. using command **git branch -a** I can see all the branches that I made. <br>![image](https://github.com/Sharjeel-Akram/Git-Assignment-MAAQ/assets/65490295/c9c32308-2094-4c25-bfb4-e06f2cc2a5ce)
7. I made two more branches in the development branch, named feature-branch1 and feature-branch2. <br>![image](https://github.com/Sharjeel-Akram/Git-Assignment-MAAQ/assets/65490295/d935f29b-80a6-4b2e-bd49-1e2c2542e18a)
8. Now I have to build a file in feature-branch1 and commit it.
9. As you can see in the picture, I have added two files, but I have not made a commit till now.<br> ![image](https://github.com/Sharjeel-Akram/Git-Assignment-MAAQ/assets/65490295/5c00ec93-75a4-4590-86f3-00ce72dac99f)
10. Now that I have added them in the stagging area, these still need to be committed.<br> ![image](https://github.com/Sharjeel-Akram/Git-Assignment-MAAQ/assets/65490295/ce1c764c-dad6-469b-b152-b0864af5fd5b)
11. Now the first task has been committed to feature-branch1. <br>![image](https://github.com/Sharjeel-Akram/Git-Assignment-MAAQ/assets/65490295/32f3080f-3fe4-48f1-b2b2-797a1fe68f66)
12. Now I have to do the same task for feature-branch2, which means that I have worked on two separate branches, and then I will merge them into a single branch.
13. The below picture shows the complete work done in feature-branch2. <br> ![image](https://github.com/Sharjeel-Akram/Git-Assignment-MAAQ/assets/65490295/03c46e79-3c3e-4823-9b9a-7029edac09ce)
14. Now I have both branches pushed to a remote repository for pull requests. <br> ![image](https://github.com/Sharjeel-Akram/Git-Assignment-MAAQ/assets/65490295/2b28d520-6fbc-4957-9543-1b32ea2dfd8a)
15. I have switched to the development branch and merged both branches, feature-branch1 and feature-branch2, into the development branch. <br>![image](https://github.com/Sharjeel-Akram/Git-Assignment-MAAQ/assets/65490295/2e7b15a1-3930-4083-9d4d-596b07b5a518)
16. Now I will also push that development branch to my remote repository. <br> ![image](https://github.com/Sharjeel-Akram/Git-Assignment-MAAQ/assets/65490295/69cf9bc2-44ac-4f9a-afc3-6d8c31e5ada5)
17. I merged the development branch into the master branch, added a third task in master branch and then pushed the master branch to remote. <br> ![image](https://github.com/Sharjeel-Akram/Git-Assignment-MAAQ/assets/65490295/5e35d412-609e-4311-9688-eefb6b1e2146) <br> ![image](https://github.com/Sharjeel-Akram/Git-Assignment-MAAQ/assets/65490295/22eac573-7660-44ee-a48e-2bfb32efd2e7)
18. The below picture shows the log of my activity. <br> ![image](https://github.com/Sharjeel-Akram/Git-Assignment-MAAQ/assets/65490295/8ad8e2c1-aa92-4e52-a7f8-2f0ce6f6170d)
19. At the end, I have merged the master branch with the main branch and pushed it to my remote repository. <br> ![image](https://github.com/Sharjeel-Akram/Git-Assignment-MAAQ/assets/65490295/3e6f8581-9603-471f-af6c-0ea8ba39cf8e)
20. If you look at the picture below, you can clearly see the tree of branches that are made and merged with other branches. <br> ![image](https://github.com/Sharjeel-Akram/Git-Assignment-MAAQ/assets/65490295/acdeb33f-0868-4248-8040-c0e78ee339c6)




 







