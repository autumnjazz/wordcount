from django.shortcuts import render

# Create your views here.

def home(request):
	return render(request, 'wordcount/home.html')
def about(request):
	return render(request, 'wordcount/about.html')
def count(request):
    full_text = request.GET['fulltext']
    #텍스트 변형
    word_list = full_text.lower().split()
    notchar_list = []
    modified = []
    for i in range(32, 127):
        if(64<i<91 or 96<i<123):
            pass
        else:
            notchar_list.append(chr(i))

    for word in word_list:
        index = []
        oh = []
        for n in notchar_list:
            if(n in word):
                index.append(n)
        if(index):
            for j in range(len(index)): # 3 -> 0 1 2 / 0/ 1 = 0.1 / 2=1.2/
                if(j == 0): 
                    oh.append(word.replace(index[j],""))
                else:
                    oh.append(oh[j-1].replace(index[j],""))
        if(oh):
            modified.append(oh[len(oh)-1])
        else:
            modified.append(word)

                

    word_dictionary = {}
    for word in modified:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1
    
    ordered = sorted(word_dictionary.items(), key=lambda t : t[1], reverse=True)

    return render(request, 'wordcount/count.html', {'fulltext': full_text, 'total': len(word_list), 'dictionary':ordered})