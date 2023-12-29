odoo.define('pos_pharmacy_management.DoctorListScreen', function(require) {
    'use strict';

    const PosComponent = require('point_of_sale.PosComponent');
    const Registries = require('point_of_sale.Registries');
    const { isConnectionError } = require('point_of_sale.utils');

    const { debounce } = require("@web/core/utils/timing");
    const { useListener } = require("@web/core/utils/hooks");

    const { onWillUnmount, useRef } = owl;

    /**
     * Render this screen using `showTempScreen` to select partner.
     * When the shown screen is confirmed ('Set Customer' or 'Deselect Customer'
     * button is clicked), the call to `showTempScreen` resolves to the
     * selected partner. E.g.
     *
     * ```js
     * const { confirmed, payload: selectedPartner } = await showTempScreen('PartnerListScreen');
     * if (confirmed) {
     *   // do something with the selectedPartner
     * }
     * ```
     *
     * @props partner - originally selected partner
     */
    class DoctorListScreen extends PosComponent {
        setup() {
            super.setup();
            useListener('click-save', () => this.env.bus.trigger('save-partner'));
            useListener('save-changes', this.saveChanges);
            this.searchWordInputRef = useRef('search-word-input-partner');

            // We are not using useState here because the object
            // passed to useState converts the object and its contents
            // to Observer proxy. Not sure of the side-effects of making
            // a persistent object, such as pos, into Observer. But it
            // is better to be safe.
            this.state = {
                query: null,
                selectedDoctor: this.props.doctor,
                detailIsShown: false,
                editModeProps: {
                    partner: null,
                },
                previousQuery: "",
                currentOffset: 0,
            };
            this.updatePartnerList = debounce(this.updatePartnerList, 70);
            onWillUnmount(this.updatePartnerList.cancel);
        }
        // Lifecycle hooks
        back() {
            if(this.state.detailIsShown) {
                this.state.detailIsShown = false;
                this.render(true);
            } else {
                this.props.resolve({ confirmed: false, payload: false });
                this.trigger('close-temp-screen');
            }
        }
        confirm() {
            this.props.resolve({ confirmed: true});
            console.log("zxc/z/xcz/xc/c/c/c/cc/c/", this.state.selectedDoctor);
            this.props.doctor = this.state.selectedDoctor;
            this.trigger('close-temp-screen');
        }
        activateEditMode() {
            this.state.detailIsShown = true;
            this.render(true);
        }
        // Getters

        get currentOrder() {
            return this.env.pos.get_order();
        }

        get partners() {
            let res;
            let final_res = new Array();
            if (this.state.query && this.state.query.trim() !== '') {
                res = this.env.pos.db.search_partner(this.state.query.trim());
            } else {
                res = this.env.pos.db.get_partners_sorted(1000);
            }
            console.log("cx/cxc/cccccccccc3445665465345", res);
            res.sort(function (a, b) { return (a.name || '').localeCompare(b.name || '') });
            // the selected partner (if any) is displayed at the top of the list
            if (this.state.selectedDoctor) {
                let indexOfSelectedDoctor = res.findIndex( partner =>
                    partner.id === this.state.selectedDoctor.id
                );
                if (indexOfSelectedDoctor !== -1) {
                    res.splice(indexOfSelectedDoctor, 1);
                    res.unshift(this.state.selectedDoctor);
                }
            }
            console.log("zx/cczx/czx/cc/c/c/c/c/c/c", res);
            for (var i = 0; i < res.length; i++) {

              if (res[i]['is_doctor'] == true)
              {
              final_res.push(res[i]);
              }
            }
            return final_res;

        }
        get isBalanceDisplayed() {
            return false;
        }
        get partnerLink() {
            return `/web#model=res.partner&id=${this.state.editModeProps.partner.id}`;
        }

        // Methods

        async _onPressEnterKey() {
            if (!this.state.query) return;
            const result = await this.searchPartner();
            if (result.length > 0) {
                this.showNotification(
                    _.str.sprintf(
                        this.env._t('%s customer(s) found for "%s".'),
                        result.length,
                        this.state.query
                    ),
                    3000
                );
            } else {
                this.showNotification(
                    _.str.sprintf(
                        this.env._t('No more customer found for "%s".'),
                        this.state.query
                    ),
                    3000
                );
            }

        }
        _clearSearch() {
            this.searchWordInputRef.el.value = '';
            this.state.query = '';
            this.render(true);
        }
        // We declare this event handler as a debounce function in
        // order to lower its trigger rate.
        async updatePartnerList(event) {
            this.state.query = event.target.value;
            this.render(true);
        }
        clickDoctor(partner) {
            console.log('xc/xzc/cccccccccccccccccccccccccccczxzxxzxcccxx232323');
            if (this.state.selectedDoctor && this.state.selectedDoctor.id === partner.id) {
                this.state.selectedDoctor = null;
            } else {
                this.state.selectedDoctor = partner;
            }
            this.confirm();
        }
        editPartner(partner) {
            this.state.editModeProps.doctor = partner;
            this.activateEditMode();
        }
        createPartner() {
            // initialize the edit screen with default details about country & state
            this.state.editModeProps.doctor = {
                country_id: this.env.pos.company.country_id,
                state_id: this.env.pos.company.state_id,
            }
            this.activateEditMode();
        }
        async saveChanges(event) {
            try {
                let partnerId = await this.rpc({
                    model: 'res.partner',
                    method: 'create_from_ui',
                    args: [event.detail.processedChanges],
                });
                await this.env.pos.load_new_partners();
                this.state.selectedDoctor = this.env.pos.db.get_partner_by_id(partnerId);
                this.confirm();
            } catch (error) {
                if (isConnectionError(error)) {
                    await this.showPopup('OfflineErrorPopup', {
                        title: this.env._t('Offline'),
                        body: this.env._t('Unable to save changes.'),
                    });
                } else {
                    throw error;
                }
            }
        }
        async searchPartner() {
            if (this.state.previousQuery != this.state.query) {
                this.state.currentOffset = 0;
            }
            let result = await this.getNewPartners();
            this.env.pos.addPartners(result);
            this.render(true);
            if (this.state.previousQuery == this.state.query) {
                this.state.currentOffset += result.length;
            } else {
                this.state.previousQuery = this.state.query;
                this.state.currentOffset = result.length;
            }
            return result;
        }
        async getNewPartners() {
            let domain = [];
            const limit = 30;
            if(this.state.query) {
                domain = ['|', ["name", "ilike", this.state.query + "%"],
                               ["parent_name", "ilike", this.state.query + "%"]];
            }
            const result = await this.env.services.rpc(
                {
                    model: 'pos.session',
                    method: 'get_pos_ui_res_partner_by_params',
                    args: [
                        [odoo.pos_session_id],
                        {
                            domain,
                            limit: limit,
                            offset: this.state.currentOffset,
                        },
                    ],
                    context: this.env.session.user_context,
                },
                {
                    timeout: 3000,
                    shadow: true,
                }
            );
            return result;
        }
    }
    DoctorListScreen.template = 'DoctorListScreen';

    Registries.Component.add(DoctorListScreen);

    return DoctorListScreen;
});
