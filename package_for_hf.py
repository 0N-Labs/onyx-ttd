import os
import shutil
from pathlib import Path

def package_for_huggingface():
    """Package the model for Hugging Face Hub."""
    # Create output directory
    output_dir = Path("onyx-tts-hf")
    output_dir.mkdir(exist_ok=True)
    
    # Copy model files
    model_files = [
        "src/onyx_tts/__init__.py",
        "src/onyx_tts/config.py",
        "src/onyx_tts/log.py",
        "src/onyx_tts/tokenizer.py",
        "src/onyx_tts/trim.py",
        "src/onyx_tts/config.json",
        "HUGGINGFACE_README.md",
        "LICENSE",
    ]
    
    # Create necessary directories
    (output_dir / "onyx_tts").mkdir(exist_ok=True)
    
    # Copy files
    for file_path in model_files:
        if file_path.startswith("src/"):
            dest = output_dir / file_path[4:]  # Remove 'src/' prefix
        else:
            dest = output_dir / Path(file_path).name
        
        # Create parent directories if they don't exist
        dest.parent.mkdir(parents=True, exist_ok=True)
        
        if os.path.isfile(file_path):
            shutil.copy2(file_path, dest)
    
    # Rename README
    os.rename(output_dir / "HUGGINGFACE_README.md", output_dir / "README.md")
    
    # Create requirements.txt
    with open(output_dir / "requirements.txt", "w") as f:
        f.write("""numpy>=2.0.2
onnxruntime>=1.20.1
colorlog>=6.9.0
espeakng-loader>=0.2.4
phonemizer-fork>=3.3.2
""")
    
    print(f"Packaged model for Hugging Face in: {output_dir}")
    print("\nTo upload to Hugging Face Hub, run:")
    print(f"cd {output_dir}")
    print("git init")
    print("git lfs install")
    print('git lfs track "onnx-*.onnx"')
    print('git lfs track "*.bin"')
    print('git add .')
    print('git commit -m "Initial commit"')
    print("huggingface-cli login")
    print("huggingface-cli create 0N-Labs/onyx-tts")
    print("git remote add origin https://huggingface.co/0N-Labs/onyx-tts")
    print("git push -u origin main")

if __name__ == "__main__":
    package_for_huggingface()
