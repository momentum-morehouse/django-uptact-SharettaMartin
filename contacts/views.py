from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact, Note
from .forms import ContactForm, NoteForm


# Create your views here.
def list_contacts(request):
    contacts = Contact.objects.all()
    return render(request, "contacts/list_contacts.html",
                  {"contacts": contacts})


def add_contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_contacts')

    return render(request, "contacts/add_contact.html", {"form": form})


def edit_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'GET':
        form = ContactForm(instance=contact)
    else:
        form = ContactForm(data=request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect(to='list_contacts')

    return render(request, "contacts/edit_contact.html", {
        "form": form,
        "contact": contact
    })


def delete_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect(to='list_contacts')

    return render(request, "contacts/delete_contact.html",
                  {"contact": contact})

def list_notes(request, pk):
  #Line 53 says go to the database to contact and get me a pk
    contact = get_object_or_404(Contact, pk=pk)
    notes = Note.objects.filter(contact=contact)


    return render(request, "contacts/contact_detail.html", {
        "notes": notes,
        "contact": contact
    })


def add_NoteForm(request, pk):    
    if request.method == 'POST': 
         form = NoteForm(request.POST) 
         if form.is_valid():
            new_note = form.save(commit=False)
            new_note.contact_id = pk
            new_note.save()

            return redirect(to='contact_detail', pk=pk) 
             
    else:
        form = NoteForm()
        return render(request,"contacts/add_note.html",{"form": form, 
        })

def add_note(request):
    if request.method == 'GET':
        form = NoteForm()
    else:
        form = NoteForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='contact_details')

    return render(request, "contacts/add_contact.html", {"form": form})
#Created to allow me to 
def contact_detail(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request,"contacts/contact.detail.html",{"contact":contact})