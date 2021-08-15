# Major-Project
**A central repo for sharing resources, workflows and roadmaps. Learn how to edit a markdown file and add more resourses if found.  Check the [Projects](https://github.com/Sanoj32/Major-Project/projects) section for project managemet plans.**

## Roadmap
0) Project proposal (In development)
1) Scrape data from all sites mentioned [below](#websites-to-scrape). (In development)
2) Clean the data and remove unnecessary variables and noise. (In development)
3) Perfrom EDA and find out the relationships between variables. (Pending)
4) Build a model to predict/give an objective price of the house based on the parameters. (Pending)
5) Deploy the model using flask(Api), HTML, CSS, JS and PHP/Laravel(Backend). (Pending)
6) Documentation (Pending)

## INFROMATION AND RESOURCES

### Breaking changes
* Some file names refactored to snake case resulting in possible crash of some working scripts eg. csv-files -> csv_files

### Folder heirarchy
    - major-project
      - csv_files
        - raw (Raw unclean data after scraping)
        - links (Links to be scrapped)
        - clean (Cleaned data)
    - jupyter_notebooks (Notebooks to clean data and develop the model)
    - scraping_files
### Tutorial resources
* [Hosing price prediction from towards data science](https://towardsdatascience.com/predict-house-prices-with-machine-learning-5b475db4e1e)
* [Coursera linear regression ](https://www.coursera.org/lecture/ml-regression/using-the-fitted-line-RjYbf) Only good for conceptual/theoritcal learning. Uses outdated libraries.
* [Vectorizaiton](https://youtu.be/BR3Qx9AVHZE) - Important for understanding numpy and pandas.
* [Gradient descent](https://youtu.be/sDv4f4s2SB8) - Important for understanding linear regression.
* [Real estate prediction](https://www.youtube.com/watch?v=rdfbcdP75KI&list=PLeo1K3hjS3uu7clOTtwsp94PcHbzqpAdg) - For brief overview of how the project will work.
* [First Class functions](https://www.youtube.com/watch?v=kr0mpwqttM0&t=334s) - How python's functions can be treated as objects.
* [For Numpy, Pandas and Matplotlib](https://www.codingninjas.com/courses/online-data-science-course)
* [Google's machine learning course](https://developers.google.com/machine-learning/crash-course/ml-intro)
* [Pip Python package manager](https://youtu.be/U2ZN104hIcc)
* [Setting up python virtual env in VSCode](https://youtu.be/Wuuiga0wKdQ)
* [Data Science Handbook](https://tanthiamhuat.files.wordpress.com/2018/04/pythondatasciencehandbook.pdf)
* [Mathematics for machine learning *Book*](https://mml-book.github.io/book/mml-book.pdf)]
* [Google Colab](https://www.youtube.com/watch?v=inN8seMm7UI&ab_channel=TensorFlow) - Online GPU for extra power.



### Important programming concepts
* creating and importing a python module and using its functions (files)
* namespace of functions in a python module
* how functions from other python modules are called
* Python data types: Lists, Tuples, dictionary and sets
* for loops, map function
* method call from a library vs function call ie how obj.method() works
* lambda function/closures/annonyomous function
* [Python virtual environmets](https://docs.python.org/3/library/venv.html)
* Basics of Object oriented python. Python class constructors. How a function gets access to the object it is called upon and how it manipulates the object.
* What is anacodna?
* How pip works

### Important Mathematics and Statistics Concepts (Add more)
* Co-relation between variables and multicollinearity.
* [Linear/Multiple](https://youtu.be/yIYKR4sgzI8)/Logistic reression
* [Squared error of regression line](https://www.khanacademy.org/math/statistics-probability/describing-relationships-quantitative-data/more-on-regression/v/squared-error-of-regression-line)
* p-value, level of significance, null and alternate hypothesis.
* contour plot
* Fit a line using least square method.
* Vectors, Partial derivative, gradient of a function and gradient descent.

### Important diagrams
* Scatter plot
* Heatmap - To find multicollinearity
* Box plot
* Histograms
* Violin plot


### Important Machine learning Comncepts
*  One hot encoding
*  Dummy variable trap

### Algorithms (listed possible best to worst)
1. Ridge regression - Because the data seems to have multicollinearity
2. Linear regression - Related = Wald's test
3. Logistic regression ??
4. Convolution neural networks
5. Random forest
6. ID3

Use waka as a testing tool and may use external librariess to check efficiency of the model.

### Miscellaneous
* Using VSCode commmand pallete
* [The Spyder IDE](https://www.spyder-ide.org/) - Optional for now
* [Markdown](https://guides.github.com/features/mastering-markdown/) - Very important for editing and adding resourses.
* [Land measurement](https://en.wikipedia.org/wiki/Nepalese_customary_units_of_measurement) - Details about the different units of measurement of land.
* [Creating checkmarks in projects](https://docs.github.com/en/issues/king-your-work-with-issues/creating-issues/about-task-lists)
* [How Much Training Data is Required for Machine Learning? (Article)](https://machinelearningmastery.com/much-training-data-required-machine-**learning**/)
* [Install jupyter lab using conda for notebook dark theme:](https://jupyter.org/install.html)

### Libraries (Must read official docs)
Go through the basic contents of the docs atleast once
* [Numpy](https://numpy.org/doc/stable/) (Vectorization and broadcasting in Numpy)
* [Pandas](https://pandas.pydata.org/docs/)
* [Seaborn](https://seaborn.pydata.org/introduction.htmlZ)
* [Matplotlib](https://matplotlib.org/stable/contents.html)

## Websites to scrape
| S.N.  | Name  | Data Amount  | Library required  | Status  | Remarks  |
|:-:|:-:|:-:|:-:|:-:|:---|
| 1  | [99aana](https://99aana.com/)  | 3K  | BS4  | Completed  |   |
| 2  | [Nepal Homes](https://www.nepalhomes.com/)  |  1K | Selenium & BS4  | Links fetched  | Data to be fetched using BS4  |
| 3  | [Basobaas](https://basobaas.com/)  | 2K  | Selenium & BS4  | Links fetched  | Data to be fetched using BS4  |
| 4  | [1Ropani](http://www.1ropani.com/)  | 600  | Selenium & BS4  | Completed  |   |
| 5  | [Hamrobazar](https://hamrobazar.com)  | 3K  |   | Halted  | Presents a captcha to check for bots  |
| 6  | [Gharbazar](https://www.gharbazar.com/)  | 340  | Selenium | Links fetched  | Low amount of data. Scan for house keyword in title.  |
| 7  | [Gharghaderi](https://www.gharghaderi.com/)  | 300  | Selenium  | Halted  | Low amount of data  |
| 8  | [Housing Nepal](https://housingnepal.com)  | less than 300  |  BS4 | Halted  | Low amount of data  |
| 9  |   [Real Estate In Nepal](https://www.realestateinnepal.com/)  | less than 300  | BS4  | Halted  | Low amount of data. Restriction for bots  |
| 10  | [Nepal Home Search](https://nepalhomesearch.com/)  |  140  | BS4  | Halted  | Low amount of data  |
| 11  |  [Nepal Realestates](https://nepalrealestates.com/) | less than 300  | BS4  | Halted | Low amoun of data. |
| 12  | [The Realtors](https://therealtors.com.np/property/view-all-buy)  | 300  | Selenium & BS4  | Halted  | Low amount of data. Scan title or house keyword  |
| 13  | [GharJagga Nepal](https://www.gharjagganepal.com/)  |  330 | Selenium  | Halted  | Low data and has infinite scrolling  |





## Parameters (*subject to change*)
1. Price
2. Location in District
3. Number of rooms
4. Number of floors
5. Area
6. Time posted
7. Road size and road type*
8. Room size *
9. Bedrooms *
10. Bathrooms *
11. Car parking *
12. kitchen *
13. Living room *
14. Garage
15. Furnished ? *
16. Guestroom *

### [Naming convention](https://softwareengineering.stackexchange.com/questions/308972/python-file-naming-convention)
* Files/Modules and variables = snake_case
* directories = all lowercase preferably without underscores
* classes = PascalCase



