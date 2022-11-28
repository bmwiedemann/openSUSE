#
# spec file for package libvshadow
#
# Copyright (c) 2022 SUSE LLC
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


%define lname	libvshadow1
Name:           libvshadow
Version:        20221030
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
BuildRequires:  %{python_module devel}
BuildRequires:  c_compiler
BuildRequires:  pkg-config
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(fuse)
BuildRequires:  pkgconfig(libbfio) >= 20221025
BuildRequires:  pkgconfig(libcdata) >= 20220115
BuildRequires:  pkgconfig(libcerror) >= 20220101
BuildRequires:  pkgconfig(libcfile) >= 20220106
BuildRequires:  pkgconfig(libclocale) >= 20220107
BuildRequires:  pkgconfig(libcnotify) >= 20220108
BuildRequires:  pkgconfig(libcpath) >= 20220108
BuildRequires:  pkgconfig(libcsplit) >= 20220109
BuildRequires:  pkgconfig(libcthreads) >= 20220102
BuildRequires:  pkgconfig(libfdatetime) >= 20220112
BuildRequires:  pkgconfig(libfguid) >= 20220113
BuildRequires:  pkgconfig(libuna) >= 20220611
%python_subpackages
# Various notes: https://en.opensuse.org/libyal

%description
Library and tools to access the Volume Shadow Snapshot (VSS) format.
The VSS format is used by Windows, as of Vista, to maintain copies of
data on a storage media volume.

%package -n %{lname}
Summary:        Library and tools to access the Volume Shadow Snapshot (VSS) format
License:        LGPL-3.0-or-later
Group:          System/Libraries

%description -n %{lname}
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
Summary:        Development files for %{name}
License:        GFDL-1.3-or-later AND LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

The package contains %{_docdir}/%{name}:

* OSDFC 2012: Paper - Windowless Shadow Snapshots
* OSDFC 2012: Slides - Windowless Shadow Snapshots

%prep
%autosetup -p1
mkdir doc
cp -av %_sourcedir/*.pdf .

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
export CXXFLAGS="%{optflags}"
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

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%license COPYING*
%{_libdir}/*.so.*

%files -n %name-tools
%{_bindir}/vshadow*
%{_mandir}/man1/*.gz

%files -n %name-devel
%license COPYING*
%doc Paper_-_Windowless_Shadow_Snapshots.pdf
%doc Slides_-_Windowless_Shadow_Snapshots.pdf
%doc Volume_Shadow_Snapshot_*.pdf
%{_includedir}/libvshadow.h
%{_includedir}/libvshadow/
%{_libdir}/*.so
%{_libdir}/pkgconfig/libvshadow.pc
%{_mandir}/man3/*.gz

%files %python_files
%license COPYING*
%python_sitearch/*.so

%changelog
