# Generated by Django 5.0.6 on 2024-06-05 18:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agentes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25, unique=True)),
                ('codigo_agente', models.CharField(blank=True, max_length=10, null=True)),
                ('razon_social', models.CharField(blank=True, max_length=50, null=True)),
                ('cuit', models.CharField(blank=True, max_length=50, null=True)),
                ('provincia', models.CharField(blank=True, max_length=25, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razon_social', models.CharField(max_length=50)),
                ('contacto', models.CharField(blank=True, max_length=50, null=True)),
                ('cuit', models.CharField(blank=True, max_length=50, null=True)),
                ('direccion', models.CharField(blank=True, max_length=80, null=True)),
                ('telefono', models.CharField(blank=True, max_length=50, null=True)),
                ('Obs', models.CharField(blank=True, max_length=100, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pagos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('importe', models.DecimalField(decimal_places=2, max_digits=18)),
                ('imagen', models.FileField(blank=True, null=True, upload_to='pagos_imagen')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('agente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.agentes')),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.proveedores')),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('Porc_costo', models.DecimalField(decimal_places=2, max_digits=18)),
                ('Porc_venta', models.DecimalField(decimal_places=2, max_digits=18)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.proveedores')),
            ],
        ),
        migrations.CreateModel(
            name='CuentaCorriente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('tipo_documento', models.CharField(choices=[('FC', 'FC'), ('FCE', 'FCE'), ('NC', 'NC'), ('NCE', 'NCE'), ('ND', 'ND')], max_length=30)),
                ('nro_documento', models.CharField(max_length=50)),
                ('alicuota', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('importe', models.DecimalField(decimal_places=2, max_digits=18)),
                ('importe_final', models.DecimalField(blank=True, decimal_places=2, max_digits=18, null=True)),
                ('fecha_devolucion', models.DateField(blank=True, null=True)),
                ('fecha_vencimiento', models.DateField()),
                ('estado', models.CharField(choices=[('Pendiente', 'Pendiente'), ('Vencido', 'Vencido'), ('Liquidado', 'Liquidado')], default='Pendiente', max_length=30)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('agente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.agentes')),
                ('pago', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.pagos')),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.proveedores')),
            ],
        ),
        migrations.CreateModel(
            name='Salidas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_salida', models.DateField()),
                ('edicion', models.CharField(max_length=15)),
                ('pvp', models.DecimalField(decimal_places=2, max_digits=18)),
                ('ri', models.DecimalField(decimal_places=2, max_digits=18)),
                ('p_costo', models.DecimalField(decimal_places=2, max_digits=18)),
                ('P_venta', models.DecimalField(decimal_places=2, max_digits=18)),
                ('alicuota', models.DecimalField(decimal_places=2, max_digits=5)),
                ('cantidad', models.IntegerField()),
                ('devolucion', models.IntegerField(blank=True, null=True)),
                ('Venta', models.IntegerField(blank=True, null=True)),
                ('importe', models.DecimalField(blank=True, decimal_places=2, max_digits=18, null=True)),
                ('fecha_devolucion', models.DateField()),
                ('estado', models.CharField(choices=[('Pendiente', 'Pendiente'), ('Vencido', 'Vencido'), ('Liquidado', 'Liquidado')], max_length=20)),
                ('nro_pago', models.CharField(blank=True, max_length=20, null=True)),
                ('fecha_pago', models.DateField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('Proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.proveedores')),
                ('agente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.agentes')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.productos')),
            ],
        ),
    ]