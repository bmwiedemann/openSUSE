#
# spec file for package libewf
#
# Copyright (c) 2023 SUSE LLC
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


%define lname libewf3
Name:           libewf
Version:        20230212
Release:        0
Summary:        Library for the Expert Witness Compression Format (EWF)
License:        GFDL-1.3-or-later AND LGPL-3.0-or-later
Group:          Productivity/File utilities
URL:            https://github.com/libyal/libewf
Source:         https://github.com/libyal/libewf/releases/download/%version/libewf-experimental-%version.tar.gz
Source2:        https://github.com/libyal/libewf/releases/download/%version/libewf-experimental-%version.tar.gz.asc
Source3:        %name.keyring
Source20:       http://downloads.sf.net/libewf/mount_ewf-20090113.py
Source21:       Expert_Witness_Compression_Format_EWF.pdf
Source23:       Expert_Witness_Compression_Format_2_EWF2.pdf
Patch1:         remove_date_time_macros.patch
Patch2:         system-libs.patch
Patch3:         20230324.diff
BuildRequires:  %{python_module devel}
BuildRequires:  bison
BuildRequires:  c_compiler
BuildRequires:  flex
BuildRequires:  gettext-tools >= 0.18.1
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  python-rpm-macros
BuildRequires:  timezone
BuildRequires:  pkgconfig(bzip2) >= 1.0
BuildRequires:  pkgconfig(fuse) >= 2.6
BuildRequires:  pkgconfig(libbfio) >= 20221025
BuildRequires:  pkgconfig(libcaes) >= 20221127
BuildRequires:  pkgconfig(libcdata) >= 20230108
BuildRequires:  pkgconfig(libcdatetime) >= 20230115
BuildRequires:  pkgconfig(libcerror) >= 20220101
BuildRequires:  pkgconfig(libcfile) >= 20220106
BuildRequires:  pkgconfig(libclocale) >= 20221218
BuildRequires:  pkgconfig(libcnotify) >= 20220108
BuildRequires:  pkgconfig(libcpath) >= 20220108
BuildRequires:  pkgconfig(libcsplit) >= 20220109
BuildRequires:  pkgconfig(libcthreads) >= 20220102
BuildRequires:  pkgconfig(libfcache) >= 20230115
BuildRequires:  pkgconfig(libfdata) >= 20220111
BuildRequires:  pkgconfig(libfdatetime) >= 20220112
BuildRequires:  pkgconfig(libfguid) >= 20220113
BuildRequires:  pkgconfig(libfvalue) >= 20220120
BuildRequires:  pkgconfig(libhmac) >= 20230205
BuildRequires:  pkgconfig(libodraw) >= 20210503
BuildRequires:  pkgconfig(libsmdev) >= 20221028
BuildRequires:  pkgconfig(libsmraw) >= 20221028
BuildRequires:  pkgconfig(libuna) >= 20220611
BuildRequires:  pkgconfig(openssl) >= 1.0.0
BuildRequires:  pkgconfig(uuid) >= 2.20
BuildRequires:  pkgconfig(zlib) >= 1.2.5
%python_subpackages

%description
libewf is a library for support of the Expert Witness Compression
Format (EWF). It supports both the SMART format (EWF-S01) and the
EnCase format (EWF-E01). libewf allows you to read and write media
information within the EWF files. libewf allows to read files created
by EnCase 1 to 6, linen and FTK Imager.

%package -n %lname
Summary:        Library to support the Expert Witness Compression Format
License:        LGPL-3.0-or-later
Group:          System/Libraries
Requires:       timezone

%description -n %lname
libewf is a library for support of the Expert Witness Compression
Format (EWF). It supports both the SMART format (EWF-S01) and the
EnCase format (EWF-E01). libewf allows you to read and write media
information within the EWF files. libewf allows to read files created
by EnCase 1 to 6, linen and FTK Imager.

%package tools
Summary:        Utilities for the Expert Witness Compression Format (EWF)
License:        LGPL-3.0-or-later
Group:          System/Filesystems
Requires:       fuse
Requires:       python3-fuse >= 0.2

%description tools
Several tools for reading and writing EWF files.
It contains tools to acquire, verify and export EWF files.

%package devel
Summary:        Development files for libewf, an Expert Witness Compression Format library
License:        GFDL-1.3-or-later AND LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
Requires:       %lname = %version
Requires:       libbfio-devel

%description devel
libewf is a library for support of the Expert Witness Compression
Format (EWF). It supports both the SMART format (EWF-S01) and the
EnCase format (EWF-E01). libewf allows you to read and write media
information within the EWF files. libewf allows to read files created
by EnCase 1 to 6, linen and FTK Imager.

This subpackage contains libraries and header files for developing
applications that want to make use of %name.

%prep
%autosetup -p1 -n libewf-%version
cp -av %_sourcedir/*.pdf .

%build
#export CFLAGS="%optflags -fno-strict-aliasing"
autoreconf -fi
# OOT builds are presently broken, so we have to install
# within each python iteration now, not in %%install.
%{python_expand #
# see libcdata for version-sc
echo "V_%version { global: *; };" >v.sym
%configure --disable-static --disable-rpath \
	--enable-wide-character-type \
	--enable-python PYTHON_VERSION="%{$python_bin_suffix}" \
	LDFLAGS="-Wl,--version-script=$PWD/v.sym"
echo "$python" >lastpython
%make_build
%make_install DESTDIR="%_builddir/rt"
%make_build clean
}

%install
mv "%_builddir/rt"/* "%buildroot/"
find "%buildroot" -type f -name "*.la" -delete -print
install -Dpm0755 %_sourcedir/mount*py "%buildroot/%_sbindir/mount.ewf"
ln -s mount.ewf "%buildroot%_sbindir/umount.ewf"

%check
export PYTHON="$(cat lastpython)"
# The testsuite has a symbol overload for malloc,
# and that no longer works when using version-script
make check || :

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%license COPYING*
%_libdir/libewf.so.*

%files -n %name-tools
%_bindir/ewfacquire
%_bindir/ewfacquirestream
%_bindir/ewfexport
%_bindir/ewfinfo
%_bindir/ewfmount
%_bindir/ewfrecover
%_bindir/ewfverify
### experimental file ###
%_bindir/ewfdebug

%_mandir/man1/ewf*.1*
%_sbindir/*mount.ewf

%files -n %name-devel
%license COPYING*
%doc *.pdf
%_includedir/libewf.h
%_includedir/libewf/
%_libdir/libewf.so
%_libdir/pkgconfig/libewf.pc
%_mandir/man3/libewf.3*

%files %python_files
%license COPYING*
%python_sitearch/*.so

%changelog
