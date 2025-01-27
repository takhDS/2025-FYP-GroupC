import csv
import math
import os
import random
import shutil


def create_csv_with_groups(folder_path, output_csv, output_dir, num_samples, num_groups):
    # Step 1: Get all images from the folder
    valid_extensions = {'.jpg', '.jpeg', '.png', '.bmp', '.tif', '.tiff'}
    all_images = [f for f in os.listdir(folder_path) if os.path.splitext(f)[1].lower() in valid_extensions]

    # Sort the images alphabetically
    all_images.sort()

    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Step 2: Save deidentified images to output directory
    file_id_mapping = {}
    for idx, file_name in enumerate(all_images):
        file_id = f"img_{idx:04d}.png"
        original_file_path = os.path.join(folder_path, file_name)
        new_file_path = os.path.join(output_dir, file_id)

        # Copy the file to the new directory with the new name
        shutil.copy2(original_file_path, new_file_path)

        file_id_mapping[file_name] = file_id

    # Step 3: Create groups ensuring full dataset coverage with dynamic overlap
    groups = []
    total_images = len(all_images)
    overlap_margin = max(1, math.ceil((total_images - num_samples) / (num_groups - 1)))

    for i in range(num_groups):
        start_idx = i * (num_samples - overlap_margin)
        group = all_images[start_idx:start_idx + num_samples]

        # If the group is smaller than num_samples, pad it with random samples
        while len(group) < num_samples:
            group.append(random.choice(all_images))

        groups.append(group)

    # Step 4: Write to CSV file
    with open(output_csv, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["File ID", "Group ID"])

        for group_id, group in enumerate(groups, start=1):
            for file_name in group:
                file_id = file_id_mapping[file_name]
                writer.writerow([file_id, group_id])


# Example usage
folder_path = './hair'  # Replace with the path to your folder
output_csv = './dataset.csv'  # Replace with your desired output CSV path
output_dir = './data'  # Replace with the path to the new directory for deidentified images
num_samples = 100  # Number of samples per group
num_groups = 17  # Number of groups to create

create_csv_with_groups(folder_path, output_csv, output_dir, num_samples, num_groups)
