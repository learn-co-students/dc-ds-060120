
# Module 2 Final Project


## Introduction

In this lesson, we'll review all of the guidelines and specifications for the final project for Module 2.

## Objectives
You will be able to:

* Describe all required aspects of the final project for Module 2
* Describe all required deliverables
* Describe what constitutes a successful project

## Final Project Summary

Another module down--you're almost half way there!

![awesome](https://raw.githubusercontent.com/learn-co-curriculum/dsc-mod-2-project-v2-1/master/halfway-there.gif)

All that remains in Module 2 is to put our newfound data science skills to use with a final project! You should expect this project to take between 20 and 25 hours of solid, focused effort. If you're done way quicker, go back and dig in deeper or try some of the optional "level up" suggestions. If you're worried that you're going to get to 30 hrs and still not even have the data imported, reach out to an instructor in Slack ASAP to get some help!

## The Dataset

For this project, you'll be working with the King County House Sales dataset. We've modified the dataset to make it a bit more fun and challenging.  The dataset can be found in the file `"kc_house_data.csv"`, in this repo.

The description of the column names can be found in the column_names.md file in this repository. As with most real world data sets, the column names are not perfectly described, so you'll have to do some research or use your best judgment if you have questions relating to what the data means.

You'll clean, explore, and model this dataset with a multivariate linear regression to predict the sale price of houses as accurately as possible.

## The Deliverables

There will be several deliverables for this project:

1. A well documented **Executive Jupyter Notebook** containing any code you've written for this project and comments explaining it. This work will need to be pushed to your GitHub repository in order to submit your project.  
2. An organized **README.md** file in the GitHub repository that describes the contents of the repository. This file should be the source of information for navigating through the repository.
3. A short **Keynote/PowerPoint/Google Slides presentation** (delivered as a PDF export) giving a high-level overview of your methodology and recommendations for non-technical stakeholders. Make sure to also add and commit this pdf of your non-technical presentation to your repository with a file name of presentation.pdf.

### Executive Jupyter Notebook Must-Haves

For this project, your Jupyter Notebook should meet the following specifications:

#### Organization/Code Cleanliness

- The notebook is written for technical audiences with a way to both understand your approach and reproduce your results. The target audience for this deliverable is other data scientists looking to validate your findings.
- Well-organized, having distinct sections in logical sequence and with appropriate headings  
- Well-commented code, including doc-strings for functions
- Notebook can be run to generate same results. Includes setting random seeds & including referenced files in repository
- Text explains purpose of project and approach used and **decision making steps** throughout your project
- Utilizes code for data cleaning through functions built elsewhere
- Text explains **reasoning** behind analytic decisions
- Text **interprets results** of analyses

#### Visualizations & EDA

* Your project contains at least 4 meaningful data visualizations, with corresponding interpretations. All visualizations are well labeled with axes labels, a title, and a legend (when appropriate)  
* Your notebook should contain 1 - 2 paragraphs briefly explaining your approach to this project.

#### Model Quality/Approach
- Pose 3 or more questions that are relevant to the business problem and answer them through regression analysis
-  Runs 3 or more regression models, including justification for each model iteration
-  Interprets 3 or more coefficients and relates them to the problem context.
- Your notebook shows an iterative approach to modeling, and details the parameters and results of the model at each iteration.  
-  Whenever necessary, you briefly explain the changes made from one iteration to the next, and why you made these choices.  
-  You provide at least 1 paragraph explaining your final model.   


### Non-Technical Presentation Must-Haves

Another deliverable should be a Keynote, PowerPoint or Google Slides presentation delivered as a pdf file in your project repository with the file name of `presentation.pdf` detailing the results of your project.  Your target audience is non-technical people interested in using your findings to maximize their profit when selling their home.

Your presentation should:

* Contain between 5 - 10 professional-quality slides.  
    * **Level Up**: The slides should use visualizations whenever possible, and avoid walls of text.
* Take no more than 5 minutes to present.   
* Avoid technical jargon and explain the results in a clear, actionable way for non-technical audiences.   

**_Based on the results of your models, your presentation should discuss at least two concrete features that highly influence housing prices._**

## The Process 
The process for this project is identical to the process you followed for your module 1 project. We specified it again below as a refresher.

### 1. Getting Started

Please start by reviewing this document. If you have any questions, please ask them in Slack ASAP so (a) we can answer the questions and (b) so we can update this repository to make it clearer.

### 2. CRISP-DM Check-In pt.1 - Monday
You will meet with your instructors on Monday to “pitch” your project idea.  Be prepared to answer the following questions:

- What questions will you be addressing?
- What ways might you visualize this data to address the question?

You will meet with the instructors to discuss your progress on the project and your plan for the rest of the week to make sure you are on the right track.  We will be focusing on the steps of the CRISP-DM model.  Be prepared to answer the following questions.

- Business Understanding
   - Have you clearly defined your goal for your analysis?
   - Have your thought about who your audience is and how they would use this information?
   - How does this help the goals of the business/organization?
- Data Understanding
   - What data are you using?
   - How does your data help you answer the business question?
   - How many observations does your dataset contain?
   - What is the distribution of your data?
   - What data types do you have?   
- Data Preparation
   - Have you looked/dealt with missing values?
   - Have you done any data-type conversion?
      - ex: numerical data incorrectly ‘typed’ as strings.
    - Does your data contain any outliers or non-sensical values?
    
### 3. CRISP-DM Check-In pt.2 - Tuesday
- EDA/Visualization
   - What visualizations have you already made/planning to make?
   - What messages are these visualizations trying to convey?
   - What visualizations have you already made/planning to assess if your data meets the assumtions of linear regression?
   
- Modeling:
    - Is this a classification task? A regression task? Something else?
    - What models will we try?
    - How do we deal with overfitting?
    - Do we need to use regularization or not?
    - What sort of validation strategy will we be using to check that our model  - works well on unseen data?
    - What loss functions will we use?
    - What threshold of performance do we consider as successful?


- Evaluation:
    - How are you determining which variables are important.
    - What overall metric of success are you using.
    - What additional steps might you need to take to improve the model? (ex: transforming data, scaling data, getting more features) 
   
### 4. Instructor Check-In & MVP Deadline- Wednesday
You will meet with an  instructor who will check if the minimum requirements of the project are completed. At this point you should have your visualizations done and they should answer the business questions.  Following this meeting you should be ready to polish your notebook and work on your slidedeck.

### 5. Practice Presentations- Thursday
You will do a practice presentation with your class.  At this point your classmates and instructors will provide verbal feedback which can be incorportated in your final presentation.

### 6. Project Presentations- Friday
You will present your project to the class using your slidedeck.  This presentation should not take more than 5 minutes and should be directed towards a non-technical audience.  Both partners should participate in the presentation of the project.

## Groups

1. Dan & Sam
2. Clair Marie & Bobby
3. James & Michael
4. Jim & Alex
5. Nick, Jake, & Raven

## Submitting your Project

You’re almost done! In order to submit your project for review, please complete the Mod 2 Project Submission form in Canvas.

## Grading Rubric

The grading rubric for the project can be found [here](https://docs.google.com/spreadsheets/d/1o90NETo6ASfPrCnRiN6wyQ-XGj4lHZ6IyQDrWkuhmVQ/edit?usp=sharing).
## Summary

The end of module projects and project reviews are a critical part of the program. They give you a chance to both bring together all the skills you've learned into realistic projects and to practice key "business judgement" and communication skills that you otherwise might not get as much practice with.
