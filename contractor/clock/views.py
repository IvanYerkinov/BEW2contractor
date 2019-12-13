from django.shortcuts import render
from django.views.generic.list import ListView

from clock.models import Clock


# Create your views here.
class ClockList(ListView):
    model = Clock

    def get(self, request):
        clocks = self.get_queryset().all()

        return render(request, 'clocklist.html', {
          'clocks': clocks
        })

    def post(self, request):
        name = str(request.POST.get("nam", ""))
        initicks = int(request.POST.get("tick", ""))
        desc = request.POST.get("desc", "")
        tocks = int(request.POST.get("tock", ""))

        if initicks > tocks:
            initicks = tocks

        nclock = Clock(name=name, ticks=initicks, desc=desc, tocks=tocks)
        nclock.save()

        clocks = self.get_queryset().all()

        return render(request, 'clocklist.html', {
          'clocks': clocks
        })


def tickdown(request):
    id = request.POST.get("tickdown", "")
    clock = Clock.objects.get(id=id)

    clock.ticks -= 1
    if clock.ticks < 0:
        clock.ticks = 0

    clock.save()

    clocks = Clock.objects.all()

    return render(request, 'clocklist.html', {
      'clocks': clocks
    })


def tickup(request):
    id = request.POST.get("tickup", "")
    clock = Clock.objects.get(id=id)

    clock.ticks += 1
    if clock.ticks > clock.tocks:
        clock.ticks = clock.tocks
    clock.save()

    clocks = Clock.objects.all()

    return render(request, 'clocklist.html', {
      'clocks': clocks
    })


def delete(request):
    id = request.POST.get("delete", "")
    clock = Clock.objects.get(id=id)
    clock.delete()

    clocks = Clock.objects.all()

    return render(request, 'clocklist.html', {
      'clocks': clocks
    })
