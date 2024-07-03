#
# spec file for package libtraceevent
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


%define sonum   1
%define dname   traceevent
%define soname  %{name}%{sonum}
%define sodname %{dname}%{sonum}

Name:           libtraceevent
Version:        1.8.2
Release:        0
Summary:        Linux kernel trace event library
License:        GPL-2.0-only AND LGPL-2.1-only
Group:          Development/Libraries/C and C++
URL:            https://git.kernel.org/pub/scm/libs/libtrace/libtraceevent.git/
Source:         https://git.kernel.org/pub/scm/libs/libtrace/%{name}.git/snapshot/%{name}-%{version}.tar.gz
Source9:        %name-rpmlintrc
BuildRequires:  asciidoc
BuildRequires:  fdupes
BuildRequires:  glibc-devel
BuildRequires:  meson
BuildRequires:  source-highlight
BuildRequires:  xmlto

%description
Linux kernel trace event library. This was once embedded in trace-cmd, but now it is its own standalone library.

%package -n %{soname}
Summary:        Linux kernel trace event library
License:        GPL-2.0-only
Group:          System/Libraries

%description -n %{soname}
The libtraceevent library provides APIs to access kernel tracepoint events located in the tracefs file system under the events directory.

%package -n %{soname}-plugins
Summary:        Plugins for the Linux kernel trace event library
License:        GPL-2.0-only AND LGPL-2.1-only
Group:          System/Libraries
Requires:       %{soname} = %{version}

%description -n %{soname}-plugins
This package provides plugins for the libtraceevent library.

%package devel
Summary:        Header files for %{name}
License:        GPL-2.0-only AND LGPL-2.1-only
Group:          Development/Libraries/C and C++
Requires:       %{soname} = %{version}

%description -n %{name}-devel
The package provides header and other needed development files for the library %{name}

%prep
%autosetup -p1

%build
export LDFLAGS="-ldl"

%meson \
    --default-library=shared \
    -Dhtmldir=%{_docdir}/%{name} \
    -Dplugindir=%{_libdir}/%{sodname}/plugins
%meson_build
%meson_build docs

%install
%meson_install

%fdupes %buildroot/%_prefix

ls -lR %{buildroot}/%{_libdir}

%post -n %{soname} -p /sbin/ldconfig
%postun -n %{soname} -p /sbin/ldconfig

%files -n %{soname}
%{_libdir}/%{name}.so.*

%files -n %{soname}-plugins
%dir %{_libdir}/%{sodname}
%dir %{_libdir}/%{sodname}/plugins
%{_libdir}/%{sodname}/plugins/*.so*
%{_libdir}/%{sodname}/plugins/libtraceevent-dynamic-list

%files devel
%dir %{_includedir}/%{dname}
%{_includedir}/%{dname}/*.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_mandir}/man3/*
%{_docdir}/%{name}/

%changelog
