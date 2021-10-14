from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Bird
from scipy.io import wavfile
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt
import numpy as np
import os
from scipy.io import wavfile
from PIL import Image 
import PIL 

birds=['American Coot','Americal Krestel','American Gold Finch','Bald Eagle','Peacock']
bird_dict={'American Coot':6,'American Gold Finch':7,'American Krestel':8,'Bald Eagle':15,'Peacock':23}

ip1=(217,334,3)
ip2=(200,200,3)

img_dict={'AFRICAN CROWNED CRANE': 0,
 'AFRICAN FIREFINCH': 1,
 'ALBATROSS': 2,
 'ALEXANDRINE PARAKEET': 3,
 'AMERICAN AVOCET': 4,
 'AMERICAN BITTERN': 5,
 'AMERICAN COOT': 6,
 'AMERICAN GOLDFINCH': 7,
 'AMERICAN KESTREL': 8,
 'AMERICAN PIPIT': 9,
 'AMERICAN REDSTART': 10,
 'ANHINGA': 11,
 'ANNAS HUMMINGBIRD': 12,
 'ARARIPE MANAKIN': 13,
 'ASIAN CRESTED IBIS': 14,
 'BALD EAGLE': 15,
 'BALI STARLING': 16,
 'BALTIMORE ORIOLE': 17,
 'BANANAQUIT': 18,
 'BANDED BROADBILL': 19,
 'BAR-TAILED GODWIT': 20,
 'BARN OWL': 21,
 'BARN SWALLOW': 22,
 'PEACOCK': 23}

img_list=[
     'AFRICAN CROWNED CRANE',
     'AFRICAN FIREFINCH',
     'ALBATROSS',
     'ALEXANDRINE PARAKEET',
     'AMERICAN AVOCET',
     'AMERICAN BITTERN',
     'AMERICAN COOT',
    'AMERICAN GOLDFINCH',
    'AMERICAN KESTREL',
    'AMERICAN PIPIT',
    'AMERICAN REDSTART',
    'ANHINGA',
    'ANNAS HUMMINGBIRD',
    'ARARIPE MANAKIN',
    'ASIAN CRESTED IBIS',
    'BALD EAGLE',
    'BALI STARLING',
    'BALTIMORE ORIOLE',
    'BANANAQUIT',
    'BANDED BROADBILL',
    'BAR-TAILED GODWIT',
    'BARN OWL',
    'BARN SWALLOW',
    'PEACOCK'
]

# This displays the index page    
def index(request):
    return render(request, 'FindBird/index.html')



# This class is used for the predictions
class predFunc:


    def SUB(request):
        return render(request, "FindBird/Submit1.html")


    '''Below Function is for Photo'''
    def predictionsPhoto(request):

        # This variable fetches the photo from front end
        if(request.method=='POST'):
            img = request.FILES['photo']

            # Write your model code here Sushil
            img = request.FILES['photo']
            im1 = Image.open(img)
            im1 = im1.save("bp.jpg")

            model=load_model('/Users/lakshmisha/Desktop/IBM_BIRD/Bird/FindBird/BirdModelFF.h5')
            img1=image.load_img('/Users/lakshmisha/Desktop/IBM_BIRD/Bird/bp.jpg',target_size=ip2)
            img1=image.img_to_array(img1)
            img1=np.expand_dims(img1,axis=0)
            index=img_dict.get(img_list[np.where((model.predict(img1))==1)[1][0]])

            a = index # Change this, It holds the value of id given my machine model
            try:
                obj = Bird.objects.get(bird_id = a)

            except:
                return error(request)

            return result(request, obj.slug)

        else:
            return error(request)



    # This is search function
    def search(request):
        return render(request, 'FindBird/search.html')



    '''Below function is for Audio'''
    def predictionsAudio(request):
        if(request.method=='POST'):
            audio = request.FILES['audio']

            # Write your model code here Sushil
            plt.axis('off')
            samplingFrequency, signalData = wavfile.read(audio)  
            Pxx, freqs, bins, im = plt.specgram(signalData,Fs=samplingFrequency,NFFT=512)
            plt.savefig('spec.png',bbox_inches='tight',pad_inches=0)

            model=load_model('/Users/lakshmisha/Desktop/IBM_BIRD/Bird/FindBird/BirdVoice_Final.h5')
            img=image.load_img('spec.png',target_size=ip1)
            img=image.img_to_array(img)
            img=np.expand_dims(img,axis=0)
            index=bird_dict.get(birds[np.where((model.predict(img))==1)[1][0]])

            a = index # Change this, It holds the value of id given my machine model
            try:
                obj = Bird.objects.get(bird_id = a)

            except:
                return error(request)

            return result(request, obj.slug)

        else:
            return error(request)



def result(request, slug):
    obj = Bird.objects.filter(slug=slug)
    return render(request, 'FindBird/Result3.html', {'i' : obj[0]})



# Finds the bird from search bar
def find(request):
    query = request.GET['query']
    query = query.lower()
    try:
        name = Bird.objects.get(search_name=query)
    except:
        return error(request)
    return result(request, name.slug)


# Throws out error page
def error(request):
    return render(request, "FindBird/Error.html")

# About Page
def about(request):
    return render(request, 'FindBird/About1.html')

def Allset(request):
    bird=Bird.objects.all()
    context = {'bird':bird}
    return render(request, 'FindBird/Allset1.html',context)