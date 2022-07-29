
## Introduction
This package is created to automate algorai blockchain app using selenium webdriver with python programming. 

## Follow Along
### Cloning the repository:

You can get a copy of all files by cloning this repository!

```shell
git clone https://github.com/UCCTesting/algorai.git
```

### Install Python

You will need to install python first. For this testing I have chosen to use python version 3.10.5.

**NOTE**: Make sure to include the python location in your PATH environment variable

### Download web driver

You will need to download a valid webdriver:

* Chrome:	https://sites.google.com/a/chromium.org/chromedriver/downloads
* Edge:	https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
* Firefox:	https://github.com/mozilla/geckodriver/releases
* Safari:	https://webkit.org/blog/6900/webdriver-support-in-safari-10/

For this testing I have chosen to use the web driver for the chrome web browser.

**NOTE**: Make sure to include the ChromeDriver location in your PATH environment variable

#### To Install The Package:
**NOTE**: You need to run this command outside the algorai folder path.

```sh
pip install ./algorai
```

Check if the package exists
```sh
pip list
```

### Setup your own wallet
Please put your **username** and your **password** to set up your own wallet on the file [account_info.txt](https://github.com/UCCTesting/algorai/blob/main/algosigner_setup/account_info.txt)

### Recovery your wallet address
Please put your **mnemonic phrase** to import your existing wallet on the file [recovery_phrase.txt](https://github.com/UCCTesting/algorai/blob/main/algosigner_setup/recovery_phrase.txt)

### Interact with Chrome via Python Selenium

Open up a terminal and navigate to the root directory of the repository. 

**File** : [main.py](https://github.com/UCCTesting/algorai/blob/main/main.py)

And then execute the test from your command line.

```shell
python main.py
```
