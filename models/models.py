# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Clientes(models.Model):
    _name = 'modelo.clientes'

    nombre = fields.Char(string='Nombre', required=True)
    primer_apellido = fields.Char(string='Primer Apellido', required=True)
    segundo_apellido = fields.Char(string='Segundo Apellido', required=True)    
    description = fields.Text()
    foto = fields.Binary(string='Foto')
    edad = fields.Integer(string='Edad')
    fecha_nacimiento = fields.Date(string="Fecha de nacimiento")    
    genero = fields.Selection([('h', 'Hombre'), ('m', 'Mujer'), ('o', 'Otro')], string='Género')
    nacionalidad = fields.Many2one('res.country', string='Nacionalidad')
    area = fields.Many2one('modelo.categorias',string='Categoria')    

class Categorias(models.Model):

    _name = "modelo.categorias"
    categoria= fields.Char(string='Categoria', required=True)    