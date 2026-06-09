import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'addressbook.settings')
django.setup()

from contacts.models import Contact, Group

# Groups
groups = {
    'Work': Group.objects.create(name='Work', color='#059669'),
    'University': Group.objects.create(name='University', color='#10b981'),
    'Family': Group.objects.create(name='Family', color='#34d399'),
    'Sports': Group.objects.create(name='Sports', color='#fbbf24'),
}

contacts = [
    dict(first_name='Amina', last_name='Osei', email='amina.osei@gmail.com', phone='+234 801 234 5678', state='Lagos', country='Nigeria', group=groups['Work'], is_favorite=True),
    dict(first_name='Kwame', last_name='Mensah', email='k.mensah@outlook.com', phone='+233 20 987 6543', state='Accra', country='Ghana', group=groups['Work']),
    dict(first_name='Fatima', last_name='Al-Hassan', email='fatima.h@yahoo.com', phone='+971 50 123 4567', state='Dubai', country='UAE', is_favorite=True),
    dict(first_name='David', last_name='Nwosu', email='dnwosu@company.ng', phone='+234 802 345 6789', state='Abuja', country='Nigeria', group=groups['Work']),
    dict(first_name='Sarah', last_name='Okafor', email='sarah.ok@unilag.edu.ng', phone='+234 803 456 7890', state='Lagos', country='Nigeria', group=groups['University']),
    dict(first_name='Emmanuel', last_name='Boateng', email='eboateng@gmail.com', phone='+233 24 567 8901', state='Kumasi', country='Ghana', group=groups['University'], is_favorite=True),
    dict(first_name='Grace', last_name='Osei', email='grace@family.com', phone='+234 805 678 9012', state='Port Harcourt', country='Nigeria', group=groups['Family']),
    dict(first_name='James', last_name='Adeyemi', email='james.a@email.com', phone='+234 806 789 0123', state='Lagos', country='Nigeria', group=groups['Sports']),
    dict(first_name='Chioma', last_name='Eze', email='chioma.eze@techco.com', phone='+234 807 890 1234', state='Lagos', country='Nigeria', group=groups['Work']),
    dict(first_name='Michael', last_name='Asante', email='m.asante@univ.gh', phone='+233 26 012 3456', state='Accra', country='Ghana', group=groups['University']),
    dict(first_name='Zara', last_name='Ibrahim', email='zara.ibrahim@mail.com', phone='+234 808 123 4567', state='Lagos', country='Nigeria'),
    dict(first_name='Oluwaseun', last_name='Adeleke', email='seun@adeleke.com', phone='+234 809 234 5678', state='Ibadan', country='Nigeria', group=groups['Family'], is_favorite=True),
]

for c in contacts:
    Contact.objects.create(**c)

print(f"✅ Created {len(contacts)} contacts and {len(groups)} groups")
