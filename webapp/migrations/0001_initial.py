# Generated by Django 3.2 on 2023-04-15 20:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MarketData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=20)),
                ('expiry', models.DateField()),
                ('underlying', models.CharField(max_length=20)),
                ('spot_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('interest_rate', models.DecimalField(decimal_places=4, max_digits=6)),
                ('volatility', models.DecimalField(decimal_places=4, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=4)),
                ('strike', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pv', models.DecimalField(decimal_places=2, max_digits=10)),
                ('market_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.marketdata')),
            ],
        ),
    ]