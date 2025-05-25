# Onyx-TTS

Onyx-TTS is a high-performance, multilingual text-to-speech system developed by 0N Labs. It's built on ONNX Runtime, delivering fast and efficient speech synthesis with minimal resource requirements.

## Model Details

- **Developed by**: 0N Labs
- **Model type**: Text-to-Speech
- **Languages**: Multiple languages supported
- **License**: Apache 2.0
- **Model size**: ~300MB (quantized: ~80MB)

## How to Use

### Installation

```bash
pip install onyx-tts
```

### Basic Usage

```python
import soundfile as sf
from onyx_tts import OnyxTTS

# Initialize the TTS engine
onyx = OnyxTTS("onyx-v1.0.onnx", "voices-v1.0.bin")

# Generate speech
samples, sample_rate = onyx.create(
    "Hello! This is Onyx TTS by 0N Labs.", 
    voice="af_sarah", 
    speed=1.0, 
    lang="en-us"
)

# Save to file
sf.write("output.wav", samples, sample_rate)
```

## Available Voices

See the latest voices and languages in the [VOICES.md](VOICES.md) file.

## License

- Onyx-TTS: MIT
- Onyx model: Apache 2.0

## Citation

```bibtex
@software{onyx-tts,
  author = {0N Labs},
  title = {Onyx-TTS: High-performance Text-to-Speech},
  year = {2025},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/0N-Labs/onyx-tts}}
}
```

## Contact

For questions and support, please contact: contact@0nlabs.ai
