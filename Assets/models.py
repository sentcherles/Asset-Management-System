from django.db import models
from django.conf import settings
from django.urls import reverse
from PIL import Image
import qrcode
import os


class Asset(models.Model):
    name = models.CharField(max_length=255)
    serialNumber = models.CharField(max_length=255, unique=True)
    manufacturer = models.CharField(max_length=255)
    datePurchased = models.DateField()
    qr = models.ImageField(upload_to='assets/qrs/', blank=True, null=True)
    state = models.CharField(

        max_length=20,
        choices=[
            ('available', 'Available'),
            ('damaged', 'Damaged'),
            ('retired', 'Retired'),
        ],
        default='available',
    )

    def get_absolute_url(self):
        return reverse('assetDetail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.qr:
            try:
                qr_data = f"Asset Name: {self.name}\nSerial No: {self.pk}\nmanufacturer: {self.manufacturer}"
                qr = qrcode.QRCode(version=1, box_size=10, border=4)
                qr.add_data(qr_data)
                qr.make(fit=True)
                qr_image = qr.make_image(fill='black', back_color='white')
                qr_directory = os.path.join(settings.MEDIA_ROOT, 'assets/qrs')
                os.makedirs(qr_directory, exist_ok=True)
                qr_path = os.path.join(qr_directory, f"{self.id}_qr.png")
                qr_image.save(qr_path)

                self.qr = f"assets/qrs/{self.id}_qr.png"
                super().save(update_fields=['qr'])

            except Exception as e:
                print(f"QR code error: {e}")


    def get_absolute_url(self):
        return reverse('assetDetail', kwargs={'pk': self.pk})


