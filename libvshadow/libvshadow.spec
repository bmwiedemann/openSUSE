#
# spec file for package libvshadow
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


Name:           libvshadow
%define lname	libvshadow1
%define timestamp	20190323
Version:        0~%{timestamp}
Release:        0
Summary:        Library to access the Volume Shadow Snapshot (VSS) format
License:        LGPL-3.0-or-later AND GFDL-1.3-or-later
Group:          System/Filesystems
Url:            https://github.com/libyal/libvshadow/wiki
Source:         https://github.com/libyal/libvshadow/releases/download/%{timestamp}/libvshadow-alpha-%{timestamp}.tar.gz
Source1:        Paper_-_Windowless_Shadow_Snapshots.pdf
Source2:        Slides_-_Windowless_Shadow_Snapshots.pdf
Source3:        Volume_Shadow_Snapshot_VSS_format.pdf
BuildRequires:  fuse-devel
BuildRequires:  gcc
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libbfio) >= 20130908
BuildRequires:  pkgconfig(libcdata) >= 20130407
BuildRequires:  pkgconfig(libcerror) > 20130904
BuildRequires:  pkgconfig(libcfile) >= 20130609
BuildRequires:  pkgconfig(libclocale) >= 20130609
BuildRequires:  pkgconfig(libcnotify) >= 20130609
BuildRequires:  pkgconfig(libcpath) >= 20130609
BuildRequires:  pkgconfig(libcsplit) > 20130904
BuildRequires:  pkgconfig(libcsystem)
BuildRequires:  pkgconfig(libcthreads) >= 20130723
BuildRequires:  pkgconfig(libfdatetime)
BuildRequires:  pkgconfig(libfguid)
BuildRequires:  pkgconfig(libuna) >= 20130609
# These packages are not released as separate packages by upstream.  Internal only
#BuildRequires:  pkgconfig(libcmulti)

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
Requires:       %{lname} = %{version}

%description    tools
Tools to access the Volume Shadow Snapshot (VSS) format. The VSS format is used by Windows, as of Vista, to maintain copies of data on a storage media volume.
 
%package        devel
Summary:        Development files for %{name}
License:        LGPL-3.0-or-later AND GFDL-1.3-or-later
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        -n python2-%{name}
Summary:        Python 2 binding for libvshadow
License:        LGPL-3.0-or-later
Group:          Development/Languages/Python
Requires:       %{lname} = %{version}
Requires:       python2
BuildRequires:  pkgconfig(python2)
Obsoletes:      python-%{name}

%description    -n python2-%{name}
Python 2 binding for libvshadow.  libvshadow can read windows event files

%package        -n python3-%{name}
Summary:        Python 3 binding for libvshadow
License:        LGPL-3.0-or-later
Group:          Development/Languages/Python
Requires:       %{lname} = %{version}
Requires:       python3
BuildRequires:  pkgconfig(python3)

%description    -n python3-%{name}
Python 3 binding for libvshadow.  libvshadow can read windows event files

%prep
%setup -q -n libvshadow-%{timestamp}
mkdir doc
cp %SOURCE1 .
cp %SOURCE2 .
cp "%SOURCE3" .

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
export CXXFLAGS="%{optflags}"
%configure --disable-static --enable-wide-character-type --enable-python2 --enable-python3

make %{?_smp_mflags}

%install
# maintain SLES compatibility
make install DESTDIR="%buildroot"
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%post -n %{lname} -p /sbin/ldconfig

%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog ABOUT-NLS
%license COPYING 
%doc doc
%{_libdir}/*.so.*

%files tools
%defattr(-,root,root,-)
%{_bindir}/vshadow*
%{_mandir}/man1/*.gz

%files devel
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog ABOUT-NLS
%license COPYING 
%doc Paper_-_Windowless_Shadow_Snapshots.pdf
%doc Slides_-_Windowless_Shadow_Snapshots.pdf
%doc Volume_Shadow_Snapshot_*.pdf
%{_includedir}/libvshadow.h
%{_includedir}/libvshadow/
%{_libdir}/*.so
%{_libdir}/pkgconfig/libvshadow.pc
%{_mandir}/man3/*.gz

%files -n python2-%{name}
%defattr(644,root,root,755)
%doc AUTHORS README
%license COPYING 
%{python_sitearch}/*.so

%files -n python3-%{name}
%defattr(644,root,root,755)
%doc AUTHORS README
%license COPYING 
%{python3_sitearch}/*.so

%changelog
