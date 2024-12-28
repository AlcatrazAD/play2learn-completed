from django.contrib.auth import get_user_model
from django.views.generic import UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import CustomUserChangeForm


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Review
from .forms import ReviewForm

def review_list(request):
    reviews = Review.objects.all().order_by('-created_at')
    return render(request, 'reviews/review_list.html', {'reviews': reviews})

@login_required
def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            messages.success(request, "Your review has been submitted!")
            return redirect('reviews:review_list')
    else:
        form = ReviewForm()
    return render(request, 'reviews/add_review.html', {'form': form})





class MyAccountPageView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = CustomUserChangeForm
    template_name = 'account/my_account.html'

    def get_object(self):
        return self.request.user
    
    
