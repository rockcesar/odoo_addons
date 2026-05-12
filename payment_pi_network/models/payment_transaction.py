import logging
from odoo import models, fields, _
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)

class PaymentTransaction(models.Model):
    _inherit = 'payment.transaction'

    pi_payment_id = fields.Char(string="Pi Payment ID", readonly=True)

    def _get_specific_rendering_values(self, processing_values):
        """Pasa los valores necesarios a la vista (Frontend)."""
        res = super()._get_specific_rendering_values(processing_values)
        if self.provider_code != 'pi_network':
            return res

        res.update({
            'api_url': '/payment/pi_network/process',
            'pi_app_id': self.provider_id.pi_app_id,
            'tx_reference': self.reference,
            'amount': self.amount,
            'memo': f"Pago de la orden {self.reference}",
        })
        return res
