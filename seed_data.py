import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'addressbook.settings')
django.setup()

from contacts.models import Contact, Group

# Groups
groups = {
    'Work': Group.objects.create(name='Work', color='#7c6af7'),
    'University': Group.objects.create(name='University', color='#34d399'),
    'Family': Group.objects.create(name='Family', color='#f87171'),
    'Sports': Group.objects.create(name='Sports', color='#fbbf24'),
}

contacts = [
    dict(first_name='Amina', last_name='Osei', email='amina.osei@gmail.com', phone='+234 801 234 5678',
         company='TechLagos', job_title='Software Engineer', city='Lagos', country='Nigeria',
         relationship='colleague', group=groups['Work'], is_favorite=True),
    dict(first_name='Kwame', last_name='Mensah', email='k.mensah@outlook.com', phone='+233 20 987 6543',
         company='Accra Finance', job_title='Product Manager', city='Accra', country='Ghana',
         relationship='colleague', group=groups['Work']),
    dict(first_name='Fatima', last_name='Al-Hassan', email='fatima.h@yahoo.com', phone='+971 50 123 4567',
         city='Dubai', country='UAE', relationship='friend', is_favorite=True),
    dict(first_name='David', last_name='Nwosu', email='dnwosu@company.ng', phone='+234 802 345 6789',
         company='Nwosu & Sons', job_title='CEO', city='Abuja', country='Nigeria',
         relationship='acquaintance', group=groups['Work']),
    dict(first_name='Sarah', last_name='Okafor', email='sarah.ok@unilag.edu.ng', phone='+234 803 456 7890',
         city='Lagos', country='Nigeria', relationship='friend', group=groups['University']),
    dict(first_name='Emmanuel', last_name='Boateng', email='eboateng@gmail.com', phone='+233 24 567 8901',
         city='Kumasi', country='Ghana', relationship='friend', group=groups['University'], is_favorite=True),
    dict(first_name='Grace', last_name='Osei', email='grace@family.com', phone='+234 805 678 9012',
         city='Port Harcourt', country='Nigeria', relationship='family', group=groups['Family']),
    dict(first_name='James', last_name='Adeyemi', email='james.a@email.com', phone='+234 806 789 0123',
         company='Lagos Athletic Club', job_title='Coach', city='Lagos', country='Nigeria',
         relationship='acquaintance', group=groups['Sports']),
    dict(first_name='Chioma', last_name='Eze', email='chioma.eze@techco.com', phone='+234 807 890 1234',
         company='FinTech Africa', job_title='Data Analyst', city='Lagos', country='Nigeria',
         relationship='colleague', group=groups['Work']),
    dict(first_name='Michael', last_name='Asante', email='m.asante@univ.gh', phone='+233 26 012 3456',
         city='Accra', country='Ghana', relationship='friend', group=groups['University']),
    dict(first_name='Zara', last_name='Ibrahim', email='zara.ibrahim@mail.com', phone='+234 808 123 4567',
         company='Media House NG', job_title='Journalist', city='Lagos', country='Nigeria',
         relationship='acquaintance'),
    dict(first_name='Oluwaseun', last_name='Adeleke', email='seun@adeleke.com', phone='+234 809 234 5678',
         city='Ibadan', country='Nigeria', relationship='family', group=groups['Family'], is_favorite=True),
]

for c in contacts:
    Contact.objects.create(**c)

print(f"✅ Created {len(contacts)} contacts and {len(groups)} groups")
