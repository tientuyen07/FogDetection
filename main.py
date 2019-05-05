
# cong thuc
# lamda = (a*H)/cos(phi)

# phi = 0 khi dat may anh thang dung, truc may anh song song mat dat
# H = chieu cao tu may anh den mat dat = 1.5 m
# a = f/tpu = f/tpv voi f la tieu cu, tpu = tpv = kich thuoc cua mot pixel

# camera:  https://www.xiaomiviet.vn/camera-hanh-trinh-g300-full-hd.html
# Thong so camera: https://shopee.vn/Camera-h%C3%A0nh-tr%C3%ACnh-Qihoo-360-Smart-Dash-Cam-G300-H%C3%A3ng-ph%C3%A2n-ph%E1%BB%91i-ch%C3%ADnh-th%E1%BB%A9c-i.97959351.1642325508
# f = 2.2 mm = 2.2 x 10^-3 m

# camera sensor: https://www.dipol.pt/camara_ip_compacta_signal_hdc-260p_2mp_2_8-12mm_0_01_lx_iv_ate_40m_h_265-h_264_poe__K1877.htm
# Thong so camera sensor: https://www.unifore.net/product-highlights/sony-imx323-cmos-image-sensor.html
# Hieu hon ve cac thong so: https://www.techspot.com/guides/850-smartphone-camera-hardware/page2.html

# tpu = tpv = 2.8 x 10^-6 m

a = (2.2/2.8)*1000
H = 1.5
lamda = a*H
vi = 478 # Tu file InflectionPoint
vh = 480 # Tu file RansacVanishingPoint
k = -2*(vi - vh)/lamda # Dau am vi tinh do lon vi vh tu tren xuong duoi buc anh

khoangcach = 3/k

print khoangcach




