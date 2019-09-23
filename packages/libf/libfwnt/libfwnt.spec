#
# spec file for package libfwnt
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


%define lname	libfwnt1
%define timestamp 20181227
Name:           libfwnt
Version:        0~%{timestamp}
Release:        0
Summary:        Library for Windows NT data types
License:        LGPL-3.0-or-later AND GFDL-1.3-or-later
Group:          Productivity/File utilities
Url:            https://github.com/libyal/libfwnt/wiki
Source:         https://github.com/libyal/libfwnt/releases/download/%timestamp/%{name}-alpha-%{timestamp}.tar.gz
Source2:        Locale_identifier_LCID.pdf
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libcdata) >= 20140105
BuildRequires:  pkgconfig(libcerror) >= 20140105
BuildRequires:  pkgconfig(libcnotify)
BuildRequires:  pkgconfig(libcstring) >= 20120425
BuildRequires:  pkgconfig(libcthreads) >= 20130723
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Library to provide Windows NT data type support for the libyal family of libraries.
libyal is typically used in digital forensic tools.

%package -n %{lname}
Summary:        Library for Windows NT data types
License:        LGPL-3.0-or-later
Group:          System/Libraries

%description -n %{lname}
Library to provide Windows NT data type support for the libyal family of libraries.
libyal is typically used in digital forensic tools.

%package devel
Summary:        Development files for libfwnt
License:        LGPL-3.0-or-later AND GFDL-1.3-or-later
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
Library to provide Windows NT data type support for the libyal family of libraries.  libyal is typically used in digital forensic tools.

This subpackage contains libraries and header files for developing
applications that want to make use of libfwnt.

%package -n python2-%{name}
Summary:        Python 2 bindings for %{name}
License:        LGPL-3.0-or-later
Group:          Development/Languages/Python
Requires:       %{lname} = %{version}
Requires:       python2
BuildRequires:  pkgconfig(python2)
Obsoletes:      python-%{name}

%description -n python2-%{name}
This packinge provides Python 2 bindings for ${name}

%package -n python3-%{name}
Summary:        Python 3 bindings for ${name}
License:        LGPL-3.0-or-later
Group:          Development/Languages/Python
Requires:       %{lname} = %{version}
Requires:       python3
BuildRequires:  pkgconfig(python3)

%description -n python3-%{name}
This packinge provides Python 3 bindings for ${name}

%prep
%setup -q -n libfwnt-%{timestamp}
cp "%{S:2}" .

%build
%configure --disable-static --enable-wide-character-type --enable-python2 --enable-python3
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
find %{buildroot} -type f -name "*.la" -delete -print

%check
# make check

%post   -n %{lname} -p /sbin/ldconfig

%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%defattr(-,root,root)
%doc AUTHORS ChangeLog
%license COPYING
%{_libdir}/libfwnt.so.*

%files devel
%defattr(-,root,root)
%doc AUTHORS README ChangeLog
%license COPYING
%doc Locale_identifier_LCID.pdf
%{_includedir}/libfwnt.h
%{_includedir}/libfwnt/
%{_libdir}/libfwnt.so
%{_libdir}/pkgconfig/libfwnt.pc
%{_mandir}/man3/libfwnt.3*

%files -n python2-%{name}
%defattr(-,root,root)
%doc AUTHORS
%license COPYING
%{python_sitearch}/pyfwnt.so

%files -n python3-%{name}
%defattr(-,root,root)
%doc AUTHORS
%license COPYING
%{python3_sitearch}/pyfwnt.so

%changelog
