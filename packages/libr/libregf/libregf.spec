#
# spec file for package libregf
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           libregf
%define lname	libregf1
%define timestamp	20190303
Version:        0~%timestamp
Release:        0
Summary:        Library to access Windows REGF-type Registry files
License:        LGPL-3.0-or-later AND GFDL-1.3-or-later
Group:          Productivity/File utilities
Url:            https://github.com/libyal/libregf/wiki
Source:         https://github.com/libyal/libregf/releases/download/%timestamp/%name-alpha-%timestamp.tar.gz
Source2:        Windows_NT_Registry_File_REGF_format.pdf
BuildRequires:  pkg-config
BuildRequires:  python-devel
BuildRequires:  pkgconfig(fuse) >= 2.6
BuildRequires:  pkgconfig(libbfio) >= 20131003
BuildRequires:  pkgconfig(libcdata) >= 20130904
BuildRequires:  pkgconfig(libcerror) >= 20140105
BuildRequires:  pkgconfig(libcfile) >= 20130809
BuildRequires:  pkgconfig(libclocale) >= 20130609
BuildRequires:  pkgconfig(libcnotify) >= 20130609
BuildRequires:  pkgconfig(libcsplit) >= 20130609
BuildRequires:  pkgconfig(libcstring) >= 20120425
BuildRequires:  pkgconfig(libcsystem) >= 20120425
BuildRequires:  pkgconfig(libfdatetime) >= 20130317
BuildRequires:  pkgconfig(libfguid) >= 20140105
BuildRequires:  pkgconfig(libuna) >= 20130728
# Using these packages (libf*) are released but are not stable per upstream
# Verified 9/19/2014; 1/1/2017 I'm going to try and use them
BuildRequires:  pkgconfig(libfcache) >= 20170111
BuildRequires:  pkgconfig(libfdata) >= 20170112
BuildRequires:  pkgconfig(libfwnt) >= 20170115
BuildRequires:  pkgconfig(libfwsi) >= 20170117

#BuildRequires:  pkgconfig(libcpath) >= 20130809
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
libregf is a library to access Windows Registry files of the REGF
type (a non-text representation).

%package -n %lname
Summary:        Library to access Windows REGF-type Registry files
License:        LGPL-3.0-or-later
Group:          System/Libraries

%description -n %lname
libregf is a library to access Windows Registry files of the REGF
type (a non-text representation).

%package tools
Summary:        Utilities to inspect Windows REGF-type Registry files
License:        LGPL-3.0-or-later
Group:          Productivity/File utilities

%description tools
Several tools for inspecting Windows REGF-type Registry files.
Typically used for computer forensics.

%package devel
Summary:        Development files for libregf, a Windows REGF-type Registry file parser
License:        LGPL-3.0-or-later AND GFDL-1.3-or-later
Group:          Development/Libraries/C and C++
Requires:       %lname = %{version}

%description devel
libregf is a library to access Windows Registry files of the REGF
type (a non-text representation).

This subpackage contains libraries and header files for developing
applications that want to make use of %{name}.

%package -n python-%{name}
Summary:        Python bindings for libregf, a library to access Windows REGF Registry files
License:        LGPL-3.0-or-later
Group:          Development/Languages/Python
Requires:       %lname = %version
Requires:       python
Provides:       pyregf = %version

%description -n python-%{name}
libregf is a library to access Windows Registry files of the REGF
type (a non-text representation).

This subpackage contains the Python bindings for libregf.

%prep
%setup -qn libregf-%timestamp
cp "%{SOURCE2}" .

%build
%configure --disable-static --enable-wide-character-type --enable-python
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -name '*.la' -delete

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%defattr(-,root,root)
%doc AUTHORS ChangeLog
%license COPYING
%{_libdir}/libregf.so.*

%files tools
%defattr(-,root,root)
%{_bindir}/regf*
%{_mandir}/man1/regf*.1*

%files devel
%defattr(-,root,root)
%doc Windows_NT_Registry_File*.pdf
%{_includedir}/libregf.h
%{_includedir}/libregf/
%{_libdir}/libregf.so
%{_libdir}/pkgconfig/libregf.pc
%{_mandir}/man3/libregf.3*

%files -n python-%{name}
%defattr(-,root,root)
%doc AUTHORS README
%license COPYING
%python_sitearch/pyregf.so

%changelog
