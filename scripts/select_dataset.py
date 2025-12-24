import os
import random
import shutil

SOURCE_DIR = "Dataset"
TARGET_DIR = "dataset_selected"
TARGET_PER_CLASS = 1500
SEED = 42

random.seed(SEED)

os.makedirs(TARGET_DIR, exist_ok=True)

for cls in os.listdir(SOURCE_DIR):
    src_cls = os.path.join(SOURCE_DIR, cls)
    dst_cls = os.path.join(TARGET_DIR, cls)
    os.makedirs(dst_cls, exist_ok=True)

    images = os.listdir(src_cls)
    selected = random.sample(images, TARGET_PER_CLASS)

    for img in selected:
        shutil.copy(
            os.path.join(src_cls, img),
            os.path.join(dst_cls, img)
        )

print("Dataset berhasil dikurangi 🎉")
