#
# spec file for package libfwsi
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


%define lname	libfwsi1
%define timestamp 20181227
Name:           libfwsi
Version:        0~%{timestamp}
Release:        0
Summary:        Library to access the Windows Shell Item format
License:        LGPL-3.0-or-later AND GFDL-1.3-or-later
Group:          Productivity/File utilities
Url:            https://github.com/libyal/libfwsi/wiki
Source:         https://github.com/libyal/libfwsi/releases/download/%timestamp/%name-experimental-%timestamp.tar.gz
Source2:        Windows_Shell_Item_format.pdf
BuildRequires:  pkg-config
BuildRequires:  python-devel
BuildRequires:  pkgconfig(libcdata) >= 20140105
BuildRequires:  pkgconfig(libcerror) >= 20140105
BuildRequires:  pkgconfig(libclocale)
BuildRequires:  pkgconfig(libcnotify)
BuildRequires:  pkgconfig(libcstring) >= 20150101
BuildRequires:  pkgconfig(libcthreads) >= 20130723
BuildRequires:  pkgconfig(libfdatetime)
BuildRequires:  pkgconfig(libfguid)
BuildRequires:  pkgconfig(libfole)
BuildRequires:  pkgconfig(libuna)
# not (yet) packaged in OBS
#BuildRequires:  pkgconfig(libfwps)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Library to access the Windows Shell Item format for the libyal family of libraries.
libyal is typically used in digital forensic tools.

%package -n %{lname}
Summary:        Library to access the Windows Shell Item format
License:        LGPL-3.0-or-later
Group:          System/Libraries

%description -n %{lname}
Library to access the Windows Shell Item format for the libyal family of libraries.
libyal is typically used in digital forensic tools.

%package devel
Summary:        Development files for libfwsi
License:        LGPL-3.0-or-later AND GFDL-1.3-or-later
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
Library to access the Windows Shell Item format for the libyal family of libraries.  libyal is typically used in digital forensic tools.

This subpackage contains libraries and header files for developing
applications that want to make use of libfwsi.

%package -n python-%name
Summary:        Python bindings for libfwsi
License:        LGPL-3.0-or-later
Group:          Development/Libraries/Python
Requires:       %{lname} = %{version}
Requires:       python
Provides:       pyfwsi = %{version}

%description -n python-%name
Python bindings for libfwsi, a library to access Windows Shell Items.

%prep
%setup -q -n libfwsi-%{timestamp}
cp "%{S:2}" .

%build
%configure --disable-static --enable-wide-character-type --enable-python
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
find %{buildroot} -type f -name "*.la" -delete -print

%post   -n %{lname} -p /sbin/ldconfig

%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%defattr(-,root,root)
%doc AUTHORS ChangeLog
%license COPYING
%{_libdir}/libfwsi.so.*

%files devel
%defattr(-,root,root)
%doc AUTHORS README ChangeLog
%license COPYING
%doc Windows_Shell_Item_format.pdf
%{_includedir}/libfwsi.h
%{_includedir}/libfwsi/
%{_libdir}/libfwsi.so
%{_libdir}/pkgconfig/libfwsi.pc
%{_mandir}/man3/libfwsi.3*

%files -n python-%name
%defattr(-,root,root)
%doc AUTHORS ChangeLog
%license COPYING
%python_sitearch/pyfwsi.so

%changelog
