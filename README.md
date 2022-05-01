# Introduction

The webapp selects a quote based on category from a dataset of quotes and then the quote is spoken out loud (text-to-speech)

# Access the dataset

The dataset needs to be accessed for successfully running the webapp. The **quotes.zip** zipped file needs to be unzipped in order to access the dataset. The extracted dataset must be placed under the application folder (where **app.py** is present)

# Python dependencies

* Flask     ```$ pip install Flask```
* pandas    ```$ pip install pandas```
* pyttsx3   ```$ pip install pyttsx3```

# Run the webapp

To run the webapp execute the following command inside the application folder: -

```
$ python app.py
```