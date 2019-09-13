#
# spec file for package libbonoboui
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           libbonoboui
#
Version:        2.24.5
Release:        0
Summary:        The Bonobo Part of the GNOME User Interface Libraries
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Development/Libraries/GNOME
Source:         http://ftp.gnome.org/pub/GNOME/sources/%{name}/2.24/%{name}-%{version}.tar.bz2
Source99:       baselibs.conf
BuildRequires:  fdupes
BuildRequires:  gtk-doc
BuildRequires:  intltool
BuildRequires:  libglade2-devel
BuildRequires:  libgnome-devel
BuildRequires:  libgnomecanvas-devel
BuildRequires:  pkgconfig
BuildRequires:  translation-update-upstream
BuildRequires:  update-desktop-files
Recommends:     %{name}-lang

%description
This library contains the Bonobo-related part of the GNOME UI
libraries.

%package tools
Summary:        Tools for the Bonobo part of the GNOME User Interface libraries
Group:          Development/Libraries/GNOME

%description tools
This library contains the Bonobo-related part of the GNOME UI
libraries.

This package contains tools to play with Bonobo, including a
tool to browse Bonobo services that are available.

%package devel
Summary:        Development files for libbonoboui
Group:          Development/Libraries/GNOME
Requires:       %{name} = %{version}
Requires:       glib2-devel
Requires:       libbonobo-devel
Requires:       libgnome-devel
Requires:       libgnomecanvas-devel
Requires:       libxml2-devel
Requires:       orbit2-devel
#

%description devel
This package contains all necessary include files and libraries needed
to compile and link applications that use libbonoboui.

%package doc
Summary:        Documentation for libbonoboui
Group:          Documentation/HTML
Requires:       %{name} = %{version}

%description doc
This package contains documentation for libbonoboui.

%lang_package

%prep
%setup -q
translation-update-upstream

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
%if 0%{?suse_version} <= 1120
rm %{buildroot}%{_datadir}/locale/en@shaw/LC_MESSAGES/*
%endif
%suse_update_desktop_file bonobo-browser System Monitor
%find_lang libbonoboui-2.0 %{?no_lang_C}
find %{buildroot} -type f -name "*.la" -delete -print
# The demo tools are not installed
rm %{buildroot}%{_libdir}/bonobo/servers/CanvDemo.server
rm %{buildroot}%{_datadir}/gnome-2.0/ui/Bonobo_Sample_Container-ui.xml
rm %{buildroot}%{_datadir}/gnome-2.0/ui/Bonobo_Sample_Hello.xml
%fdupes %{buildroot}/%{_prefix}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%post tools
%desktop_database_post

%postun tools
%desktop_database_postun

%files
%license COPYING
%doc AUTHORS README NEWS ChangeLog
# generic directory for UI files
%dir %{_datadir}/gnome-2.0
%dir %{_datadir}/gnome-2.0/ui
%{_libdir}/*.so.*
%{_libdir}/libglade/2.0/*.so*

%files tools
%{_bindir}/bonobo-browser
%{_bindir}/test-moniker
%{_datadir}/applications/bonobo-browser.desktop
%{_datadir}/gnome-2.0/ui/bonobo-browser.xml

%files devel
%{_includedir}/libbonoboui-2.0
%{_libdir}/*.so
%{_libdir}/pkgconfig/libbonoboui-2.0.pc

%files doc
%{_datadir}/gtk-doc/html/*
%dir %{_libdir}/bonobo-2.0
%{_libdir}/bonobo/servers/Bonobo_Sample_Controls.server
%dir %{_libdir}/bonobo-2.0/samples/
%{_libdir}/bonobo-2.0/samples/bonobo-sample-controls-2

%files lang -f libbonoboui-2.0.lang

%changelog
