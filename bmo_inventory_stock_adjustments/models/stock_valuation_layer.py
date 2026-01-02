# -*- coding: utf-8 -*-
from odoo import models, fields, api

class StockValuationLayer(models.Model):
    _inherit = 'stock.valuation.layer'

    stock_inventory_id = fields.Many2one('stock.inventory')
    
    def _validate_accounting_entries(self):
        # Gunakan list untuk menampung record yang akan diproses super
        # atau modifikasi self sebelum dikirim ke super.
        for svl in self:
            if not svl.with_company(svl.company_id).product_id.valuation == 'real_time':
                continue
            
            # Pengecekan aman terhadap field custom stock_inventory_id
            move = svl.stock_move_id
            if move and hasattr(move, 'stock_inventory_id') and move.stock_inventory_id:
                if move.stock_inventory_id.type_adjustments == 'qty_only':
                    # Paksa nilai menjadi 0 agar tidak terbentuk Account Move (jurnal)
                    # Kita gunakan write agar tersimpan ke DB sebelum validasi accounting
                    svl.write({
                        'value': 0.0,
                        'remaining_value': 0.0, # Penting di Odoo 18 agar balance
                    })
                    if move:
                        move.write({'price_unit': 0.0})
        
        # Jalankan fungsi asli Odoo
        # Odoo hanya akan membuat jurnal jika svl.value != 0
        return super(StockValuationLayer, self)._validate_accounting_entries()