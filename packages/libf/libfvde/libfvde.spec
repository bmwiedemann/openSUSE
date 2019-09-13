#
# spec file for package libfvde
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


%define lname	libfvde1
%define timestamp 20190104
Name:           libfvde
Version:        0~%{timestamp}
Release:        0
Summary:        Library to access the File Vault Drive Encryption format
License:        LGPL-3.0-or-later AND GFDL-1.3-or-later
Group:          Productivity/File utilities
Url:            https://github.com/libyal/libfvde/
Source:         https://github.com/libyal/libfvde/releases/download/%{timestamp}/libfvde-experimental-%{timestamp}.tar.gz
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(fuse)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(zlib)

BuildRequires:  pkgconfig(libbfio) >= 20130721
BuildRequires:  pkgconfig(libcaes)
BuildRequires:  pkgconfig(libcdata) >= 20140105
BuildRequires:  pkgconfig(libcfile) >= 20130609
BuildRequires:  pkgconfig(libclocale) >= 20130609
BuildRequires:  pkgconfig(libcnotify) >= 20120425
BuildRequires:  pkgconfig(libcpath) >= 20130609
BuildRequires:  pkgconfig(libcsplit) >= 20130609
BuildRequires:  pkgconfig(libcsystem) >= 20120425
BuildRequires:  pkgconfig(libcthreads) >= 20150101
BuildRequires:  pkgconfig(libfcache) >= 20120405
BuildRequires:  pkgconfig(libfdata) >= 20120405
BuildRequires:  pkgconfig(libfguid)
BuildRequires:  pkgconfig(libfvalue) >= 20150101
BuildRequires:  pkgconfig(libhmac)
BuildRequires:  pkgconfig(libuna) >= 20150101
#BuildRequires:  pkgconfig(libtool) 
#BuildRequires:  pkgconfig(libcerror) >= 20140105
#BuildRequires:  pkgconfig(libcstring) >= 20120425

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
libfvde is a library to access the File Vault Drive Encryption format.

%package -n %{lname}
Summary:        Library to access the File Vault Drive Encryption format
License:        LGPL-3.0-or-later
Group:          System/Libraries

%description -n %{lname}
The libfvde library is a library to access the File Vault Drive Encryption format

%package tools
Summary:        Several tools for reading the File Vault Drive Encryption format
License:        LGPL-3.0-or-later
Group:          Productivity/File utilities
Requires:       %{lname} = %{version}

%description tools
Several tools for reading the File Vault Drive Encryption format

See libfvde for additional details.

%package devel
Summary:        Header files and libraries for developing applications for libfvde
License:        LGPL-3.0-or-later AND GFDL-1.3-or-later
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
Header files and libraries for developing applications for libfvde

See libfvde for additional details.

This package contains libraries and header files for developing
applications that want to make use of libfvde.

%package -n python2-%{name}
Summary:        Python 2 bindings for libfvde
License:        LGPL-3.0-or-later
Group:          Development/Libraries/Python
Requires:       %{lname} = %{version}
BuildRequires:  pkgconfig(python2)
Obsoletes:      python-%{name}

%description -n python2-%{name}
This packinge provides Python 2 bindings for libfvde

%package -n python3-%{name}
Summary:        Python 3 bindings for libfvde
License:        LGPL-3.0-or-later
Group:          Development/Libraries/Python
Requires:       %{lname} = %{version}
Requires:       python3
BuildRequires:  pkgconfig(python3)

%description -n python3-%{name}
This packinge provides Python 3 bindings for libfvde

%prep
%setup -q -n libfvde-%{timestamp}

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
%doc AUTHORS COPYING NEWS README ChangeLog
%{_libdir}/libfvde.so.*

%files tools
%defattr(-,root,root)
%doc AUTHORS 
%license COPYING
%{_bindir}/fvde*
%{_mandir}/man1/fvde*.1*

%files devel
%defattr(-,root,root)
%doc AUTHORS 
%license COPYING
%{_includedir}/libfvde.h
%{_includedir}/libfvde/
%{_libdir}/libfvde.so
%{_libdir}/pkgconfig/libfvde.pc
%{_mandir}/man3/libfvde.3*

%files -n python2-%{name}
%defattr(-,root,root)
%doc AUTHORS 
%license COPYING
%{python_sitearch}/pyfvde.so

%files -n python3-%{name}
%defattr(-,root,root)
%doc AUTHORS 
%license COPYING
%{python3_sitearch}/pyfvde.so

%changelog
