from django import forms
from .models import CountryData, TaskDue
from django.core.validators import RegexValidator

class CountryDataFrom(forms.ModelForm):
    class Meta:
        model = CountryData
        fields = '__all__'

class TaskForm (forms.ModelForm):
    # Validation
    taskjira = forms.CharField(
        label='Task Jira', 
        min_length=10, 
        max_length=500, 
        widget=forms.TextInput(attrs={'placeholder': 'Nhập link task Jira, example:https://...'})
    )
    taskcreate = forms.DateField(
        label= 'Ngày bắt đầu',
        widget=forms.TextInput(attrs={'type': 'date'}), required=False
    )
    taskend = forms.DateField(
        label='Ngày hết hạn',
        widget=forms.TextInput(attrs={'type': 'date'}), required=True
    )
    PERSON = [
            ('', '---Chọn người thực hiện---'),
            ('Lê Minh Đức', 'Lê Minh Đức'),
			('Phạm Đình Nghĩa', 'Phạm Đình Nghĩa'),
            ('Hà Văn Huân', 'Hà Văn Huân'),
            ('Nguyễn Khắc Xuân Tùng', 'Nguyễn Khắc Xuân Tùng'),
            ('Nguyễn Tiến Dũng', 'Nguyễn Tiến Dũng'),
            ('Nguyễn Kế Toàn', 'Nguyễn Kế Toàn'),
            ('Nguyễn An', 'Nguyễn An'),
            ('Hà Đa Sĩ', 'Hà Đa Sĩ'),
        ]
    excecute = forms.CharField(
        label='Người thực hiện', max_length=200, min_length= 5,
        widget=forms.Select(attrs={'placeholder': 'Nhập tên người thực hiện'},choices=PERSON)
    )
    request= forms.CharField(
        label='Người yêu cầu',
    )

    don_vi = [
            ('', '---Chọn đơn vị yêu cầu---'),
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
	] 
    department= forms.CharField(
        label='Đơn vị yêu cầu',
        widget=forms.Select(choices=don_vi)
    )

    class Meta:
        model = TaskDue
        fields = '__all__'

      