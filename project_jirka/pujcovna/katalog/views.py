from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

class IndexView(View):
    def get(self, request):
        return HttpResponse("Zde bude titulní stránka.")

class SeznamView(View):
    def get(self, request):
        return HttpResponse("""<nav class="w3-bar w3-black">
  <a href="#home" class="w3-button w3-bar-item">Home</a>
  <a href="#band" class="w3-button w3-bar-item">Band</a>
  <a href="#tour" class="w3-button w3-bar-item">Tour</a>
  <a href="#contact" class="w3-button w3-bar-item">Contact</a>
</nav><h1>Vítejte v naší autopůjčovně!</h1>
<a href='http://localhost:8000/katalog/seznam/'>Jaká auta máme?</a><br>
<h2>O naší autopůjčovně</h2>
<p>Naše půjčovna vznikla v roce 2011 a dnes nabízí přibližně 30 aut.</p> <ul>
  <li>Coffee</li>
  <li>Tea</li>
  <li>Milk</li>
</ul><section>
  <img style="width:400px" height="300px" src="https://get.pxhere.com/photo/geotagged-north-carolina-united-states-usa-American-Classic-Car-American-Muscle-Car-auto-automobile-automotive-photography-Automotive-Portrait-Big-Tires-car-car-photo-car-photography-car-show-Car-Wrap-classic-classic-auto-classic-automobile-classic-car-Classic-Vehicle-coche-colorful-custom-car-Custom-Vehicle-Drag-Car-Drag-Racing-Car-Drag-Radials-Dragcar-Forest-City-Hot-Nights-Cool-Rides-Hot-Nights-Cool-Rides-Car-Show-hot-rod-Kranken-Signs-Vehicle-Wrap-Kustom-Kulture-Kustom-Vehicle-Major-Kiser-Drag-Car-muscle-car-nc-NC-Car-Show-North-Carolina-Car-Show-performance-car-Photoshop-Composite-Photoshop-Lens-Blur-Prostreet-race-car-Rutherford-County-Rutherford-County-NC-Rutherford-County-North-Carolina-Rutherfordton-County-SONY-a6500-SONY-Alpha-6500-super-car-v8-vehicle-vendimia-voiture-Wheelie-Bar-motor-vehicle-automotive-design-automotive-exterior-mid-size-car-compact-car-1447261.jpg" style="width:100%">
</section>""")

