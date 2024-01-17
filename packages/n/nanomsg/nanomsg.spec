#
# spec file for package nanomsg
#
# Copyright (c) 2022 SUSE LLC
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


%define sover 6
Name:           nanomsg
Version:        1.2
Release:        0
Summary:        Socket library providing several common communication patterns
License:        MIT
Group:          Development/Languages/C and C++
URL:            https://nanomsg.org/
Source:         https://github.com/nanomsg/nanomsg/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         nanomsg-fix-rpath-issue.patch
BuildRequires:  cmake
BuildRequires:  libtool
BuildRequires:  pkgconfig

%description
nanomsg is a C socket library providing several common communication
patterns.

%package -n libnanomsg%{sover}
Summary:        Shared library for nanomsg
Group:          System/Libraries

%description -n libnanomsg%{sover}
nanomsg is a C socket library providing several common communication
patterns.

%package devel
Summary:        Header files for nanomsg
Group:          Development/Libraries/C and C++
Requires:       libnanomsg%{sover} = %{version}

%description devel
Development and header files for nanomsg.

%prep
%setup -q
%patch0 -p1

%build
%cmake
make %{?_smp_mflags}

%install
%cmake_install

%post   -n libnanomsg%{sover} -p /sbin/ldconfig
%postun -n libnanomsg%{sover} -p /sbin/ldconfig

%files -n libnanomsg%{sover}
%license COPYING
%doc RELEASING AUTHORS README.md
%{_libdir}/libnanomsg.so.*

%files devel
%{_includedir}/nanomsg
%{_libdir}/libnanomsg.so
%{_bindir}/nanocat
%{_libdir}/pkgconfig/nanomsg.pc
%dir %{_libdir}/cmake/nanomsg-1.1.5
%{_libdir}/cmake/nanomsg-1.1.5/nanomsg-config*.cmake
%{_libdir}/cmake/nanomsg-1.1.5/nanomsg-target*.cmake

%changelog
