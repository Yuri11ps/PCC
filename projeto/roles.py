from rolepermissions.roles import AbstractUserRole

class Usuario(AbstractUserRole):
    available_permissions = {
        'adicionar_avaliacao':True,
        'editar_avaliacao':True,
        'deletar_avaliacao':True,
        'listar_avaliacao':True,
        'listar_empresa':True,
        'listar_equipamento':True,
        'listar_rota':True,
        'listar_residuo':True,
    }

class Admin(AbstractUserRole):
    available_permissions = {
        'listar_avaliacao':True,
        'adicionar_avaliacao':True,
        'editar_avaliacao':True,
        'deletar_avaliacao':True,

        'listar_empresa':True,
        'adicionar_empresa': True,
        'editar_empresa': True,
        'deletar_empresa': True,

        'listar_equipamento':True,
        'adicionar_equipamento':True,
        'editar_equipamento':True,
        'deletar_equipamento':True,
        
        'listar_residuo':True,
        'adicionar_residuo':True,
        'editar_residuo':True,
        'deletar_residuo':True,

        'listar_rota':True,
        'adicionar_rota':True,
        'editar_rota':True,
        'deletar_rota':True,
    }

class Empresa(AbstractUserRole):
    available_permissions = {
        'listar_avaliacao':True,
        'listar_empresa':True,
        'listar_equipamento':True,
        'listar_rota':True,
        'listar_residuo':True,
        'adicionar_equipamento':True,
        'editar_equipamento':True,
        'deletar_equipamento':True,
        'adicionar_residuo':True,
        'editar_residuo':True,
        'deletar_residuo':True,
        'adicionar_rota':True,
        'editar_rota':True,
        'deletar_rota':True,
    }








