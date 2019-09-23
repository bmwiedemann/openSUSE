#
# spec file for package libhubbub
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           libhubbub
Version:        0.3.0
Release:        0
Summary:        An HTML5 compliant parsing library
License:        MIT
Group:          Development/Libraries/C and C++
Url:            http://www.netsurf-browser.org/projects/hubbub/
Source:         http://download.netsurf-browser.org/libs/releases/%{name}-%{version}-src.tar.gz
Patch0:         libhubbub-0.3.0-notimestamp.patch
Patch1:         0001-workaround-fail-on-ppc64.patch
Patch2:         libhubbub-0.3.0-is_error.patch
BuildRequires:  check-devel
BuildRequires:  doxygen
BuildRequires:  libjson-c-devel >= 0.11
BuildRequires:  libparserutils-devel >= 0.2.0
BuildRequires:  netsurf-buildsystem >= 1.1
BuildRequires:  pkg-config
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Hubbub is an HTML5 compliant parsing library, written in C. It was
developed as part of the NetSurf project.

%package -n libhubbub0
Summary:        An HTML5 compliant parsing library
Group:          System/Libraries

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
Group:          Development/Libraries/C and C++
Requires:       libhubbub0 = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package doc
Summary:        Documentation of %{name} API
Group:          Documentation
%if 0%{?suse_version} >= 1120
BuildArch:      noarch
%endif

%description doc
The %{name}-doc package contains documentation files for %{name}.

%global make_vars COMPONENT_TYPE=lib-shared PREFIX=%{_prefix} LIBDIR=%{_lib} Q=
%global build_vars OPTCFLAGS='%{optflags}' OPTLDFLAGS="$RPM_LD_FLAGS"

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

sed -i -e s@-Werror@@ Makefile

%build
make %{?_smp_mflags} %{make_vars} %{build_vars}
make %{?_smp_mflags} docs %{make_vars}

%install
make install DESTDIR=%{buildroot} %{make_vars}

%post -n libhubbub0 -p /sbin/ldconfig

%postun -n libhubbub0 -p /sbin/ldconfig

%check
make %{?_smp_mflags} test %{make_vars}

%files -n libhubbub0
%defattr(-,root,root)
%{_libdir}/%{name}.so.*

%files devel
%defattr(-,root,root)
%{_includedir}/hubbub
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files doc
%defattr(-,root,root)
%doc COPYING README
%doc docs/Architecture docs/Macros docs/Todo docs/Treebuilder docs/Updated
%doc build/docs/html

%changelog
