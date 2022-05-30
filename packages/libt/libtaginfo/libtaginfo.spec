#
# spec file for package libtaginfo
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


Name:           libtaginfo
Version:        0.2.1
Release:        0
Summary:        Library for reading media metadata (tags)
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://bitbucket.org/shuerhaaken/libtaginfo
Source:         https://bitbucket.org/shuerhaaken/%{name}/downloads/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  vala
BuildRequires:  pkgconfig(taglib) >= 1.9.1

%description
libtaginfo is a convenience wrapper for taglib with C and vala
bindings.

Features are reading/writing fields like: Artist, Album, Title, Genre,
AlbumArtist, Comments, Disk number, Compilation flag, User labels,
Embedded Images, Lyrics, Audio properties (length, bitrate, samplerate,
channels ...), ...

%package -n libtaginfo1
Summary:        Library for reading media metadata (tags)
Group:          System/Libraries
Conflicts:      libtaginfo < %{version}-%{release}

%description -n libtaginfo1
libtaginfo is a convenience wrapper for taglib with C and vala
bindings.

Features are reading/writing fields like: Artist, Album, Title, Genre,
AlbumArtist, Comments, Disk number, Compilation flag, User labels,
Embedded Images, Lyrics, Audio properties (length, bitrate, samplerate,
channels ...), ...

%package -n libtaginfo_c0
Summary:        Library for reading media metadata (tags)
Group:          System/Libraries
Conflicts:      libtaginfo < %{version}-%{release}

%description -n libtaginfo_c0
libtaginfo is a convenience wrapper for taglib with C and vala
bindings.

%package devel
Summary:        Development files for libtaginfo
Group:          Development/Libraries
Requires:       libtaginfo1 = %{version}-%{release}
Requires:       libtaginfo_c0 = %{version}-%{release}

%description devel
The libtaglib development package includes the header files, libraries,
configuration files and development tools necessary for compiling and
linking application which will use libtaginfo.

%prep
%autosetup -p1

%build
autoreconf -fi
%configure
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post   -n libtaginfo1 -p /sbin/ldconfig
%postun -n libtaginfo1 -p /sbin/ldconfig
%post   -n libtaginfo_c0 -p /sbin/ldconfig
%postun -n libtaginfo_c0 -p /sbin/ldconfig

%files -n libtaginfo1
%license COPYING
%{_libdir}/libtaginfo.so.1*

%files -n libtaginfo_c0
%{_libdir}/libtaginfo_c.so.0*

%files -n %{name}-devel
%doc AUTHORS ChangeLog NEWS README
%{_includedir}/%{name}/
%{_libdir}/%{name}.so
%{_libdir}/%{name}_c.so
%{_libdir}/%{name}/
%{_datadir}/vala/
%{_libdir}/pkgconfig/*.pc

%changelog
