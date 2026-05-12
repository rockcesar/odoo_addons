import logging
import requests
from odoo import http
from odoo.http import request

_logger = logging.getLogger(__name__)

class PiNetworkController(http.Controller):

    @http.route('/payment/pi_network/approve', type='json', auth='public', csrf=False)
    def pi_approve_payment(self, paymentId, tx_reference, **kwargs):
        """Aprobación del lado del servidor llamada por el SDK de Pi."""
        tx = request.env['payment.transaction'].sudo().search([('reference', '=', tx_reference)], limit=1)
        if not tx:
            return {'error': 'Transaction not found'}

        # Lógica para llamar a la API de Pi y aprobar el pago
        api_key = tx.provider_id.pi_api_key
        headers = {'Authorization': f'Key {api_key}'}
        
        try:
            # 1. Llamar a la API de Pi para verificar que el pago es legítimo
            verify_url = f"https://api.minepi.com/v2/payments/{paymentId}"
            response = requests.get(verify_url, headers=headers)
            response.raise_for_status()
            
            # 2. Si todo es correcto, aprobar el pago en Pi Network
            approve_url = f"https://api.minepi.com/v2/payments/{paymentId}/approve"
            requests.post(approve_url, headers=headers)
            
            # Guardamos el ID en la transacción de Odoo
            tx.write({'pi_payment_id': paymentId})
            
            return {'status': 'approved'}
        except Exception as e:
            _logger.error(f"Error al aprobar el pago en Pi Network: {str(e)}")
            return {'error': 'Server approval failed'}

    @http.route('/payment/pi_network/complete', type='json', auth='public', csrf=False)
    def pi_complete_payment(self, paymentId, txid, tx_reference, **kwargs):
        """Completar el pago una vez que la blockchain lo confirma."""
        tx = request.env['payment.transaction'].sudo().search([('reference', '=', tx_reference)], limit=1)
        if not tx:
            return {'error': 'Transaction not found'}

        api_key = tx.provider_id.pi_api_key
        headers = {'Authorization': f'Key {api_key}'}
        
        try:
            # Notificar a Pi que entregamos el servicio/producto
            complete_url = f"https://api.minepi.com/v2/payments/{paymentId}/complete"
            data = {'txid': txid}
            requests.post(complete_url, headers=headers, json=data)
            
            # Marcar la transacción de Odoo como Exitosa (Done)
            tx._set_done()
            
            return {'status': 'completed'}
        except Exception as e:
            _logger.error(f"Error al completar el pago en Pi Network: {str(e)}")
            tx._set_error("El pago no pudo completarse en la blockchain de Pi.")
            return {'error': 'Server completion failed'}
