from odoo import fields, models

class PaymentProvider(models.Model):
    _inherit = 'payment.provider'

    code = fields.Selection(
        selection_add=[('pi_network', 'Pi Network')],
        ondelete={'pi_network': 'set default'}
    )
    pi_app_id = fields.Char(
        string="Pi App ID", 
        help="El ID de la aplicación proporcionado por Pi Developer Portal.",
        required_if_provider='pi_network'
    )
    pi_api_key = fields.Char(
        string="Pi API Key", 
        help="Tu clave API secreta para verificar los pagos en el backend.",
        required_if_provider='pi_network'
    )
    
    def _get_supported_currencies(self):
        """Pi Network utiliza su propia criptomoneda (Pi)."""
        res = super()._get_supported_currencies()
        # Asegúrate de tener la moneda PI creada en tu Odoo para que esto funcione correctamente.
        # res |= self.env['res.currency'].search([('name', '=', 'PI')])
        return res
