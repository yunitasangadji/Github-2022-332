import os, shutil
from sklearn.model_selection import train_test_split

SOURCE_DIR = "dataset_selected"
TARGET_DIR = "dataset_split"
SEED = 42

train_ratio = 0.7
val_ratio = 0.15
test_ratio = 0.15

assert abs(train_ratio + val_ratio + test_ratio - 1.0) < 1e-6

for split in ["train", "val", "test"]:
    for cls in os.listdir(SOURCE_DIR):
        os.makedirs(os.path.join(TARGET_DIR, split, cls), exist_ok=True)

for cls in os.listdir(SOURCE_DIR):
    cls_path = os.path.join(SOURCE_DIR, cls)
    images = [f for f in os.listdir(cls_path) if os.path.isfile(os.path.join(cls_path, f))]

    train_files, temp_files = train_test_split(
        images, test_size=(1 - train_ratio), random_state=SEED, shuffle=True
    )
    val_files, test_files = train_test_split(
        temp_files, test_size=(test_ratio / (val_ratio + test_ratio)),
        random_state=SEED, shuffle=True
    )

    for f in train_files:
        shutil.copy(os.path.join(cls_path, f), os.path.join(TARGET_DIR, "train", cls, f))
    for f in val_files:
        shutil.copy(os.path.join(cls_path, f), os.path.join(TARGET_DIR, "val", cls, f))
    for f in test_files:
        shutil.copy(os.path.join(cls_path, f), os.path.join(TARGET_DIR, "test", cls, f))

print("Split dataset selesai ✅")
