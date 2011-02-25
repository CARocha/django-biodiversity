tinyMCE.init({
	// General options
	mode : "textareas",
	theme : "advanced",
	plugins : "pagebreak,style,layer,table,save,advhr,advimage,advlink,emotions,iespell,insertdatetime,preview,media,searchreplace,print,contextmenu,paste,directionality,fullscreen,noneditable,visualchars,nonbreaking,xhtmlxtras,template,inlinepopups,autosave",
	// Theme options
	theme_advanced_buttons1 : "bold,italic,underline,strikethrough,link,unlink,|,bullist,numlist,outdent,indent,|,justifyleft,justifycenter,justifyright,justifyfull,|,styleselect,fontselect,",
	theme_advanced_buttons2 : "", //cut,copy,paste,|,bullist,numlist,|,blockquote,|,undo,redo,|,link,unlink,image,media,cleanup,code,|,emotions,inserttime,preview,|,forecolor,",
	theme_advanced_buttons3 : "",
	theme_advanced_buttons4 : "",
	theme_advanced_toolbar_location : "top",
	theme_advanced_toolbar_align : "left",
	theme_advanced_statusbar_location : "",
	invalid_elements: "script,form,textarea,input,label,div",
	file_browser_callback: "CustomFileBrowser",
	content_css : "/files/js/tiny_mce/css/word.css",
        height: "200"
});

