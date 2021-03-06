from django.db import models
from django.contrib.auth.models import User
from .utils import unique_slug_generator
from django.db.models import signals
from django.dispatch import receiver



class LaptopSpec(models.Model):
    Company = models.CharField(max_length=32)
    slug = models.SlugField(max_length=250, null=True, blank=True)
    Model = models.CharField(max_length=255)
    FullName = models.CharField(max_length=256, null=True, blank=True)
    DisplayName = models.CharField(
        max_length=128, null=True, blank=True, default="testing")
    Image = models.ImageField(upload_to="LapImages/", blank=True)
    # Physical info
    Weight = models.CharField(max_length=5)  # "Item Weight"
    Dimensions = models.CharField(max_length=20)  # "Product Dimensions"
    ScreenSize = models.CharField(max_length=4)  #
    ScreenResolution = models.CharField(max_length=10)
    MaxResolution = models.CharField(max_length=10)
    DisplayType = models.BooleanField(
        default=True
    )  # true if LED-backlight ...... false TFTLCD
    Color = models.CharField(max_length=10)
    Speaker = models.CharField(max_length=30, blank=True)
    # Wifi = models.BooleanField(default=True)
    # Bluetooth = models.DecimalField(
    #     default=5, max_digits=3, decimal_places=1
    # )  # Bluetooth-V(integerValue)
    # Infrared = models.BooleanField(default=False)
    # AudioType = models.CharField(max_length=30)
    # KeyboardBacklit = models.BooleanField(default=True)
    # OpticalDriveType = models.BooleanField(default=False)
    # CardReader = models.BooleanField(default=True)

    # PORTS
    PortsUsb2 = models.CharField(max_length=2)
    PortsUsb3 = models.CharField(max_length=2)
    PortsHdmi = models.CharField(max_length=2)
    PortsAudio = models.CharField(max_length=2)
    PortsEthernet = models.CharField(max_length=2)
    PortsMicrophone = models.CharField(max_length=2)
    PortsVga = models.CharField(max_length=2)
    # PortsCtype = models.PositiveIntegerField()     have to loook up for column type

    # RAM Hard drive and SSD info
    Ram = models.CharField(max_length=6)  # In Gb
    RamTechnology = models.CharField(max_length=8)
    # ExtraRam = models.PositiveIntegerField()  # In Gb
    HardDrive = models.CharField(
        max_length=10, default="512", blank=True)  # In Gb
    HardDriveType = models.CharField(max_length=12, default=None)  # In Gb

    # Battery
    Battery = models.CharField(max_length=15)
    # BatteryAvgLife = models.PositiveIntegerField()
    # BatteryAvgLifeStandby = models.PositiveIntegerField(blank=True)
    # PowerSource = models.CharField(default="Battery Powered", max_length=30, blank=True)

    Os = models.CharField(max_length=20)
    # INTEL = "Intel"
    # AMD = "Amd"
    # ProcCompanies = [
    #     (INTEL, "Intel"),
    #     (AMD, "Amd"),
    # ]
    ProcessorName = models.CharField(max_length=5)
    ProcessorSpeed = models.CharField(max_length=8)  # In ghz
    ProcessorType = models.CharField(max_length=20)
    # GraphicsCard = models.BooleanField(
    #     default=True
    # )  # True if Integrated .... false if Dedicated
    Graphics = models.CharField(max_length=25)

    IncludedComponents = models.TextField()
    SoftwareIncluded = models.TextField()
    DataLinkProtocol = models.CharField(
        default="IEEE 802.11 a/b/g/n/ac", max_length=20)
    # URL
    url = models.CharField(max_length=40, blank=True)
    def __str__(self):
        return self.DisplayName

@receiver(signals.pre_save, sender=LaptopSpec)
def set_slug(sender, instance,*args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance) 

class Type(models.Model):
    business = models.ManyToManyField(LaptopSpec, related_name="business")
    gaming = models.ManyToManyField(LaptopSpec, related_name="gaming")
    student = models.ManyToManyField(LaptopSpec, related_name="student")

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank = True)
    date = models.DateField(auto_now_add=True)
    counter = models.PositiveSmallIntegerField(default=0,null=True,blank=True)


    def add(self):
        if self.counter >= 0 and self.counter < 3:
            self.counter += 1
            self.save()
            return True
        else:
            return False
    def delete(self):
        if self.counter <=3 and self.counter > 0:
            self.counter -= 1
            self.save()
            return True
        else:
            return False

    def __str__(self):
        return str(self.id)


class cartItem(models.Model):
    laptop = models.ForeignKey(LaptopSpec, on_delete=models.SET_NULL, null=True, blank = True)
    cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True, blank = True)
    
    def __str__(self):
        return self.laptop.DisplayName