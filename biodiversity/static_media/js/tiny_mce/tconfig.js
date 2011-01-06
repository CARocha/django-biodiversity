function CustomFileBrowser(field_name, url, type, win) {
    //alert("Field_Name: " + field_name + "\nURL: " + url + "\nType: " + type + "\nWin: " + win);
    var cmsURL = "/admin/filebrowser/";
    cmsURL = cmsURL + "&type=" + type;

    tinyMCE.activeEditor.windowManager.open({
        file: cmsURL,
        width: 400,  // Your dimensions may differ - toy around with them!
        height: 300,
        resizable: "yes",
        scrollbars: "yes",
        inline: "no",  // This parameter only has an effect if you use the inlinepopups plugin!
        popup_css : false,
        close_previous: "no"        
    }, {
        window: win,
        input: field_name,
        editor_id: tinyMCE.selectedInstance.editorId
    });
    return false;
}

tinyMCE.init({
	// General options
	mode : "textareas",
	theme : "advanced",
	plugins : "pagebreak,style,layer,table,save,advhr,advimage,advlink,emotions,iespell,insertdatetime,preview,media,searchreplace,print,contextmenu,paste,directionality,fullscreen,noneditable,visualchars,nonbreaking,xhtmlxtras,template,inlinepopups,autosave",
	// Theme options
	theme_advanced_buttons1 : "bold,italic,underline,strikethrough,|,justifyleft,justifycenter,justifyright,justifyfull,|,styleselect,formatselect,fontselect,fontsizeselect",
	theme_advanced_buttons2 : "cut,copy,paste,|,bullist,numlist,|,blockquote,|,undo,redo,|,link,unlink,image,media,cleanup,code,|,emotions,inserttime,preview,|,forecolor,",
	theme_advanced_buttons3 : "",
	theme_advanced_buttons4 : "",
	theme_advanced_toolbar_location : "top",
	theme_advanced_toolbar_align : "left",
	theme_advanced_statusbar_location : "bottom",
	invalid_elements: "script,form,textarea,input,label,div",
	file_browser_callback: "CustomFileBrowser",
	// Example word content CSS (should be your site CSS) this one removes paragraph margins
	content_css : "/files/js/tiny_mce/css/word.css"

});

