# Contributing to symmetrical-meme

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing to this project.

## Getting Started

### Install Dependencies

```bash
# Runtime dependencies
pip install -r requirements.txt

# Development tools (formatters, linters, security tools)
pip install -r requirements-dev.txt
```

### Environment Variables

Set required environment variables:

```bash
export SUPABASE_URL="https://<your-project>.supabase.co"
export SUPABASE_KEY="<your-service-role-or-anon-key>"
```

## Development Workflow

### Pre-commit Hooks

This project uses pre-commit hooks to ensure code quality before commits. The hooks automatically check:

- Code formatting (Black)
- Linting (Ruff)
- Import sorting (isort)
- Type checking (mypy)
- Code quality (pylint)
- Commit message format (Conventional Commits)
- Branch name format (Conventional Branch)
- File validation (trailing whitespace, large files, secrets, etc.)

**Installation:**

```bash
# Install pre-commit
pip install pre-commit

# Install git hooks (runs on git commit)
pre-commit install

# Install commit-msg hook (validates commit messages)
pre-commit install --hook-type commit-msg

# (Optional) Test on all files
pre-commit run --all-files
```

**Usage:**

- Hooks run automatically on `git commit`
- Auto-fixable issues (formatting, imports) are corrected automatically
- Stage the auto-fixed changes and commit again
- Critical issues block the commit until fixed
- To bypass temporarily: `git commit --no-verify` (not recommended)

**Update hooks:**
```bash
pre-commit autoupdate
```

### Branch Naming

Follow the [Conventional Branch](https://conventional-branch.github.io/) specification:

**Format:** `<type>/<description>`

**Allowed types:**
- `feature/` or `feat/` - New features
- `bugfix/` or `fix/` - Bug fixes
- `hotfix/` - Urgent fixes
- `release/` - Release preparation
- `chore/` - Maintenance tasks

**Rules:**
- Use lowercase letters, numbers, hyphens, and dots only
- No underscores, spaces, or special characters
- Keep it clear and concise
- Include ticket numbers when applicable

**Examples:**
```bash
feat/add-oauth-login
fix/header-bug
hotfix/security-patch
release/v1.2.0
chore/update-dependencies
```

### Commit Messages

Follow [Conventional Commits](https://www.conventionalcommits.org/) specification:

**Format:** `<type>(<scope>): <subject>`

**Allowed types:**
- `feat` - New feature
- `fix` - Bug fix
- `chore` - Maintenance
- `ci` - CI/CD changes
- `docs` - Documentation
- `style` - Code style (formatting)
- `refactor` - Code refactoring
- `perf` - Performance improvements
- `test` - Tests
- `build` - Build system
- `revert` - Revert changes

**Rules:**
- Use lowercase for type
- Scope is optional but recommended
- Subject should be concise and clear
- No period at the end
- Use imperative mood ("add" not "added")

**Examples:**
```bash
feat(auth): add OAuth login
fix(api): handle 500 error on fetch
chore(deps): bump pandas to 2.2
docs(readme): update setup instructions
ci(workflow): add security scan step
```

### Running Quality Checks Locally

Run the same checks that execute in CI/CD:

```bash
# Format code
black .

# Lint code
ruff check .
ruff check --select S .  # Security rules

# Sort imports
isort .

# Type check
mypy . --ignore-missing-imports

# Code quality
pylint **/*.py --disable=C0111,C0103,R0913,R0914 --max-line-length=100

# Security scans
bandit -r . -x tests,notebooks
pip-audit
safety scan --full-report

# Secret scan (requires Docker)
docker run --rm -v "$PWD":/repo ghcr.io/gitleaks/gitleaks:latest detect -v -s /repo
```

## CI/CD Workflows

GitHub Actions workflows automatically run on pull requests to `main`:

### Code Quality (`python-quality.yml`)
- Black (code formatting)
- Ruff (linting)
- isort (import sorting)
- mypy (type checking)
- pylint (code analysis)

### Security (`security.yml`)
- Gitleaks (secret scanning)
- Ruff security rules
- Bandit (static security analysis)
- pip-audit (dependency vulnerabilities)
- Safety (dependency security scan)

### Conventions (`conventions.yml`)
- Branch name validation (Conventional Branch)
- Commit message validation (Conventional Commits)

All checks must pass before a PR can be merged.

## Pull Request Process

1. Create a branch following the naming convention
2. Make your changes with proper commit messages
3. Ensure all pre-commit hooks pass
4. Push your branch and create a pull request
5. Wait for CI checks to pass
6. Address any review feedback
7. Once approved, your PR will be merged

## Questions or Issues?

If you have questions or encounter issues, please:
- Check existing issues on GitHub
- Review this contributing guide
- Open a new issue with details about your question or problem

Thank you for contributing! 🎉
