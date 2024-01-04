# Generated by Django 4.2.8 on 2023-12-26 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('babyapp', '0005_delete_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vaxcycle',
            name='name',
        ),
        migrations.RemoveField(
            model_name='vaxcycle',
            name='program',
        ),
        migrations.RemoveField(
            model_name='vaxprogram',
            name='child',
        ),
        migrations.RemoveField(
            model_name='vaxprogram',
            name='vax_program_name',
        ),
        migrations.DeleteModel(
            name='Vax',
        ),
        migrations.DeleteModel(
            name='VaxCycle',
        ),
        migrations.DeleteModel(
            name='VaxCycleName',
        ),
        migrations.DeleteModel(
            name='VaxProgram',
        ),
        migrations.DeleteModel(
            name='VaxProgramName',
        ),
    ]
