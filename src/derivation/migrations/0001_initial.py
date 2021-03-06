# Generated by Django 3.2.6 on 2021-08-12 15:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('run', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('O', 'Other'), ('F', 'Female'), ('M', 'Male')], max_length=1)),
                ('phone', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
                ('adress', models.CharField(max_length=50)),
                ('birthday', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('personal_information', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='derivation.personalinformation')),
                ('health_plan_insurance', models.CharField(choices=[('fon', 'Fonasa'), ('isa', 'Isapre'), ('oth', 'Other')], max_length=3)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Clinic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TherapySession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('attendance', models.BooleanField()),
                ('pay', models.BooleanField()),
                ('pay_date', models.DateField()),
                ('modality', models.CharField(choices=[('onl', 'Online'), ('prs', 'Presential')], max_length=3)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='derivation.patient')),
            ],
            options={
                'ordering': ('-date',),
            },
        ),
        migrations.CreateModel(
            name='Professional',
            fields=[
                ('personal_information', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='derivation.personalinformation')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.AddField(
            model_name='patient',
            name='clinic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='derivation.clinic'),
        ),
        migrations.AddField(
            model_name='patient',
            name='professional',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='derivation.professional'),
        ),
        migrations.CreateModel(
            name='EmergencyContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='derivation.patient')),
            ],
        ),
    ]
