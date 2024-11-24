import os

def split_file(file_path, chunk_size):
    """
    Splits a large file into smaller chunks.
    
    Args:
        file_path (str): Path to the large file.
        chunk_size (int): Size of each chunk in bytes.
    """
    if not os.path.exists(file_path):
        print(f"File '{file_path}' not found.")
        return

    file_size = os.path.getsize(file_path)
    base_name = os.path.basename(file_path)
    output_dir = f"{base_name}_chunks"

    # Create a directory to store chunks
    os.makedirs(output_dir, exist_ok=True)
    
    with open(file_path, 'rb') as f:
        chunk_num = 0
        while chunk := f.read(chunk_size):
            chunk_file_name = os.path.join(output_dir, f"{base_name}.part{chunk_num}")
            with open(chunk_file_name, 'wb') as chunk_file:
                chunk_file.write(chunk)
            print(f"Created chunk: {chunk_file_name}")
            chunk_num += 1

    print(f"File split into {chunk_num} chunks, saved in '{output_dir}'.")

# Usage
file_path = r"C:\Users\Saurav\Documents\PredictiveAnalyticsProject-ChangePrediction\GeospatialChangePrediction\src\full_model.pth"  # Replace with your file path
chunk_size = 100 * 1024 * 1024  # 100 MB chunks
split_file(file_path, chunk_size)
