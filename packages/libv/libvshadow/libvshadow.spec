#
# spec file for package libvshadow
#
# Copyright (c) 2021 SUSE LLC
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
Version:        20210507
Release:        0
Summary:        Library to access the Volume Shadow Snapshot (VSS) format
License:        GFDL-1.3-or-later AND LGPL-3.0-or-later
Group:          System/Filesystems
URL:            https://github.com/libyal/libvshadow
Source:         %{name}-%{version}.tar.xz
Source1:        Paper_-_Windowless_Shadow_Snapshots.pdf
Source2:        Slides_-_Windowless_Shadow_Snapshots.pdf
Source3:        Volume_Shadow_Snapshot_VSS_format.pdf
Patch1:         system-libs.patch
BuildRequires:  c_compiler
BuildRequires:  gettext-tools >= 0.18.1
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(fuse)
BuildRequires:  pkgconfig(libbfio) >= 20201229
BuildRequires:  pkgconfig(libcdata) >= 20200509
BuildRequires:  pkgconfig(libcerror) >= 20201121
BuildRequires:  pkgconfig(libcfile) >= 20201229
BuildRequires:  pkgconfig(libclocale) >= 20200913
BuildRequires:  pkgconfig(libcnotify) >= 20200913
BuildRequires:  pkgconfig(libcpath) >= 20200623
BuildRequires:  pkgconfig(libcsplit) >= 20200703
BuildRequires:  pkgconfig(libcthreads) >= 20200508
BuildRequires:  pkgconfig(libfdatetime) >= 20180910
BuildRequires:  pkgconfig(libfguid) >= 20180724
BuildRequires:  pkgconfig(libuna) >= 20201204
BuildRequires:  pkgconfig(python3)

%description
Library and tools to access the Volume Shadow Snapshot (VSS) format. The VSS format is used by Windows, as of Vista, to maintain copies of data on a storage media volume.

The devel package contains:

    OSDFC 2012: Paper - Windowless Shadow Snapshots
    OSDFC 2012: Slides - Windowless Shadow Snapshots
    Volume_Shadow_Snapshot_(VSS)_format.pdf

%package -n %{lname}
Summary:        Library and tools to access the Volume Shadow Snapshot (VSS) format
License:        LGPL-3.0-or-later
Group:          System/Libraries

%description -n %{lname}
Library and tools to access the Volume Shadow Snapshot (VSS) format. The VSS format is used by Windows, as of Vista, to maintain copies of data on a storage media volume.

The package contains %{_docdir}/%{name}:

    OSDFC 2012: Paper - Windowless Shadow Snapshots
    OSDFC 2012: Slides - Windowless Shadow Snapshots

%package        tools
Summary:        Tools to access the Volume Shadow Snapshot (VSS) format
License:        LGPL-3.0-or-later
Group:          System/Filesystems

%description    tools
Tools to access the Volume Shadow Snapshot (VSS) format. The VSS format is used by Windows, as of Vista, to maintain copies of data on a storage media volume.

%package        devel
Summary:        Development files for %{name}
License:        GFDL-1.3-or-later AND LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        -n python3-%{name}
Summary:        Python 3 binding for libvshadow
License:        LGPL-3.0-or-later
Group:          Development/Languages/Python

%description    -n python3-%{name}
Python 3 binding for libvshadow.  libvshadow can read windows event files

%prep
%autosetup -p1
mkdir doc
cp %SOURCE1 .
cp %SOURCE2 .
cp "%SOURCE3" .

%build
if [ ! -e configure ]; then ./autogen.sh; fi
export CFLAGS="%{optflags} -fno-strict-aliasing"
export CXXFLAGS="%{optflags}"
%configure --disable-static --enable-wide-character-type --enable-python3
%make_build

%install
%make_install
find %{buildroot} -name '*.la' -delete

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%license COPYING*
%doc doc
%{_libdir}/*.so.*

%files tools
%{_bindir}/vshadow*
%{_mandir}/man1/*.gz

%files devel
%license COPYING*
%doc Paper_-_Windowless_Shadow_Snapshots.pdf
%doc Slides_-_Windowless_Shadow_Snapshots.pdf
%doc Volume_Shadow_Snapshot_*.pdf
%{_includedir}/libvshadow.h
%{_includedir}/libvshadow/
%{_libdir}/*.so
%{_libdir}/pkgconfig/libvshadow.pc
%{_mandir}/man3/*.gz

%files -n python3-%{name}
%license COPYING*
%{python3_sitearch}/*.so

%changelog
