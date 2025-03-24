from django.http import JsonResponse
import pickle
from django.views.decorators.csrf import csrf_exempt
import json

# Load trained model and vectorizer
model = pickle.load(open("classifier/spam_model.pkl", "rb"))
vectorizer = pickle.load(open("classifier/vectorizer.pkl", "rb"))

@csrf_exempt
def predict_spam(request):
    if request.method == "POST":
        data = json.loads(request.body)
        message = data.get("message", "")

        transformed = vectorizer.transform([message])
        prediction = model.predict(transformed)[0]

        return JsonResponse({"prediction": "Spam" if prediction == 1 else "Not Spam"})

    return JsonResponse({"error": "Invalid request"}, status=400)
from django.shortcuts import render

def home(request):
    prediction = None
    if request.method == "POST":
        message = request.POST.get("message", "")
        transformed = vectorizer.transform([message])
        prediction = "Spam" if model.predict(transformed)[0] == 1 else "Not Spam"

    return render(request, "classifier/index.html", {"prediction": prediction})
