#
# spec file for package libpff
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


Name:           libpff
%define lname	libpff1
%define timestamp 20180714
Version:        0~%timestamp
Release:        0
Summary:        Library and tools to access Microsoft PFF and OFF format files
License:        LGPL-3.0-or-later AND GFDL-1.1-or-later AND GFDL-1.3-or-later
Group:          Productivity/File utilities
Url:            https://github.com/libyal/libpff/wiki
Source:         https://github.com/libyal/libpff/releases/download/%{timestamp}/libpff-experimental-%{timestamp}.tar.gz
Source2:        PFF_Forensics_-_analyzing_the_horrible_reference_file_format.pdf
Source3:        PFF_forensics_-_e-mail_and_appoinment_falsification_analysis.pdf
Source4:        Personal_Folder_File_PFF_format.pdf
Source5:        MAPI_definitions.pdf
Source6:        libpff-libfdata.pdf
Patch1:         pkgconfig.diff

BuildRequires:  pkg-config
BuildRequires:  python-devel
# use factory packages if available
%if 0%{?suse_version} > 1230
BuildRequires:  pkgconfig(libbfio) >= 20130721
BuildRequires:  pkgconfig(libcdata) >= 20190112
BuildRequires:  pkgconfig(libcerror) >= 20181117
BuildRequires:  pkgconfig(libcfile) >= 20130609
BuildRequires:  pkgconfig(libclocale) >= 20130609
BuildRequires:  pkgconfig(libcnotify) >= 20120425
BuildRequires:  pkgconfig(libcsplit) >= 20130609
BuildRequires:  pkgconfig(libcstring) >= 20120425
BuildRequires:  pkgconfig(libcsystem) >= 20120425
BuildRequires:  pkgconfig(libcthreads)
BuildRequires:  pkgconfig(libfcache) >= 20120405
BuildRequires:  pkgconfig(libfdata) >= 20120405
BuildRequires:  pkgconfig(libfdatetime) >= 20120522
BuildRequires:  pkgconfig(libfguid) >= 20120426
BuildRequires:  pkgconfig(libfmapi) >= 20180714
BuildRequires:  pkgconfig(libfvalue) >= 20120428
BuildRequires:  pkgconfig(libfwnt) >= 20120426
BuildRequires:  pkgconfig(libuna) >= 20120425
%endif
# fails to build with factory package, use internal
# verified 4/19/2019
#BuildRequires:  pkgconfig(libcpath) >= 20181228
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
libpff is a library to access the Personal Folder File (PFF) and the
Offline Folder File (OFF) format. These are used in several file
Types: PAB (Personal Address Book), PST (Personal Storage Table) and
OST (Offline Storage Table).

%package -n %lname
Summary:        Library to access Microsoft PFF and OFF format files
License:        LGPL-3.0-or-later
Group:          System/Libraries

%description -n %lname
libpff is a library to access the Personal Folder File (PFF) and the
Offline Folder File (OFF) format. These are used in several file
Types: PAB (Personal Address Book), PST (Personal Storage Table) and
OST (Offline Storage Table).

%package tools
Summary:        Tools to access Microsoft PST and OST files
License:        LGPL-3.0-or-later
Group:          Productivity/File utilities
Requires:       %lname = %version

%description tools
Tools to access the Personal Folder File (PFF) and the Offline Folder
File (OFF) format. These are used in several file types: PAB
(Personal Address Book), PST (Personal Storage Table) and OST
(Offline Storage Table).

%package devel
Summary:        Development files for libpff, a PFF/OFF file format library
License:        LGPL-3.0-or-later AND GFDL-1.1-or-later AND GFDL-1.3-or-later
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
libpff is a library to access the Personal Folder File (PFF) and the
Offline Folder File (OFF) format. These are used in several file
Types: PAB (Personal Address Book), PST (Personal Storage Table) and
OST (Offline Storage Table).

This subpackage contains libraries and header files for developing
applications that want to make use of libpff.

%package -n python-%name
Summary:        Python bindings for libpff, a PFF/OFF file format parser
License:        LGPL-3.0-or-later
Group:          Development/Libraries/Python
Requires:       python

%description -n python-%name
Python bindings for libpff, which can read Personal Folder File (PFF)
and Offline Folder File (OFF) formats.

%prep
%setup -qn libpff-%timestamp
%patch -P 1 -p1
cp "%{S:2}" "%{S:3}" "%{S:4}" "%{S:5}" "%{S:6}" .

%build
%configure --disable-static --enable-wide-character-type --enable-python
make %{?_smp_mflags}

%install
make install DESTDIR="%buildroot"
find "%buildroot" -name "*.la" -delete

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%defattr(-,root,root)
%doc AUTHORS ChangeLog
%license COPYING 
%_libdir/libpff.so.*

%files tools
%defattr(-,root,root)
%doc AUTHORS ChangeLog
%license COPYING 
%_bindir/pff*
%_mandir/man1/pff*.1*

%files devel
%defattr(-,root,root)
%doc AUTHORS README ChangeLog
%license COPYING 
%doc MAPI_definitions.pdf
%doc PFF_Forensics_-_analyzing_the_horrible_reference_file_format.pdf
%doc PFF_forensics_-_e-mail_and_appoinment_falsification_analysis.pdf
%doc Personal_Folder_File_*.pdf
%_includedir/libpff.h
%_includedir/libpff/
%_libdir/libpff.so
%_libdir/pkgconfig/libpff.pc
%_mandir/man3/libpff.3*

%files -n python-%name
%defattr(-,root,root)
%python_sitearch/pypff.so

%changelog
