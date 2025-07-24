# DNS Speed Test

This is a simple Python script designed to test the response speed of various public DNS servers. The goal is to help you find the fastest and most reliable DNS server for your internet connection, which can result in a more agile and responsive browsing experience.

---

## Why Use This Script?

The DNS server you use acts as the "phonebook" of the internet. A faster server translates domain names (like `www.google.com`) into IP addresses more efficiently, reducing the waiting time before a page starts to load.

In addition to speed, choosing a good DNS can offer extra layers of **security** (by blocking malicious sites) and **privacy**.

This script automates the process of testing dozens of servers directly from your machine, providing real data on the performance of each one on your network.

---

## Features

- Tests a comprehensive list of popular and secure DNS servers.
- Measures the **average response time** for each server in milliseconds (ms).
- Groups servers by provider for easy identification (Google, Cloudflare, etc.).
- Checks reliability and reports servers that fail the test.
- Ranks the results from fastest to slowest in a clear ranking.
- Easy to use and customize.

---

## Prerequisites

To run this script, you will need:

- Python 3.x installed on your system.
- Internet access.
- The `pip` package manager (usually included with Python installations).

---

## Installation

This script depends on the `dnspython` library. To install it, open your terminal or command prompt and run:

```bash
pip install dnspython
```

---

## How to Use

1. Save the script's code into a file named, for example, `main.py`.

2. Open a terminal or command prompt.

3. Navigate to the folder where you saved the file. Example:

   ```bash
   cd /path/to/your/folder
   ```

4. Run the script with the following command:

   ```bash
   python main.py
   ```

The script will start testing each server and, at the end, will display the performance ranking.

---

## Understanding the Results

The script will test each server on the list, showing the progress in real-time. The final result will be a ranking similar to this:

```
--- Final Ranking (from fastest to slowest) ---

1. Cloudflare (1.1.1.1) - Average time: 12.34 ms
2. Google (8.8.8.8) - Average time: 15.67 ms
3. Quad9 (9.9.9.9) - Average time: 21.80 ms
...
4. Yandex.DNS (77.88.8.1) - Test failed
```

- **Lower is better**: The lowest time in ms (milliseconds) indicates superior performance.
- **Test failed**: If a server fails, it means it did not respond to requests in time (or was offline) and should be avoided.

Based on this ranking, you can choose the **primary server** (No. 1 on the list) and the **secondary server** (No. 2) to configure in your operating system or router.

---

## Customization

### Add or Remove DNS Servers

You can easily edit the list of servers to be tested. Just modify the `dns_servers` dictionary at the beginning of the `main.py` file:

```python
dns_servers = {
    'Google': ['8.8.8.8', '8.8.4.4'],
    'Cloudflare': ['1.1.1.1', '1.0.0.1'],  # Add or remove providers and IPs here
}
```

### Change the Test Domain

By default, the script uses `www.wikipedia.org` for testing. You can change this in the `test_domain` variable. It is recommended to use a popular and globally distributed website for more consistent results.

```python
# Domain for testing
test_domain = 'www.example.com'
```

---
