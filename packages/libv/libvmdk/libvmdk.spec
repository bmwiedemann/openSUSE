#
# spec file for package libvmdk
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


%define lname	libvmdk1
%define timestamp 20181227
Name:           libvmdk
Version:        0~%{timestamp}
Release:        0
Summary:        Library to access the VMware Virtual Disk (VMDK) format
License:        LGPL-3.0-or-later AND GFDL-1.3-or-later
Group:          Productivity/File utilities
Url:            https://github.com/libyal/libvmdk/
Source:         https://github.com/libyal/libvmdk/releases/download/%{timestamp}/libvmdk-alpha-%{timestamp}.tar.gz
Source2:        VMWare_Virtual_Disk_Format_VMDK.pdf
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(fuse)
BuildRequires:  pkgconfig(libbfio) >= 20130721
BuildRequires:  pkgconfig(libcdata) >= 20140105
BuildRequires:  pkgconfig(libcerror) >= 20140105
BuildRequires:  pkgconfig(libcfile) >= 20130609
BuildRequires:  pkgconfig(libclocale) >= 20130609
BuildRequires:  pkgconfig(libcpath) >= 20130609
BuildRequires:  pkgconfig(libcsplit) >= 20130609
BuildRequires:  pkgconfig(libcstring) >= 20120425
BuildRequires:  pkgconfig(libcsystem) >= 20120425
BuildRequires:  pkgconfig(libcthreads) >= 20150101
BuildRequires:  pkgconfig(libfcache) >= 20120405
BuildRequires:  pkgconfig(libfdata) >= 20120405
BuildRequires:  pkgconfig(libfvalue) >= 20150101
BuildRequires:  pkgconfig(libuna) >= 20150101
BuildRequires:  pkgconfig(python2)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(zlib)

#fails to build with this package from factory - Oct 2, 2017
#BuildRequires:  pkgconfig(libcnotify) > 20170311
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The libvmdk library is a library to access the VMware Virtual Disk (VMDK) format. 

Read supported extent file formats:
- RAW (flat)
- COWD version 1 (sparse)
- VMDK version 1, 2 and 3 (sparse)

Supported VMDK format features:
- delta links
- grain compression (as of version 20131209)
- data markers (as of version 20140416)

VMDK format features not supported at the moment:
- images that use a physical device
- changed block tracking (CBT) (supported by VMDK version 3 (sparse)) / change tracking filek

%package -n %{lname}
Summary:        Library to access the VMDK image format
License:        LGPL-3.0-or-later
Group:          System/Libraries

%description -n %{lname}
The libvmdk library is a library to access the VMware Virtual Disk (VMDK) format. 

Read supported extent file formats:
- RAW (flat)
- COWD version 1 (sparse)
- VMDK version 1, 2 and 3 (sparse)

Supported VMDK format features:
- delta links
- grain compression (as of version 20131209)
- data markers (as of version 20140416)

VMDK format features not supported at the moment:
- images that use a physical device
- changed block tracking (CBT) (supported by VMDK version 3 (sparse)) / change tracking filek


%package tools
Summary:        Tools to access the VMDK image format
License:        LGPL-3.0-or-later
Group:          Productivity/File utilities
Requires:       %{lname} = %{version}

%description tools
Several tools for accessing VMware Virtual Disk (VMDK) files.  

See libvmdk for additional details.

%package devel
Summary:        Header files and libraries for developing applications for libvmdk
License:        LGPL-3.0-or-later AND GFDL-1.3-or-later
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
The libvmdk library is a library to access the VMware Virtual Disk (VMDK) format.  

See libvmdk for additional details.

This package contains libraries and header files for developing
applications that want to make use of libvmdk.

%package -n python2-%{name}
Summary:        Python 2 bindings for libvmdk, a VMDK image format parser
License:        LGPL-3.0-or-later
Group:          Development/Languages/Python
Requires:       %{lname} = %{version}
Requires:       python
Obsoletes:      python-%{name}

%description -n python2-%{name}
The libvmdk library is a library to access the VMware Virtual Disk (VMDK) format.  

This package contains the Python 2 bindings for libvmdk.

%package -n python3-%{name}
Summary:        Python 3 bindings for libvmdk, a VMDK image format parser
License:        LGPL-3.0-or-later
Group:          Development/Languages/Python
Requires:       %{lname} = %{version}
Requires:       python3

%description -n python3-%{name}
The libvmdk library is a library to access the VMware Virtual Disk (VMDK) format.  

This package contains the Python 3 bindings for libvmdk.

%prep
%setup -q -n libvmdk-%{timestamp}
cp "%{SOURCE2}" .

%build
%configure --disable-static --enable-wide-character-type --enable-python2 --enable-python3
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
find %{buildroot} -type f -name "*.la" -delete -print

%check
#make check

%post   -n %{lname} -p /sbin/ldconfig

%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%defattr(-,root,root)
%doc AUTHORS NEWS README ChangeLog
%license COPYING
%{_libdir}/libvmdk.so.*

%files tools
%defattr(-,root,root)
%doc AUTHORS
%license COPYING
%{_bindir}/vmdk*
%{_mandir}/man1/vmdk*.1*

%files devel
%defattr(-,root,root)
%doc AUTHORS
%license COPYING
%doc VMWare_Virtual_Disk_Format*
%{_includedir}/libvmdk.h
%{_includedir}/libvmdk/
%{_libdir}/libvmdk.so
%{_libdir}/pkgconfig/libvmdk.pc
%{_mandir}/man3/libvmdk.3*

%files -n python2-%{name}
%defattr(-,root,root)
%doc AUTHORS
%license COPYING
%{python_sitearch}/pyvmdk.so

%files -n python3-%{name}
%defattr(-,root,root)
%doc AUTHORS
%license COPYING
%{python3_sitearch}/pyvmdk.so

%changelog
