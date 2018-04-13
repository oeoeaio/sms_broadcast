import logging

from odoo import models, fields, api

_logger = logging.getLogger(__name__)


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    default_broadcast_username = fields.Char(string='Username', default_model='sms.broadcast.mixin')
    default_broadcast_password = fields.Char(string='Password', default_model='sms.broadcast.mixin')
