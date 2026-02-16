#
# spec file for package mujs
#
# Copyright (c) 2025 SUSE LLC
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


%define ucd_ver 16.0.0
Name:           mujs
Version:        1.3.7
Release:        0
Summary:        An embeddable Javascript interpreter
License:        ISC
Group:          Development/Languages/C and C++
URL:            https://github.com/ccxvii/%{name}
Source0:        https://github.com/ccxvii/%{name}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# v=16.0.0 && u=https://www.unicode.org/Public/$v/ucd && f1=SpecialCasing.txt && f2=UnicodeData.txt && f=ucd-$v.tar.xz && cd /tmp && curl -O $u/$f1 -O $u/$f2 && tar c --remove-files "$f1" "$f2" | xz -9e > "$f"
Source1:        ucd-%{ucd_ver}.tar.xz
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  pkgconfig(readline)

%description
MuJS is a lightweight Javascript interpreter designed for embedding in other software to extend them with scripting capabilities.

%package devel
Summary:        MuJS development files
Group:          Development/Languages/C and C++
Provides:       %{name}-static = %{version}

%description devel
This package provides the MuJS static library.

%prep
%autosetup -p1 -a1

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
%make_build CFLAGS="%{optflags} -fPIC"

%install
%make_install CFLAGS="%{optflags} -fPIC" prefix="%{_prefix}" libdir="%{_libdir}"

%files
%license COPYING
%doc AUTHORS README
%{_bindir}/%{name}{,-pp}

%files devel
%license COPYING
%doc AUTHORS README
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.a

%changelog
