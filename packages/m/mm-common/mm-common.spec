#
# spec file for package mm-common
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2016 Bjørn Lie, Bryne, Norway.
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


Name:           mm-common
Version:        1.0.1
Release:        0
Summary:        Common build files of the GNOME C++ bindings
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://gtkmm.org
Source:         https://download.gnome.org/sources/%{name}/1.0/%{name}-%{version}.tar.xz
Source99:       mm-common-rpmlintrc
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildArch:      noarch

%description
The mm-common module provides the build infrastructure and utilities
shared among the GNOME C++ binding libraries.  It is a required dependency
to build glibmm and gtkmm from git.

%package docs
Summary:        Documentation for %{name}, includes example mm module skeleton
Group:          Documentation/Other
Requires:       %{name} = %{version}

%description docs
Package contains short documentation for %{name} and example skeleton module,
which could be used as a base for new mm module.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%files
%license COPYING
%doc NEWS AUTHORS README
%{_bindir}/mm-common-get
%{_bindir}/mm-common-prepare
%{_mandir}/man1/mm-common-get.1%{?ext_man}
%{_mandir}/man1/mm-common-prepare.1%{?ext_man}
%dir %{_datadir}/aclocal
%{_datadir}/aclocal/mm-*.m4
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
# Not split out as the entire point of this package is development.
%{_datadir}/pkgconfig/mm-common-libstdc++.pc
%{_datadir}/pkgconfig/mm-common-util.pc

%files docs
%dir %{_datadir}/doc/%{name}
%{_datadir}/doc/mm-common/*

%changelog
