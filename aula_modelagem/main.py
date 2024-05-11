from controller.Controller import add_user, insert_task

if __name__ == '__main__':
    id_user = add_user("Joao Teste6", "teste6@teste8.com")
    insert_task("Teste", "Pendente", "Alta", "2021-12-31", id_user)