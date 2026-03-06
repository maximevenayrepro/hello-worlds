# Python demo template

## Structure

```
python-{framework}/
├── README.md
├── Dockerfile
├── main.py
├── requirements.txt      # only if dependencies exist
└── test_main.py
```

## Dockerfile

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt 2>/dev/null || true
CMD ["python", "main.py"]
```

## Test

```python
from main import app  # or whatever is exported

def test_hello():
    # adapt to the framework's test client
    assert True
```
