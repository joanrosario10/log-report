# Summarize an access log

An Apache-style access log is in your working directory at `/app/access.log`.
Each non-empty line is one request. A line looks like:

```
192.168.0.1 - - [16/Jun/2026:10:00:01 +0000] "GET /index.html HTTP/1.1" 200 1024
```

The first whitespace-separated field is the client IP address, and the
requested path is the second token inside the quoted request (`/index.html`
above).

## Your task

Write a JSON report to `/app/report.json` containing exactly these three fields:

- `total_requests` (integer): the number of non-empty lines in the log.
- `unique_ips` (integer): the number of distinct client IP addresses.
- `top_path` (string): the requested path that appears most often.

Example of the required shape (values are illustrative, not the answer):

```json
{"total_requests": 123, "unique_ips": 10, "top_path": "/index.html"}
```

## Success criteria

1. A file exists at `/app/report.json`.
2. `/app/report.json` contains valid JSON (a single JSON object).
3. `total_requests` equals the number of non-empty lines in the log.
4. `unique_ips` equals the number of distinct client IP addresses.
5. `top_path` equals the most frequently requested path.
