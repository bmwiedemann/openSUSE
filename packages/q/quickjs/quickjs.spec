#
# spec file for package quickjs
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


%define ver  2026-06-04
%if 0%{?suse_version} && 0%{?suse_version} < 1500
%define compiler CC=gcc-7
# /usr/include/c++/12/stdatomic.h
BuildRequires:  gcc7-c++
%else
BuildRequires:  gcc-c++
%endif
Name:           quickjs
Version:        20260604
Release:        0
Summary:        Small and embeddable Javascript engine
License:        MIT
URL:            https://bellard.org/quickjs
Source0:        https://bellard.org/quickjs/%{name}-%{ver}.tar.xz
BuildRequires:  make

%description
QuickJS is a small and embeddable JavaScript engine and compiler that supports reference ES2020.

%package docs
BuildArch:      noarch
Summary:        Documentation for quickjs

%description docs
Documentation for quickjs

%package devel
Summary:        Development headers for quickjs

%description devel
Development headers for quickjs

%prep
%setup -q -n %{name}-%{ver}
# inject optflags (cannot be passed normally to build)
cat >> "./Makefile" <<-EOF
CFLAGS += %{optflags} -ffat-lto-objects
LDFLAGS += %{optflags}
EOF

%build
%make_build PREFIX=%{_prefix}

%install
%make_install PREFIX=%{_prefix}
#remove extraneous binary
rm -f %{buildroot}%{_prefix}/lib/quickjs/libquickjs.lto.a

%files
%license LICENSE
%{_bindir}/qjs
%{_bindir}/qjsc

%files devel
%{_includedir}/%{name}
%dir %{_prefix}/lib/%{name}
%{_prefix}/lib/quickjs/libquickjs.a

%files docs
%doc doc

%changelog
