/*
Script: sequentialdownload.js
    The client-side javascript code for the SequentialDownload plugin.
*/

SequentialDownloadPlugin = Ext.extend(Deluge.Plugin, {
	constructor: function(config) {
		config = Ext.apply({
			name: "SequentialDownload"
		}, config);
		SequentialDownloadPlugin.superclass.constructor.call(this, config);
	},

	onDisable: function() {

	},

	onEnable: function() {

	}
});
new SequentialDownloadPlugin();
