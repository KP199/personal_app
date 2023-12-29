odoo.define('pos_pharmacy_management.AdvanceSearchPopup', function(require) {
    'use strict';

    const AbstractAwaitablePopup = require('point_of_sale.AbstractAwaitablePopup');
    const Registries = require('point_of_sale.Registries');
    var core = require('web.core');

    var QWeb = core.qweb;

    const { useState } = owl;

    class AdvanceSearchPopup extends AbstractAwaitablePopup {
        setup() {
            super.setup();

        }

        SearchByName(ev){
            let res = document.getElementById("result");
            res.innerHTML = '';
            let list = '';
          const inputContainer = ev.currentTarget;
          let value = ev.currentTarget.value;
              for (var i = 0; i < this.env.pos.medicine_manu_by_id.length; i++) {
                  let position = this.env.pos.medicine_manu_by_id[i]['name'].search(value);
                  if(position==0){
                     list += '<li style="padding: 5px 0;" class="manufacture_name">' + this.env.pos.medicine_manu_by_id[i]['name'] + '</li>';

                  }

              }
          res.innerHTML = '<ul>' + list + '</ul>';
          if ($(".manufacture_name")){
          $(".manufacture_name")[0].addEventListener('click', this.OnClickProduct.bind(this));
          }





        }

        OnClickProduct(ev){
           let textValue = ev.target.innerText;

           $('#search_name').val(textValue);
        }
    }

    AdvanceSearchPopup.template = 'AdvanceSearchPopup';
    AdvanceSearchPopup.defaultProps = { cancelKey: true };
    Registries.Component.add(AdvanceSearchPopup);

    return AdvanceSearchPopup;
});
