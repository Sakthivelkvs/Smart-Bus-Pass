# Generated by Django 4.2.5 on 2023-12-03 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AccNo', models.CharField(max_length=100)),
                ('ifsc', models.CharField(max_length=100)),
                ('hoder_name', models.CharField(max_length=100)),
                ('amount', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Charge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('From_Place', models.CharField(max_length=100)),
                ('To_Place', models.CharField(max_length=100)),
                ('Type', models.CharField(max_length=100)),
                ('Amouont', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Depo_officer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Gender', models.CharField(max_length=100)),
                ('Date_of_birth', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=100)),
                ('Phone_Number', models.CharField(max_length=100)),
                ('Depo', models.CharField(default='', max_length=100)),
                ('Proof', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pass_req',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('From_place', models.CharField(max_length=100)),
                ('To_Place', models.CharField(max_length=100)),
                ('Type', models.CharField(max_length=100)),
                ('Date', models.DateField()),
                ('Time_period', models.CharField(max_length=100)),
                ('Amouont', models.CharField(max_length=100)),
                ('id_proof', models.CharField(default='', max_length=200)),
                ('Status', models.CharField(default='', max_length=100)),
                ('DEPO_OFFICER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.depo_officer')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Gender', models.CharField(max_length=100)),
                ('Date_of_birth', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=100)),
                ('Phone_Number', models.CharField(max_length=100)),
                ('House_Name', models.CharField(max_length=100)),
                ('Place', models.CharField(max_length=100)),
                ('City', models.CharField(max_length=100)),
                ('State', models.CharField(default='', max_length=100)),
                ('Pincode', models.CharField(max_length=100)),
                ('Photo', models.CharField(max_length=200)),
                ('LOGIN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.login')),
            ],
        ),
        migrations.CreateModel(
            name='Updated_pass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Valid_from', models.DateField()),
                ('Expiry_date', models.DateField()),
                ('Status', models.CharField(max_length=100)),
                ('PASS_REQ', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.pass_req')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('Account_Number', models.CharField(max_length=100)),
                ('Status', models.CharField(max_length=100)),
                ('Amount', models.CharField(max_length=100)),
                ('PASS_REQ', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.pass_req')),
                ('USERS', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.users')),
            ],
        ),
        migrations.AddField(
            model_name='pass_req',
            name='USERS',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.users'),
        ),
        migrations.AddField(
            model_name='depo_officer',
            name='LOGIN',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.login'),
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('Complaints', models.CharField(max_length=300)),
                ('status', models.CharField(max_length=100)),
                ('reply', models.CharField(max_length=200)),
                ('USERS', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.users')),
            ],
        ),
        migrations.CreateModel(
            name='Cancel_pass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('Status', models.CharField(max_length=100)),
                ('Reason', models.CharField(default='', max_length=200)),
                ('PASS_REQ', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.pass_req')),
            ],
        ),
    ]
