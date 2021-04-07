# Set up

We'll need a few things to install for this section:

- https://sites.google.com/a/chromium.org/chromedriver/downloads
- behave (http://pythonhosted.org/behave/)
- selenium (http://selenium-python.readthedocs.io/installation.html)


## Running the tests

To run the tests, you'll need to do this in a terminal (but remember to have the Flask app running!):

```bash
source venv/bin/activate
cd section6/video_code/
python -m behave tests/acceptance
```

If you want to run the tests in PyCharm, you'll need to create appropriate configurations. We cover this in the course!


---------

Running the tests

>> behave tests/acceptance

------

If you do have the 'make' package in your machine:

>> make test

------

To enable debugging in VS Code

{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Behave (.venv)",
            "type": "python",
            "request": "launch",
            "module": "behave",
            "console": "integratedTerminal",
            "args": [
                "./tests/acceptance"
            ]
        },
        {
            "name": "Python: Arquivo Atual",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal"
        }
    ]
}