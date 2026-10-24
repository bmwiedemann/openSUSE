#
# spec file for package libocxl
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


%define soversion 1
Name:           libocxl
Version:        1.2.1
Release:        0%{?dist}
Summary:        Access library for OpenCAPI accelerators
License:        Apache-2.0
URL:            https://github.com/OpenCAPI/libocxl
Source:         %{name}-%{version}.tar.gz
Patch1:         add_missing_ocxl_header_from_glibc_devel_in_leap.patch
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  make
ExclusiveArch:  ppc64le

%description
Access library for OpenCAPI accelerator (refer to lib package with soversion)

%package -n %{name}%{soversion}
Summary:        OpenCAPI accelerator shared library

%description -n %{name}%{soversion}
Access library which allows to implement a user-space
driver for an OpenCAPI accelerator.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{soversion}%{?_isa} = %{version}-%{release}
Recommends:     %{name}-doc

%description    devel
The *-devel package contains header file and man pages for
developing applications that use %{name}.

%package doc
Summary:        Documentation files for %{name}
BuildArch:      noarch

%description doc
The *-doc package contains doxygen pages for
developing applications that use %{name}.

%prep
%autosetup -p1

%build
CFLAGS="%{optflags}" CXXFLAGS="%{optflags}" %make_build V=1

%install
%make_install PREFIX=%{_prefix} docdir=%{_docdir}

%fdupes %{buildroot}/%{_prefix}

%ldconfig_scriptlets -n %{name}%{soversion}

%files -n %{name}%{soversion}
%license COPYING
%doc README.md
%{_libdir}/libocxl.so.*

%files devel
%{_includedir}/*
%{_libdir}/libocxl.so
%{_mandir}/man3/*

%files doc
%{_docdir}/%{name}
%exclude %{_docdir}/%{name}/README.md

%changelog
