from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="onyx-tts",
    version="1.0.0",
    author="0N Labs",
    author_email="contact@0nlabs.ai",
    description="High-performance multilingual text-to-speech system by 0N Labs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/0N-Labs/onyx-tts",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    package_data={"onyx_tts": ["config.json"]},
    python_requires=">=3.10",
    install_requires=[
        "onnxruntime>=1.20.1",
        "colorlog>=6.9.0",
        "espeakng-loader>=0.2.4",
        "phonemizer-fork>=3.3.2",
        "numpy>=2.0.2",
    ],
    extras_require={
        "gpu": [
            "onnxruntime-gpu>=1.20.1; platform_machine == 'x86_64' and sys_platform != 'darwin'"
        ],
        "dev": [
            "ruff>=0.11.0",
            "sounddevice>=0.5.1",
            "soundfile>=0.13.0",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Multimedia :: Sound/Audio :: Speech",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    keywords=["tts", "text-to-speech", "onnx", "ai", "machine-learning"],
)
