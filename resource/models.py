from django.db import models

# Create your models here.


class Site(models.Model):
    site_id = models.CharField(max_length=100, primary_key=True)
    site_name = models.CharField(max_length=200)

    def __str__(self):
        return self.site_id

class IP_public_test(models.Model):
    don_vi = (
			('Trung tâm Điều hành IT', 'Trung tâm Điều hành IT'),
			('Trung tâm Chính phủ điện tử', 'Trung tâm Chính phủ điện tử'),
            ('Trung tâm Y tế điện tử', 'Trung tâm Y tế điện tử'),
            ('Trung tâm Sáng tạo (IC)', 'Trung tâm Sáng tạo (IC)'),
            ('Trung tâm Giáo dục điện tử', 'Trung tâm Giáo dục điện tử'),
            ('Trung tâm Giải pháp tích hợp hệ thống', 'Trung tâm Giải pháp tích hợp hệ thống'),
            ('Trung tâm An toàn thông tin', 'Trung tâm An toàn thông tin'),
            ('Trung tâm giải pháp Quản trị doanh nghiệp', 'Trung tâm giải pháp Quản trị doanh nghiệp'),
            ('Trung tâm IT Khu vực 1', 'Trung tâm IT Khu vực 1'),
            ('Trung tâm IT Khu vực 2', 'Trung tâm IT Khu vực 2'),
            ('Trung tâm IT Khu vực 3', 'Trung tâm IT Khu vực 3'),
            ('Trung tâm IT Khu vực 4', 'Trung tâm IT Khu vực 4'),
            ('Trung tâm IT Khu vực 5', 'Trung tâm IT Khu vực 5'),
            ('Ban Kỹ thuật hạ tầng', 'Ban Kỹ thuật hạ tầng'),
            ('Trung tâm Hạ tầng IDC', 'Trung tâm Hạ tầng IDC'),
            ('Ban Chất lượng sản phẩm', 'Ban Chất lượng sản phẩm'),
            ('Ban Tiếp thị Bán hàng', 'Ban Tiếp thị Bán hàng'),
            ('Ban Kế toán Tài chính', 'Ban Kế toán Tài chính'),
            ('Ban Chiến lược sản phẩm', 'Ban Chiến lược sản phẩm'),
            ('Ban Kế hoạch Đầu tư', 'Ban Kế hoạch Đầu tư'),
            ('Ban Quản lý dự án', 'Ban Quản lý dự án'),
			) 

    thiet_bi = (
            ('SRX 5400 IDC NTL (2019)', 'SRX 5400 IDC NTL (2019)'),
            ('SRX 5400 IDC NTL (2020)', 'SRX 5400 IDC NTL (2020)'),
            ('SRX 5400 IDC NTL (2021)', 'SRX 5400 IDC NTL (2021)'),
			('F5-7600-IDC NTL (2019)-10.193.8.15', 'F5-7600-IDC NTL (2019)-10.193.8.15'),
			('F5-7200 IDC NTL (2019)-10.193.79.5', 'F5-7200 IDC NTL (2019)-10.193.79.5'),
            ('F5-DDOS IDC NTL', 'F5-DDOS IDC NTL'),
            ('WAF-F5-7600 IDC NTL (2020)-10.163.0.15', 'WAF-F5-7600 IDC NTL (2020)-10.163.0.15'),
            ('WAF-I7800-IDC NTL (2021)-10.169.9.57', 'WAF-I7800-IDC NTL (2021)-10.169.9.57'),
            ('LTM-7600-IDC NTL (2021)-10.169.9.59', 'LTM-7600-IDC NTL (2021)-10.169.9.59'),
            ('SRX 5400 IDC TTN (2019)', 'SRX 5400 IDC TTN (2019)'),
            ('SRX 5400 IDC TTN (2020)', 'SRX 5400 IDC TTN (2020)'),
            ('SRX 5400 IDC TTN (2021)', 'SRX 5400 IDC TTN (2021)'),
            ('F5-7200  IDC TTN (2019)-10.195.8.3', 'F5-7200  IDC TTN (2019)-10.195.8.3'),
            ('F5-7200_NEW IDC TTN (2019)-10.159.128.195', 'F5-7200_NEW IDC TTN (2019)-10.159.128.195'),
            ('WAF-F5-7600 IDC TTN (2020)-10.163.128.15', 'WAF-F5-7600 IDC TTN (2020)-10.163.128.15'),
            ('LTM-7600-IDC TTN (2021)-10.169.41.57', 'LTM-7600-IDC TTN (2021)-10.169.41.57'),
            ('WAF-I7800-IDC TTN (2021)', 'WAF-I7800-IDC TTN (2021)'),
            ('Checkpoint ADN', 'Checkpoint ADN'),
			) 

    ip_public = models.CharField(max_length=100, primary_key=True)
    ip_privates = models.CharField(max_length=500, null=True, blank=True)
    dichvu = models.CharField(max_length=200,null=True, blank=True)
    ngay_cp = models.DateField(null=True, blank=True)
    nguoi_duoc_cp = models.CharField(max_length=200,null=True, blank=True)
    don_vi_duoc_cp = models.CharField(max_length=200,null=True, blank=True, choices=don_vi)
    muc_dich_cp = models.CharField(max_length=500, null=True, blank=True)
    ma_IT360_or_VB = models.CharField(max_length=200,null=True, blank=True)
    tren_thiet_bi = models.CharField(max_length=200,null=True, blank=True, choices=thiet_bi)

    class Meta:
        verbose_name_plural = 'IPv4 public Management'

    def __str__(self):
        return self.ip_public