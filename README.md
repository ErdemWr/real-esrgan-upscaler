# 🚀 AI Image Upscaler (Real-ESRGAN + CUDA)

An AI-powered image upscaling tool built with Real-ESRGAN and PyTorch.  
It enhances low-resolution images by reconstructing missing details using deep learning and NVIDIA GPU acceleration.

---

# 🇹🇷 Yapay Zekâ Görüntü Yükseltici (Real-ESRGAN + CUDA)

Real-ESRGAN ve PyTorch kullanılarak geliştirilmiş yapay zekâ tabanlı görüntü yükseltme aracıdır.  
Düşük çözünürlüklü görselleri derin öğrenme ile analiz ederek eksik detayları yeniden oluşturur ve NVIDIA GPU ile hızlandırır.

---

## 🚀 Features / Özellikler

### 🇬🇧 English
- AI-based image upscaling (up to 4x)
- NVIDIA GPU (CUDA) acceleration support
- Anime and real photo enhancement
- Fast processing on RTX series GPUs
- Lightweight Python implementation

### 🇹🇷 Türkçe
- Yapay zekâ ile görüntü yükseltme (4x’e kadar)
- NVIDIA GPU (CUDA) desteği
- Anime ve gerçek fotoğraf iyileştirme
- RTX serisi ekran kartlarında hızlı çalışma
- Hafif Python tabanlı yapı

---

## 🧠 Requirements / Gereksinimler

### 🇬🇧 English
Before running the project, make sure you have:

- Python 3.10+
- NVIDIA GPU (recommended: RTX series)
- CUDA-enabled PyTorch
- Required Python packages:

```bash
pip install torch==2.0.1 torchvision==0.15.2
pip install realesrgan basicsr opencv-python
