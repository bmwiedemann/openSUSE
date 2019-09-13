#
# spec file for package libolecf
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


Name:           libolecf
%define lname	libolecf1
%define timestamp	20181231
Version:        0~%timestamp
Release:        0
Summary:        Library and tools to access the OLE 2 Compound File (OLECF) format
License:        LGPL-3.0-or-later AND GFDL-1.3-or-later
Group:          Productivity/File utilities
Url:            https://github.com/libyal/libolecf/wiki
Source:         https://github.com/libyal/libolecf/releases/download/%timestamp/%name-alpha-%timestamp.tar.gz
Source2:        OLE_Compound_File_format.pdf
BuildRequires:  pkg-config
BuildRequires:  python-devel
BuildRequires:  pkgconfig(libbfio)
BuildRequires:  pkgconfig(libcdata) >= 20190112
BuildRequires:  pkgconfig(libcfile)
BuildRequires:  pkgconfig(libclocale)
BuildRequires:  pkgconfig(libcnotify)
BuildRequires:  pkgconfig(libcpath)
BuildRequires:  pkgconfig(libcsplit)
# BuildRequires:  pkgconfig(libcsystem) >= 20120425
BuildRequires:  pkgconfig(libcthreads) >= 20130723
BuildRequires:  pkgconfig(libfguid) >= 20140103
BuildRequires:  pkgconfig(libfole) >= 20120426
BuildRequires:  pkgconfig(libuna)

# testing fails with external package from factory - verified Jan 27, 2016
#BuildRequires:  pkgconfig(libfdatetime) > 20150507
#BuildRequires:  pkgconfig(libcstring) > 20150101
#BuildRequires:  pkgconfig(libfvalue) > 20151226
# build fails with external package from factory - verified Jul 12, 2016
#BuildRequires:  pkgconfig(libcerror) > 20160327
# released, but not yet packaged.  This is the only user in OBS.
#BuildRequires:  pkgconfig(libwfps) > 20150104
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Library and tools to access the OLE 2 Compound File (OLECF) format. The OLE 2 Compound File format is used to store certain versions of Microsoft Office files, thumbs.db and other file formats. 

%package -n %lname
Summary:        Library to access the OLE 2 Compound File (OLECF) format
License:        LGPL-3.0-or-later
Group:          System/Libraries

%description -n %lname
Library to access the OLE 2 Compound File (OLECF) format. The OLE 2 Compound File format is used to store certain versions of Microsoft Office files, thumbs.db and other file formats. 


%package tools
Summary:        Tools to access the OLE 2 Compound File (OLECF) format
License:        LGPL-3.0-or-later
Group:          System/Filesystems
Requires:       %lname = %version

%description tools
Tools to access the OLE 2 Compound File (OLECF) format. The OLE 2 Compound File format is used to store certain versions of Microsoft Office files, thumbs.db and other file formats. 

 
%package devel
Summary:        Development files for %name
License:        LGPL-3.0-or-later AND GFDL-1.3-or-later
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
libolecf is a library to access the OLE 2 Compound File (OLECF) format.

This subpackage contains libraries and header files for developing
applications that want to make use of %name.

%package -n python-%name
Summary:        Python bindings for libolecf
License:        LGPL-3.0-or-later
Group:          Development/Libraries/Python
Requires:       %lname = %version
Requires:       python
Provides:       pyolecf = %version

%description -n python-%name
Python bindings for libolecf, which can read MS IE cache files.

%prep
%setup -qn libolecf-%timestamp
cp "%SOURCE2" .

%build
%configure --disable-static --enable-wide-character-type --enable-python
make %{?_smp_mflags}

%install
make install DESTDIR="%buildroot"
find %buildroot -name '*.la' -delete

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%defattr(-,root,root)
%doc AUTHORS ChangeLog
%license COPYING 
%_libdir/libolecf.so.*

%files tools
%defattr(-,root,root)
%_bindir/olecf*
%_mandir/man1/olecf*.1*

%files devel
%defattr(-,root,root)
%doc OLE_Compound_File_format.pdf
%_includedir/libolecf.h
%_includedir/libolecf/
%_libdir/libolecf.so
%_libdir/pkgconfig/libolecf.pc
%_mandir/man3/libolecf.3*

%files -n python-%name
%defattr(-,root,root)
%doc AUTHORS README
%license COPYING 
%python_sitearch/pyolecf.so

%changelog
