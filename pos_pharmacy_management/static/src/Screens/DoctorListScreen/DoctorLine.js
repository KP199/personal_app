odoo.define('point_of_sale.DoctorLine', function(require) {
    'use strict';

    const PosComponent = require('point_of_sale.PosComponent');
    const Registries = require('point_of_sale.Registries');

    class DoctorLine extends PosComponent {
        get highlight() {
            return this._isDoctorSelected ? 'highlight' : '';
        }
        get shortAddress() {
            console.log("zx/c/zx/zxc/zxc/xz", shortAddress);
            const { partner } = this.doctor;
            return partner.address;
        }
        get _isDoctorSelected() {
            return this.props.doctor === this.props.selectedDoctor;
        }
    }
    DoctorLine.template = 'DoctorLine';

    Registries.Component.add(DoctorLine);

    return DoctorLine;
});
