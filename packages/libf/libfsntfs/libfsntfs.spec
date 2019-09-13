#
# spec file for package libfsntfs
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


%define lname	libfsntfs1
%define timestamp 	20190104
Name:           libfsntfs
Version:        0~%{timestamp}
Release:        0
Summary:        Library and tools to access the NTFS filesystem
License:        LGPL-3.0-or-later AND GFDL-1.3-or-later
Group:          Productivity/File utilities
Url:            https://github.com/libyal/libfsntfs/wiki
Source:         https://github.com/libyal/libfsntfs/releases/download/%{timestamp}/%{name}-experimental-%{timestamp}.tar.gz
BuildRequires:  pkg-config
BuildRequires:  python-devel
BuildRequires:  pkgconfig(libbfio) >= 20130721
BuildRequires:  pkgconfig(libcdata) >= 20130904
BuildRequires:  pkgconfig(libcfile) >= 20130609
BuildRequires:  pkgconfig(libclocale) >= 20130609
BuildRequires:  pkgconfig(libcnotify) >= 20130609
BuildRequires:  pkgconfig(libcpath) >= 20130609
BuildRequires:  pkgconfig(libcsplit) >= 20130609
BuildRequires:  pkgconfig(libcstring) >= 20150101
BuildRequires:  pkgconfig(libcsystem) >= 20120425
BuildRequires:  pkgconfig(libcthreads)
BuildRequires:  pkgconfig(libfdatetime) >= 20130317
BuildRequires:  pkgconfig(libfguid) >= 20130904
BuildRequires:  pkgconfig(libfwnt)
BuildRequires:  pkgconfig(libuna) >= 20120425
#as of Feb 28, 2017, recent releases of the below all cause compile errors.
#BuildRequires:  pkgconfig(libfdata)
#BuildRequires:  pkgconfig(libfcache)
#BuildRequires:  pkgconfig(libcerror) > 20170101
#not yet in OBS
#BuildRequires:  pkgconfig(libfusn)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Library and tools to access the New Technology File System (NTFS).

Note that this project currently only focuses on the analysis of the format.

%package -n %{lname}
Summary:        Library to access the New Technology File System (NTFS)
License:        LGPL-3.0-or-later
Group:          System/Libraries

%description -n %{lname}
libfsntfs is a library to access the New Technology File System (NTFS).

Note that this project currently only focuses on the analysis of the format.

%package tools
Summary:        Tools to access the New Technology File System (NTFS)
License:        LGPL-3.0-or-later
Group:          Productivity/File utilities

%description tools
libfsntfs-tools is a project to access the NTFS filesystem

Note that this project currently only focuses on the analysis of the format.

%package devel
Summary:        Development files for libfsntfs
License:        LGPL-3.0-or-later AND GFDL-1.3-or-later
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
%{name} is a library to access the New Technology File System (NTFS).

This subpackage contains libraries and header files for developing
applications that want to make use of %{name}.

%package -n python2-%{name}
Summary:        Python 2 bindings for libfsntfs
License:        LGPL-3.0-or-later
Group:          Development/Languages/Python
Requires:       %{lname} = %{version}
Requires:       python2
BuildRequires:  pkgconfig(python2)
Obsoletes:      python-%{name}

%description -n python2-%{name}
Python 2 binding for libfsntfs, which can access the NTFS filesystem.

%package -n python3-%{name}
Summary:        Python 3 bindings for libfsntfs
License:        LGPL-3.0-or-later
Group:          Development/Languages/Python
Requires:       %{lname} = %{version}
Requires:       python3
BuildRequires:  pkgconfig(python3)

%description -n python3-%{name}
Python 3 binding for libfsntfs, which can access the NTFS filesystem.

%prep
%setup -q -n libfsntfs-%{timestamp}

%build
%configure --disable-static --enable-wide-character-type --enable-python2 --enable-python3
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
find %{buildroot} -type f -name "*.la" -delete -print

%post   -n %{lname} -p /sbin/ldconfig

%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog
%{_libdir}/libfsntfs.so.*

%files tools
%defattr(-,root,root)
%{_bindir}/fsntfs*
%{_mandir}/man1/fsntfsinfo.1*

%files devel
%defattr(-,root,root)
%{_includedir}/libfsntfs.h
%{_includedir}/libfsntfs/
%{_libdir}/libfsntfs.so
%{_libdir}/pkgconfig/libfsntfs.pc
%{_mandir}/man3/libfsntfs.3*

%files -n python2-%{name}
%defattr(-,root,root)
%doc AUTHORS README
%license COPYING 
%{python_sitearch}/pyfsntfs.so

%files -n python3-%{name}
%defattr(-,root,root)
%doc AUTHORS 
%license COPYING 
%{python3_sitearch}/pyfsntfs.so

%changelog
