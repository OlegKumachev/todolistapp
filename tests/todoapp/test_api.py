import pytest
from django.template.defaultfilters import title
from rest_framework.test import APIClient
from model_bakery import baker

from todoapp.models import Tasks, Tag


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def task_factory():
    def factory(**kwargs):
        return baker.make(Tasks, **kwargs)
    return factory

@pytest.mark.django_db
def test_api(client, task_factory):
    tasks = task_factory(title='Task', description='Description', due_date=None, is_completed=False, tags=[], _quantity=10)

    response = client.get('/api/task/')

    assert response.status_code == 200
    data = response.json()
    assert len(data['results']) == len(tasks)

    for i, t in enumerate(data['results']):
        assert t['title'] == 'Task'
        assert t['description'] == 'Description'
        assert t['due_date'] is None
        assert t['is_completed'] == False
        assert len(t['tags']) == 0



@pytest.mark.django_db
def test_create_task(client):
    # Создайте теги, если они необходимы
    tag1 = Tag.objects.create(name="Important")
    tag2 = Tag.objects.create(name="Urgent")

    # Данные для отправки
    payload = {
        "title": "New Task",
        "description": "This is a new task.",
        "due_date": "2024-01-01T00:00:00Z",
        "is_completed": False,
        "tags": [tag1.id, tag2.id],
    }

    response = client.post('/api/task/', data=payload)


    assert response.status_code == 201

    created_task = Tasks.objects.last()
    assert created_task.title == payload['title']
    assert created_task.description == payload['description']
    assert created_task.is_completed == payload['is_completed']
    assert created_task.tags.count() == 2
    assert set(created_task.tags.values_list('name', flat=True)) == {'Important', 'Urgent'}


@pytest.mark.django_db
def test_api_delete(client):
    task = Tasks.objects.create(title='test', description='test test')
    response = client.delete(f'/api/task/{task.id}/')
    assert response.status_code == 204

