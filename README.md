# ROS 2 Sıcaklık İzleyici

## Proje Hakkında

Bu proje, ROS 2 Humble kullanılarak Python ile geliştirilmiş basit bir sıcaklık izleme uygulamasıdır. Sistem, rastgele sıcaklık değerleri üretir ve bu değerleri bir topic üzerinden başka bir düğüme iletir. Sıcaklık 30°C'nin üzerine çıktığında uyarı mesajı verir.

## Kullanılan Teknolojiler

- Ubuntu 22.04
- ROS 2 Humble
- Python
- `rclpy`
- `std_msgs`
- `rqt_graph`

## Paket Yapısı

```text
sicaklik_izleyici_py/
├── sicaklik_izleyici_py/
│   ├── __init__.py
│   ├── sensor.py
│   └── izleyici.py
├── resource/
├── package.xml
├── setup.py
└── README.md
```

## Çalışma Mantığı

1. `sicaklik_sensoru` düğümü 20–40°C arasında rastgele sıcaklık değeri üretir.
2. Sıcaklık değeri her saniye `/sicaklik` topic'i üzerinden yayınlanır.
3. `sicaklik_izleyici` düğümü yayınlanan verileri alır.
4. Sıcaklık 30°C'nin üzerine çıktığında uyarı mesajı gösterilir.
5. Sıcaklık uyarı eşiği ROS 2 parametresi kullanılarak değiştirilebilir.

## Kurulum ve Çalıştırma

### 1. Gereksinimler

- Ubuntu 22.04
- ROS 2 Humble
- Python 3
- Git
- `colcon`

### 2. Projeyi GitHub'dan indirme

```bash
git clone https://github.com/canonacan/sicaklik_izleyici_py.git
```

### 3. ROS 2 çalışma alanını oluşturma

```bash
mkdir -p ~/robotik/ros2_ws/src
mv sicaklik_izleyici_py ~/robotik/ros2_ws/src/
```

> Depoyu doğrudan `~/robotik/ros2_ws/src/` içine klonladıysanız `mv` komutunu çalıştırmayın.

### 4. Projeyi derleme

```bash
cd ~/robotik/ros2_ws
source /opt/ros/humble/setup.bash
rosdep install --from-paths src --ignore-src -r -y
colcon build --packages-select sicaklik_izleyici_py
source install/setup.bash
```

### 5. Sıcaklık sensörünü çalıştırma

Birinci terminalde:

```bash
source /opt/ros/humble/setup.bash
source ~/robotik/ros2_ws/install/setup.bash
ros2 run sicaklik_izleyici_py sensor
```

### 6. Sıcaklık izleyicisini çalıştırma

İkinci terminalde:

```bash
source /opt/ros/humble/setup.bash
source ~/robotik/ros2_ws/install/setup.bash
ros2 run sicaklik_izleyici_py izleyici
```

### 7. Sıcaklık eşik değerini değiştirme

Varsayılan sıcaklık uyarı eşiği 30°C'dir. Bu değer, `sicaklik_esigi` parametresiyle değiştirilebilir.

Örneğin, uyarı eşiğini 35°C yapmak için mevcut izleyici düğümünü `Ctrl + C` ile durdurun ve aşağıdaki komutla yeniden başlatın:

```bash
ros2 run sicaklik_izleyici_py izleyici --ros-args -p sicaklik_esigi:=35.0
```

Bu durumda sıcaklık 35°C'nin üzerine çıktığında uyarı mesajı gösterilir. Sensör düğümünü durdurmanız gerekmez.

### 8. ROS 2 düğüm grafiğini görüntüleme

Üçüncü terminalde:

```bash
source /opt/ros/humble/setup.bash
source ~/robotik/ros2_ws/install/setup.bash
ros2 run rqt_graph rqt_graph
```

## Beklenen Çıktı

Sıcaklık izleyici, gelen sıcaklık değerlerini terminalde gösterir. Sıcaklık belirlenen eşiği aştığında uyarı verir.

Örnek:

```text
Gelen sicaklik: 36.0 C
UYARI! Sicaklik 30 C ustunde: 36.0 C
```

## ROS 2 Düğüm Grafiği

Sistem üç bileşenden oluşur:

- `/sicaklik_sensoru`: Sıcaklık verilerini yayınlar.
- `/sicaklik`: Sıcaklık verilerinin aktarıldığı topic.
- `/sicaklik_izleyici`: Verileri alır ve sıcaklık eşiğini kontrol eder.

## GitHub Deposu

Projenin kaynak kodlarına aşağıdaki bağlantıdan ulaşabilirsiniz:

https://github.com/canonacan/sicaklik_izleyici_py

## Lisans

Bu proje eğitim ve öğrenme amacıyla geliştirilmiştir.
