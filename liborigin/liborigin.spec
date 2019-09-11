#
# spec file for package liborigin
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define shlib %{name}3
Name:           liborigin
Version:        3.0.0
Release:        0
Summary:        A library for reading OriginLab OPJ project files
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
URL:            http://sourceforge.net/projects/liborigin/
Source:         http://downloads.sourceforge.net/liborigin/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM liborigin-link-opj2dat-against-sharedlib.patch badshah400@gmail.com -- Link opj2dat against the shared library so we avoid generating and installing the static lib (https://sourceforge.net/p/liborigin/bugs/24)
Patch1:         liborigin-link-opj2dat-against-sharedlib.patch
# PATCH-FIX-UPSTREAM liborigin-remove-exit-calls.patch badshah400@gmail.com -- Remove exit calls from library; patch taken from upstream commit
Patch2:         liborigin-remove-exit-calls.patch
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig

%description
A library for reading OriginLab OPJ project files.
Features:
* reads any worksheets with all columns
* supports 4.1, 5.0, 6.0, 6.1, 7.0, 7.5 projects

%package     -n %{shlib}
Summary:        A library for reading OriginLab OPJ project files
Group:          System/Libraries

%description -n %{shlib}
A library for reading OriginLab OPJ project files.
Features:
* reads any worksheets with all columns
* supports 4.1, 5.0, 6.0, 6.1, 7.0, 7.5 projects

%package        devel
Summary:        Libraries and header files for liborigin
Group:          Development/Libraries/C and C++
Requires:       %{shlib} = %{version}
Recommends:     %{name}-doc

%description    devel
This package contains libraries and header files for developing
applications that read OriginLab OPJ project files.

%package        doc
Summary:        Documentation for liborigin
Group:          Documentation/Other
%if 0%{?suse_version} > 1110
BuildArch:      noarch
%endif

%description    doc
This package provides the documentation for liborigin.

%package        tools
Summary:        Converter for OriginLab OPJ project files
Group:          Productivity/Scientific/Other

%description    tools
Converter for OriginLab OPJ project files.
Features:
* reads any worksheets with all columns
* supports 4.1, 5.0, 6.0, 6.1, 7.0, 7.5 projects

%prep
%autosetup -p1

# fix documentation directory
sed -i "s|DESTINATION share/doc/liborigin|DESTINATION %{_docdir}/%{name}|" CMakeLists.txt

%build
%cmake
%cmake_build origin opj2dat doc

%install
%cmake_install

%post -n %{shlib} -p /sbin/ldconfig
%postun -n %{shlib} -p /sbin/ldconfig

%files -n %{shlib}
%{_libdir}/%{name}.so.*

%files devel
%{_libdir}/%{name}.so
%{_includedir}/%{name}/
%{_libdir}/pkgconfig/*.pc

%files doc
%{_docdir}/%{name}/

%files tools
%{_bindir}/opj2dat

%changelog
