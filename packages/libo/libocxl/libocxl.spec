#
# spec file for package libocxl
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


%define soversion 1
Name:           libocxl
Version:        1.1.0
Release:        0%{?dist}
Summary:        Allows to implement a user-space driver for an OpenCAPI accelerator
License:        Apache-2.0
Group:          Development/Libraries/C and C++
URL:            https://github.com/OpenCAPI/libocxl
Source:         %{name}-%{version}.tar.gz
Patch1:         remove_2_backslashes_in_shell_call.patch
Patch2:         add_missing_ocxl_header_from_glibc_devel_in_leap.patch
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc
ExclusiveArch:  ppc64le

%description
Access library for OpenCAPI accelerator (refer to lib package with soversion)

%package -n %{name}%{soversion}
Summary:        OpenCAPI accelerator shared library
Group:          System/Libraries

%description -n %{name}%{soversion}
Access library which allows to implement a user-space
driver for an OpenCAPI accelerator.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{name}%{soversion}%{?_isa} = %{version}-%{release}
Recommends:     %{name}-doc

%description    devel
The *-devel package contains header file and man pages for
developing applications that use %{name}.

%package doc
Summary:        Documentation files for %{name}
Group:          Documentation/Man
BuildArch:      noarch

%description doc
The *-docs package contains doxygen pages for
developing applications that use %{name}.

%prep
%autosetup -p1

%build
CFLAGS="%{optflags}" CXXFLAGS="%{optflags}" make %{?_smp_mflags} V=1

%install
%make_install PREFIX=%{_prefix} docdir=%{_docdir}

%fdupes %{buildroot}/%{_prefix}

%post -n %{name}%{soversion} -p /sbin/ldconfig
%postun -n %{name}%{soversion} -p /sbin/ldconfig

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
