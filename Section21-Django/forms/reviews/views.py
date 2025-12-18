from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ReviewForm
from .models import Review

def review(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            username = form.cleaned_data["username"]
            review_text = form.cleaned_data["review"]
            rating = form.cleaned_data["rating"]
            review = Review(
                name=name,
                username=username,
                review=review_text,
                rating=rating
            )
            review.save()
            request.session["name"] = name
            return HttpResponseRedirect(reverse("feedback"))
    form = ReviewForm()
    return render(request, "reviews/review.html", {
        "form":form
    })

def feedback(request):
    name = request.session.get("name")
    return render(request, "reviews/feedback.html", {
        'name':name
    })