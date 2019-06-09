odoo.translator_odoo = function(instance, local) {

    local.HomePage = instance.Widget.extend({
        start: function() {
            console.log("pet store home page loaded");
        },
    });

    instance.web.client_actions.add(
        'petstore.homepage', 'instance.oepetstore.HomePage');
};
