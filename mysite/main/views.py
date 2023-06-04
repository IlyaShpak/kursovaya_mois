from django.shortcuts import render, HttpResponse
from . models import BusStation, Routes, PassengerBit
from django.http import HttpResponseRedirect, JsonResponse
import time
from datetime import date


def index(request, id):
    station_info = BusStation.objects.get(id=id)
    all_routes = Routes.objects.filter(stations__contains=[station_info.name]).order_by("number")
    all_numbers = [i.number for i in all_routes]
    return render(request, 'main/index.html', context={"data": all_numbers, "station": station_info.name})


def second(request):
    route = request.GET.get('route')
    if request.method == 'POST':
        # Обработка отправленной формы
        return HttpResponseRedirect(request.path_info)
    else:
        pass


def my_view(request):
    if request.method == 'POST':
        key = request.POST.get('key', None)
        if key is not None:
            # обработка данных
            print("here")
            return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'})


def create_record(request):
    if request.method == 'POST':
        my_field_value = request.POST.get('my_field')
        route_number = my_field_value[:my_field_value.find("#")]
        station = my_field_value[my_field_value.find("#") + 1:]
        new_record = PassengerBit(current_time=time.strftime("%H:%M:%S"), current_data=date.today(), bus_station=station, route_number=route_number)
        new_record.save()
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})