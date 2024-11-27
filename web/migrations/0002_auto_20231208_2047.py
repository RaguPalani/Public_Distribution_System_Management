# Generated by Django 3.2.22 on 2023-12-08 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CardDetails',
            fields=[
                ('card_number', models.IntegerField(primary_key=True, serialize=False)),
                ('head_of_house', models.CharField(max_length=30)),
                ('husband_or_father_name', models.CharField(max_length=30)),
                ('date_of_birth', models.DateField()),
                ('address', models.CharField(max_length=250)),
                ('total_member', models.IntegerField(max_length=2)),
                ('phone_number', models.IntegerField()),
                ('mail', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='CardEntitlement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=30, unique=True)),
                ('required_quantity', models.FloatField()),
                ('balance_quantity', models.FloatField()),
                ('card_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.carddetails')),
            ],
        ),
        migrations.CreateModel(
            name='DistrictCollector',
            fields=[
                ('id_number', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('district', models.CharField(max_length=30)),
                ('phone', models.IntegerField()),
                ('mail', models.CharField(max_length=255)),
                ('collector_name', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='DistrictSupplyOfficer',
            fields=[
                ('idnumber', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('designation', models.CharField(max_length=30)),
                ('district', models.CharField(max_length=30)),
                ('phone', models.IntegerField()),
                ('mail', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='ProductPrice',
            fields=[
                ('product_name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='RationShopOfficer',
            fields=[
                ('id_number', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=255)),
                ('phonenumber', models.IntegerField()),
                ('mail', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='RationShopStocks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('quantity', models.FloatField()),
                ('productname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.productprice')),
            ],
        ),
        migrations.CreateModel(
            name='ShopDetails',
            fields=[
                ('shopno', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('district', models.CharField(max_length=40)),
                ('taluk', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction_histroy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField(null=True)),
                ('total_cost', models.FloatField()),
                ('card_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.carddetails')),
                ('product_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.productprice')),
            ],
        ),
        migrations.DeleteModel(
            name='Member',
        ),
        migrations.AddField(
            model_name='rationshopstocks',
            name='rationshop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.shopdetails'),
        ),
        migrations.AddField(
            model_name='rationshopofficer',
            name='shopno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.shopdetails'),
        ),
        migrations.AddField(
            model_name='carddetails',
            name='shopno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.shopdetails'),
        ),
    ]