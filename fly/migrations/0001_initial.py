# Generated by Django 3.1.2 on 2021-04-20 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('admin_id', models.AutoField(primary_key=True, serialize=False)),
                ('admin_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=20)),
                ('password', models.CharField(max_length=30)),
                ('contact', models.IntegerField()),
                ('otp', models.CharField(max_length=10, null=True)),
                ('otp_used', models.IntegerField()),
            ],
            options={
                'db_table': 'Admin',
            },
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('area_id', models.AutoField(primary_key=True, serialize=False)),
                ('area_name', models.CharField(max_length=15)),
                ('pincode', models.IntegerField()),
            ],
            options={
                'db_table': 'Area',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'Category',
            },
        ),
        migrations.CreateModel(
            name='Hall',
            fields=[
                ('hall_id', models.AutoField(primary_key=True, serialize=False)),
                ('hall_name', models.CharField(max_length=15)),
                ('contact', models.IntegerField()),
                ('address', models.CharField(max_length=100, null=True)),
                ('h_path', models.CharField(max_length=200)),
                ('hall_desc', models.CharField(max_length=1000)),
                ('area_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fly.area')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fly.category')),
            ],
            options={
                'db_table': 'Hall',
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('service_id', models.AutoField(primary_key=True, serialize=False)),
                ('service_type', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'Services',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=30)),
                ('contact', models.IntegerField(null=True)),
                ('otp', models.CharField(max_length=10)),
                ('otp_used', models.IntegerField()),
                ('area_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fly.area')),
            ],
            options={
                'db_table': 'User',
            },
        ),
        migrations.CreateModel(
            name='Packages',
            fields=[
                ('package_id', models.AutoField(primary_key=True, serialize=False)),
                ('package_name', models.CharField(max_length=10)),
                ('package_type', models.CharField(max_length=20)),
                ('package_desc', models.CharField(max_length=30)),
                ('package_price', models.IntegerField()),
                ('hall_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fly.hall')),
                ('service_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fly.services')),
            ],
            options={
                'db_table': 'Packages',
            },
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('owner_id', models.AutoField(primary_key=True, serialize=False)),
                ('owner_name', models.CharField(max_length=20)),
                ('owner_email', models.EmailField(max_length=100)),
                ('owner_password', models.CharField(max_length=30)),
                ('owner_contact', models.IntegerField(null=True)),
                ('otp', models.CharField(max_length=10)),
                ('otp_used', models.IntegerField()),
                ('area_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fly.area')),
            ],
            options={
                'db_table': 'Owner',
            },
        ),
        migrations.AddField(
            model_name='hall',
            name='owner_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fly.owner'),
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('gallery_id', models.AutoField(primary_key=True, serialize=False)),
                ('g_path', models.CharField(max_length=200)),
                ('hall_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fly.hall')),
            ],
            options={
                'db_table': 'Gallery',
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('feedback_id', models.AutoField(primary_key=True, serialize=False)),
                ('feedback_date', models.DateField()),
                ('description', models.CharField(max_length=30)),
                ('rate', models.IntegerField(verbose_name=5)),
                ('hall_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fly.hall')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fly.user')),
            ],
            options={
                'db_table': 'Feedback',
            },
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('booking_id', models.AutoField(primary_key=True, serialize=False)),
                ('booking_date', models.DateTimeField(auto_now=True)),
                ('total', models.IntegerField()),
                ('payment_status', models.IntegerField()),
                ('order_status', models.IntegerField()),
                ('req_date', models.DateField()),
                ('owner_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fly.owner')),
                ('package_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fly.packages')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fly.user')),
            ],
            options={
                'db_table': 'Booking',
            },
        ),
    ]
