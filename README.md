Build status: [![Build Status](https://travis-ci.org/javilumbrales/magento-selenium-checkout.svg?branch=master)](https://travis-ci.org/javilumbrales/magento-selenium-checkout)

## Scope
This projects aims to create a automated browser tests with Selenium Webdriver to test a generic Magento Checkout.

## Requirements

- Python
- Selenium server up and running (might require Java)

## How to use this on my Magento Store?

You can just fork the repository and change the url in the `.travis.yml` file and it should just work. Your might need to amend some selectors if you are using a customised template that modifies magento standard html markups.

## Running the tests

```python checkout.until.payment.py www.42moto.com```

## WIP

- Use more stable/generic element selectors
- Add a settings file for selectors, assertion texts, etc.
- Use Gherkin like tests
- Add logged in tests
- many, many more

## About

This project is used for a real production environment on our website www.42moto.com.
Drop us a line at our blog www.thedeveloperworldisyours.com or alternative you can get in touch with us at www.lumbrales-software.com

