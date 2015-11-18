define(["marionette","../core","../query"],function(t,e,i){var n=t.Layout.extend({className:"workspace-workflow",template:"workflows/workspace",regions:{queries:".query-region",publicQueries:".public-query-region",editQueryRegion:".save-query-modal",deleteQueryRegion:".delete-query-modal"},regionViews:{queries:i.QueryList,publicQueries:i.QueryList},initialize:function(){if(this.data={},e.isSupported("2.2.0")&&!(this.data.publicQueries=this.options.public_queries))throw new Error("public queries collection required");if(!(this.data.queries=this.options.queries))throw new Error("queries collection required");if(!(this.data.context=this.options.context))throw new Error("context model required");if(!(this.data.view=this.options.view))throw new Error("view model required");this.on("router:load",function(){e.panels.context.closePanel({full:!0}),e.panels.concept.closePanel({full:!0})})},onRender:function(){var t=new this.regionViews.queries({editQueryRegion:this.editQueryRegion,deleteQueryRegion:this.deleteQueryRegion,collection:this.data.queries,context:this.data.context,view:this.data.view,editable:!0});if(this.queries.show(t),e.isSupported("2.2.0")){var i=new this.regionViews.publicQueries({collection:this.data.publicQueries,context:this.data.context,view:this.data.view,title:"Public Queries",emptyMessage:"There are no public queries. You can create a new, public query by navigating to the 'Results'page and clicking on the 'Save Query...' button. While filling out the query form, you can mark the query as public which will make it visible to all users and cause it to be listed here."});this.listenTo(this.data.queries,"sync",function(){this.data.publicQueries.fetch({reset:!0})}),this.publicQueries.show(i)}}});return{WorkspaceWorkflow:n}});
//@ sourceMappingURL=workspace.js.map