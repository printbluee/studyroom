from django.shortcuts import render

def main(requset):
    return render(requset, 'index.html')