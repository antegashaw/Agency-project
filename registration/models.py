from django.db import models

class Applicant(models.Model):
    pass
    # ከዚህ በታች ያሉት መስኮች በሙሉ 4 ስፔስ ወደ ውስጥ መግባት አለባቸው (Indented)
    full_name = models.CharField(max_length=100)
    passport_no = models.CharField(max_length=50)
    # ያንተን የፎቶ መስክ እዚህ ጨምር
    passport_photo = models.ImageField(upload_to='passport_photos/', blank=True, null=True)
    
    def str(self):
        return self.full_name

class EmployeeApplication(models.Model):
   
class Applicant(models.Model):
    # ሌሎች የፎርም መረጃዎች እዚህ አሉ...
    full_photo = models.ImageField(upload_to='photos/', verbose_name="ሙሉ የቁም ፎቶ")
    half_photo = models.ImageField(upload_to='photos/', verbose_name="ጉርድ ፎቶ")
    GENDER_CHOICES = [('ወንድ', 'ወንድ'), ('ሴት', 'ሴት')]
        REGION_CHOICES = [
        ('አዲስ አበባ', 'አዲስ አበባ'), ('ድሬዳዋ', 'ድሬዳዋ'), ('ኦሮሚያ', 'ኦሮሚያ'),
        ('አማራ', 'አማራ'), ('ሲዳማ', 'ሲዳማ'), ('ደቡብ ኢትዮጵያ', 'ደቡብ ኢትዮጵያ'),
        ('ማዕከላዊ ኢትዮጵያ', 'ማዕከላዊ ኢትዮጵያ'), ('ደቡብ ምዕራብ ኢትዮጵያ', 'ደቡብ ምዕራብ ኢትዮጵያ'),
        ('ትግራይ', 'ትግራይ'), ('ሶማሌ', 'ሶማሌ'), ('አፋር', 'አፋር'),
        ('ቤንሻንጉል ጉሙዝ', 'ቤንሻንጉል ጉሙዝ'), ('ጋምቤላ', 'ጋምቤላ'), ('ሀረሪ', 'ሀረሪ')
    ]
    
    EDUCATION_CHOICES = [
        ('ያልተማረ/መጻፍ ማነብ', 'ያልተማረ/መጻፍ ማነብ'), ('1ኛ-8ኛ ክፍል', '1ኛ-8ኛ ክፍል'),
        ('9ኛ-12ኛ ክፍል', '9ኛ-12ኛ ክፍል'), ('ሰርተፍኬት (Certificate)', 'ሰርተፍኬት (Certificate)'),
        ('ዲፕሎማ (Diploma)', 'ዲፕሎማ (Diploma)'), ('የመጀመሪያ ዲግሪ (BSc/BA)', 'የመጀመሪያ ዲግሪ (BSc/BA)'),
        ('ማስተርስ እና ከዚያ በላይ', 'ማስተርስ እና ከዚያ በላይ')
    ]
    
    COUNTRY_CHOICES = [('ሳውዲ አረቢያ', 'ሳውዲ አረቢያ'), ('ዱባይ (UAE)', 'ዱባይ (UAE)'), ('ኩዌት', 'ኩዌት'), ('ኳታር', 'ኳታር'), ('ዮርዳኖስ', 'ዮርዳኖስ')]
    JOB_CHOICES = [('የቤት ሰራተኛ', 'የቤት ሰራተኛ'), ('ሹፌር', 'ሹፌር'), ('የህንጻ ጥበቃ', 'የህንጻ ጥበቃ'), ('የሆቴል ሰራተኛ', 'የሆቴል ሰራተኛ')]

    full_name = models.CharField("ሙሉ ስም", max_length=100)
    gender = models.CharField("ጾታ", max_length=10, choices=GENDER_CHOICES)
    age = models.IntegerField("ዕድሜ")
    phone_number = models.CharField("የስልክ ቁጥር", max_length=20)
    region = models.CharField("ያሉበት ክልል", max_length=50, choices=REGION_CHOICES)
    education_level = models.CharField("የትምህርት ደረጃ", max_length=50, choices=EDUCATION_CHOICES)
    destination_country = models.CharField("መሄድ የሚፈልጉት ሀገር", max_length=50, choices=COUNTRY_CHOICES)
    job_type = models.CharField("የሚፈልጉት የሥራ ዓይነት", max_length=50, choices=JOB_CHOICES)

    def str(self):
        return self.full_name