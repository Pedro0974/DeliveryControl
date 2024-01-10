# Generated by Django 4.0.7 on 2024-01-09 22:48

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('motoboys', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryFee',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modificado_em', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('price', models.FloatField(verbose_name='Price')),
            ],
            options={
                'verbose_name': 'Delivery Fee',
                'verbose_name_plural': 'Delivery Fees',
                'ordering': ('price',),
            },
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modificado_em', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Payment Method',
                'verbose_name_plural': 'Payment Methods',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modificado_em', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
                ('price', models.FloatField(verbose_name='Price')),
                ('status', models.CharField(choices=[('CREDITO', 'Credito'), ('DEBITO', 'Debito'), ('DINHEIRO', 'Dinheiro'), ('PIX', 'Pix'), ('PAGAMENTO ONLINE', 'Pagamento Online')], max_length=50, verbose_name='Status')),
                ('delivery_fee_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='deliveries.deliveryfee')),
                ('motoboy_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='motoboys.motoboy')),
                ('payment_method_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='deliveries.paymentmethod')),
            ],
            options={
                'verbose_name': 'Delivery',
                'verbose_name_plural': 'Deliveries',
                'ordering': ('date',),
            },
        ),
    ]
