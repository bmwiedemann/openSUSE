#
# spec file for package libscca
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


%define lname	libscca1
%define timestamp 	20200717
Name:           libscca
Version:        0~%{timestamp}
Release:        0
Summary:        Library and tools to access the Windows Prefetch File (PF) format
License:        LGPL-3.0-or-later AND GFDL-1.3-only
Group:          Productivity/File utilities
URL:            https://github.com/libyal/libscca/wiki
Source:         https://github.com/libyal/libscca/releases/download/%{timestamp}/%{name}-alpha-%{timestamp}.tar.gz
#BuildRequires:  pkgconfig
BuildRequires:  python-devel
BuildRequires:  pkgconfig(libbfio) >= 20130721
BuildRequires:  pkgconfig(libcdata) >= 20130904
BuildRequires:  pkgconfig(libcerror) > 20150407
BuildRequires:  pkgconfig(libcfile) >= 20130609
BuildRequires:  pkgconfig(libclocale) >= 20130609
BuildRequires:  pkgconfig(libcnotify) >= 20130609
BuildRequires:  pkgconfig(libcpath) >= 20130609
BuildRequires:  pkgconfig(libcsplit) >= 20130609
BuildRequires:  pkgconfig(libcsystem) >= 20120425
BuildRequires:  pkgconfig(libcthreads)
BuildRequires:  pkgconfig(libfcache)
BuildRequires:  pkgconfig(libfdata)
BuildRequires:  pkgconfig(libfdatetime) >= 20130317
BuildRequires:  pkgconfig(libfvalue)
BuildRequires:  pkgconfig(libfwnt)
BuildRequires:  pkgconfig(libuna) >= 20120425

%description
Library and tools to access the Windows Prefetch File (PF) format.

Note that this project currently only focuses on the analysis of the format.

%package -n %{lname}
Summary:        Library to access the Windows Prefetch File (PF) format
License:        LGPL-3.0-or-later
Group:          System/Libraries

%description -n %{lname}
libscca is a library to access the Windows Prefetch File (PF) format.

Note that this project currently only focuses on the analysis of the format.

%package tools
Summary:        Tools to access the Windows Prefetch File (PF) format
License:        LGPL-3.0-or-later
Group:          Productivity/File utilities

%description tools
libscca-tools is a project to access the Windows Prefetch File (PF) format.

Note that this project currently only focuses on the analysis of the format.

%package devel
Summary:        Development files for libscca
License:        LGPL-3.0-or-later AND GFDL-1.3-or-later
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
%{name} is a library to access the Windows Prefetch File (PF) format.

This subpackage contains libraries and header files for developing
applications that want to make use of %{name}.

%package -n python3-%{name}
Summary:        Python 3 bindings for libscca
License:        LGPL-3.0-or-later
Group:          Development/Languages/Python
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(python3)
Requires:       %{lname} = %{version}
Requires:       python3

%description -n python3-%{name}
Python 3 binding for libscca, which can access the Windows Prefetch File (PF) format.

%prep
%setup -q -n libscca-%{timestamp}

%build
%configure --disable-static --enable-wide-character-type --enable-python3
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post   -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%license COPYING*
%doc AUTHORS ChangeLog
%{_libdir}/libscca.so.*

%files tools
%{_bindir}/scca*
%{_mandir}/man1/sccainfo.1%{?ext_man}

%files devel
%{_includedir}/libscca.h
%{_includedir}/libscca/
%{_libdir}/libscca.so
%{_libdir}/pkgconfig/libscca.pc
%{_mandir}/man3/libscca.3%{?ext_man}

%files -n python3-%{name}
%license COPYING*
%doc AUTHORS
%{python3_sitearch}/pyscca.so

%changelog
