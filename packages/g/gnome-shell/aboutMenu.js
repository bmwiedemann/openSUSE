// -*- mode: js; js-indent-level: 4; indent-tabs-mode: nil -*-

const GLib = imports.gi.GLib;
const Gio = imports.gi.Gio;
const Lang = imports.lang;
const Clutter = imports.gi.Clutter;
const St = imports.gi.St;
const DBus = imports.gi.DBus;

const PanelMenu = imports.ui.panelMenu;

const HostnameIface = '<node> \
<interface name="org.freedesktop.DBus.Properties"> \
    <method name="Get"> \
        <arg type="s" direction="in" /> \
        <arg type="s" direction="in" /> \
        <arg type="v" direction="out" /> \
    </method> \
</interface> \
</node>';
const HostnameProxy = Gio.DBusProxy.makeProxyWrapper(HostnameIface);

var AboutMenuButton = new Lang.Class({
    Name: 'AboutMenuButton',
    Extends: PanelMenu.Button,
    _init: function() {
        this._hostname = null;
        this._updateHostnameId = 0;
        this._ticket = 1;

        let hbox;
        let vbox;
        let menuAlignment = 0.25;

        if (Clutter.get_default_text_direction() == Clutter.TextDirection.RTL)
            menuAlignment = 1.0 - menuAlignment;
        this.parent(menuAlignment, 'About Me');

        this.about_hbox = new St.BoxLayout({ style_class: 'panel-status-menu-box' });
        this.hostname_label = new St.Label({y_align: Clutter.ActorAlign.CENTER});
        this.about_hbox.add_child(this.hostname_label);

        this.actor.add_child(this.about_hbox);
        hbox = new St.BoxLayout({ name: 'aboutArea' });
        this.menu.box.add_child(hbox);

        vbox = new St.BoxLayout({vertical: true});
        hbox.add(vbox);

        ///// Section: read '/etc/os-release' to get pretty name
        //
        // Note: previously this is defaulted to 'SUSE Linux Enterprise', now
        // let's use a "safer" option.
        let sysinfo_text = 'SUSE Linux';
        try {
            let success, contents, tag;
            let _os_release = Gio.File.new_for_path('/etc/os-release');
            [success, contents, tag] = _os_release.load_contents(null);

            let osReleaseContentStr = contents.toString();
            let prettyNameReg = /^PRETTY_NAME="(.+)"/;
            let match = null;
            for (let line of osReleaseContentStr.split('\n')) {
                match = prettyNameReg.exec(line);
                if (match) {
                    sysinfo_text = match[1];
                }
            }
        }
        catch (e) {
            // NOTE soft fail, 'sysinfo_text' is the default
            warn('ERROR: fail to read /etc/os-release');
        }

        this._sysinfo = new St.Label({ text: sysinfo_text, can_focus: true });
        vbox.add(this._sysinfo);
        this.actor.hide();

        this._updateHostnameId = GLib.timeout_add(GLib.PRIORITY_DEFAULT,
                                                  this._ticket,
                                                  Lang.bind(this, function() {
                                                      if (this._ticket < 60*60)
                                                          this._ticket *= 2;
                                                      this._updateHostnameId = 0;
                                                      this._updateHostname();
                                                      return false;
                                                  }));

        return;
    },

    _updateHostname: function(){
        let hostname_text = get_hostname();

        if ((this._hostname == null) || (this._hostname != hostname_text)) {
            this._ticket = 1;
            this._hostname = hostname_text;
            this.hostname_label.set_text(this._hostname);
            this.actor.show();
        }
        this._updateHostnameId = GLib.timeout_add_seconds(GLib.PRIORITY_DEFAULT,
                                                  this._ticket,
                                                  Lang.bind(this, function() {
                                                      if (this._ticket < 60*60)
                                                          this._ticket *= 2;
                                                      this._updateHostnameId = 0;
                                                      this._updateHostname();
                                                      return false;
                                                  }));
    },

    _destroy: function() {
        this._ticket = 1;
        if (this._updateHostnameId) {
            GLib.source_remove (this._updateHostnameId);
            this._updateHostnameId = 0;
        }
    },

});

function get_hostname() {
    let hostnameProxy = HostnameProxy(Gio.DBus.system,
	                             'org.freedesktop.hostname1',
	                             '/org/freedesktop/hostname1',
	                             null, null);

    try {
        let name = hostnameProxy.GetSync('org.freedesktop.hostname1', 'Hostname');
        return name[0].get_string()[0];

    } catch(e) {
        return 'localhost';
    }
}
