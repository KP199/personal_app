odoo.define('pos_pharmacy_management.MedicineInfoPopup', function(require) {
    'use strict';

    const AbstractAwaitablePopup = require('point_of_sale.AbstractAwaitablePopup');
    const Registries = require('point_of_sale.Registries');

    const { useState } = owl;

    class MedicineInfoPopup extends AbstractAwaitablePopup {
        setup() {
            super.setup();

            $(":input[id=tab1]").hide();
            $(":input[id=tab2]").hide();
            $(":input[id=tab3]").hide();
            var final_arr = [];
            var final_salt = [];
            var safety_arr = [];
            for (var i = 0; i < this.env.pos.medicine_usage_by_id.length; i++) {
              if (this.props.info.medicine_usage_ids.includes(this.env.pos.medicine_usage_by_id[i]['id']))
              {

              final_arr.push({
              'id':this.env.pos.medicine_usage_by_id[i]['id'],
              'name':this.env.pos.medicine_usage_by_id[i]['name'],
              'description':this.env.pos.medicine_usage_by_id[i]['description']
              });
              }
            }
            for (var i = 0; i < this.env.pos.safety_advice_by_id.length; i++) {
              if (this.props.info.medicine_safety_device_ids.includes(this.env.pos.safety_advice_by_id[i]['id']))
              {

              safety_arr.push({
              'id':this.env.pos.safety_advice_by_id[i]['id'],
              'name':this.env.pos.safety_advice_by_id[i]['name'],
              'safety_advice':this.env.pos.safety_advice_by_id[i]['safety_advice']
              });
              }
            }
            for (var i = 0; i < this.env.pos.basic_salt_by_id.length; i++) {
              if (this.props.info.basic_salt_ids.includes(this.env.pos.basic_salt_by_id[i]['id']))
              {
              final_salt.push({
              'name':this.env.pos.basic_salt_by_id[i]['name'],
              'id':this.env.pos.basic_salt_by_id[i]['id']
              });
              }
            }
            this.props.basic_salt = final_salt;
            this.props.medicine_usge = final_arr;
            this.props.safety_advice = safety_arr;
            console.log("zx/cczxc/zcx/c/xzc/czx", this.props.medicine_usge);


        }

    }

    MedicineInfoPopup.template = 'MedicineInfoPopup';
    MedicineInfoPopup.defaultProps = { cancelKey: true };
    Registries.Component.add(MedicineInfoPopup);

    return MedicineInfoPopup;
});
