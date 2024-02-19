from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework import serializers
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse


class StampSerializer(serializers.Serializer):
    pass  # Placeholder serializer class


class StampDetailView(RetrieveUpdateDestroyAPIView):
    http_method_names = ["post"]
    serializer_class = StampSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        name = data.get('fullName')
        email = data.get('email')

        message = ""
        for key, value in data.items():
            message += f"{key}: {value}\n"

        if name and email:
            send_mail(
                'New Stamp Order',
                message,
                settings.EMAIL_HOST_USER,  # Sender's email address
                [settings.EMAIL_HOST_USER],  # List of recipients
                fail_silently=False,
            )
            thank_you_message = (
                "Thank you for contacting Nova Discs,\n\n"
                "We got your message and if it requires a response we will be in touch shortly.\n"
                "If you have an inspiration photo for a stamp feel free to reply to this email with it, and any other "
                "questions you might have."
                "\n\n"
                "Cheers,\nMandy"
            )
            send_mail(
                'Thank You!',
                thank_you_message,
                settings.EMAIL_HOST_USER,
                [email]
            )
            return JsonResponse({'message': 'Email sent successfully'}, status=200)
        else:
            return JsonResponse({'error': 'Missing required data'}, status=400)
