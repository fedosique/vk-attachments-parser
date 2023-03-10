# VK-parser in Python :: bs4, Requests

Classic python parser on BeautifulSoup4 + Requests. The program is written to extract links and download images from the VKontakte archive uploaded by request. The repository is loaded with sample messages (50 pieces each) as the service outputs them when uploading. With a slight change of filters you can find links to attached videos or gifs. 

## Structure: 
- Importing libraries;
- I use the "loading" function with the library to describe the process of unloading photos to the root;
- I create an empty list to unload the links;
- Using the function "file_counter" and the Path method, I count the number of files in the folder for automating the parsing script;
- In the while loop I run through the folder with the archive and use the methods of the bs4 library to get a response for the <\a> tags in the form of a list of links;
- I check the link filter in order to separate only images;
- I add the found links to the list and iterate the cycle forward by 50 messages and 1 step (epoch). 
- Through pandas I translate the list of links into a dataframe and output as a csv-file.

## Opportunities for improvement:
- Adding multithreading to parallelize the query;
- Improving the loop and adding a nested loop to pass through the links correctly, adding other tags for other inputs
- Exceptions in the code to give the pass command when an error occurs
- Working with "O" - speeding up the algorithm

