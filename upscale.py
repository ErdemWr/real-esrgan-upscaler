from realesrgan import RealESRGANer
from basicsr.archs.rrdbnet_arch import RRDBNet
import cv2
import torch

# model
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
    model_path='RealESRGAN_x4plus_anime_6B.pth',
    model=model,
    tile=0,          # 🔥 KRİTİK: tile kapat
    tile_pad=0,
    pre_pad=0,
    half=False,      # 🔥 CPU/GPU uyum sorunu çözülür
    gpu_id=0
)

img = cv2.imread("input.jpg")

with torch.no_grad():
    output, _ = upsampler.enhance(img, outscale=1)

cv2.imwrite("output.png", output)

print("GPU stable çalıştı")