odoo.define('pos_pharmacy_management.models', function (require) {
    "use strict";

var { PosGlobalState, Order } = require('point_of_sale.models');
const Registries = require('point_of_sale.Registries');


const PosHrPosGlobalState = (PosGlobalState) => class PosHrPosGlobalState extends PosGlobalState {
    async _processData(loadedData) {
        await super._processData(...arguments);
            this.medicine_usage_by_id = loadedData['medicine.usage'];
            this.basic_salt_by_id = loadedData['basic.salt'];
            this.safety_advice_by_id = loadedData['medicine.safety.advice'];
            this.safety_advice_by_id = loadedData['medicine.safety.advice'];
            this.medicine_manu_by_id = loadedData['medicine.manufacture'];
    }

}
Registries.Model.extend(PosGlobalState, PosHrPosGlobalState);
});

