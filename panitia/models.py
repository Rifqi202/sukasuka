from django.db import models

# Create your models here.


class pemilih(models.Model):
    namapemilih = models.TextField(default='')
    nikpemilih = models.IntegerField(unique=True)
    tempatpemilih = models.TextField(default='')
    nomerpemilih = models.IntegerField(default='13')
    emailpemilih = models.EmailField(max_length=224)
    password = models.CharField(max_length=8)


class tambahkandidat(models.Model):
    namakandidat = models.TextField(max_length=100, default='')
    nomerurut = models.IntegerField(default='')
    tempatlahir = models.TextField(max_length=100, default='')
    tanggallahir = models.CharField(max_length=200)
    alamat = models.TextField(max_length=100, default='')
    pengalaman = models.TextField(max_length=100, default='')
    prestasi = models.TextField(max_length=100, default='')
    visi = models.TextField(max_length=100, default='')
    misi = models.TextField(max_length=100, default='')
    programkerja = models.TextField(max_length=100, default='')
    kandidat_Main_Img = models.ImageField (upload_to='images/')

class tambahadmin(models.Model):
    namapanitia = models.TextField(default='')
    username = models.TextField(default='')
    emailpanitia = models.EmailField(max_length= 224)
    password = models.CharField(max_length= 8)


class judul(models.Model):
    judul = models.TextField(default='')
