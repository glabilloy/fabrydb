define(["underscore","marionette","../core"],function(t,e,i){var n=e.ItemView.extend({className:"query-loader",template:"query/loader",ui:{loadingMessage:".loading-message",errorMessage:".error-message"},initialize:function(){if(this.data={},!(this.data.context=this.options.context))throw new Error("context model required");if(!(this.data.view=this.options.view))throw new Error("view model required");if(!(this.data.queries=this.options.queries))throw new Error("queries collection required");this.on("router:load",this.onRouterLoad),this.listenTo(this.data.queries,"sync",this.loadRequestedQuery)},onRouterLoad:function(t,e,i){this.requestedQueryId=parseInt(i)||null},loadRequestedQuery:function(){if(this.requestedQueryId){var t=this.data.queries.get(this.requestedQueryId);delete this.requestedQueryId,t?(this.data.view.save("json",t.get("view_json")),this.data.context.save("json",t.get("context_json"),{reset:!0}),i.router.navigate("results",{trigger:!0})):(this.ui.loadingMessage.hide(),this.ui.errorMessage.show())}}});return{QueryLoader:n}});
//@ sourceMappingURL=loader.js.map