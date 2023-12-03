"""
This module provides the HtmlPage class for creating simple HTML files.
It allows adding of basic HTML elements like headings (h1) and paragraphs (p)
and renders them into an HTML file.
"""


class HtmlPage:
  """
  A simple HTML page generator.

  Attributes:
      filename (str): The name of the HTML file to be created.
      contents (str): A string representation of the HTML content.

  Methods:
      add_h1(text): Adds an h1 tag with the provided text to the HTML content.
      add_p(text): Adds a paragraph tag with the provided text.
      render(): Writes the HTML content to the specified file.
  """

  def __init__(self, filename):
    """
    Initializes the HtmlPage with a specified filename.

    Args:
        filename (str): The name of the file.
    """
    self.filename = filename
    self.contents = ('<html>\n<head>\n<title>'
                     'News Analysis Report</title>\n</head>\n<body>\n')

  def add_h1(self, text):
    """
    Adds an h1 element with the provided text to the HTML content.

    Args:
        text (str): The text to be enclosed in the h1 tag.
    """
    self.contents += f'<h1>{text}</h1>\n'

  def add_p(self, text):
    """
    Adds a paragraph element with the provided text to the HTML content.

    Args:
        text (str): The text to be enclosed in the paragraph tag.
    """
    self.contents += f'<p>{text}</p>\n'

  def render(self):
    """
    Finalizes the HTML content and writes it to the specified file.
    """
    self.contents += '</body>\n</html>'
    with open(self.filename, 'w', encoding='utf8') as file:
      file.write(self.contents)
