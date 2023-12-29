/** @odoo-module **/

import ProductItem from "point_of_sale.ProductItem";
import Registries from "point_of_sale.Registries";
import {format} from "web.field_utils";
import utils from "web.utils";
const StockProductItem = (ProductItem) =>
    class StockProductItem extends ProductItem {

       setup() {
            super.setup();
            var final_arr = [];
            var final_salt = [];
            for (var i = 0; i < this.env.pos.medicine_usage_by_id.length; i++) {
              console.log("zx/cc/zxc/zc/cx/czxc/cx/cx/c",this.env.pos.medicine_usage_by_id[i]['id']);
              if (this.props.product.medicine_usage_ids.includes(this.env.pos.medicine_usage_by_id[i]['id']))
              {
              final_arr.push(this.env.pos.medicine_usage_by_id[i]['name']);
              }
            }
            for (var i = 0; i < this.env.pos.basic_salt_by_id.length; i++) {
              if (this.props.product.basic_salt_ids.includes(this.env.pos.basic_salt_by_id[i]['id']))
              {
              final_salt.push(this.env.pos.basic_salt_by_id[i]['name']);
              }
            }
            this.props.basic_salt = final_salt.toString();
            this.props.medicine_usge = final_arr.toString();


          }

       async _medicineusge(ids){
        var arr = [];
        var final_result = false;
        for (var i = 0; i < ids.length; i++) {
              arr.push(ids[i]);
        }
        const state_id = await this.rpc({
            model: 'medicine.usage',
            method: 'search_read',
            fields: ['name'],
            domain: [['id', 'in', arr]],
        });
        var final_arr = [];
        for (var i = 0; i < state_id.length; i++) {
              final_arr.push(state_id[i]['name']);
        }
        this.props.medicine_usge = final_arr.toString();
        return this.props.medicine_usge;

       }



      _onClickShowMedicineInfo(){
      this.showPopup('MedicineInfoPopup', {
          info: this.props.product,
          exitButtonIsShown: true,

      });
      }
      _onClickAlternateMedicine(){
       this.showPopup('AlternateMedicinePopup', {
          info: this.props.product,
          exitButtonIsShown: true,

      });
      }

    };

Registries.Component.extend(ProductItem, StockProductItem);
