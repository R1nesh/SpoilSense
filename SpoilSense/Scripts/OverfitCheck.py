import os
import glob
from collections import defaultdict
# Update as needed
LBL_DIR = r'..\train\labels'

# Count how many images are in each cclass
class_image_counts = defaultdict(int)
total_images = 0

for lbl_path in glob.glob(os.path.join(LBL_DIR, "*.txt")):
    total_images += 1
    classes_in_image = set()
    with open(lbl_path, 'r') as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) == 5:
                c = int(float(parts[0]))
                classes_in_image.add(c)
    for c in classes_in_image:
        class_image_counts[c] += 1

# Clculate percentage of imageS for each class
for c in sorted(class_image_counts.keys()):
    percent = (class_image_counts[c] / total_images) * 100
    print(f"Class {c} is present in {class_image_counts[c]} images, which is {percent:.2f}% of total images ({total_images})")
