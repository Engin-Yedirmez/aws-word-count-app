from django.shortcuts import render

# Create your views here.
def word_count(request):
    if request.method == 'POST':
        text = request.POST['text']
        word_count = len(text.split())
        return render(request, 'wordcount/result.html', {'count': word_count})
    return render(request, 'wordcount/wordcount.html')
