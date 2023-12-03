# News Category Dataset Processor

## Overview
Developed by Jiechao Li, this Python application processes a dataset of news articles, with a focus on analyzing headlines. It categorizes, tokenizes, and counts word occurrences within these headlines, identifying the top 10 most frequent words in each news category. The application employs multi-threading for concurrent processing across different news categories, and outputs the results in an HTML file.

## Prerequisites
Before running the application, ensure you have:
- Python 3.x installed on your system.
- NLTK data (tokenizers and stopwords) available.

## Installation
1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the required Python packages:

`pip install -r requirements.txt`


## Running the Application
To run the application, use the following command in your terminal:

`python main.py data/News_Category_Dataset_v3.json`

## Application Structure
- `main.py`: The main script managing the dataset processing. It creates threads for each news category and generates the HTML report.
- `htmls.py`: A module for creating simple HTML files, supporting h1 headings and p paragraphs.
- `data/`: Contains the `News_Category_Dataset_v3.json` file, the dataset used by the application.

## Output
The application generates an HTML file (`output.html`) in the project's root directory, listing the top 10 words for each news category, with each category as an `h1` heading and the words in `p` tags.

## Logging
Operational logs of the application are recorded in `logs/main.log`, including progress updates and error tracking for each news category's processing.

## Modifications and Notes
Filename Change: html.py to htmls.py. 
Due to a keyword conflict with the nltk library, the file originally named html.py has been renamed to htmls.py. This change is made to avoid conflicts with any internal keywords or modules used by nltk. The application should function as intended with this change.

## Author
Jiechao Li
