#
# spec file for package galculator
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


Name:           galculator
Version:        2.1.4
Release:        0
Summary:        A GTK 3 based calculator
License:        GPL-2.0-or-later
Group:          System/GUI/GNOME
URL:            http://galculator.mnim.org/
Source0:        http://galculator.mnim.org/downloads/%{name}-%{version}.tar.bz2
BuildRequires:  flex
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(gtk+-3.0)
Recommends:     %{name}-lang

%description
galculator is a GTK 3 based calculator with ordinary notation/reverse
polish notation (RPN), a formula entry mode, different number bases
(DEC, HEX, OCT, BIN) and different units of angular measure (DEG, RAD, GRAD).
It supports quad-precision floating point and 112-bit binary arithmetic.

%lang_package

%prep
%setup -q

%build
# workaround for GCC10 build failure
export CFLAGS="%(echo %{optflags}) -fcommon"
export CXXFLAGS="$CFLAGS"
%configure
make %{?_smp_mflags}

%install
%make_install
%if 0%{?suse_version} == 1310
rm  %{buildroot}/%{_datadir}/appdata/galculator.appdata.xml
%endif
%suse_update_desktop_file -r %{name} GTK Utility Calculator
%find_lang %{name}

%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun

%files
%doc AUTHORS ChangeLog COPYING NEWS README THANKS doc/shortcuts
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/*
%if 0%{?suse_version} > 1310
%dir %{_datadir}/appdata
%{_datadir}/appdata/galculator.appdata.xml
%endif
%{_datadir}/icons/hicolor/*/*/%{name}.*
%{_datadir}/pixmaps/%{name}.*
%{_mandir}/man1/%{name}.1%{ext_man}

%files lang -f %{name}.lang

%changelog
