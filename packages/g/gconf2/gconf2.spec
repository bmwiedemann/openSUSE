#
# spec file for package gconf2
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define _name GConf
Name:           gconf2
Version:        3.2.6
Release:        0
Summary:        GNOME Configuration Database System
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/GUI/GNOME
URL:            http://www.gnome.org/
Source:         http://download.gnome.org/sources/GConf/3.2/%{_name}-%{version}.tar.xz
# Generic tool, not upstreamed:
Source1:        gconftool-rebuild
# RPM specific macros:
Source2:        macros.gconf2
Source99:       baselibs.conf
# PATCH-FIX-OPENSUSE gconf2-gconftool-reload.patch -- Include sabayon paths to the default configuration. Simplifies scriptlets:
Patch2:         gconf2-gconftool-reload.patch
# PATCH-FIX-OPENSUSE gconf2-schemas-path.patch
Patch3:         gconf2-schemas-path.patch
# PATCH-FIX-OPENSUSE gconf2-sabayon.patch
Patch4:         gconf2-sabayon.patch
# PATCH-FIX-OPENSUSE gconf2-pk-default-path.patch vuntz@novell.com -- Use the right gconf path for the defaults in the pk helper
Patch5:         gconf2-pk-default-path.patch
# PATCH-FIX-UPSTREAM gconf2-pass-warning-to-caller.patch bnc#872110 dliang@suse.com
Patch6:         gconf2-pass-warning-to-caller.patch
# PATCH-FIX-OPENSUSE gconf2-fdatasync.patch mgorse@suse.com bsc#909045 -- Use fdatasync instead of fsync, and only if not installing
Patch7:         gconf2-fdatasync.patch
BuildRequires:  dbus-1-glib-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  intltool
BuildRequires:  libxml2-devel
BuildRequires:  polkit-devel
# for 2to3
BuildRequires:  python3-tools
BuildRequires:  translation-update-upstream
BuildRequires:  update-desktop-files
# gconf-sanity-check was dropped by upstream in GConf 3.2.6
Obsoletes:      gconf-sanity-check < %{version}

%description
GConf is a configuration database system for storing application
preferences. It supports default or mandatory settings set by the
administrator, and changes to the database are instantly applied to all
running applications. It is written for the GNOME desktop but doesn't
require it.

%package -n gconf-polkit
Summary:        GNOME Configuration Database System - PolicyKit service
Group:          System/GUI/GNOME
Requires:       %{name} = %{version}
Supplements:    packageand(%{name}:polkit)

%description -n gconf-polkit
GConf is a configuration database system for storing application
preferences. It supports default or mandatory settings set by the
administrator, and changes to the database are instantly applied to all
running applications. It is written for the GNOME desktop but doesn't
require it.

This package contains the PolicyKit service that allows to edit the
system-wide defaults from a user session.

%package devel
Summary:        Include files and libraries mandatory for development
Group:          Development/Libraries/GNOME
Requires:       %{name} = %{version}
# For gsettings-schema-convert (xml/etree):
Requires:       python3-base
Provides:       gconf2-doc = %{version}
Obsoletes:      gconf2-doc < %{version}

%description devel
This package contains all necessary include files and libraries needed
to develop applications that require these.

%lang_package

%prep
%setup -q -n %{_name}-%{version}
translation-update-upstream
%patch2
%patch3
%patch4
%patch5 -p1
%patch6 -p1
%patch7 -p1
2to3 --write --nobackup gsettings/gsettings-schema-convert
sed -i "s/env python$/python3/" gsettings/gsettings-schema-convert
cp -a %{SOURCE1} %{SOURCE2} .

%build
%configure --with-pic\
	--libexecdir=%{_libexecdir}/GConf/2\
	--disable-static \
        --disable-gtk \
        --disable-orbit
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{_name}2
%suse_update_desktop_file gsettings-data-convert
# Empty dir for schemas.
mkdir -p %{buildroot}%{_datadir}/GConf/schemas
mkdir -p %{buildroot}%{_sysconfdir}/gconf/gconf.xml.mandatory
mkdir -p %{buildroot}%{_sysconfdir}/gconf/gconf.xml.schemas
mkdir -p %{buildroot}%{_sysconfdir}/gconf/gconf.xml.system
mkdir -p %{buildroot}%{_sysconfdir}/gconf/gconf.xml.vendor
mkdir -p %{buildroot}%{_sysconfdir}/gconf/gconf.xml.defaults
# Directory for gsettings-data-convert
mkdir -p %{buildroot}%{_datadir}/GConf/gsettings
# Install gconftool-rebuild
install gconftool-rebuild %{buildroot}%{_bindir}
echo xml:merged:%{_sysconfdir}/gconf/gconf.xml.schemas >%{buildroot}%{_sysconfdir}/gconf/schema-install-source
# Install rpm macros
mkdir -p %{buildroot}%{_rpmmacrodir}
cp macros.gconf2 %{buildroot}%{_rpmmacrodir}

