/** @odoo-module **/

import ProductScreen from "point_of_sale.ProductScreen";
import Registries from "point_of_sale.Registries";
import {format} from "web.field_utils";
import utils from "web.utils";
 const { useListener } = require("@web/core/utils/hooks");
const ProductScreenInherit = (ProductScreen) =>
    class ProductScreenInherit extends ProductScreen {

      setup() {
            super.setup();
            useListener('click-doctor', this.onClickDoctor);
      }

      async onClickDoctor() {
       const currentPartner = this.currentOrder.get_partner();
            if (currentPartner && this.currentOrder.getHasRefundLines()) {
                this.showPopup('ErrorPopup', {
                    title: this.env._t("Can't change customer"),
                    body: _.str.sprintf(
                        this.env._t(
                            "This order already has refund lines for %s. We can't change the customer associated to it. Create a new order for the new customer."
                        ),
                        currentPartner.name
                    ),
                });
                return;
            }
            const { confirmed, payload: newPartner } = await this.showTempScreen(
                'DoctorListScreen',
                { doctor: currentPartner }
            );
            if (confirmed) {
                this.currentOrder.set_partner(newPartner);
                this.currentOrder.updatePricelist(newPartner);
            }
      }


      _onClickShowSideMenu(ev){
            $('#side_menu').toggle();
      }

      _onClickDeleteOrderLine(ev){
           this.env.pos.get_order().remove_orderline(this.env.pos.get_order().get_selected_orderline());
      }
      _onClickDeleteOrder(ev){
           this.env.pos.removeOrder(this.env.pos.get_order());
           this.env.pos.add_new_order();
      }

    };

Registries.Component.extend(ProductScreen, ProductScreenInherit);
