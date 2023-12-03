"""
This module processes a news category dataset, analyzing and
reporting on word frequencies in news headlines. It uses
multi-threading for concurrent processing and generates an HTML
report of the top words in each news category.
"""

import json
import os
import threading
import argparse
import logging
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk
from htmls import HtmlPage

# Initialize logging
logging.basicConfig(filename='logs/main.log',
                    level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

# Global variables
stop_words = None
html_report = HtmlPage('output.html')


def process_category(category, articles):
  """Process each news category to find the top words."""
  logging.info('Processing category: %s', category)
  word_counts = Counter()
  for article in articles:
    words = word_tokenize(article['headline'])
    filtered_words = [
      word.lower()
      for word in words if word.lower() not in stop_words and word.isalpha()
    ]
    word_counts.update(filtered_words)

  top_words = word_counts.most_common(10)
  logging.info('Top words in %s: %s', category, top_words)

  html_report.add_h1(category)
  for word, count in top_words:
    html_report.add_p(f'{word}: {count}')

  return top_words


def setup_nltk_data(data_dir):
  """Set up NLTK data required for processing."""
  nltk.data.path.append(data_dir)
  punkt_path = os.path.join(data_dir, 'tokenizers/punkt')
  stopwords_path = os.path.join(data_dir, 'corpora/stopwords')

  if not os.path.exists(punkt_path):
    logging.info('Downloading NLTK "punkt" tokenizer...')
    nltk.download('punkt', download_dir=data_dir)
  else:
    logging.info('NLTK "punkt" tokenizer already downloaded.')

  if not os.path.exists(stopwords_path):
    logging.info('Downloading NLTK "stopwords"...')
    nltk.download('stopwords', download_dir=data_dir)
  else:
    logging.info('NLTK "stopwords" already downloaded.')


def load_data(file_path):
  """Load data from the given file path."""
  data = []
  with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
      try:
        data.append(json.loads(line))
      except json.JSONDecodeError as e:
        logging.error('Error decoding JSON: %s', e)
  return data


def main(file_path):
  """Main function to process the news category dataset."""
  data_dir = 'data'
  setup_nltk_data(data_dir)
  global stop_words
  stop_words = set(stopwords.words('english'))

  data = load_data(file_path)
  if not data:
    logging.error('Failed to load data from: %s', file_path)
    return

  category_data = {}
  for item in data:
    category = item['category']
    category_data.setdefault(category, []).append(item)

  threads = []
  for category, articles in category_data.items():
    thread = threading.Thread(
      target=process_category,
      args=(category, articles)
    )
    thread.start()
    threads.append(thread)

  for thread in threads:
    thread.join()

  html_report.render()
  logging.info('Processing complete.')


if __name__ == '__main__':
  parser = argparse.ArgumentParser(
    description='News Category Dataset Processor'
  )
  parser.add_argument(
    'file_path',
    type=str,
    help='Path to the news category dataset file'
  )
  args = parser.parse_args()

  main(args.file_path)
