#
# spec file for package liborigin
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%define shlib %{name}3
Name:           liborigin
Version:        3.0.3
Release:        0
Summary:        A library for reading OriginLab OPJ project files
License:        GPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://sourceforge.net/projects/liborigin/
Source:         http://downloads.sourceforge.net/liborigin/%{name}-%{version}.tar.gz
BuildRequires:  c++_compiler
BuildRequires:  cmake
BuildRequires:  doxygen
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
BuildArch:      noarch

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

%build
%cmake \
	-DBUILD_STATIC_LIBS=off \
	-DCMAKE_INSTALL_DOCDIR=%{_docdir}/%{name}
%cmake_build origin opj2dat doc

%install
%cmake_install
# installed via macro
rm %{buildroot}%{_docdir}/%{name}/COPYING

%check
%ctest

%ldconfig_scriptlets -n %{shlib}

%files -n %{shlib}
%license COPYING
%{_libdir}/%{name}.so.*

%files devel
%license COPYING
%{_libdir}/%{name}.so
%{_includedir}/%{name}/
%{_libdir}/pkgconfig/*.pc

%files doc
%license COPYING
%{_docdir}/%{name}/

%files tools
%license COPYING
%{_bindir}/opj2dat

%changelog
