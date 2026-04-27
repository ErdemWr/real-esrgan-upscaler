import os
import sys
import cv2
import torch
from realesrgan import RealESRGANer
from basicsr.archs.rrdbnet_arch import RRDBNet

# ----------------------------
# 🔍 SYSTEM CHECK
# ----------------------------

if not torch.cuda.is_available():
    print("❌ CUDA GPU bulunamadı! CPU ile çalışacak.")
    device_gpu = False
else:
    print("✅ CUDA GPU bulundu:", torch.cuda.get_device_name(0))
    device_gpu = True

model_path = "RealESRGAN_x4plus_anime_6B.pth"

if not os.path.exists(model_path):
    print("❌ Model dosyası yok:", model_path)
    sys.exit()

input_path = "input.jpg"

if not os.path.exists(input_path):
    print("❌ input.jpg bulunamadı!")
    sys.exit()

# ----------------------------
# 🧠 MODEL
# ----------------------------

model = RRDBNet(
    num_in_ch=3,
    num_out_ch=3,
    num_feat=64,
    num_block=6,
    num_grow_ch=32,
    scale=4
)

upsampler = RealESRGANer(
    scale=4,
    model_path=model_path,
    model=model,
    tile=0,
    tile_pad=0,
    pre_pad=0,
    half=False,  # stable mode
    gpu_id=0 if device_gpu else None
)

# ----------------------------
# 📷 IMAGE LOAD
# ----------------------------

img = cv2.imread(input_path)

if img is None:
    print("❌ Görsel okunamadı!")
    sys.exit()

h, w = img.shape[:2]
print(f"📏 Input resolution: {w}x{h}")

# ----------------------------
# ⚡ UPSCALE
# ----------------------------

with torch.no_grad():
    output, _ = upsampler.enhance(img, outscale=1)

# ----------------------------
# 🎯 FORCE 1080p OUTPUT
# ----------------------------

target_w = 1920
target_h = 1080

output_1080p = cv2.resize(
    output,
    (target_w, target_h),
    interpolation=cv2.INTER_LANCZOS4
)

# ----------------------------
# 💾 SAVE
# ----------------------------

output_path = "output_1080p.png"
cv2.imwrite(output_path, output_1080p)

print("✅ Bitti! Çıktı:", output_path)
