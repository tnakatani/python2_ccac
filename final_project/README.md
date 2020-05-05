






### Things to Improve On

#### Multithreaded Scraping

The scraping process took several hours to finish due the script calling a request for each url one at a time.  After running the script the first time, I came across some articles about [multithreaded](https://beckernick.github.io/faster-web-scraping-python/) web scraping.  Here is an interesting section on the difference between multithreaded versus multiprocessed scraping from the linked blog post:

> The benefits of multiprocessing are basically capped by the number of cores in the machine, and multiple Python processes come with more overhead than simply using multiple threads. If I were to use multiprocessing on my 2015 Macbook Air, it would at best make my web scraping task just less than 2x faster on my machine (two physical cores, minus the overhead of multiprocessing).  

If this scraping process were to operated at scale, it would make sense to split the scraping task across multiple threads or CPUs to accomplish the task in a reasonable time frame.
