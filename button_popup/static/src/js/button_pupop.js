odoo.define('button_popup.FormView', function (require) {
"use strict";
    
    //var instance = openerp;
    
    var FormController = require('web.FormController');
    
    var core = require('web.core');
    
    var QWeb = core.qweb;
    
    var FormView_Extend = FormController.include({
        renderButtons: function($node) {
            this._super($node);
            if (this.$buttons) {
                this.$buttons.find('.o_form_button_popup').on('click', this.on_button_popup);
            }
        },
        on_button_popup: function() {
            var self = this;
            
            self.url_val = self.get_action_value('URL');

            if(!self.url_val)
            {
                $("input[type='radio']").each(function(index, item){
                    if($(item).is( ":checked" ))
                    {
                        if($(item).attr("data-value").startsWith("URL:"))
                        {
                            self.url_val = $(item).attr("data-value").substr(4);
                            return;
                        }
                    }
                });
            }
            
            if(self.url_val)
            {
                var width = 900;
                var height = 600;
                if(self.get_action_value('URL-width'))
                    width = self.get_action_value('URL-width');
                else if(self.get_action_value('URL-height'))
                    height = self.get_action_value('URL-height');
                    
                $.colorbox({href:self.url_val, iframe:true, width:width, height:height});
            }
            else
                $.colorbox({html:'<h3><strong>There is no popup option selected.</strong></h3><br/><br/>'
                    
                                /*'You should set a selection field in the model with the format URL:dns_address<br/>' + 
                                'urls = fields.Selection(string="URLs",' + 
                                'selection = [("URL:https://www.google.com", "https://www.google.com"),' + 
                                '("URL:https://www.wikipedia.com", "https://www.wikipedia.com"),' + 
                                '("URL:http://localhost:8069", "http://localhost:8069")])<br/><br/>' + 
                                
                                'And set the selection field with widget="radio" in the view:<br/>' + 
                                '&lt;field name="urls" options="{\'horizontal\': true}" widget="radio"/&gt;<br/><br/>' + 
                                
                                'Or set the property URL="https://www.wikipedia.com" in the \'form\' tag:<br/>' + 
                                '&lt;form string="Form title one" URL="https://www.wikipedia.com" URL-width="900" URL-height="600"&gt;<br/>' + 
                                '    ...<br/>' + 
                                '    ...<br/>' + 
                                '&lt;form/&gt;'*/});
        },
        /*is_action_enabled: function(action) {
            var attrs = this.fields_view.arch.attrs;
            return (action in attrs) ? JSON.parse(attrs[action]) : false;
            //return (action in attrs) ? JSON.parse(attrs[action]) : true;
        },*/
        get_action_value: function(action) {
            var attrs = this.renderer.arch.attrs;
            return (action in attrs) ? attrs[action] : false;
            //return (action in attrs) ? JSON.parse(attrs[action]) : true;
        },
    });
    
    /*return {
        FormView: FormView_Extend,
    };*/
    
});
