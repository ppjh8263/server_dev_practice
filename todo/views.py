from rest_framework.views import APIView
from .models import Task
from rest_framework.response import Response
from datetime import datetime
from django.shortcuts import render


class TaskSelect(APIView):
    def post(self, request):
        tasks = Task.objects.all()
        task_list=[]
        for task in tasks:
            task_list.append(dict(id=task.id,
                                  name=task.name,
                                  done=task.done))

        return Response(status=200, data=dict(tasks=task_list))
    # return Response(status=400, data=dict(code=100003)) 직접 정의한 에러코드 사용법


class Todo(APIView):
    def post(self, request):
        user_id = request.data.get('user_id', "")
        name = request.data.get('name', "")
        end_date = request.data.get('end_date', None)
        if end_date:
            end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
        Task.objects.create(user_id=user_id, name=name, end_date=end_date)

        tasks = Task.objects.all()
        task_list = []
        for task in tasks:
            task_list.append(
                    dict(name=task.name,
                        start_date=task.start_date,
                        end_date=task.end_date,
                        state=task.state))

        context = dict(task_list=task_list)
        return render(request, 'todo/todo.html', context=context)


    def get(self, request):
        tasks = Task.objects.all()
        task_list = []
        for task in tasks:
            task_list.append(
                dict(name=task.name,
                     start_date=task.start_date,
                     end_date=task.end_date,
                     state=task.state))

        context = dict(task_list=task_list)
        return render(request, 'todo/todo.html', context=context)

class TaskCreate(APIView):
    def post(self, request):
        user_id = request.data.get('user_id', '')
        todo_id = request.data.get('todo_id','')
        name = request.data.get('name', '')

        task = Task.objects.create(id=todo_id, user_id=user_id, name=name)

        return Response()
        # return Response(data=dict(task=task))
        #
        # end_date = request.data.get('end_date', None)
        # if end_date:
        #     end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
        #     task = Task.objects.create(user_id=user_id, name=name, end_date=end_date)
        #
        #     return Response(
        #         dict(msg="To-Do 생성 완료",
        #              name=task.name,
        #              start_date=task.start_date.strftime('%Y-%m-%d'),
        #              end_date=task.end_date))

class TaskToggle(APIView):
    def post(self, resquest):
        todo_id = resquest.data.get('todo_id','')
        task = Task.objects.get(id=todo_id)
        if task:
            task.done = False if task.done is True else True
            task.save()

        return Response()

class TaskDelete(APIView):
    def post(self, resquest):
        todo_id = resquest.data.get('todo_id','')
        task = Task.objects.get(id=todo_id)
        if task:
            task.delete()

        return Response()