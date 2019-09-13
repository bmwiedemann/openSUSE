#
# spec file for package byzanz
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2007 wberrier@gmail.com
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


%define build_applet 0%{suse_version} < 1310

Name:           byzanz
Version:        0.3.0+git20140619
Release:        0
Summary:        Tool to record a running X desktop to an animated GIF file
License:        GPL-2.0+
Group:          Productivity/Multimedia/Video/Editors and Convertors
Url:            https://github.com/GNOME/byzanz
Source:         https://launchpad.net/ubuntu/+archive/primary/+files/%{name}_%{version}.orig.tar.xz
BuildRequires:  gettext-devel
BuildRequires:  gnome-common
BuildRequires:  intltool
BuildRequires:  translation-update-upstream
BuildRequires:  perl(XML::Parser)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(xdamage)
%if %{build_applet}
BuildRequires:  pkgconfig(libpanelapplet-4.0)
%endif
Recommends:     %{name}-lang
%if %{build_applet}
%glib2_gsettings_schema_requires
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Byzanz is a simple tool to record a running X desktop to an animated GIF file.
It is implemented as a GNOME applet. A command line tool for testing purposes
is also available.


%lang_package

%prep
%setup -q
# Disable strict build failing - that's for the devs..
sed -i 's:BYZANZ_CVS="yes":BYZANZ_CVS="no":g' configure.ac

%build
NOCONFIGURE=1 gnome-autogen.sh
%configure \
        --disable-schemas-install
make %{?_smp_mflags}

%install
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
%makeinstall
%find_lang %{name} %{?no_lang_C}

%post
%icon_theme_cache_post
%if %{build_applet}
%glib2_gsettings_schema_post
%endif

%postun
%icon_theme_cache_postun
%if %{build_applet}
%glib2_gsettings_schema_postun
%endif

%files 
%defattr(-, root, root)
%doc AUTHORS ChangeLog COPYING NEWS
%if %{build_applet}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/byzanzapplet.xml
%{_datadir}/glib-2.0/schemas/org.gnome.byzanz.applet.gschema.xml
%{_datadir}/gnome-panel/4.0/applets/org.gnome.ByzanzApplet.panel-applet
%{_libexecdir}/%{name}-applet
%endif
%{_bindir}/byzanz-playback
%{_bindir}/byzanz-record
%{_datadir}/icons/hicolor/*/apps/byzanz-record-area.*
%{_datadir}/icons/hicolor/*/apps/byzanz-record-desktop.*
%{_datadir}/icons/hicolor/*/apps/byzanz-record-window.*
%{_mandir}/man1/byzanz.1*
%{_mandir}/man1/byzanz-playback.1*
%{_mandir}/man1/byzanz-record.1*

%files lang -f %{name}.lang

%changelog
