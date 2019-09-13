#
# spec file for package libtaginfo
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


%define _sover 1
Name:           libtaginfo
Version:        0.2.1
Release:        0
Summary:        Library for reading media metadata (tags)
License:        LGPL-2.1+
Group:          System/Libraries
Url:            https://bitbucket.org/shuerhaaken/libtaginfo
Source:         https://bitbucket.org/shuerhaaken/%{name}/downloads/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(taglib) >= 1.9.1
BuildRequires:  vala

%description
libtaginfo is a convenience wrapper for taglib with C and vala
bindings.

Features are reading/writing fields like: Artist, Album, Title, Genre,
AlbumArtist, Comments, Disk number, Compilation flag, User labels,
Embedded Images, Lyrics, Audio properties (length, bitrate, samplerate,
channels ...), ...

%package -n %{name}%{_sover}
Summary:        Library for reading media metadata (tags)
Group:          System/Libraries

%description -n %{name}%{_sover}
libtaginfo is a convenience wrapper for taglib with C and vala
bindings.

Features are reading/writing fields like: Artist, Album, Title, Genre,
AlbumArtist, Comments, Disk number, Compilation flag, User labels,
Embedded Images, Lyrics, Audio properties (length, bitrate, samplerate,
channels ...), ...

%package -n %{name}-devel
Summary:        Development files of libtaginfo
Group:          Development/Libraries
Requires:       %{name}%{_sover} = %{version}

%description -n %{name}-devel
The libtaglib development package includes the header files, libraries,
configuration files and development tools necessary for compiling and
linking application which will use libtaginfo.

%prep
%setup -q

%build
autoreconf -fi
%configure
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{name}%{_sover} -p /sbin/ldconfig

%postun -n %{name}%{_sover} -p /sbin/ldconfig

%files -n %{name}%{_sover}
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_libdir}/%{name}.so.*
%{_libdir}/%{name}_c.so.*

%files -n %{name}-devel
%defattr(-, root, root)
%{_includedir}/%{name}/
%{_libdir}/%{name}.so
%{_libdir}/%{name}_c.so
%{_libdir}/%{name}/
%{_datadir}/vala/
%{_libdir}/pkgconfig/*.pc

%changelog
