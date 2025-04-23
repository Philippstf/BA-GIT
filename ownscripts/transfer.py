from huggingface_hub import hf_hub_download
import shutil
import os

# Zielverzeichnis für Videos + Annotations
target_dir = "./inference_data"
os.makedirs(target_dir, exist_ok=True)

# Liste deiner Videos
video_files = [
    f"Fehler{i}.mp4" for i in range(1, 31)
]

# Annotation
annotation_file = "annotations.json"

# Dataset
repo_id = "Philippstf/30vids"

# Videos herunterladen
for vf in video_files:
    video_path = hf_hub_download(repo_id=repo_id, filename=vf, repo_type="dataset")
    shutil.copy(video_path, os.path.join(target_dir, vf))

# Annotations.json herunterladen
anno_path = hf_hub_download(repo_id=repo_id, filename=annotation_file, repo_type="dataset")
shutil.copy(anno_path, os.path.join(target_dir, annotation_file))

print(f"✅ Dateien erfolgreich kopiert nach: {target_dir}")
