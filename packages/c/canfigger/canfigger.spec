#
# spec file for package canfigger
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

%define api   0.3
%define sover 0
%define soname 0
%define libname lib%{name}%{soname}
%define devname lib%{name}%{soname}-devel

Name:           canfigger
Version:        0.3.2
Release:        0
Summary:        Lightweight configuration file parser library with XDG path helpers
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://github.com/andy5995/canfigger
Source:         https://github.com/andy5995/canfigger/releases/download/v%{version}/%{name}-%{version}.tar.xz
BuildRequires:  fdupes
BuildRequires:  meson >= 0.48.0

%description
Canfigger is a lightweight C language library designed to parse configuration
files. It provides functionality to read them and represent their contents as
a linked list of key-value pairs, along with associated attributes for each
pair. It also includes utility functions for locating standard per-user
directories (config, data, cache) and joining paths, with support for XDG on
Linux/macOS and the Windows CSIDL equivalents.

%package -n %{libname}
Summary:        Lightweight configuration file parser library with XDG path helpers
Group:          System/Libraries

%description -n %{libname}
Canfigger is a lightweight C language library designed to parse configuration
files. It provides functionality to read them and represent their contents as
a linked list of key-value pairs, along with associated attributes for each
pair. It also includes utility functions for locating standard per-user
directories (config, data, cache) and joining paths, with support for XDG on
Linux/macOS and the Windows CSIDL equivalents.

This package contains the shared library for %{name}

%package -n %{devname}
Summary:        The development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description -n %{devname}
This package contains the development files for %{name}

%package -n %{libname}-doc
Summary:        Documentation for %{name}
Group:          Documentation/HTML
BuildArch:      noarch

%description -n %{libname}-doc
This package contains the HTML documentation for %{name}

%prep
%setup -q

%build
%meson \
	-Ddocdir=%{_docdir}/%{libname} \
%meson_build

%install
%meson_install

rm %{buildroot}%{_docdir}/%{libname}/LICENSE
%fdupes %{buildroot}%{_docdir}/%{libname}/html

%check
%meson_test

%ldconfig_scriptlets -n %{libname}

%files -n %{libname}
%defattr(-,root,root)
%license LICENSE
%doc README.md ChangeLog.txt example-01.c example-01.conf example-02.c example-02.conf
%{_libdir}/libcanfigger.so.*

%files -n %{devname}
%defattr(-,root,root)
%{_libdir}/libcanfigger.so
%{_libdir}/pkgconfig/canfigger.pc
%dir %{_includedir}/canfigger
%{_includedir}/canfigger/canfigger.h
%{_includedir}/canfigger/canfigger_version.h

%files -n %{libname}-doc
%defattr(-,root,root)
%doc %{_docdir}/%{libname}/html

%changelog
