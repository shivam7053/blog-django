import os
from django.conf import settings

def banner_images(request):
    banner_dir = os.path.join(settings.STATICFILES_DIRS[0], 'banners')
    if not os.path.exists(banner_dir):
        return {'carousel_images': []}
    
    images = [f for f in os.listdir(banner_dir) if f.endswith(('.jpg', '.jpeg', '.png'))]
    carousel_images = [{'url': f'/static/banners/{img}'} for img in images]

    return {'carousel_images': carousel_images}
