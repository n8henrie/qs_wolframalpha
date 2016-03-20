# qs_wolframalpha.py

A quick and dirty way to query Wolfram Alpha with Quicksilver.

## Setup

- Sign up for the [Wolfram Alpha API](http://products.wolframalpha.com/api/)
- Put your `appid` into Keychain (`File` -> `New Password Item`) with service
  `wolframalpha` and account name `appid`
- Save the `.applescript` as a `.scpt` file in your Quicksilver Actions
  directory, changing the path to python3 and `qs_wolframalpha.py`
- Restart Quicksilver

## Usage

Type a simple query into Quicksilver's search box and select `Ask Wolfram
Alpha` as the action. After a few second delay while it thinks, it should
return its best guess of the answer.
