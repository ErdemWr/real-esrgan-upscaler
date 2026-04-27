# Real-Esrgan-UpScaler
An AI-powered image upscaling tool using Real-ESRGAN and PyTorch with NVIDIA CUDA acceleration. This script enhances low-resolution images by reconstructing details with deep learning.

---

# 🇹🇷 Yapay Zekâ Görüntü Yükseltici (Real-ESRGAN + CUDA)

Real-ESRGAN ve PyTorch kullanılarak geliştirilmiş, NVIDIA CUDA ile hızlandırılmış yapay zekâ tabanlı görüntü yükseltme aracıdır. Bu betik, düşük çözünürlüklü görselleri derin öğrenme ile analiz ederek eksik detayları yeniden oluşturur.

---

## 🚀 Features / Özellikler

### 🇬🇧 English
- AI-based image upscaling (up to 4x)
- NVIDIA GPU (CUDA) acceleration support
- Optimized for anime-style illustrations
- Fast processing on modern GPUs
- Lightweight and simple Python implementation

### 🇹🇷 Türkçe
- Yapay zekâ ile görüntü yükseltme (4x’e kadar)
- NVIDIA GPU (CUDA) desteği
- Anime tarzı illüstrasyonlar için optimize edilmiştir
- Modern ekran kartlarında hızlı çalışma
- Hafif ve basit Python tabanlı yapı

---

## 🧠 Requirements / Gereksinimler

### 🇬🇧 English
- Python 3.10+
- An NVIDIA GPU is highly recommended for performance.
- CUDA-enabled PyTorch environment.

### 🇹🇷 Türkçe
- Python 3.10+
- Performans için NVIDIA ekran kartı şiddetle tavsiye edilir.
- CUDA destekli PyTorch ortamı.

---

## ⚙️ Installation / Kurulum

### 🇬🇧 English
1.  **Clone the repository:**
    ```bash
    git clone https://github.com/erdemwr/real-esrgan-upscaler.git
    cd real-esrgan-upscaler
    ```

2.  **Download the Model:**
    The script requires the `RealESRGAN_x4plus_anime_6B.pth` model. Download it from the official [Real-ESRGAN model repository](https://github.com/xinntao/Real-ESRGAN/releases/download/v0.2.2.4/RealESRGAN_x4plus_anime_6B.pth) and place it in the project's root directory.

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### 🇹🇷 Türkçe
1.  **Depoyu klonlayın:**
    ```bash
    git clone https://github.com/erdemwr/real-esrgan-upscaler.git
    cd real-esrgan-upscaler
    ```

2.  **Modeli İndirin:**
    Betik, `RealESRGAN_x4plus_anime_6B.pth` modelini gerektirir. Modeli resmi [Real-ESRGAN model deposundan](https://github.com/xinntao/Real-ESRGAN/releases/download/v0.2.2.4/RealESRGAN_x4plus_anime_6B.pth) indirin ve projenin ana dizinine yerleştirin.

3.  **Gereksinimleri yükleyin:**
    ```bash
    pip install -r requirements.txt
    ```

---

## 💡 Usage / Kullanım

### 🇬🇧 English
1.  Place the image you want to upscale in the project's root directory and name it `input.jpg`.
2.  Run the upscaling script from your terminal:
    ```bash
    python upscale.py
    ```
3.  The script will check for a CUDA-enabled GPU. If found, it will use it for acceleration.
4.  The final image will be upscaled, resized to 1920x1080, and saved as `output_1080p.png` in the root directory.

### 🇹🇷 Türkçe
1.  Yükseltmek istediğiniz görseli projenin ana dizinine `input.jpg` olarak adlandırıp yerleştirin.
2.  Yükseltme betiğini terminalinizden çalıştırın:
    ```bash
    python upscale.py
    ```
3.  Betik, CUDA destekli bir GPU'nun varlığını kontrol edecek ve bulursa hızlandırma için kullanacaktır.
4.  Sonuç görseli yükseltilecek, 1920x1080 boyutuna yeniden boyutlandırılacak ve ana dizine `output_1080p.png` olarak kaydedilecektir.

---

## 📜 License / Lisans

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
