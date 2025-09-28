# DevStudio AI (MVP)

## Run locally

1. (Optional) Set `OPENAI_API_KEY` environment variable for real LLM responses.
2. Install deps:
   ```bash
   pip install -r backend/requirements.txt

3. Run the backend
   cd backend
   python app.py

Note - flake8 is used for linter output (install globally or in the environment).

This is an MVP. For production, add authentication, rate-limiting, and secure API usage.

How to use

Start your backend API:

cd backend
python app.py


Run the batch tester from the project root:

python batch_test.py


Results will be saved in a new folder:

results/
├── calc.py.json
├── buggy.py.json
├── security.py.json
└── style.py.json


Each .json contains both flake8 static analysis output and AI feedback.
