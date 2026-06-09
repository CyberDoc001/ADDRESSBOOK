from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.http import JsonResponse
from .models import Contact, Group
from .forms import ContactForm, GroupForm, SearchForm


def landing(request):
    if request.user.is_authenticated:
        return redirect('contact_list')
    return render(request, 'landing.html')


def register(request):
    if request.user.is_authenticated:
        return redirect('contact_list')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, 'Registration successful. Welcome to AddressBook!')
            return redirect('contact_list')
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})


@login_required(login_url='login')
def contact_list(request):
    query = request.GET.get('q', '')
    group_id = request.GET.get('group', '')
    show_favorites = request.GET.get('favorites', '')
    sort = request.GET.get('sort', 'name')

    contacts = Contact.objects.all()

    if query:
        contacts = contacts.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(email__icontains=query) |
            Q(phone__icontains=query) |
            Q(state__icontains=query) |
            Q(country__icontains=query)
        )

    if group_id:
        contacts = contacts.filter(group_id=group_id)

    if show_favorites:
        contacts = contacts.filter(is_favorite=True)

    if sort == 'name':
        contacts = contacts.order_by('first_name', 'last_name')
    elif sort == 'recent':
        contacts = contacts.order_by('-created_at')

    groups = Group.objects.all()
    total = contacts.count()

    # Group contacts alphabetically
    alpha_groups = {}
    for contact in contacts:
        letter = contact.first_name[0].upper() if contact.first_name else '#'
        if letter not in alpha_groups:
            alpha_groups[letter] = []
        alpha_groups[letter].append(contact)

    return render(request, 'contacts/list.html', {
        'contacts': contacts,
        'alpha_groups': dict(sorted(alpha_groups.items())),
        'groups': groups,
        'total': total,
        'query': query,
        'current_group': group_id,
        'show_favorites': show_favorites,
        'sort': sort,
        'search_form': SearchForm(initial={'q': query}),
    })

@login_required(login_url='login')
def contact_detail(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, 'contacts/detail.html', {'contact': contact})


@login_required(login_url='login')
def contact_create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            contact = form.save()
            messages.success(request, f'Contact "{contact.get_full_name()}" created successfully!')
            return redirect('contact_detail', pk=contact.pk)
    else:
        form = ContactForm()
    return render(request, 'contacts/form.html', {'form': form, 'title': 'Add Contact', 'action': 'Create'})

@login_required(login_url='login')
def contact_edit(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES, instance=contact)
        if form.is_valid():
            contact = form.save()
            messages.success(request, f'Contact "{contact.get_full_name()}" updated successfully!')
            return redirect('contact_detail', pk=contact.pk)
    else:
        form = ContactForm(instance=contact)
    return render(request, 'contacts/form.html', {'form': form, 'title': 'Edit Contact', 'action': 'Save Changes', 'contact': contact})


@login_required(login_url='login')
def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        name = contact.get_full_name()
        contact.delete()
        messages.success(request, f'Contact "{name}" deleted.')
        return redirect('contact_list')
    return render(request, 'contacts/confirm_delete.html', {'contact': contact})

@login_required(login_url='login')
def toggle_favorite(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    contact.is_favorite = not contact.is_favorite
    contact.save()
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({'is_favorite': contact.is_favorite})
    return redirect(request.META.get('HTTP_REFERER', 'contact_list'))


@login_required(login_url='login')
def group_list(request):
    groups = Group.objects.all()
    return render(request, 'contacts/groups.html', {'groups': groups})

@login_required(login_url='login')
def group_create(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            group = form.save()
            messages.success(request, f'Group "{group.name}" created!')
            return redirect('group_list')
    else:
        form = GroupForm()
    return render(request, 'contacts/group_form.html', {'form': form, 'title': 'New Group'})


@login_required(login_url='login')
def group_edit(request, pk):
    group = get_object_or_404(Group, pk=pk)
    if request.method == 'POST':
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            messages.success(request, f'Group updated!')
            return redirect('group_list')
    else:
        form = GroupForm(instance=group)
    return render(request, 'contacts/group_form.html', {'form': form, 'title': 'Edit Group', 'group': group})

@login_required(login_url='login')
def group_delete(request, pk):
    group = get_object_or_404(Group, pk=pk)
    if request.method == 'POST':
        group.delete()
        messages.success(request, 'Group deleted.')
        return redirect('group_list')
    return render(request, 'contacts/group_confirm_delete.html', {'group': group})
