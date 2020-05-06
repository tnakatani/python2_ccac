# More Explorations with MoMA Scrape

![image](img/gallery.webp)

This notebook further explores web data scraped from the MoMA collection.

The [previous notebook](https://github.com/tnakatani/python2_ccac/blob/master/wk_8/moma_scrape/moma_scrape.ipynb) explored scraped data of specific artists.  This time, the script was revised to randomly sample artworks from the collection in order to explore trends in the larger collection.

## Step 1: Data Collection 

The [moma_scrape.py](moma_scrape.py) script created an artwork dataset with the following steps:
1. NumPy's [`randint`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randint.html?highlight=randint#numpy.random.randint) method creates a list of random integers.
2. The `ArtworkSoup` class contains a method `scrape`, which takes the integers as a parameter.  The class subsequently builds a URL with the integer and makes a HTTP request.  Both successful and unsuccessful HTTP calls are logged in a separate `scrape.log` file.
3. If the HTTP request is successful, the class instantiates a `BeautifulSoup` object, extracts relevant artwork data from the HTML and builds a data structure from it.
4. Once all HTTP calls are made, the resulting data structure is dumped to a CSV file.

## Step 2: Data Analysis

This [Jupyter notebook](notebooks/moma_scrape_exploration.ipynb) follows the general extract, transform and load (ETL) functions using the Pandas framework.  Some findings of the analysis is then visualized using Matplotlib.

## Notes About the Project

Below are some extra notes that I took while creating this project, mainly focusing on areas of improvement.

### Multithreaded Scraping to Improve Scrape Speed

The scraping process took several hours to finish due the script calling a request for each url one at a time.  After running the script the first time, I came across some articles about [multithreaded](https://beckernick.github.io/faster-web-scraping-python/) web scraping.  Here is an interesting section on the difference between multithreaded versus multiprocessed scraping from the linked blog post:

> The benefits of multiprocessing are basically capped by the number of cores in the machine, and multiple Python processes come with more overhead than simply using multiple threads. If I were to use multiprocessing on my 2015 Macbook Air, it would at best make my web scraping task just less than 2x faster on my machine (two physical cores, minus the overhead of multiprocessing).  

If this scraping process were to operated at scale, it would make sense to split the scraping task across multiple threads or CPUs to accomplish the task in a reasonable time frame.

#### Plotting

Note to self: Look into more ways to transform categorical data into quantitative output which can then be plotted in more engaging ways.
