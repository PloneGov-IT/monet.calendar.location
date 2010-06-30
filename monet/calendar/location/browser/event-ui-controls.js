/**
 * 
 */

jq(document).ready(function() {
	var kupu = jq("#kupu-editor-annotations");
	if (kupu.length>0) {
		kupu.hide();
		var label = jq("#archetypes-fieldname-annotations label.formQuestion");
		var js_baseurl = jq("head base").attr('href');
		var toggle = jq('&nbsp;<a href="javascript:;"><img alt="Mostra" src="'+js_baseurl+'/++resource++monet.calendar.location.images/show_control.gif" /></a>')
				.data("opened", false).click(function() {
					var img = toggle.children("img");
					if (toggle.data('opened')) {
						toggle.data('opened', false);
						img.attr("alt", "Mostra").attr("src", js_baseurl+'/++resource++monet.calendar.location.images/show_control.gif');
						kupu.hide();
					}
					else {
						toggle.data('opened', true);
						img.attr("alt", "Nascondi").attr("src", js_baseurl+'/++resource++monet.calendar.location.images/hide_control.gif');
						kupu.show();						
					}
				});
		label.after(toggle);
	}
});