%pre
# FIXME: We should probably remove this entire section for 11.3 (Checked my mboman@suse.de, 2009-02-21)
# Remove probably obsolete /etc/opt/gnome/gconf/schemas and above.
# Needed only for old->10.3->11.x update scenario (now fixed in opt_gnome-compat).
rmdir --ignore-fail-on-non-empty etc/opt/gnome/gconf/schemas 2>/dev/null || :
rmdir --ignore-fail-on-non-empty etc/opt/gnome/gconf 2>/dev/null || :
rmdir --ignore-fail-on-non-empty etc/opt/gnome 2>/dev/null || :
# FIXME: remove this section for 12.2 (we deprecated /etc/gconf/schemas in favor if /usr/share/gconf/schemas during development of 11.2)
rmdir --ignore-fail-on-non-empty etc/gconf/schemas 2>/dev/null || :
# FIXME: remove this section for 11.4+3 (we deprecated /usr/share/gconf/schemas in favor if /usr/share/GConf/schemas during development of 11.4)
rmdir --ignore-fail-on-non-empty usr/share/gconf/schemas 2>/dev/null || :

%post
/sbin/ldconfig
# FIXME: Consider removing the rest of this section for 12.2:
# If it is an update from SuSE Linux version causing orphan files,
# avoid orphan GConf database keys. (#48114).
# Worked-around by database rebuild from scratch after each update of
# gconf2 package at the cost of extra time.
# http://bugzilla.gnome.org/show_bug.cgi?id=306924
# Since SuSE Linux 10.3, scriptlets are correct, but we have to provide
# upgrade protection for third party packages with broken scriptlets
# for a long time.
# During openSUSE 11.2 development, we moved to a merged xml file.
usr/bin/gconftool-rebuild

%postun
/sbin/ldconfig
# No other gconf instance exist and schemas directory, too.
# Delete gconf.xml.schemas and keep others (they can contain local
# customization).
# WARNING: If this package will be renamed to gconf and upgraded from <=9.0,
# the directory /etc/opt/gnome/gconf will be deleted by mistake.
# FIXME: remove test for etc/gconf/schemas for 12.2
if test $1 = 0 -a ! \( -d etc/gconf/schemas -o -d usr/share/gconf/schemas \) ; then
    rm -rf etc/gconf/gconf.xml.schemas
fi

%files
%license COPYING
%doc AUTHORS NEWS README
%{_bindir}/gconf-merge-tree
%{_bindir}/gconftool-2
%{_bindir}/gconftool-rebuild
%{_bindir}/gsettings-data-convert
%{_mandir}/man1/gconftool-2.1*
%{_mandir}/man1/gsettings-data-convert.1*
%{_datadir}/dbus-1/services/org.gnome.GConf.service
%{_libdir}/girepository-1.0/GConf-2.0.typelib
%{_datadir}/sgml/gconf
%{_libdir}/*.so.*
%dir %{_libdir}/GConf
%dir %{_libdir}/GConf/2
%{_libdir}/GConf/2/*.so*
%if "%{_libdir}" != "%{_libexecdir}"
%dir %{_libexecdir}/GConf
%dir %{_libexecdir}/GConf/2
%endif
%{_libexecdir}/GConf/2/gconfd-2
%{_libdir}/gio/modules/libgsettingsgconfbackend.so
%dir %{_datadir}/GConf
%dir %{_datadir}/GConf/gsettings
%dir %{_datadir}/GConf/schemas
%dir %{_sysconfdir}/gconf
%dir %{_sysconfdir}/gconf/gconf.xml.defaults
%dir %{_sysconfdir}/gconf/gconf.xml.mandatory
%dir %{_sysconfdir}/gconf/gconf.xml.vendor
%dir %{_sysconfdir}/gconf/gconf.xml.system
%dir %{_sysconfdir}/gconf/gconf.xml.schemas
%{_sysconfdir}/gconf/schema-install-source
%config %{_sysconfdir}/gconf/2/
%{_sysconfdir}/xdg/autostart/gsettings-data-convert.desktop

%files -n gconf-polkit
%{_libexecdir}/GConf/2/gconf-defaults-mechanism
%{_datadir}/dbus-1/system-services/org.gnome.GConf.Defaults.service
%{_datadir}/polkit-1/actions/org.gnome.gconf.defaults.policy
%{_sysconfdir}/dbus-1/system.d/org.gnome.GConf.Defaults.conf

%files lang -f %{_name}2.lang

%files devel
%doc %{_datadir}/gtk-doc/html/gconf/
%{_datadir}/aclocal/gconf-2.m4
%{_datadir}/gir-1.0/GConf-2.0.gir
%{_includedir}/gconf/
%{_libdir}/*.so
%{_libdir}/pkgconfig/gconf-2.0.pc
%{_bindir}/gsettings-schema-convert
%{_mandir}/man1/gsettings-schema-convert.1*
%{_rpmmacrodir}/macros.gconf2

%changelog
