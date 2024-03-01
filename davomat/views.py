import os
import xlwt
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from datetime import date
from django.http import HttpResponse
import pandas as pd
from .models import Team, Attendance, Worker, Mark, Yonalish, Kurs



@csrf_exempt
def attendance_detail(request, team_id):
    team = Team.objects.get(id=team_id)
    is_att_taken = True if Attendance.objects.filter(date=date.today(), team=team) else False
    return render(request, "asosiy/detail.html", {'team':team, "is_att_taken":is_att_taken})


@csrf_exempt
def attendance_take(request, team_id):
    team = Team.objects.get(id=team_id)
    today = date.today()
    if not Attendance.objects.filter(date=today, team=team):
        if request.method == 'POST':
            attendance = Attendance.objects.create(team=team, date=today)
            marks = []
            for worker in team.workers.all():
                is_attended_input = request.POST.get(f"is_attended_{worker.id}")
                is_attended = True if is_attended_input == "on" else False                
                mark = Mark(attendance=attendance, worker=worker, is_attended=is_attended)
                marks.append(mark)
            
            Mark.objects.bulk_create(marks)
            return  redirect('detail', team.id)    

                

        return render(request, 'asosiy/take.html', {"team":team})
    else:
        return HttpResponse("Davomat allaqachon olib bo'lingan")
    

@csrf_exempt
def attendance_update(request, attendance_id):
    attendance = Attendance.objects.get(id=attendance_id)
    if attendance.date == date.today():
        if request.method == "POST":
            marks = attendance.marks.all()
            for mark in marks:
                is_attended_input = request.POST.get(f"is_attended_{mark.id}")
                is_attended = True if is_attended_input == "on" else False                
                mark.is_attended = is_attended

            Mark.objects.bulk_update(marks, ['is_attended'])
            return redirect("detail", attendance.team.id)
                
        return render(request, "asosiy/update.html", {'attendance':attendance})
    else:
        return HttpResponse("Faqatagina bugungi olingan davomadlarni tahrirlash mumkin.")
    



@csrf_exempt
def baza(request):
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="davomat.xls"'
        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet("sheet1")
        row_num = 0
        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = [
            'FISH',
            'Yo`nalish',
            'Kurs',
            'Guruh',
            'Borlar',
            'Kun'                                
        ]

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        font_style = xlwt.XFStyle()
        mark_son = 0
        for t in Mark.objects.all():
            mark_son += 1


        marks = Mark.objects.all()[mark_son-4000:mark_son]
        if marks:            
            for my_row in marks:                
                row_num = row_num + 1
                kun = f'{my_row.attendance.date}'
                def bor(qiymat):
                    if qiymat == True:
                        borlar = 2
                    else:
                        borlar = ''
                    return borlar                
                

                ws.write(row_num, 0, my_row.worker.fish, font_style)
                ws.write(row_num, 1, my_row.attendance.team.yonalish.name, font_style)
                ws.write(row_num, 2, my_row.attendance.team.kurs.name, font_style)
                ws.write(row_num, 3, my_row.attendance.team.guruh.name, font_style)
                ws.write(row_num, 4, bor(my_row.is_attended), font_style)
                ws.write(row_num, 5, kun, font_style)                              

            wb.save(response)
            return response
        else:
            return redirect('/')
        

