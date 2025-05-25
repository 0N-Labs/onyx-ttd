# Building Onyx-TTS

This document provides instructions for building and publishing the Onyx-TTS package.

## Development Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/0N-Labs/onyx-tts.git
   cd onyx-tts
   ```

2. Set up the development environment using `uv`:
   ```bash
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -e .[dev]
   ```

## Release Process

1. Update the version number in `pyproject.toml` following semantic versioning.

2. Build the package:

```console
rm -rf dist
uv build
UV_PUBLISH_TOKEN="pypi token here" uv publish
```

## Code Quality

Before committing changes, ensure your code meets our quality standards:

```console
uv run ruff format
uv run ruff check
```

## Debugging

To enable debug logging:

```bash
LOG_LEVEL=DEBUG python your_script.py
```

## Contributing

We welcome contributions! Please follow our [contribution guidelines](CONTRIBUTE.md) for more information on how to contribute to Onyx-TTS.

## License

Onyx-TTS is released under the MIT License. See [LICENSE](LICENSE) for details.
