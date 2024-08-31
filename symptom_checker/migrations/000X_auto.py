from django.db import migrations

def add_conditions(apps, schema_editor):
    Condition = apps.get_model('symptom_checker', 'Condition')
    conditions = [
        ('Common Cold', 'cough, sore throat, runny nose, sneezing'),
        ('Influenza (Flu)', 'fever, chills, muscle aches, cough, congestion'),
        ('COVID-19', 'fever, cough, fatigue, loss of taste, difficulty breathing'),
        ('Lung Cancer', 'persistent cough, chest pain, weight loss, coughing up blood'),
        # ('Breast Cancer', 'lump in breast, breast pain, nipple discharge'),
        ('Malaria', 'fever, chills, sweating, headache, muscle pain'),
        ('Dengue Fever', 'high fever, severe headache, pain behind the eyes, joint pain'),
        ('Diabetes', 'increased thirst, frequent urination, hunger, fatigue, blurred vision'),
    ]
    for name, symptoms in conditions:
        Condition.objects.create(name=name, symptoms=symptoms)

class Migration(migrations.Migration):

    dependencies = [
        ('symptom_checker', '0001_initial'),  # replace with your previous migration file
    ]

    operations = [
        migrations.RunPython(add_conditions),
    ]
