#
# spec file for package libcreg
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


Name:           libcreg
%define lname	libcreg1
%define timestamp	20200725
Version:        0~%timestamp
Release:        0
Summary:        Library to access Windows 9x/Me REGF-type Registry files
License:        LGPL-3.0-or-later AND GFDL-1.3-or-later
Group:          Productivity/File utilities
URL:            https://github.com/libyal/libcreg/wiki
Source:         https://github.com/libyal/libcreg/releases/download/%timestamp/%name-experimental-%timestamp.tar.gz
BuildRequires:  pkgconfig(libbfio) 
BuildRequires:  pkgconfig(libcdata)
BuildRequires:  pkgconfig(libcerror)
BuildRequires:  pkgconfig(libcfile)
BuildRequires:  pkgconfig(libclocale)
BuildRequires:  pkgconfig(libcnotify)
BuildRequires:  pkgconfig(libcpath)
BuildRequires:  pkgconfig(libcsplit)
BuildRequires:  pkgconfig(libcthreads)
BuildRequires:  pkgconfig(libfcache)
BuildRequires:  pkgconfig(libfdata)
BuildRequires:  pkgconfig(libuna)


#BuildRequires:  pkgconfig(libcpath) >= 20130809
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
libcreg is a library to access Windows 9x/Me Registry files of the REGF
type (a non-text representation).

%package -n %lname
Summary:        Library to access Windows 9x/Me REGF-type Registry files
License:        LGPL-3.0-or-later
Group:          System/Libraries

%description -n %lname
libcreg is a library to access Windows 9x/Me Registry files of the REGF
type (a non-text representation).

%package tools
Summary:        Utilities to inspect Windows 9x/Me REGF-type Registry files
License:        LGPL-3.0-or-later
Group:          Productivity/File utilities

%description tools
Several tools for inspecting Windows 9x/Me REGF-type Registry files.
Typically used for computer forensics.

%package devel
Summary:        Development files for libcreg, a Windows 9x/Me REGF-type Registry file parser
License:        LGPL-3.0-or-later AND GFDL-1.3-or-later
Group:          Development/Libraries/C and C++
Requires:       %lname = %{version}

%description devel
libcreg is a library to access Windows 9x/Me Registry files of the REGF
type (a non-text representation).

This subpackage contains libraries and header files for developing
applications that want to make use of %{name}.

%package -n python3-%{name}
Summary:        Python3 bindings for libcreg, a library to access Windows 9x/Me REGF Registry files
License:        LGPL-3.0-or-later
Group:          Development/Languages/Python
Requires:       %lname = %version
Requires:       python3
BuildRequires:  pkgconfig(python3)

%description -n python3-%{name}
libcreg is a library to access Windows 9x/Me Registry files of the REGF
type (a non-text representation).

This subpackage contains the Python3 bindings for libcreg.

%prep
%setup -qn libcreg-%timestamp

%build
%configure \
    --disable-static \
    --enable-wide-character-type \
    --enable-python3
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -name '*.la' -delete

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%defattr(-,root,root)
%doc AUTHORS ChangeLog
%license COPYING*
%{_libdir}/libcreg.so.*

%files tools
%defattr(-,root,root)
%{_bindir}/creg*
%{_mandir}/man1/creg*.1*

%files devel
%defattr(-,root,root)
%{_includedir}/libcreg.h
%{_includedir}/libcreg/
%{_libdir}/libcreg.so
%{_libdir}/pkgconfig/libcreg.pc
%{_mandir}/man3/libcreg.3*

%files -n python3-%{name}
%defattr(-,root,root)
%doc AUTHORS README
%license COPYING*
%{python3_sitearch}/pycreg.so

%changelog
