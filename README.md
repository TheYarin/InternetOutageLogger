# InternetOutageLogger

Log internet outages to sqlite and to stdout!

# How it works

InternetOutageLogger simply pings 1.1.1.1 and if no response is received in a timely manner, an outage is logged.

# Requirements

- Linux (because of the lazy ping implementation)
- Python

# Usage

Run:

```bash
python ./InternetOutageLogger.py
```

An `outages.db` file will be created locally.
