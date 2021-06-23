# Major-Project
**A central repo for sharing resources, workflows and roadmaps. Learn how to edit a markdown file and add more resourses if found.  Check the [Projects](https://github.com/Sanoj32/Major-Project/projects) section for project managemet plans.**

## Roadmap
0) Project proposal (In development)
1) Scrape data from all sites mentioned [below](#websites-to-scrape). (In development)
2) Clean the data and remove unnecessary variables and noise. (Pending)
3) Perfrom EDA and find out the relationships between variables. (Pending)
4) Build a model to predict/give an objective price of the house based on the parameters. (Pending)
5) Deploy the model using flask(Api), HTML, CSS, JS and PHP/Laravel(Backend). (Pending)
6) Documentation (Pending)

## INFROMATION AND RESOURCES

### Tutorial videos
* [Real estate prediction](https://www.youtube.com/watch?v=rdfbcdP75KI&list=PLeo1K3hjS3uu7clOTtwsp94PcHbzqpAdg)
* [First Class functions](https://www.youtube.com/watch?v=kr0mpwqttM0&t=334s)
* [For Numpy, Pandas and Matplotlib](https://www.codingninjas.com/courses/online-data-science-course)
* [Google's machine learning course](https://developers.google.com/machine-learning/crash-course/ml-intro)
* [Pip Python package manager](https://youtu.be/U2ZN104hIcc)
* [Setting up python virtual env in VSCode](https://youtu.be/Wuuiga0wKdQ)
* [Data Science Handbook](https://tanthiamhuat.files.wordpress.com/2018/04/pythondatasciencehandbook.pdf)



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

### Important Statistics Concepts (Add more)
* Co-relation between variables
* [Linear/Multiple](https://youtu.be/yIYKR4sgzI8)/Lo[[[](https://youtu.be/PaFPbb66DxQ)](https://youtu.be/PaFPbb66DxQ)](https://youtu.be/PaFPbb66DxQ)gistic reression
* p-value, level of significance, null and alternate hypothesis.

### Importatn Machine learning Comncepts
*  One hot encoding
*  Dummy variable trap
### Algorithms (listed possible best to worst)
1. Logistic regression - Related = Wald's test
2. Convolution neural networks
3. Random forest
4. ID3

Use waka as a testing tool and may use external librariess to check efficiency of the model.

### Miscellaneous
* [Basobass data](https://www.kaggle.com/sagyamthapa/nepali-housing-price-dataset?select=2020-4-27.csv)
* Using VSCode commmand pallete
* [The Spyder IDE](https://www.spyder-ide.org/)
* [Markdown](https://guides.github.com/features/mastering-markdown/)
* [Land measurement](https://en.wikipedia.org/wiki/Nepalese_customary_units_of_measurement)
* [Creating checkmarks in projects](https://docs.github.com/en/issues/king-your-work-with-issues/creating-issues/about-task-lists)
* [How Much Training Data is Required for Machine Learning? (Article)](https://machinelearningmastery.com/much-training-data-required-machine-learning/)

### Libraries (Must read official docs)
* [Numpy](https://numpy.org/doc/stable/)
* [Pandas](https://pandas.pydata.org/docs/)
* [Seaborn](https://seaborn.pydata.org/introduction.htmlZ)
* [Matplotlib](https://matplotlib.org/stable/contents.html)

## Websites to scrape
Always try to check if the data is in kaggle before writing a script yourself.

1.  [99aana](https://99aana.com/properties/?_offer_type=sale&keyword_search=&_listing=&realteo_order=date-desc&_property_type=houses&_price_min=&_price_max=) - BS4
2.  [Nepal Homes](https://www.nepalhomes.com/) - Might need Selenium
3.  [Hamrobazar](https://hamrobazar.com)
4.  [Gharbazar](https://www.gharbazar.com/) - Selenium
5.  [Basobaas](https://basobaas.com/) - Selenium (found on kaggle)
6.  [1Ropani](http://www.1ropani.com/) - BS4
7.  [Gharghaderi](https://www.gharghaderi.com/) - Selenium
8.  [Housing Nepal](https://housingnepal.com) - BS4
9.  [Real Estate In Nepal](https://www.realestateinnepal.com/) - BS4
10. [Nepal Home Search](https://nepalhomesearch.com/) -BS4
11. [Nepal Realestates](https://nepalrealestates.com/) -BS4 very low amount of data
12. [The Realtors](https://therealtors.com.np/property/view-all-buy) - search with selenium and scrapte with BS4. Scan title for house keyword. Not properly catagorized
13. [GharJagga Nepal](https://www.gharjagganepal.com/) - BS4

## Parameters (*subject to change*)
1. Price
2. Location in District
3. Number of rooms
4. Number of floors
5. Area
6. Time posted
7. Road ahead of the house *
8. Room size *
9. Bedrooms *
10. Bathrooms *
11. Garage *
12. Car parking *
13. kitchen *
14. Living room *
15. Furnished ? *


