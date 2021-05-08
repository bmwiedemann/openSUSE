#
# spec file for package ibus-m17n
#
# Copyright (c) 2021 SUSE LLC
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
Version:        1.4.5
Release:        0
Summary:        The M17N engine for IBus platform
License:        GPL-2.0-or-later
Group:          System/Localization
Provides:       locale(ibus:am;ar;as;bn;fa;gu;he;hi;ja;ka;kk;kn;ko;lo;ml;my;ur;ru;vi;zh)
URL:            https://github.com/ibus/ibus-m17n
Source:         https://github.com/ibus/ibus-m17n/releases/download/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(ibus-1.0) >= 1.4
BuildRequires:  pkgconfig(m17n-shell)
Requires:       ibus

%description
M17N engine for IBus input platform. It allows input of many languages using
the input table maps from m17n-db.

%prep
%setup -q

%build
%configure --disable-static \
           --libexecdir=%{_prefix}/%{_lib}/ibus \
           --with-gtk=3.0
%make_build

%install
%makeinstall

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc AUTHORS README
%{_datadir}/ibus-*
%{_libdir}/ibus/ibus-*
%{_datadir}/ibus/component/*
%{_datadir}/applications/ibus-setup-m17n.desktop
%{_datadir}/glib-2.0/schemas/org.freedesktop.ibus.engine.m17n.gschema.xml
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/m17n.appdata.xml

%changelog
