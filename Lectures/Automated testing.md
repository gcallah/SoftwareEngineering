
## The Main Challenge of Testing

Reduce both false positives and false negatives as much as possible.

## Test the Interface, not the Implementation

What is a proper test for an accelerator pedal and its transmission mechanism?

## Some testing principles

* Make sure to test what happens on bad input!
* Tests must be independent of the code they are testing!

## Some testing tools we will employ

### Major packages
* **pytest**: runs our tests
* **coverage**: measures test coverage
* **flake8**: our lint tool: fix formatting and detect possible bugs
* **unittest**: we get `mock` from here

### Functions and decorators
* **pytest.raises()**: check for exceptions
* **unittest.mock.patch()**: replace a function
* **pytest.skip()**: skip a test
* **pytest.fixture()**: setup tests




