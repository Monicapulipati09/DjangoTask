from django.shortcuts import render

# Create your views here.
# from django.template import RequestContext
# from .forms import ArticleForm
# from django.conf import settings

# def index(request):
#     json = {
#         "all": {
#             "active": True
#         }
#     }
#     # for lang in settings.LANGUAGES:
#     #     data[lang.split(",")[1]] = ""
#     context = {}
#     form = ArticleForm(request.POST or None, initial={'Title':json})
#     if form.is_valid():
#         pass
#
#     context['form']= form
#     return render(request, "djangoapp/index.html", context)


# def policy_edit(request, pk):
#     policy = get_object_or_404(Policy, pk=pk)
#     if request.method == "POST":
#         form = PolicyForm(request.POST, instance=policy)
#         if form.is_valid():
#            post = form.save(commit=False)
#            post.config = form.data
#            post.save()
#            return redirect('ui:config-list')
#     else:
#         form = PolicyForm(instance=policy, initial={'data': policy.config})
  #  return render(request, 'index.html', {'form': form})