#
# spec file for package libdom
#
# Copyright (c) 2024 SUSE LLC
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
%define library_name libdom0
Name:           libdom
Version:        0.4.2
Release:        0
Summary:        C implementation of the W3C DOM API
License:        MIT
URL:            http://www.netsurf-browser.org/projects/libdom/
Source:         http://download.netsurf-browser.org/libs/releases/%{name}-%{version}-src.tar.gz
# PATCH-FIX-OPENSUSE gcc14-fix-calloc-transposed-args.patch -- Fix builds with gcc14
Patch1:         gcc14-fix-calloc-transposed-args.patch
BuildRequires:  netsurf-buildsystem
BuildRequires:  perl(Switch)
BuildRequires:  perl(XML::Parser::PerlSAX)
BuildRequires:  perl(XML::XPath)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(libhubbub)
BuildRequires:  pkgconfig(libparserutils)
BuildRequires:  pkgconfig(libwapcaplet)

%description
LibDOM is an implementation of the W3C DOM API written in C. It was developed as
part of the NetSurf project.

%package -n %{library_name}
Summary:        C implementation of the W3C DOM API

%description -n %{library_name}
LibDOM is an implementation of the W3C DOM API written in C. It was developed as
part of the NetSurf project.

%package        devel
Summary:        Development files for %{name}
Requires:       %{library_name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1

%build
%make_build %{make_vars} %{build_vars}

%install
%make_install %{make_vars}

%check
%make_build test %{make_vars} %{build_vars}

%post -n %{library_name} -p /sbin/ldconfig
%postun -n %{library_name} -p /sbin/ldconfig

%files -n %{library_name}
%license COPYING
%{_libdir}/%{name}.so.*

%files devel
%doc docs/* README
%{_includedir}/dom/
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
