from setuptools import setup

import io
import os

here = os.path.abspath(os.path.dirname(__file__))

try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = "Python package for automating algorai finance app"


setup(name='algosigner_setup',
      version='1.0',
      packages=['algosigner_setup'],
      description="Python package for automating algorai finance app",
      keywords="python algosigner blockchain automate-algosigner install-algosigner-extension-selenium selenium-algosigner algosigner-automation",
      install_requires=["selenium>=4.0", "pywin32"],
      python_requires='>=3.10',
      url='https://github.com/UCCTesting/algorai.git',
      homepage='https://github.com/UCCTesting/algorai.git',
      author='Maya Maulani',
      author_email='my.maulani@gmail.com',
      long_description=long_description,
      long_description_content_type='text/markdown'

)