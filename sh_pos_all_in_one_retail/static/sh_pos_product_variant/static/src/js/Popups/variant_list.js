odoo.define('sh_pos_product_variant.VariantProductItem', function (require) {
    'use strict';

    const PosComponent = require('point_of_sale.PosComponent');
    const Registries = require('point_of_sale.Registries');

    class VariantProductItem extends PosComponent {
        /**
         * For accessibility, pressing <space> should be like clicking the product.
         * <enter> is not considered because it conflicts with the barcode.
         *
         * @param {KeyPressEvent} event
         */
        get order() {
            return this.env.pos.get_order();
        }
        spaceClickProduct(event) {
            if (event.which === 32) {
                this.trigger('click-variant-product', this.props.product);
            }
        }
        get imageUrl() {
            const product = this.props.product;
            return `/web/image?model=product.product&field=image_128&id=${product.id}&write_date=${product.write_date}&unique=1`;
        }
        get pricelist() {
            const current_order = this.env.pos.get_order();
            if (current_order) {
                return current_order.pricelist;
            }
            return this.env.pos.default_pricelist;
        }
        get price() {
            const formattedUnitPrice = this.env.pos.format_currency(
                this.props.product.get_price(this.pricelist, 1),
                'Product Price'
            );
            if (this.props.product.to_weight) {
                return `${formattedUnitPrice}/${this.env.pos.units_by_id[this.props.product.uom_id[0]].name
                    }`;
            } else {
                return formattedUnitPrice;
            }
        }
    }
    VariantProductItem.template = 'VariantProductItem';

    Registries.Component.add(VariantProductItem);

    return VariantProductItem;
});
