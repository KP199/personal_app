odoo.define('pos_pharmacy_management.AlternateMedicinePopup', function(require) {
    'use strict';

    const AbstractAwaitablePopup = require('point_of_sale.AbstractAwaitablePopup');
    const Registries = require('point_of_sale.Registries');

    const { useState } = owl;

    class AlternateMedicinePopup extends AbstractAwaitablePopup {
        setup() {
            super.setup();
            var final_arr = [];

            for (var i = 0; i < this.props.info.alternate_medicine_ids.length; i++) {
               console.log("x/zcc/xzc/zcc/////////////", this.props.info.alternate_medicine_ids[i]);
              final_arr.push({
              'id':this.env.pos.db.product_by_id[this.props.info.alternate_medicine_ids[i]]['id'],
              'display_name':this.env.pos.db.product_by_id[this.props.info.alternate_medicine_ids[i]]['display_name'],
              'image_url':`/web/image?model=product.product&field=image_128&id=${this.env.pos.db.product_by_id[this.props.info.alternate_medicine_ids[i]]['id']}`,
              });
            }
            this.alternate_medicines = final_arr;

        }
    confirm(event) {
        for (var i = 0; i < $(".image-checkbox:checked").length; i++) {
             var ret = $(".image-checkbox:checked")[i].id.replace('cb','');
             var product = this.env.pos.db.get_product_by_id(ret);
             this.env.pos.get_order().add_product(product,  {
                    price: 23.44,
                    merge: false,
                });
        }
    }


    }

    AlternateMedicinePopup.template = 'AlternateMedicinePopup';
    AlternateMedicinePopup.defaultProps = { cancelKey: true };
    Registries.Component.add(AlternateMedicinePopup);

    return AlternateMedicinePopup;
});
