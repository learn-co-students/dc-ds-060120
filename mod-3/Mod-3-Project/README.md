
# Module 3 Final Project


## Introduction

In this lesson, we'll review all the guidelines and specifications for the final project for Module 3.


## Objectives

- Understand all required aspects of the Final Project for Module 3
- Understand all required deliverables
- Understand what constitutes a successful project

## Final Project Summary

Congratulations! You've made it through another _intense_ module, and now you're ready to show off your newfound Machine Learning skills!

![awesome](https://raw.githubusercontent.com/learn-co-curriculum/dsc-mod-3-project-v2-1/master/smart.gif)

All that remains for Module 3 is to complete the final project!

## The Project

The main goal of this project is to create a classification model. For this project you have to choose a data set from the curated list below.

For this project, you're going to select a dataset of your choosing and create a classification model. You'll start by identifying a problem you can solve with classification, and then identify a dataset. You'll then use everything you've learned about Data Science and Machine Learning thus far to source a dataset, preprocess and explore it, and then build and interpret a classification model that answers your chosen question.

### Choosing the data from the curated list

You will select one of the four data sets described below. Each comes with its own advantages and disadvantages, and, of course, its own associated business problem and stakeholders. It may be desirable to flesh out your understanding of the audience or the business proposition a little more than sketched out here.

1) [Chicago Car Crash Data](https://data.cityofchicago.org/Transportation/Traffic-Crashes-Crashes/85ca-t3if). Note this links also to [Vehicle Data](https://data.cityofchicago.org/Transportation/Traffic-Crashes-Vehicles/68nd-jvt3) and to [Driver/Passenger Data](https://data.cityofchicago.org/Transportation/Traffic-Crashes-People/u6pd-qa9d).

Build a classifier to predict the primary contributory cause of a car accident, given information about the car, the people in the car, the road conditions etc. You might imagine your audience as a Vehicle Safety Board who's interested in reducing traffic accidents, or as the City of Chicago who's interested in becoming aware of any interesting patterns. Note that there is a **multi-class** classification problem. You will almost certainly want to bin or trim or otherwise limit the number of target categories on which you ultimately predict. Note e.g. that some primary contributory causes have very few samples.

2) [Terry Stops Data](https://catalog.data.gov/dataset/terry-stops).
In [*Terry v. Ohio*](https://www.oyez.org/cases/1967/67), a landmark Supreme Court case in 1967-8, the court found that a police officer was not in violation of the "unreasonable search and seizure" clause of the Fourth Amendment, even though he stopped and frisked a couple of suspects only because their behavior was suspicious. Thus was born the notion of "reasonable suspicion", according to which an agent of the police may e.g. temporarily detain a person, even in the absence of clearer evidence that would be required for full-blown arrests etc. Terry Stops are stops made of suspicious drivers.

Build a classifier to predict whether an arrest was made after a Terry Stop, given information about the presence of weapons, the time of day of the call, etc. Note that this is a **binary** classification problem.

Note that this dataset also includes information about gender and race. You **may** use this data as well. You may, e.g. pitch your project as an inquiry into whether race (of officer or of subject) plays a role in whether or not an arrest is made.

If you **do** elect to make use of race or gender data, be aware that this can make your project a highly sensitive one; your discretion will be important, as well as your transparency about how you use the data and the ethical issues surrounding it.

3) [Customer Churn Data](https://www.kaggle.com/becksddf/churn-in-telecoms-dataset)

Build a classifier to predict whether a customer will ("soon") stop doing business with SyriaTel, a telecommunications company. Note that this is a **binary** classification problem.

Most naturally, your audience here would be the telecom business itself, interested in losing money on customers who don't stick around very long. Are there any predictable patterns here?

4) [Tanzanian Water Well Data](https://www.drivendata.org/competitions/7/pump-it-up-data-mining-the-water-table/page/23/) (*active competition*!)
Tanzania, as a developing country, struggles with providing clean water to its population of over 57,000,000. There are many waterpoints already established in the country, but some are in need of repair while others have failed altogether.

Build a classifier to predict the condition of a water well, using information about the sort of pump, when it was installed, etc. Note that this is a **ternary** classification problem.

## The Deliverables

Your completed project should contain the following four deliverables:

1. A well documented **_Executive Jupyter Notebook_** containing any code you've written for this project. This work will need to be pushed to a public GitHub repository dedicated for this project.

2. An organized **README.md** file in the GitHub repository that describes the contents of the repository. This file should be the source of information for navigating through the repository. 

4. An **_Keynote/PowerPoint/Google Slides Presentation_** that gives a brief overview of your problem/dataset, and each step of the CRISP-DM process.  The intended audience of this notebook is non-technical stakeholders.


### Excective Jupyter Notebook Must-Haves

For this project, your Jupyter Notebook should meet the following specifications:

#### Organization/Code Cleanliness

- The notebook is written for technical audiences with a way to both understand your approach and reproduce your results. The target audience for this deliverable is other data scientists looking to validate your findings.
- Well-organized, having distinct sections in logical sequence and with appropriate headings  
- Well-commented code, including doc-strings for functions
- Notebook can be run to generate same results. Includes setting random seeds & including referenced files in repository
- Text explains purpose of project and approach used and **decision making steps** throughout your project
- Text explains what code cells do
- Utilizes code for data cleaning through functions built elsewhere
- Text explains **reasoning** behind analytic decisions
- Text **interprets results** of analyses

#### Visualizations & EDA

* Your project contains at least 4 meaningful data visualizations, with corresponding interpretations. All visualizations are well labeled with axes labels, a title, and a legend (when appropriate)  
* Your notebook should contain 1 - 2 paragraphs briefly explaining your approach to this project.

#### Model Quality/Approach
- Pose at least one question that is relevant to the business problem and answer them through classification models
-  Runs 3 or more classification models, including justification for each model iteration
-  Models interations include hyperparameter tuning.
-  Models are validated
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
* Clearly state the goals of the project
* Clearly describe the data used
* Relate the resulting analysis back to the organizational problem
* Include ideas to further develop the project 

**_Based on the results of your models, your presentation should discuss at least two concrete recommendations/solutions for the business problem._**


## Developing your Machine Learning Model

As you develop your machine learning model to address your selected problem mae sure to keep the following process, steps, and tools in mind.

![](Mod 3 Learning Goals (1).png)


## The Process

These steps are informed by Smart Vision's<sup>1</sup> description of the CRISP-DM process.

### 1. Getting Started

Please start by reviewing this document. If you have any questions, please ask them in Slack ASAP so (a) we can answer the questions and (b) so we can update this documentation to make it clearer.

### 2. CRISP-DM Check-In pt.1 - Monday
You will meet with your instructors on Monday to “pitch” your project idea. We will be focusing on the steps of the CRISP-DM model.  Be prepared to answer the following questions. Be prepared to answer the following questions:


- Business Understanding
	- What is the business problem?
	- What questions will you be addressing?
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
You will meet with your instructors on Tuesday to further discuss your approach to modeling.  We expect you to have done a thorough EDA and have run at least one model.

- EDA/Visualization
   - What visualizations have you already made/planning to make?
   - What messages are these visualizations trying to convey?
   - Will your visualizations be of EDA steps or to convey the results of your modeling?
   - Are your visualizations clearly understood by a layperson?
   
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
   
### 4. MVP Checkin - Wednesday
You will meet with an instructor who will check if the minimum requirements of the project are completed. At this point you should have a "best" model that "works" in answering the business question but may need some final adjustments.  Following this meeting you should be ready to polish your notebook and work on your slidedeck.

### 5. Practice Presentations- Thursday
You do a practice presentation in front of the class.  At this point the instructors and other students will provide verbal feedback which can be incorportated in your final presentation.

### 6. Project Presentations- Friday
You will present your project to the class using your slidedeck.  This presentation should not take more than 5 minutes and should be directed towards a non-technical audience.  Both partners should participate in the presentation of the project.

## Groups

1. Clair Marie & Raven
2. Alex & James
3. Bobby & Dan
4. Jake & Sam
5. Jim, Nick, & Michael

## Submitting your Project

You’re almost done! In order to submit your project for review, please complete the Mod 3 Project Submission form in Canvas.

## Grading Rubric

The grading rubric for the project can be found [here](https://docs.google.com/spreadsheets/d/1ufEoJ0erjNzCplQI5Sh3qmNzeQ3QIimU7afLA0K2UoE/edit?usp=sharing).

## Summary

The end of module projects and project reviews are a critical part of the program. They give you a chance to both bring together all the skills you've learned into realistic projects and to practice key "business judgement" and communication skills that you otherwise might not get as much practice with.