# tropo-ip-info
A HireIQ interview coding challenge based (in part) on a for-real problem

## Setup
0. Fork this repo to your own github account
1. Clone your forked repo to your local machine
2. Write some code and push it to your fork

## The problem
We use a few services from a company called Tropo. Part of our integration with Tropo requires that their systems be able to connect to our systems. For security purposes we whitelist which IP addresses that should be allowed to connect to these endpoints. So we need to make sure that all of the IP addresses that Tropo traffic will be coming from is whitelisted in our configuration.

Helpfully, Tropo publishes their IP addresses (in CIDR block notation) in a format that is readily accessible programmatically. What you need to do is write a simple script to retrieve and output the current IP addresses.

## (Part of) The solution
1. Search for documentation on how to retrieve Tropo's current IP information for whitelisting purposes.
2. You should now have a command to run that will query and display Tropo's IP information. Write a Python script that retrieves this information and prints to STDOUT just the CIDR blocks, one per line, in a simple CSV format. Prefix each line with the word ```tropo``` - for example:
```python
tropo,10.10.0.10/24
```
This format is important as this script would be part of a larger toolchain, including some additional "downstream" tools that manage updating the rest of the IP whitelisting configuration as needed.

## Notes
* There are pretty much no restrictions/guidelines as to how you implement this - it's up to you
* Use a virtualenv. Always!
* If you find a useful third-party package, use it!
* Code style is just as important as functionality - maintainability costs are the silent killer! There are some tools to help you write properly presentable python (namely pep8 and pyflakes - worth checking out)

We're interested in seeing how you *approach* solving a problem like this as much as how you actually *implement* it.

## Questions?
Submit it as an [issue](https://github.com/HireIQ/tropo-ip-info/issues) to this repo! Odds are someone else will have a similar question, so sharing questions and answers that way seems like a good idea.
