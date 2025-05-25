# Onyx-TTS

> A high-performance, multilingual text-to-speech system by 0N Labs

[![ONNX Runtime](https://img.shields.io/badge/ONNX%20Runtime-%E2%89%A51.20.1-blue)](https://github.com/microsoft/onnxruntime)
![CPU](https://img.shields.io/badge/CPU-supported-brightgreen)
![GPU](https://img.shields.io/badge/GPU-supported-brightgreen)

A lightweight, efficient Text-to-Speech system built on ONNX Runtime, delivering high-quality speech synthesis with minimal resource requirements.

🚀 Version 1.0 models are out now! 🎉

<audio controls><source src="https://0N-Labs.github.io/example-one.wav" type="audio/wav"></audio>
<audio controls><source src="https://0N-Labs.github.io/example-two.wav>" type="audio/wav"></audio>


## Features

- Supports multiple languages
- Fast performance near real-time on macOS M1
- Offer multiple voices
- Lightweight: ~300MB (quantized: ~80MB)

## Setup

```console
pip install -U kokoro-onnx
```

<details>

<summary>Instructions</summary>

1. Install [uv](https://docs.astral.sh/uv/getting-started/installation) for isolated Python (Recommend).

Basically open the terminal (PowerShell / Bash) and run the command listed in their website.

_Note: you don't have to use `uv`. but it just make things much simpler. You can use regular Python as well._

2. Create new project folder (you name it)
3. Run in the project folder

```console
uv init -p 3.12
uv add kokoro-onnx soundfile
```

4. Paste the contents of [`examples/save.py`](https://github.com/thewh1teagle/kokoro-onnx/blob/main/examples/save.py) in `hello.py`
5. Download the files [`kokoro-v1.0.onnx`](https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/kokoro-v1.0.onnx), and [`voices-v1.0.bin`](https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/voices-v1.0.bin) and place them in the same directory.
6. Run

```console
uv run hello.py
```

You can edit the text in `hello.py`

That's it! `audio.wav` should be created.

</details>

## Examples

See [examples](examples)

## Voices

See the latest voices and languages in [Kokoro-82M/VOICES.md](https://huggingface.co/hexgrad/Kokoro-82M/blob/main/VOICES.md)

Note: It's recommend to use misaki g2p package from v1.0, see [examples](examples)

## Contribute

See [CONTRIBUTE.md](CONTRIBUTE.md)

## License

- Onyx-TTS: MIT
- Onyx model: Apache 2.0
