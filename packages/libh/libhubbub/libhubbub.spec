#
# spec file for package libhubbub
#
# Copyright (c) 2021 SUSE LLC
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


%{!?make_build:%global make_build make %{?_smp_mflags}}
%global make_vars COMPONENT_TYPE=lib-shared PREFIX=%{_prefix} LIBDIR=%{_lib} CC=cc Q=
%global build_vars OPTCFLAGS='%{optflags}' OPTLDFLAGS="$RPM_LD_FLAGS"
Name:           libhubbub
Version:        0.3.7
Release:        0
Summary:        An HTML5 compliant parsing library
License:        MIT
URL:            https://www.netsurf-browser.org/projects/hubbub/
Source:         http://download.netsurf-browser.org/libs/releases/%{name}-%{version}-src.tar.gz
Patch0:         0001-do-not-use-deprecated-is_error.patch
BuildRequires:  netsurf-buildsystem >= 1.1
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(check)
BuildRequires:  pkgconfig(json-c) >= 0.11
BuildRequires:  pkgconfig(libparserutils) >= 0.2.0

%description
Hubbub is an HTML5 compliant parsing library, written in C. It was
developed as part of the NetSurf project.

%package -n libhubbub0
Summary:        An HTML5 compliant parsing library

%description -n libhubbub0
Hubbub is an HTML5 compliant parsing library, written in C. It was
developed as part of the NetSurf project.

The HTML5 specification defines a parsing algorithm, based on the
behaviour of mainstream browsers, which provides instructions for how to
parse all markup, both valid and invalid. As a result, Hubbub parses web
content well.

Features:
* Parses HTML, good and bad
* Simple C API
* Fast
* Character encoding detection
* Well-tested (~90% test coverage)
* Portable

%package devel
Summary:        Development files for %{name}
Requires:       libhubbub0 = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1

sed -i -e s@-Werror@@ Makefile

%build
%make_build %{make_vars} %{build_vars}

%install
%make_install %{make_vars}

%post -n libhubbub0 -p /sbin/ldconfig
%postun -n libhubbub0 -p /sbin/ldconfig

%check
%make_build test %{make_vars} %{build_vars}

%files -n libhubbub0
%license COPYING
%{_libdir}/%{name}.so.*

%files devel
%{_includedir}/hubbub
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
