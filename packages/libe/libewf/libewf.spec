#
# spec file for package libewf
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define lname	libewf2
%define timestamp 20140608
Name:           libewf
Version:        0~%{timestamp}
Release:        0
Summary:        Library for the Expert Witness Compression Format (EWF)
License:        LGPL-3.0+ and GFDL-1.3+
Group:          Productivity/File utilities
Url:            http://code.google.com/p/libewf/
#DL-URL:        https://googledrive.com/host/0B3fBvzttpiiSMTdoaVExWWNsRjg/libewf-20140608.tar.gz
Source:         %{name}-%{timestamp}.tar.gz
Source2:        http://downloads.sf.net/libewf/mount_ewf-20090113.py
Source3:        Expert_Witness_Compression_Format_EWF.pdf
Source4:        Expert_Witness_Compression_Format_2_EWF2.pdf
Patch1:         remove_date_time_macros.patch
BuildRequires:  bison
BuildRequires:  flex
# Needed for language translation support
BuildRequires:  gettext
BuildRequires:  pkg-config
BuildRequires:  python-devel
BuildRequires:  pkgconfig(bzip2) >= 1.0
BuildRequires:  pkgconfig(fuse) >= 2.6
BuildRequires:  pkgconfig(libcaes) >= 20120425
BuildRequires:  pkgconfig(libcdatetime)
BuildRequires:  pkgconfig(libcfile) >= 20120526
BuildRequires:  pkgconfig(libclocale) >= 20120425
BuildRequires:  pkgconfig(libcnotify) >= 20120425
BuildRequires:  pkgconfig(libcsplit) >= 20120701
BuildRequires:  pkgconfig(libcthreads) >= 20130723
BuildRequires:  pkgconfig(libfvalue) >= 20120428
BuildRequires:  pkgconfig(libhmac) >= 20120425
BuildRequires:  pkgconfig(libsmdev) >= 20120630
BuildRequires:  pkgconfig(libuna) >= 20120425
BuildRequires:  pkgconfig(openssl) >= 1.0.0
BuildRequires:  pkgconfig(uuid) >= 2.20
BuildRequires:  pkgconfig(zlib) >= 1.2.5
# build fails if libyal package from OBS is used
# verified 1/10/2015
#BuildRequires:  pkgconfig(libcstring) >= 20120425
#BuildRequires:  pkgconfig(libcerror) >= 20120425
#BuildRequires:  pkgconfig(libcdata) >= 20120425
#BuildRequires:  pkgconfig(libbfio) >= 20120426
#BuildRequires:  pkgconfig(libcsystem) >= 20120425
#BuildRequires:  pkgconfig(libfcache) >= 20120405
#BuildRequires:  pkgconfig(libfdata)
#BuildRequires:  pkgconfig(libsmraw) >= 20120630
#BuildRequires:  pkgconfig(libodraw) >= 20120630
# verified 4/19/2019  -  libewf hasn't been updated in 5 years and it depends on old versions of libyal. :(
#BuildRequires:  pkgconfig(libcpath) >= 20120701
# these packages not yet released by upstream
#BuildRequires:  pkgconfig(libmfdata) >= 20120425
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
libewf is a library for support of the Expert Witness Compression
Format (EWF). It supports both the SMART format (EWF-S01) and the
EnCase format (EWF-E01). libewf allows you to read and write media
information within the EWF files. libewf allows to read files created
by EnCase 1 to 6, linen and FTK Imager.

%package -n %{lname}
Summary:        Library to support the Expert Witness Compression Format
License:        LGPL-3.0+
Group:          System/Libraries

%description -n %{lname}
libewf is a library for support of the Expert Witness Compression
Format (EWF). It supports both the SMART format (EWF-S01) and the
EnCase format (EWF-E01). libewf allows you to read and write media
information within the EWF files. libewf allows to read files created
by EnCase 1 to 6, linen and FTK Imager.

