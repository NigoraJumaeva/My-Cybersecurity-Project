# SQL Injection Prevention Demo (Python + SQLite)

Shows the difference between **unsafe string concatenation** and **safe parameterized queries**.

## Run
```bash
python demo.py
```

You should see the **unsafe** query succeed with an injection payload, while the **safe** query blocks it.
