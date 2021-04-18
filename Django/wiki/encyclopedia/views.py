from django import forms
from django.shortcuts import render
from markdown2 import Markdown
from django.urls import reverse
from django.http import HttpResponseRedirect
from . import util
import os
import random

# Django form for adding a new article to the disk.
class add_article(forms.Form):
    title = forms.CharField(label="Title of the article:")
    content = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":4},))



def edit(request, title):
    # util based method returened list of all the .md filenames
    all_entries = util.list_entries()
    # Casefolded list of entries based on all_entries
    casefold_entries = [tmp.casefold() for tmp in all_entries]
    title = title.casefold()
    i = casefold_entries.index(title)
    if request.method == "GET":
        edit_form = add_article(initial={'title': title.capitalize(), 'content' : util.get_entry(all_entries[i]) })
        return render(request, 'encyclopedia/edit.html', {
            "form" : edit_form,
            "heading" : title.capitalize(),
            })
    else:
        form = add_article(request.POST)
        if form.is_valid():
            # then save the contents of the markdown into a newfile .md file to given pathed directory.
            path = "/home/pragat/Downloads/PostCS50/PSETS/wiki/entries"
            # name this file <title.capitalize()>
            file = all_entries[i] +'.md'
            # open this created file
            with open(os.path.join(path, file), 'w') as fp:
                # write the markdown into this file.
                fp.write(form.cleaned_data["content"])
                # close the file.
                fp.close()
            return HttpResponseRedirect(reverse("wiki_page", kwargs={'title': all_entries[i]}))

def wiki_random(request):
    all_entries = util.list_entries()
    n = random.randint(0,len(all_entries)-1)
    md = Markdown()
    # With help of get_entry from util.py fetch the markdown ContentFile.
    entry = util.get_entry(all_entries[n])
    exist = True

    # convert markdown to HTML using convert method from markdown2
    md = md.convert(entry)
    # return the html and title to wiki_page.html
    return render(request, "encyclopedia/wiki_page.html", {
        "title" : all_entries[n].capitalize(),
        "exist" : exist,
        "html"  : md,
        })






# Index view loads the list of existing articles inside our encyclopedia.
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
    })


# View from which user proceeds to add new article.
def wiki_add(request):
    # On get requests
    if request.method == "GET":
        # render the form to add new article
        return render(request, 'encyclopedia/add.html',{
            "form" : add_article()
        })

    # On form submission
    if request.method == "POST":
        # store the form data into an object of class add_article.
        new_page = add_article(request.POST)
        # If the form is valid
        if new_page.is_valid():
            # store the markdown into a variable content.
            content = new_page.cleaned_data["content"]
            # Casefolded list of all existing entires
            entries = [item.casefold() for item in util.list_entries()]
            # If there's already an article under that title
            if new_page.cleaned_data["title"].casefold() in entries:
                # present the user with the error.
                return render(request, 'encyclopedia/add.html', {
                    "error" : True,
                    "title" : new_page.cleaned_data["title"].capitalize()
                })
            # If this is a unique title,
            else:
                # then save the contents of the markdown into a newfile .md file to given pathed directory.
                path = "./entries"
                # name this file <title.capitalize()>
                file = (new_page.cleaned_data["title"]+'.md').capitalize()
                # open this created file
                with open(os.path.join(path, file), 'w') as fp:
                    # write the markdown into this file.
                    fp.write(content)
                    # close the file.
                    fp.close()
                # Return index on successfull addition of new article.
                return HttpResponseRedirect(reverse("index"))
        else:
            # in  calse of get request get the form view.
            return render(request, 'encyclopedia/add.html',{
                "form": new_page,
                "error": False
            })




def wiki_view(request, title):

    # util based method returened list of all the .md filenames
    all_entries = util.list_entries()
    # Casefolded list of entries based on all_entries
    casefold_entries = [tmp.casefold() for tmp in all_entries]


    # When users performs a search it actions this view with post method
    if request.method == "POST":
        # and we retrive the form data and stores it in a variable called title.
        title = request.POST.get('q', 'default_if_not_found_value')
        # Casefold the title so we can ignore cases!
        title = title.casefold()
        # Try to retrive the index of casefolded title in casefolded entries list.
        try:
            # This also retrieves the index in the all_entries list!
            i = casefold_entries.index(title)
        # if it's not in the list than python will through an ValueError. so except this.
        except ValueError:
            # articles with matched substring with the search query.
            matched_sstring = []
            # just to keep track of index
            j = 0
            # checking for string matching
            for item in casefold_entries:
                tmp = item.find(title)
                # if matched then append it in matched string list with cases as in all_entries
                if tmp != -1:
                    matched_sstring.append(all_entries[j])
                j += 1

            if len(matched_sstring) > 0:
                # If in doesn't exist and matched_sstring list in not empty then render index.html with matched_sstrings.
                return render(request, "encyclopedia/index.html", {
                    "entries" : matched_sstring,
                    })
            else:
                # if there are no matched sub-string then just say article not-found.
                return render(request, "encyclopedia/wiki_page.html", {
                    "title" : title.capitalize(),
                    "exist" : False,
                    })

    else:
        # Casefolding the title in case user has messed up in cases for an article name.
        title = title.casefold()
        # Try to find the titled article in the casefolded list !
        try:
            # This also retrieves the index in the all_entries list!
            i = casefold_entries.index(title)
        except ValueError:
            # If in doesn't exist then render wiki_page.html with error message. That article not found.
            return render(request, "encyclopedia/wiki_page.html", {
                "title" : title.capitalize(),
                "exist" : False,
                })

    # Initialize an empty Markdown object
    md = Markdown()
    # With help of get_entry from util.py fetch the markdown ContentFile.
    entry = util.get_entry(all_entries[i])
    exist = True

    # convert markdown to HTML using convert method from markdown2
    md = md.convert(entry)
    # return the html and title to wiki_page.html
    return render(request, "encyclopedia/wiki_page.html", {
        "title" : title.capitalize(),
        "exist" : exist,
        "html"  : md,
        })
