# Introduction

The webapp selects a quote based on category from a dataset of quotes and then the quote is spoken out loud (text-to-speech).

# Access the dataset

The dataset **quotes.csv** is zipped inside **quotes.zip** which the program internally unzips to read the data. To manually read the data the user needs to unzip it manually and extract the **.csv** file.

# Python dependencies

* Flask     ```$ pip install Flask```
* pandas    ```$ pip install pandas```
* pyttsx3   ```$ pip install pyttsx3```

# Run the webapp

To run the webapp execute the following command inside the application folder: -

```
$ flask run
```