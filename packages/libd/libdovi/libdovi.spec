#
# spec file for package libdovi
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


%define sover 3

Name:           libdovi
Version:        3.1.2
Release:        0
Summary:        Library to read & write Dolby Vision metadata
Group:          Development/Libraries/Rust
License:        MIT
URL:            https://github.com/quietvoid/dovi_tool/tree/main/dolby_vision
Source0:        https://github.com/quietvoid/dovi_tool/archive/refs/tags/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
Source2:        cargo_config
Source9:        baselibs.conf
BuildRequires:  cargo-c
BuildRequires:  cargo-packaging
BuildRequires:  git

%description
Library to read & write Dolby Vision metadata

%package devel
Summary:        Development libraries for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{name}%{sover} = %{version}

%description devel
The %{name}-devel package contains C header files for
developing applications that use %{name}.

%package     -n %{name}%{sover}
Summary:        Library to read & write Dolby Vision metadata
Group:          System/Libraries

%description -n %{name}%{sover}
Library to read & write Dolby Vision metadata

%prep
%setup -a1 -q -n dovi_tool-%{name}-%{version}/dolby_vision
mkdir .cargo
cp %{SOURCE2} .cargo/config

%build
CFLAGS="%{optflags}" cargo cbuild \
    --release \
    --frozen \
    --prefix=%{_prefix} \
    --library-type=cdylib

%install
cargo cinstall \
    --release \
    --frozen \
    --destdir=%{buildroot} \
    --prefix=%{_prefix} \
    --libdir=%{_libdir} \
    --includedir=%{_includedir} \
    --pkgconfigdir=%{_libdir}/pkgconfig \
    --library-type=cdylib

%post   -n %{name}%{sover} -p /sbin/ldconfig
%postun -n %{name}%{sover} -p /sbin/ldconfig

%files -n %{name}%{sover}
%doc README.md
%license LICENSE
%{_libdir}/%{name}.so.*

%files devel
%doc README.md
%license LICENSE
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/dovi.pc
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/rpu_parser.h

%changelog
