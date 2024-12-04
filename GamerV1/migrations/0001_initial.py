# Generated by Django 4.2 on 2024-11-07 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('usuario', models.AutoField(primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=8)),
                ('direccion', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('cod_producto', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=40)),
                ('descripcion', models.CharField(max_length=100)),
                ('referencia', models.CharField(max_length=8)),
                ('modelo', models.CharField(max_length=100)),
                ('marca', models.CharField(max_length=60)),
                ('stock', models.IntegerField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GamerV1.usuario')),
            ],
        ),
    ]