%package tools
Summary:        Utilities for the Expert Witness Compression Format (EWF)
License:        LGPL-3.0+
Group:          System/Filesystems
Requires:       fuse
Requires:       python-fuse >= 0.2
#Don't use obsoletes because new 0~yyyymmdd version is less than old 0.0.0+yyyymmdd version
#zypper dup should "downgrade" ewftools to ewftools in factory regardless, so this should work
#Obsoletes:      ewftools <= 0.0.0+20130128
Provides:       ewftools = %{version}

%description tools
Several tools for reading and writing EWF files.
It contains tools to acquire, verify and export EWF files.

%package devel
Summary:        Development files for libewf, an Expert Witness Compression Format library
License:        LGPL-3.0+ and GFDL-1.3+
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
libewf is a library for support of the Expert Witness Compression
Format (EWF). It supports both the SMART format (EWF-S01) and the
EnCase format (EWF-E01). libewf allows you to read and write media
information within the EWF files. libewf allows to read files created
by EnCase 1 to 6, linen and FTK Imager.

This subpackage contains libraries and header files for developing
applications that want to make use of %{name}.

%package -n python2-%{name}
Summary:        Python 2 bindings for libewf, an Expert Witness Compression format library
License:        LGPL-3.0+
Group:          Development/Libraries/Python
Requires:       %{lname} = %{version}
BuildRequires:  pkgconfig(python2)
Provides:       python-%{name} = %{version}
Obsoletes:      python-%{name} < 20140608

%description -n python2-%{name}
Python 2 binding for libewf, which can create and read EnCase forensic
images.

%package -n python3-%{name}
Summary:        Python 3 bindings for libewf, an Expert Witness Compression format library
License:        LGPL-3.0+
Group:          Development/Libraries/Python
Requires:       %{lname} = %{version}
BuildRequires:  pkgconfig(python3)

%description -n python3-%{name}
Python 3 binding for libewf, which can create and read EnCase forensic
images.

%prep
%setup -q -n libewf-%{timestamp}
%patch1 -p1
cp "%{SOURCE3}" "%{SOURCE4}" .

%build
#export CFLAGS="%optflags -fno-strict-aliasing"
%configure --disable-static \
  --enable-wide-character-type \
  --enable-python --enable-python3

#Remove rpath from libtool
#sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
#sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

# clean unused-direct-shlib-dependencies
#sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool

make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
find %{buildroot} -type f -name "*.la" -delete -print

install -Dpm0755 "%{SOURCE2}" "%{buildroot}/sbin/mount.ewf"
ln -s mount.ewf "%{buildroot}/sbin/umount.ewf"

%post   -n %{lname} -p /sbin/ldconfig

%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%defattr(-,root,root)
%doc AUTHORS COPYING NEWS ChangeLog
%{_libdir}/libewf.so.*

%files tools
%defattr(-,root,root)
%{_bindir}/ewfacquire
%{_bindir}/ewfacquirestream
%{_bindir}/ewfexport
%{_bindir}/ewfinfo
%{_bindir}/ewfmount
%{_bindir}/ewfrecover
%{_bindir}/ewfverify
### experimental file ###
%{_bindir}/ewfdebug

%{_mandir}/man1/ewf*.1*
/sbin/*mount.ewf

%files devel
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING NEWS README
%doc *.pdf
%{_includedir}/libewf.h
%{_includedir}/libewf/
%{_libdir}/libewf.so
%{_libdir}/pkgconfig/libewf.pc
%{_mandir}/man3/libewf.3*

%files -n python2-%{name}
%defattr(-,root,root)
%doc AUTHORS COPYING NEWS README
%{python_sitearch}/pyewf.so

# this is a skeleton package with no actual binary.  Upstream doesn't have python3 support in stable
%files -n python3-%{name}
%defattr(-,root,root)
%doc AUTHORS COPYING NEWS README

%changelog
