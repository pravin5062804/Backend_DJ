from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def workout(request):
    return HttpResponse("<h1>Do Fullbody exercise</h1>")


def chest(request):
    return HttpResponse("<h1>Do Chest Excercise</h1>")

def back(request):
    return HttpResponse("<h1>Do back Excercise</h1>")


def shoulder(request):
    return HttpResponse("<h1>Do shoulder Excercise</h1>")

def legs(request):
    return HttpResponse("<h1>Do legs Excercise</h1>")



def abs(request):
    return HttpResponse("<h1>Do abs Excercise</h1>")

def comeback(request):
    return HttpResponse(""" 
                        <!DOCTYPE html>

<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Comeback</title>
</head>

<body style="margin:0; padding:0; background:#0a0a0a; font-family: 'Segoe UI', sans-serif; color:white; display:flex; justify-content:center; align-items:center; height:100vh;">

```
<div style="text-align:center; max-width:600px; padding:40px; border-radius:20px; background:rgba(255,255,255,0.05); backdrop-filter:blur(10px); box-shadow:0 0 40px rgba(0,0,0,0.8);">

    <h1 style="font-size:48px; margin-bottom:10px; letter-spacing:2px;">
        I'M BACK
    </h1>

    <p style="color:#aaa; font-size:18px; margin-bottom:30px;">
        Stronger. Sharper. Unstoppable.
    </p>

    <div style="height:2px; width:80px; background:#fff; margin:20px auto;"></div>

    <p style="font-size:16px; color:#ccc; line-height:1.6;">
        They doubted. They ignored.  
        Now they will watch.  
        This is not just a return — it's a statement.
    </p>

    <button style="margin-top:30px; padding:12px 30px; border:none; border-radius:30px; background:white; color:black; font-size:16px; cursor:pointer; transition:0.3s;"
    onmouseover="this.style.background='#ccc'"
    onmouseout="this.style.background='white'">
        Watch Me
    </button>

</div>
```

</body>
</html>

                        """)
