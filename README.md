# Otus - functional testing
Create automated tests from the tests that you documented in the student profile test plan assignment.

## Technologies used and tested
* vscode
* python 3.7.1
* selenium 3.141.0
* urllib3 1.26.2
* Firefox 83.0(64-bit)

## Requirements
* Have Python 3.* installed.
* CD into github project.
* Install a virtual environment (Optional).
    * ```console
        $ pip install virtualenv
        ```
    * ```console
        $ virtualenv env
        ```
    * On Linux:
        ```console
        $ source env/bin/activate
        ```
    * On Windows:
        ```console
        $ & env\Scripts\activate
        ```
* Install selenium
    * ```console
        $ pip install -r requirements.txt
        ```
## Before executing
* The follow variables on *utils.py* need to be set up.
    ```python
        OtusEmail = ""
        OtusPsw = ""
    ```
* Some test cases need parameters before executing.
    ```python
        """
        Case_bookshelf09:
        # variables need to be set befor executing
        fileName_from_oneDrive
        oneDriveUser
        OneDrivePassword
        """
        class Case_bookshelf09():...
    ```
* To execute a single test case from a file:
    ```console
    $ python .\Test_assesment.py Case_bookshelf05
    ```
* To execute the whole test set:
    ```console
    $ python .\Test_assesment.py
    ```
---
# Architecture
*requirements.txt*:
> This file contains all the python packages that are required for this project.

*utils.py*:
> Utils contains the selenium driver set up; And automation methods.

*xpath_elements.py*:
> Here you can find a dictionary with all the web elements' xpath used.

*Test_{name}.py*
> These files contains the test cases by scenarios.
