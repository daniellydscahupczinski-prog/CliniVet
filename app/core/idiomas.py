class Idioma:

    ATUAL = "pt"

    TEXTOS = { # portugues 
        "pt": {

            # Comuns a várias telas
            "comum.id": "ID", #classe com o seu valor 
            "comum.nome": "Nome",
            "comum.novo": "Novo",
            "comum.salvar": "Salvar",
            "comum.alterar": "Alterar",
            "comum.excluir": "Excluir",
            "comum.fechar": "Fechar",
            "comum.cancelar": "Cancelar",
            "comum.confirmacao": "Confirmação",
            "comum.erro_prefixo": "Erro: ",

            #Tela de Animal
            "animal.janela_titulo": "CRUD de Animais",
            "animal.titulo" : "Cadastro de animal",
            "animal.dados_frame": "Dados do Animal",
            "animal.sexo": "Sexo:",
            "animal.peso": "Peso:",
            "animal.cliente_id": "Cliente ID:",
            "animal.especie_id": "Espécie ID:",
            "animal.raca_id": "Raça ID:",
            "animal.confirmacao_exclusao": "Deseja realmente excluir este animal?",
            "animal.selecionar_animal": "Selecione um animal na lista.",
            "animal.atualizacao": "Animal atualizado com sucesso!",
            "animal.exclusao": "Animal excluído com sucesso!",
            "animal.nao_encontrado": "Animal não encontrado.",
            "animal.problema_exclusao": "Problemas ao excluir animal",

            #Tela de Aplicacao_vacina
            "aplicacao_vacina.janela_titulo": "CRUD de Aplicações de Vacina",
            "aplicacao_vacina.titulo": "Criação de aplicação de vacina",
            "aplicacao_vacina.dadso_frame": "Dados da Aplicação de Vacina",
            "aplicacao_vacina.tipo_servico": "Tipo de Serviço:",
            "aplicacao_vacina.data_vacina": "Data Vacina:",
            "aplicacao_vacina.horario_vacina": "Horário Vacina:",
            "aplicacao_vacina.status_vacina": "Status Vacina:",
            "aplicacao_vacina.animal_id": "Animal ID:",
            "aplicacao_vacina.vacina_id": "Vacina ID:",
            "aplicacao_vacina.confirmacao_exclusao": "Deseja realmente excluir esta aplicação de vacina?",
            "aplicacao_vacina.cadastro_sucesso": "Aplicação da vacina cadastrada com sucesso!",
            "aplicacao_vacina.selecionar_aplicacao": "Selecione uma aplicação da vacina na lista.",
            "aplicacao_vacina.atualizacao": "Aplicação da vacina atualizada com sucesso!",
            "aplicacao_vacina.exclusao": "Usuário excluído com sucesso!",
            "aplicacao_vacina.nao_encontrado": "Aplicação da vacina não encontrado",
            "aplicacao_vacina.problema_exclusao": "Problemas ao excluir a aplicação da vacina.",

            #Tela de Vacina
            "vacina.cadastro_sucesso": "Estado cadastrado com sucesso!",
            "vacina.selecionar_vacina": "Selecione uma vacina na lista.",
            "vacina.atualizacao": "Vacina atualizada com sucesso!",
            "vacina.exclusao": "Vacina excluída com sucesso!",
            "vacina.nao_encontrada": "Vacina não encontrada.",
            "vacina.problema_exclusao": "Problemas ao excluir vacina",
            "vacina.janela_titulo": "CRUD de Vacinas",
            "vacina.dados_frame": "Dados da Vacina",
            "vacina.descricao": "Descricao",
            "vacina.confirmacao_exclusao": "Deseja realmente excluir esta vacina?",
            "vacina.titulo": "Criação de vacina",

            #Tela de Cliente
            "cliente.janela_titulo" : "Crud de Clientes",
            "cliente.titulo" : "Cadastro de cliente",
            "cliente.dados_frame" : "Dados do cliente",
            "cliente.telefone" : "Numero de telefone:",
            "cliente.cpf" : "Numero do cpf:",
            "cliente.confirmacao_exclusao" : "Deseja realmente excluir este cliente?",
            "cliente.selecionar_animal" : "Selecione um animal",
            "cliente.cadastro_sucesso" : "Cliente cadastrado com sucesso!",
            "cliente.problema_exclusao" : "Problemas ao excluir cliente!!",
            "cliente.atualizacao" : "Cliente atualizado!",
            "cliente.selecionar" : "Selecione um cliente",
            "cliente.exclusao" : "Cliente excluido com sucesso!",
            "cliente.nao_encontrado" : "Nenhum cliente encontrado!",

            #Tela de Raça
            "raca.": "CRUD de Racas",
            "raca.": "Cadastro de raca",
            "raca.": "dados da raca",
            "raca.": "Deseja realmente excluir esta raça?",
            "raca.": "Raça cadastrada com sucesso!",
            "raca.": "Selecione uma raça da lista",
            "raca.": "Raça atualizada",
            "raca.": "Raça excluida com sucesso",
            "raca.": "Raça nao encontrada",
            "raca.": "Problemas ao excluir raça",
        
            #Tela de Agendamento
            "agendamento.": "Crud de agendamentos",
            "agendamento.": "Cadastro de agendamento",
            "agendamento.": "Dados do agendamento",
            "agendamento.": "Serviços",
            "agendamento.": "Horarios",
            "agendamento.": "Data do agendamento",
            "agendamento.": "Status:",
            "agendamento.": "Deseja realmente excluir este agendamento?",
            "agendamento.": "Agendamento cadastrado",
            "agendamento.": "Selecione um agendamento da lista",
            "agendamento.": "Agendamento atualizado",
            "agendamento.": "Agendamento excluido",
            "agendamento.": "Agendamento nao encontrado",
            "agendamento.": "Problomas ao excluir agendamento",

            #Tela de Especie
            "especie.": "",
            "especie.": "",        
            "especie.": "",
            "especie.": "",
            "especie.": "",
            "especie.": "",
            "especie.": "",
            "especie.": "",
            "especie.": "",
            "especie.": "",
            "especie.": "",
            "especie.": "",
            "especie.": "",
            "especie.": "",
            "especie.": "",

            #Tela de Consulta
            "consulta.": "",
            "consulta.": "",
            "consulta.": "",
            "consulta.": "",
            "consulta.": "",
            "consulta.": "",
            "consulta.": "",
            "consulta.": "",
            "consulta.": "",
            "consulta.": "",
            "consulta.": "",
            "consulta.": "",
            "consulta.": "",
            "consulta.": "",
            "consulta.": "",

            #Tela de Veterinario
            "veterinario.": "",
            "veterinario.": "",
            "veterinario.": "",
            "veterinario.": "",
            "veterinario.": "",
            "veterinario.": "",
            "veterinario.": "",
            "veterinario.": "",
            "veterinario.": "",
            "veterinario.": "",
            "veterinario.": "",
            "veterinario.": "",
            "veterinario.": "",
            "veterinario.": "",
            "veterinario.": "",

            # Menu principal
            "menu.animal": "Animal",
            "menu.vacina": "Vacina",
            "menu.aplicacao_vacina": "Aplicação de Vacinas",
            "menu.agendamento": "Agendamento",
            "menu.cliente": "Cliente",
            "menu.raca": "Raça",
            "menu.veterinario": "Veterinário",
            "menu.especie": "Espécie",
            "menu.consulta": "Consulta",
            "menu.idioma": "Idioma",
            "menu.sair": "Sair",
            "menu.data_nascimento": "Data de Nascimento:",

        },
        "en": { #ingles
            # Comuns a várias telas

            #Tela de Animal
            "animal.janela_titulo": "Animal CRUD",
            "animal.titulo" : "Animal Registration",
            "animal.dados_frame": "Animal Details",
            "animal.sexo": "Sex:",
            "animal.peso": "Weight:",
            "animal.cliente_id": "Client ID:",
            "animal.especie_id": "Species ID:",
            "animal.raca_id": "Breed ID:",
            "animal.confirmacao_exclusao": "Are you sure you want to delete this animal?",
            "animal.selecionar_animal": "Select an animal from the list.",
            "animal.atualizacao": "Animal updated successfully!",
            "animal.exclusao": "Animal deleted successfully!",
            "animal.nao_encontrado": "Animal not found.",
            "animal.problema_exclusao": "Error deleting animal",

            #Tela de Aplicacao_vacina
            "aplicacao_vacina.janela_titulo": "Vaccine Administration CRUD",
            "aplicacao_vacina.titulo": "Create Vaccine Administration",
            "aplicacao_vacina.dadso_frame": "Vaccine Administration Data",
            "aplicacao_vacina.tipo_servico": "Service Type:",
            "aplicacao_vacina.data_vacina": "Vaccination Date:",
            "aplicacao_vacina.horario_vacina": "Vaccination Time:",
            "aplicacao_vacina.status_vacina": "Vaccination Status:",
            "aplicacao_vacina.animal_id": "Animal ID:",
            "aplicacao_vacina.vacina_id": "Vaccine ID:",
            "aplicacao_vacina.confirmacao_exclusao": "Are you sure you want to delete this vaccine administration record?",
            "aplicacao_vacina.cadastro_sucesso": "Vaccine administration successfully registered!",
            "aplicacao_vacina.selecionar_aplicacao": "Select a vaccine administration record from the list.",
            "aplicacao_vacina.atualizacao": "Vaccine administration successfully updated!",
            "aplicacao_vacina.exclusao": "Vaccine administration successfully deleted!",
            "aplicacao_vacina.nao_encontrado": "Vaccine administration record not found",
            "aplicacao_vacina.problema_exclusao": "Error deleting vaccine administration record.",

            #Tela de Vacina
            "vacina.cadastro_sucesso": "Vaccine registered successfully!",
            "vacina.selecionar_vacina": "Select a vaccine from the list.",
            "vacina.atualizacao": "Vaccine updated successfully!",
            "vacina.exclusao": "Vaccine deleted successfully!",
            "vacina.nao_encontrada": "Vaccine not found.",
            "vacina.problema_exclusao": "Error deleting vaccine",
            "vacina.janela_titulo": "Vaccine CRUD",
            "vacina.dados_frame": "Vaccine Data",
            "vacina.descricao": "Description",
            "vacina.confirmacao_exclusao": "Are you sure you want to delete this vaccine?",
            "vacina.titulo": "Vaccine Creation",

            #Tela de Cliente 
            "cliente.janela_titulo" : "Client Management",
            "cliente.titulo" : "Client Registration",
            "cliente.dados_frame" : "Client Details",
            "cliente.telefone" : "Phone number:",
            "cliente.cpf" : "CPF number:",
            "cliente.confirmacao_exclusao" : "Are you sure you want to delete this client?",
            "cliente.selecionar_animal" : "Select an animal",
            "cliente.cadastro_sucesso" : "Client registered successfully!",
            "cliente.problema_exclusao" : "Error deleting client!!",
            "cliente.atualizacao" : "Client updated!",
            "cliente.selecionar" : "Select a client",
            "cliente.exclusao" : "Client deleted successfully!",
            "cliente.nao_encontrado" : "No client found!",

            #Tela de Raça 
            "raca.": "CRUD of Breeds",
            "raca.": "Breed Registration",
            "raca.": "Breed Data",
            "raca.": "Do you really want to delete this breed?",
            "raca.": "Breed successfully registered!",
            "raca.": "Select a breed from the list",
            "raca.": "Breed updated",
            "raca.": "Breed successfully deleted",
            "raca.": "Breed not found",
            "raca.": "Problems deleting breed",

            #Tela de Agendamento
            "agendamento.": "Appointment management",
            "agendamento.": "Appointment registration",
            "agendamento.": "Appointment details",
            "agendamento.": "Services",
            "agendamento.": "Time slots",
            "agendamento.": "Appointment date",
            "agendamento.": "Status:",
            "agendamento.": "Are you sure you want to delete this appointment?",
            "agendamento.": "Appointment registered",
            "agendamento.": "Select an appointment from the list",
            "agendamento.": "Appointment updated",
            "agendamento.": "Appointment deleted",
            "agendamento.": "Appointment not found",
            "agendamento.": "Error deleting appointment",

            #Tela de Especie

            #Tela de Consulta

            #Tela de Veterinario

            # Menu principal
        
            }
    }

    @classmethod # é usado quando tem algum atributo que eu quero que os metodos acessem e modifiquem eles
    def definir(cls, codigo): #cls = um self, que eu passo a propria classe como referencia
        cls.ATUAL = codigo # no codigo eu determino o idioma 

    @classmethod
    def t(cls, chave): # t = é um metodo normalmente de tradução 
        return cls.TEXTOS[cls.ATUAL].get(chave, chave)
