#
# spec file for package liblc3
#
# Copyright (c) 2023 SUSE LLC
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


%define lc3soname liblc3-1

Name:           liblc3
Version:        1.0.2
Release:        0
Summary:        Low Complexity Communication Codec (LC3)
License:        Apache-2.0
URL:            https://github.com/google/liblc3
Source:         %{name}-%{version}.tar.xz
Source99:       baselibs.conf
BuildRequires:  c_compiler
BuildRequires:  meson
BuildRequires:  pkgconfig

%description
Low Complexity Communication Codec (LC3).
The LC3 is an low latency audio codec.

%package -n     %{lc3soname}
Summary:        Low Complexity Communication Codec (LC3) - Shared library

%description -n %{lc3soname}
Low Complexity Communication Codec (LC3).
The LC3 is an low latency audio codec.

This package provides the shared library of %{name}.

%package        tools
Summary:        Low Complexity Communication Codec (LC3) - Tools

%description    tools
Low Complexity Communication Codec (LC3).
The LC3 is an low latency audio codec.

This package provides tools for %{name}.

%package devel
Summary:        Low Complexity Communication Codec (LC3) - Development Files
Requires:       %{lc3soname} = %{version}

%description devel
Low Complexity Communication Codec (LC3).
The LC3 is an low latency audio codec.

This package provides all the necessary files for development with
%{name}.

%prep
%autosetup -p1

%build
%meson \
	--includedir=%{_includedir}/%{name} \
	-D tools=true \
	%{nil}
%meson_build

%install
%meson_install

%ldconfig_scriptlets -n %{lc3soname}

%files -n %{lc3soname}
%license LICENSE
%{_libdir}/liblc3.so.*

%files tools
%{_bindir}/dlc3
%{_bindir}/elc3

%files devel
%doc README.md
%{_includedir}/%{name}
%{_libdir}/pkgconfig/lc3.pc
%{_libdir}/liblc3.so

%changelog
