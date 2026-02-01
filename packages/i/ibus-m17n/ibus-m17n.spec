#
# spec file for package ibus-m17n
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Version:        1.4.37
Release:        0
Summary:        The M17N engine for IBus platform
License:        GPL-2.0-or-later
Group:          System/Localization
URL:            https://github.com/ibus/ibus-m17n
Source:         https://github.com/ibus/%{name}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  ibus-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig(gtk4) >= 4.10.0
BuildRequires:  pkgconfig(m17n-shell)
Requires:       ibus
Provides:       locale(ibus:am;ar;as;bn;fa;gu;he;hi;ja;ka;kk;kn;ko;lo;ml;my;ur;ru;vi;zh)

%description
M17N engine for IBus input platform. It allows input of many languages using
the input table maps from m17n-db.

%lang_package

%prep
%setup -q

%build
./autogen.sh \
           --disable-static \
           --prefix=%{_prefix} \
           --libexecdir=%{_ibus_libexecdir} \
           --libdir=%{_libdir} \
           --datadir=%{_datadir}

%make_build %{?_smp_mflags}

%install
%make_install %{?_smp_mflags}

%find_lang %{name}

%files
%license COPYING
%doc AUTHORS README
%{_datadir}/ibus-*
%{_libexecdir}/ibus/ibus-*
%{_datadir}/ibus/component/*
%{_datadir}/applications/ibus-setup-m17n.desktop
%{_datadir}/glib-2.0/schemas/org.freedesktop.ibus.engine.m17n.gschema.xml
%{_datadir}/metainfo/org.freedesktop.ibus.engine.m17n.metainfo.xml
%{_datadir}/icons/hicolor/scalable/apps/ibus-m17n.svg
%{_datadir}/icons/hicolor/16x16/apps/ibus-m17n.png
%{_datadir}/icons/hicolor/22x22/apps/ibus-m17n.png
%{_datadir}/icons/hicolor/24x24/apps/ibus-m17n.png
%{_datadir}/icons/hicolor/32x32/apps/ibus-m17n.png
%{_datadir}/icons/hicolor/48x48/apps/ibus-m17n.png
%{_datadir}/icons/hicolor/64x64/apps/ibus-m17n.png
%{_datadir}/icons/hicolor/128x128/apps/ibus-m17n.png
%{_datadir}/icons/hicolor/256x256/apps/ibus-m17n.png

%files lang -f %{name}.lang

%changelog
