#
# spec file for package libvshadow
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%{?sle15_python_module_pythons}

%define lname	libvshadow1
Name:           libvshadow
Version:        20240504
Release:        0
Summary:        Library to access the Volume Shadow Snapshot (VSS) format
License:        GFDL-1.3-or-later AND LGPL-3.0-or-later
Group:          System/Filesystems
URL:            https://github.com/libyal/libvshadow
Source:         https://github.com/libyal/libvshadow/releases/download/%version/libvshadow-alpha-%version.tar.gz
Source2:        https://github.com/libyal/libvshadow/releases/download/%version/libvshadow-alpha-%version.tar.gz.asc
Source3:        %name.keyring
Source11:       Paper_-_Windowless_Shadow_Snapshots.pdf
Source12:       Slides_-_Windowless_Shadow_Snapshots.pdf
Source13:       Volume_Shadow_Snapshot_VSS_format.pdf
BuildRequires:  %python_module devel
BuildRequires:  %python_module setuptools
BuildRequires:  c_compiler
BuildRequires:  pkg-config
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(fuse3)
BuildRequires:  pkgconfig(libbfio) >= 20240414
BuildRequires:  pkgconfig(libcdata) >= 20240414
BuildRequires:  pkgconfig(libcerror) >= 20240413
BuildRequires:  pkgconfig(libcfile) >= 20240414
BuildRequires:  pkgconfig(libclocale) >= 20240414
BuildRequires:  pkgconfig(libcnotify) >= 20240414
BuildRequires:  pkgconfig(libcpath) >= 20240414
BuildRequires:  pkgconfig(libcsplit) >= 20240414
BuildRequires:  pkgconfig(libcthreads) >= 20240413
BuildRequires:  pkgconfig(libfdatetime) >= 20240414
BuildRequires:  pkgconfig(libfguid) >= 20240414
BuildRequires:  pkgconfig(libuna) >= 20240414
%python_subpackages
# Various notes: https://en.opensuse.org/libyal

%description
Library and tools to access the Volume Shadow Snapshot (VSS) format.
The VSS format is used by Windows, as of Vista, to maintain copies of
data on a storage media volume.

%package -n %lname
Summary:        Library and tools to access the Volume Shadow Snapshot (VSS) format
License:        LGPL-3.0-or-later
Group:          System/Libraries

%description -n %lname
Library and tools to access the Volume Shadow Snapshot (VSS) format.
The VSS format is used by Windows, as of Vista, to maintain copies of
data on a storage media volume.

%package        tools
Summary:        Tools to access the Volume Shadow Snapshot (VSS) format
License:        LGPL-3.0-or-later
Group:          System/Filesystems

%description    tools
Tools to access the Volume Shadow Snapshot (VSS) format. The VSS
format is used by Windows, as of Vista, to maintain copies of data on
a storage media volume.

%package        devel
Summary:        Development files for %name
License:        GFDL-1.3-or-later AND LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
Requires:       %lname = %version
Requires:       libbfio-devel

%description    devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

The package contains %_docdir/%name:

* OSDFC 2012: Paper - Windowless Shadow Snapshots
* OSDFC 2012: Slides - Windowless Shadow Snapshots

%prep
%autosetup -p1
mkdir doc
cp -av %_sourcedir/*.pdf .

%build
export CFLAGS="%optflags -fno-strict-aliasing"
export CXXFLAGS="%optflags"
%{python_expand #
echo "V_%version { global: *; };" >v.sym
%configure --disable-static --enable-wide-character-type \
	--enable-python PYTHON_VERSION="%{$python_bin_suffix}" \
	LDFLAGS="-Wl,--version-script=$PWD/v.sym"
grep ' '' ''local' config.log && exit 1
%make_build
%make_install DESTDIR="%_builddir/rt"
%make_build clean
}

%install
mv "%_builddir/rt"/* "%buildroot/"
find "%buildroot" -type f -name "*.la" -delete -print

%post -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%license COPYING*
%_libdir/*.so.*

%files -n %name-tools
%_bindir/vshadow*
%_mandir/man1/*.gz

%files -n %name-devel
%license COPYING*
%doc Paper_-_Windowless_Shadow_Snapshots.pdf
%doc Slides_-_Windowless_Shadow_Snapshots.pdf
%doc Volume_Shadow_Snapshot_*.pdf
%_includedir/libvshadow.h
%_includedir/libvshadow/
%_libdir/*.so
%_libdir/pkgconfig/libvshadow.pc
%_mandir/man3/*.gz

%files %python_files
%license COPYING*
%python_sitearch/*.so

%changelog
