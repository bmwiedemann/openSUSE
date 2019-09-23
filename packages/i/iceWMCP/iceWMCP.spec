#
# spec file for package iceWMCP
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           iceWMCP
Version:        3.2
Release:        0
Summary:        An IceWM Configuration Panel
License:        GPL-2.0+
Group:          System/GUI/Other
Url:            http://www.phrozensmoke.com/projects/icewmcp/
Source:         http://downloads.sf.net/icesoundmanager/IceWMControlPanel-%version.tar.bz2
Source1:        iceWMCP         
Patch:          %{name}-%{version}-applets.patch
Patch2:         %{name}-%{version}-deprecated.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
Requires:       python
Requires:       python-gtk

%description
IceWM Control Panel (IceWMCP) is full-featured, Gtk-based control panel
for IceWM. It is meant to run in IceWM, but can be used in ANY window
manager as a general-purpose control panel.



Authors:
--------
    Erica Andrews PhrozenSmoke@yahoo.com

%package addons
Summary:        An IceWM Configuration Panel
Group:          System/GUI/Other
Requires:       %{name} = %{version} 
Recommends:     java-sun xscreensaver usbview kde4-kcron kde4-kuser gamix

%description addons
IceWM Control Panel (IceWMCP) is full-featured, Gtk-based control panel
for IceWM. It is meant to run in IceWM, but can be used in ANY window
manager as a general-purpose control panel.



Authors:
--------
    Erica Andrews PhrozenSmoke@yahoo.com

%prep
%setup -n INSTALL-IceWMCP
# remove not wanted applets
for APPLET in tkantivir gpassword userinfo gfcc gnorpm usermount godbc sysinfo; do
	rm applets/$APPLET.cpl
	rm applets/es/$APPLET.cpl
	rm applets/fr/$APPLET.cpl
	rm applets/ru/$APPLET.cpl
	rm applets/zh_tw/$APPLET.cpl
	rm applet-icons/$APPLET.png
done
%patch
%patch2

%build
#nothing

%install
mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}
cp -a doc/* $RPM_BUILD_ROOT%{_docdir}/%{name}
cp -ar licenses $RPM_BUILD_ROOT%{_docdir}/%{name}
rm -r doc licenses
rm .cvsignore INSTALL-ME.sh install-pix.gif PyInstallShield
mkdir -p $RPM_BUILD_ROOT/usr/share/%{name}
cp -ra * $RPM_BUILD_ROOT/usr/share/%{name}
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m 755 $RPM_SOURCE_DIR/iceWMCP $RPM_BUILD_ROOT%{_bindir}
%find_lang icewmcp-iceme
%find_lang icewmcp-icepref icewmcp-iceme.lang
%find_lang icewmcp-ism icewmcp-iceme.lang
%find_lang icewmcp icewmcp-iceme.lang

%files -f icewmcp-iceme.lang
%defattr(-,root,root)
/usr/share/%{name}
%doc %{_docdir}/%{name}
%{_bindir}/iceWMCP
%exclude /usr/share/%{name}/applets/gfloppy.cpl
%exclude /usr/share/%{name}/applets/*/gfloppy.cpl
%exclude /usr/share/%{name}/applet-icons/gfloppy.png
%exclude /usr/share/%{name}/applets/java.cpl
%exclude /usr/share/%{name}/applets/*/java.cpl
%exclude /usr/share/%{name}/applet-icons/java.png
%exclude /usr/share/%{name}/applets/gtop.cpl
%exclude /usr/share/%{name}/applets/*/gtop.cpl
%exclude /usr/share/%{name}/applet-icons/gtop.png
%exclude /usr/share/%{name}/applets/xscreensaver.cpl
%exclude /usr/share/%{name}/applets/*/xscreensaver.cpl
%exclude /usr/share/%{name}/applet-icons/screensaver.png
%exclude /usr/share/%{name}/applets/usbview.cpl
%exclude /usr/share/%{name}/applets/*/usbview.cpl
%exclude /usr/share/%{name}/applet-icons/usbview.png
%exclude /usr/share/%{name}/applets/soundprop.cpl
%exclude /usr/share/%{name}/applets/*/soundprop.cpl
%exclude /usr/share/%{name}/applet-icons/soundprop.png
%exclude /usr/share/%{name}/applets/kcron.cpl
%exclude /usr/share/%{name}/applets/*/kcron.cpl
%exclude /usr/share/%{name}/applet-icons/kcron.png
%exclude /usr/share/%{name}/applets/kusers.cpl
%exclude /usr/share/%{name}/applets/*/kusers.cpl
%exclude /usr/share/%{name}/applet-icons/kusers.png

%files addons
%defattr(-,root,root)
/usr/share/%{name}/applets/gfloppy.cpl
/usr/share/%{name}/applets/*/gfloppy.cpl
/usr/share/%{name}/applet-icons/gfloppy.png
/usr/share/%{name}/applets/java.cpl
/usr/share/%{name}/applets/*/java.cpl
/usr/share/%{name}/applet-icons/java.png
/usr/share/%{name}/applets/gtop.cpl
/usr/share/%{name}/applets/*/gtop.cpl
/usr/share/%{name}/applet-icons/gtop.png
/usr/share/%{name}/applets/xscreensaver.cpl
/usr/share/%{name}/applets/*/xscreensaver.cpl
/usr/share/%{name}/applet-icons/screensaver.png
/usr/share/%{name}/applets/usbview.cpl
/usr/share/%{name}/applets/*/usbview.cpl
/usr/share/%{name}/applet-icons/usbview.png
/usr/share/%{name}/applets/soundprop.cpl
/usr/share/%{name}/applets/*/soundprop.cpl
/usr/share/%{name}/applet-icons/soundprop.png
/usr/share/%{name}/applets/kcron.cpl
/usr/share/%{name}/applets/*/kcron.cpl
/usr/share/%{name}/applet-icons/kcron.png
/usr/share/%{name}/applets/kusers.cpl
/usr/share/%{name}/applets/*/kusers.cpl
/usr/share/%{name}/applet-icons/kusers.png

%changelog
