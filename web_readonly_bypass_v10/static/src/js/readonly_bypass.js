odoo.define('web_readonly_bypass.base', function (require) {
"use strict";
    
    function retrieve_readonly_by_pass_fields(options, context){
        var readonly_by_pass_fields = {};
        if (options && 'readonly_fields' in options &&
           options['readonly_fields'] && context &&
           'readonly_by_pass' in context && context['readonly_by_pass']){
            if (_.isArray(context['readonly_by_pass'])){
                $.each( options.readonly_fields, function( key, value ) {
                    if(_.contains(context['readonly_by_pass'], key)){
                        readonly_by_pass_fields[key] = value;
                    }
                });
            }else{
                readonly_by_pass_fields = options.readonly_fields;
            }
        }
        return readonly_by_pass_fields;
    }
    
    function ignore_readonly(data, options, mode, context){
        var readonly_by_pass_fields = retrieve_readonly_by_pass_fields(
            options, context);
        if(mode){
            $.each( readonly_by_pass_fields, function( key, value ) {
                if(value==false){
                    delete(readonly_by_pass_fields[key]);
                }
            });
        }
        data = $.extend(data,readonly_by_pass_fields);
    }
    
    return {
        ignore_readonly: ignore_readonly,
        retrieve_readonly_by_pass_fields: retrieve_readonly_by_pass_fields
        };

});

odoo.define('web_readonly_bypass.readonly_bypass', function (require) {
"use strict";
    
    //var instance = openerp;
    var core = require('web.core');
    
    var web = require('web.data');
    
    var readonly_bypass = require('web_readonly_bypass.base');
    
    var pyeval = require('web.pyeval');
    
    var QWeb = core.qweb;
    var _t = core._t;

    web.BufferedDataSet.include({

        init : function() {
            this._super.apply(this, arguments);
        },
        /**
         * Creates Overriding
         *
         * @param {Object} data field values to set on the new record
         * @param {Object} options Dictionary that can contain the following keys:
         *   - readonly_fields: Values from readonly fields that were updated by
         *     on_changes. Only used by the BufferedDataSet to make the o2m work correctly.
         * @returns super {$.Deferred}
         */
        create : function(data, options) {
            var self = this;
            var context = pyeval.eval('contexts',
                                                   self.context.__eval_context);
            readonly_bypass.ignore_readonly(data, options, true, context);
            return self._super(data,options);
        },
        /**
         * Creates Overriding
         *
         * @param {Object} data field values to set on the new record
         * @param {Object} options Dictionary that can contain the following keys:
         *   - readonly_fields: Values from readonly fields that were updated by
         *     on_changes. Only used by the BufferedDataSet to make the o2m work correctly.
         * @returns super {$.Deferred}
         */
        write : function(id, data, options) {
            var self = this;
            var context = pyeval.eval('contexts',
                                                   self.context.__eval_context);
            readonly_bypass.ignore_readonly(data, options, false, context);
            return self._super(id,data,options);
        },

    });

    web.DataSet.include({
        /*
        BufferedDataSet: case of 'add an item' into a form view
        */
        init : function() {
            this._super.apply(this, arguments);
        },
        /**
         * Creates Overriding
         *
         * @param {Object} data field values to set on the new record
         * @param {Object} options Dictionary that can contain the following keys:
         *   - readonly_fields: Values from readonly fields that were updated by
         *     on_changes. Only used by the BufferedDataSet to make the o2m work correctly.
         * @returns super {$.Deferred}
         */
        create : function(data, options) {
            var self = this;
            readonly_bypass.ignore_readonly(data, options, true, self.context);
            return self._super(data,options);
        },
        /**
         * Creates Overriding
         *
         * @param {Object} data field values to set on the new record
         * @param {Object} options Dictionary that can contain the following keys:
         *   - readonly_fields: Values from readonly fields that were updated by
         *     on_changes. Only used by the BufferedDataSet to make the o2m work correctly.
         * @returns super {$.Deferred}
         */
        write : function(id, data, options) {
            var self = this;
            readonly_bypass.ignore_readonly(data, options, false, self.context);
            return self._super(id,data,options);
        },

    });
});
