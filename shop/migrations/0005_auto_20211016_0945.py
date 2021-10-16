# Generated by Django 3.2.7 on 2021-10-16 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_order_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='VarietySpec',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
            ],
        ),
        migrations.AddField(
            model_name='orderitem',
            name='variety',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.varietyspec'),
        ),
        migrations.AddField(
            model_name='product',
            name='available_varieties',
            field=models.ManyToManyField(to='shop.VarietySpec'),
        ),
    ]