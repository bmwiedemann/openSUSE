#
# spec file for package ibus-m17n
#
# Copyright (c) 2020 SUSE LLC
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


Name:           ibus-m17n
BuildRequires:  ibus-devel
BuildRequires:  m17n-lib-devel
BuildRequires:  pkgconfig
Version:        1.4.2
Release:        0
Summary:        The M17N engine for IBus platform
License:        GPL-2.0-or-later
Group:          System Environment/Libraries
Provides:       locale(ibus:am;ar;as;bn;fa;gu;he;hi;ja;ka;kk;kn;ko;lo;ml;my;ur;ru;vi;zh)
URL:            http://code.google.com/p/ibus/
Source:         %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       ibus

%description
M17N engine for IBus input platform. It allows input of many languages using
the input table maps from m17n-db.

%prep
%setup -q

%build
%configure --disable-static --libexecdir=%{_prefix}/%{_lib}/ibus
make %{?jobs:-j %jobs}

%install
%makeinstall

%find_lang %{name}

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS README
%license COPYING
%{_datadir}/ibus-*
%dir %{_libdir}/ibus
%{_libdir}/ibus/ibus-*
%dir %{_datadir}/ibus
%dir %{_datadir}/ibus/component
%{_datadir}/ibus/component/*
%{_datadir}/applications/ibus-setup-m17n.desktop
%{_datadir}/glib-2.0/schemas/org.freedesktop.ibus.engine.m17n.gschema.xml
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/m17n.appdata.xml

%changelog
