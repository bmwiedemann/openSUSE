#
# spec file for package libspng
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2025 Florian "sp1rit" <sp1rit@disroot.org>
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

%define sover 0

Name:           libspng
Version:        0.7.4
Release:        0
Summary:        PNG reader/writer library
License:        BSD-2-Clause
URL:            https://libspng.org/
Source0:        https://github.com/randy408/%{name}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(zlib)

%define _description %{expand:
A C library for reading and writing Portable Network Graphics (PNG)
format files with a focus on security.}

%description %{_description}

%package -n %{name}%{sover}
Summary:        PNG reader/writer library
Group:          System/Libraries

%description -n %{name}%{sover} %{_description}

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{name}%{sover} = %{version}

%description devel %{_description}

This subpackage contains development files for %{name}.

%prep
%autosetup -p1

%build
%meson \
	-Dbuild_examples=false \
	%{nil}
%meson_build

%install
%meson_install

%ldconfig_scriptlets -n %{name}%{sover}

%files -n %{name}%{sover}
%license LICENSE
%{_libdir}/libspng.so.%{sover}
%{_libdir}/libspng.so.%{version}

%files devel
%doc README.md
%doc SECURITY.md
%{_includedir}/spng.h
%{_libdir}/libspng.so
%{_libdir}/pkgconfig/spng.pc

%changelog
