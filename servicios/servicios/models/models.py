# -*- coding: utf-8 -*-

from odoo import models, fields, api

#masajes,disco,comedor,casino,spa

class gestionServicio(models.Model):
    _name = 'servicios.gestion'
    _description = 'Id del servicio'

    name = fields.Char(string="Id del servicio")
    name2 = fields.Char(string="Nombre y apellidos")
    dni = fields.Char(string="DNI")
    contratacion = fields.Date()


class ServicioSpa(models.Model):
    _name = 'servicios.spa'
    _description = 'Modelo servicio spa'
    
    gestion_id = fields.Many2one('servicios.gestion', string='Id del servicio')

    jacuzzi = fields.Boolean(string="Jacuzzi")
    sauna = fields.Boolean(string="Sauna")
    banio_turco = fields.Boolean(string="Baño Turco")
    piscina_olimpica = fields.Boolean(string="Piscina Olímpica")
    precio_total = fields.Float(string="Precio Total", compute='_compute_precio_total')

    @api.depends('jacuzzi', 'sauna', 'banio_turco', 'piscina_olimpica')
    def _compute_precio_total(self):
        for servicio in self:
            precio_base = 95  # Precio base arbitrario
            total = precio_base
            if servicio.jacuzzi:
                total += 20
            if servicio.sauna:
                total += 15
            if servicio.banio_turco:
                total += 25
            if servicio.piscina_olimpica:
                total += 10
            servicio.precio_total = total

class ServicioCasino(models.Model):
    _name = 'servicios.casino'
    _description = 'Modelo servicio casino'

    gestion_id = fields.Many2one('servicios.gestion', string='Id del servicio')
    ruleta = fields.Boolean(string="Ruleta")
    black_jack = fields.Boolean(string="Black Jack")
    maquinas = fields.Boolean(string="Máquinas")
    poker = fields.Boolean(string="Poker")
    precio_total = fields.Float(string="Precio Total", compute='_compute_precio_total')

    @api.depends('ruleta', 'black_jack', 'maquinas', 'poker')
    def _compute_precio_total(self):
        for servicio in self:
            precio_base = 20  # Precio base arbitrario
            total = precio_base
            if servicio.ruleta:
                total += 25
            if servicio.black_jack:
                total += 40
            if servicio.maquinas:
                total += 50
            if servicio.poker:
                total += 70
            servicio.precio_total = total



    
class ServicioRestaurante(models.Model):
    _name = 'servicios.restaurante'
    _description = 'Modelo servicio restaurante'

    gestion_id = fields.Many2one('servicios.gestion', string='Id del servicio')
    menu_dia = fields.Boolean(string="Menú del día")
    desayuno = fields.Boolean(string="Desayuno")
    cena = fields.Boolean(string="Cena")
    copas = fields.Boolean(string="Copas")
    precio_total = fields.Float(string="Precio Total", compute='_compute_precio_total')

    @api.depends('menu_dia', 'desayuno', 'cena', 'copas')
    def _compute_precio_total(self):
        for servicio in self:
            precio_base = 12  # Precio base arbitrario
            total = precio_base
            if servicio.menu_dia:
                total += 15
            if servicio.desayuno:
                total += 10
            if servicio.cena:
                total += 25
            if servicio.copas:
                total += 20
            servicio.precio_total = total

class ServicioMasajes(models.Model):
    _name = 'servicios.masajes'
    _description = 'Modelo servicio masajes'

    gestion_id = fields.Many2one('servicios.gestion', string='Id del servicio')
    tailandes = fields.Boolean(string="Masaje Tailandés")
    japones = fields.Boolean(string="Masaje Japonés")
    italiano = fields.Boolean(string="Masaje Italiano")
    precio_total = fields.Float(string="Precio Total", compute='_compute_precio_total')

    @api.depends('tailandes', 'japones', 'italiano')
    def _compute_precio_total(self):
        for servicio in self:
            precio_base = 20  # Precio base arbitrario
            total = precio_base
            if servicio.tailandes:
                total += 30
            if servicio.japones:
                total += 90
            if servicio.italiano:
                total += 35
            servicio.precio_total = total

class ServicioDiscoteca(models.Model):
    _name = 'servicios.discoteca'
    _description = 'Modelo servicio discoteca'

    gestion_id = fields.Many2one('servicios.gestion', string='Id del servicio')
    pista_baile = fields.Boolean(string="Pista de baile")
    vip = fields.Boolean(string="VIP")
    copas = fields.Boolean(string="Copas")
    precio_total = fields.Float(string="Precio Total", compute='_compute_precio_total')

    @api.depends('pista_baile', 'vip', 'copas')
    def _compute_precio_total(self):
        for servicio in self:
            precio_base = 10 # Precio base arbitrario
            total = precio_base
            if servicio.pista_baile:
                total += 10
            if servicio.vip:
                total += 90
            if servicio.copas:
                total += 20
            servicio.precio_total = total

    