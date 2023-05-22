from django.db import models

# Create your models here.
class CountryData(models.Model):
    country = models.CharField(max_length=100)
    population = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Country Population Data'

    def __str__(self):
        return f'{self.country}-{self.population}'

class TaskDue(models.Model):
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
            ('Viễn thông tỉnh', 'Viễn thông tỉnh'),
			) 
    thuchien = (
			('Lê Minh Đức', 'Lê Minh Đức'),
			('Phạm Đình Nghĩa', 'Phạm Đình Nghĩa'),
            ('Hà Văn Huân', 'Hà Văn Huân'),
            ('Nguyễn Khắc Xuân Tùng', 'Nguyễn Khắc Xuân Tùng'),
            ('Nguyễn Tiến Dũng', 'Nguyễn Tiến Dũng'),
            ('Nguyễn Kế Toàn', 'Nguyễn Kế Toàn'),
            ('Nguyễn An', 'Nguyễn An'),
            ('Hà Đa Sĩ', 'Hà Đa Sĩ'),
			)
    number = models.AutoField(primary_key=True,auto_created=True,serialize=False,verbose_name='ID')
    taskjira = models.CharField(max_length=500,unique=True)
    taskcreate = models.DateTimeField()
    taskend = models.DateTimeField()
    excecute = models.CharField(max_length=200,choices=thuchien)
    request = models.CharField(max_length=200)
    department = models.CharField(max_length=200,choices=don_vi)

    class Meta:
        verbose_name_plural = 'Task Expired'

    def __str__(self):
        return f'{self.number}-{self.taskjira}-{self.taskcreate}-{self.taskend}-{self.excecute}-{self.request}-{self.department}'