#
# spec file for package libkiwix
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

%define lib_name %{name}14
Name:           libkiwix
Version:        14.2.1
Release:        0
Summary:        Common code base for all Kiwix ports
License:        GPL-3.0-or-later
URL:            https://github.com/kiwix/libkiwix/
Source0:        https://mirror.download.kiwix.org/release/libkiwix/libkiwix-%{version}.tar.xz
BuildRequires:  meson
BuildRequires:  pkgconfig(gtest)
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libmicrohttpd)
BuildRequires:  pkgconfig(libzim)
BuildRequires:  pkgconfig(pugixml)
BuildRequires:  python-rpm-macros
BuildRequires:  libkainjow-mustache-devel

%description
The Libkiwix provides the Kiwix software suite core. It contains the code shared by all Kiwix ports.

%package -n %{lib_name}
Summary:        The libkiwix library

%description -n %{lib_name}
This subpackage contians the %{lib_name} library

%package devel
Summary:        Development files for libkiwix
Requires:       %{lib_name} = %{version}

%description devel

Development files for libkiwix.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
%python3_fix_shebang

%check
%meson_test

%ldconfig_scriptlets -n %{lib_name}

%files -n %{lib_name}
%license COPYING
%{_libdir}/%{name}.so.*

%files devel
%license COPYING
%doc ChangeLog README.md
%{_bindir}/kiwix-compile-i18n
%{_bindir}/kiwix-compile-resources
%{_includedir}/kiwix
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/%{name}.so
%{_mandir}/man1/kiwix-compile-i18n*
%{_mandir}/man1/kiwix-compile-resources*

%changelog

