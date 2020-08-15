from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect
from . import models


def contact(request):
    """Handles inquiry form submission"""
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing_title']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']
        
        # check if user has made inquiry already
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = models.Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            
            if has_contacted:
                messages.error(request, 'You have already made an inquiry for this listing')
                return redirect('/listings/' + listing_id)

        contact = models.Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone,
                                 message=message,
                                 user_id=user_id)

        contact.save()
        
        # send email
        send_mail(
            subject='Property Listing Inquiry',
            message=f'There has been an inquiry for {listing}. sign in to the admin area for more information',
            from_email=email,
            recipient_list=[realtor_email, 'inquiry@knavelsrs.co'],
            fail_silently=True
        )

        messages.success(request, 'Your request has been submitted, a realtor will get back to you')
        return redirect('/listings/' + listing_id)
