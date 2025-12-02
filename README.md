# symmetrical-meme


## Setup

### Install Dependencies

```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt  # optional: tooling for lint/type/security
```

### Pre-commit Hooks

This project uses pre-commit hooks to ensure code quality. The hooks run automatically before each commit to check:

- Code formatting (Black)
- Linting (Ruff)
- Import sorting (isort)
- Type checking (mypy)
- Code quality (pylint)
- File validation (trailing whitespace, large files, etc.)

**Install pre-commit hooks:**

```bash
# Install pre-commit
pip install pre-commit

# Install the git hooks
pre-commit install

# (Optional) Run on all files to check current state
pre-commit run --all-files
```

**Usage:**

The hooks run automatically on `git commit`. If issues are found:
- Auto-fixable issues (formatting, imports) will be corrected automatically
- You'll need to stage the changes and commit again
- Critical issues will block the commit until fixed

To update hook versions:
```bash
pre-commit autoupdate
```

### Environment Variables

Set required environment variables (e.g., Supabase):

```bash
export SUPABASE_URL="https://<your-project>.supabase.co"
export SUPABASE_KEY="<your-service-role-or-anon-key>"
```

## Development

### Running Quality Checks

The same checks that run in CI/CD can be run locally:

```bash
# Format code
black .

# Lint code
ruff check .

# Sort imports
isort .

# Type check
mypy . --ignore-missing-imports

# Full lint
pylint **/*.py --disable=C0111,C0103,R0913,R0914 --max-line-length=100
```

## CI/CD

GitHub Actions workflows run on PRs to `main`:

- `python-quality.yml`: Black, Ruff, isort, mypy, pylint
- `security.yml`: Secret scan (Gitleaks), Ruff security rules, Bandit, dependency audits (`pip-audit`, `safety`)

Run security scan locally (optional):

```bash
docker run --rm -v "$PWD":/repo ghcr.io/gitleaks/gitleaks:latest detect -v -s /repo
```
