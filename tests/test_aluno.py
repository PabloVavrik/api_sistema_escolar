def test_get_aluno(client):
    response = client.get('/alunos/')

    assert response.status_code == 200
    assert isinstance(response.json, list)
