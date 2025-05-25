import os

def update_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace package imports and class names
    content = content.replace('kokoro_onnx', 'onyx_tts')
    content = content.replace('Kokoro', 'OnyxTTS')
    content = content.replace('kokoro = ', 'onyx = ')
    content = content.replace('kokoro.', 'onyx.')
    
    # Update model file names
    content = content.replace('kokoro-v1.0.onnx', 'onyx-v1.0.onnx')
    
    # Update repository URLs
    content = content.replace('thewh1teagle/kokoro-onnx', '0N-Labs/onyx-tts')
    content = content.replace('kokoro-onnx', 'onyx-tts')
    
    # Update any remaining references
    content = content.replace('Kokoro', 'Onyx')
    content = content.replace('kokoro', 'onyx')
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    examples_dir = os.path.join(os.path.dirname(__file__), 'examples')
    for filename in os.listdir(examples_dir):
        if filename.endswith('.py'):
            file_path = os.path.join(examples_dir, filename)
            print(f'Updating {file_path}...')
            update_file(file_path)

if __name__ == '__main__':
    main()
