#
# spec file for package atlascpp
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


%define soname 0_6-1
Name:           atlascpp
Version:        0.6.4
Release:        0
Summary:        Remote protocol for the Worldforge MMORPG system
License:        LGPL-2.1-only AND GPL-2.0-or-later
Group:          Development/Languages/C and C++
Url:            http://www.worldforge.org/index.php/components/atlas-cpp/
Source:         http://downloads.sourceforge.net/worldforge/Atlas-C++-%{version}.tar.bz2
BuildRequires:  gcc-c++
BuildRequires:  libbz2-devel
BuildRequires:  libstdc++-devel
BuildRequires:  pkgconfig
BuildRequires:  zlib-devel

%description
This library implements the Atlas protocol for use in client-server
game applications. It is the standard implementation used by games written
by the WorldForge project.

%package -n lib%{name}-%{soname}
Summary:        Remote protocol for the Worldforge MMORPG system
Group:          System/Libraries

%description -n lib%{name}-%{soname}
This library implements the Atlas protocol for use in client-server
game applications. It is the standard implementation used by games written
by the WorldForge project. This library is suitable for linking to either
clients or servers.

%package devel
Summary:        Development files for the Atlas protocol C++ implementation
Group:          Development/Languages/C and C++
Requires:       lib%{name}-%{soname} = %{version}

%description devel
This library implements the Atlas protocol for use in client-server
game applications. It is the standard implementation used by games written
by the WorldForge project. This library is suitable for linking to either
clients or servers.

%prep
%setup -q -n Atlas-C++-%{version}

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
export CPPFLAGS="$CFLAGS"
%configure
make %{?_smp_mflags}

%install
%makeinstall

# Do not package libtool archives.
rm %{buildroot}%{_libdir}/lib*.la

%post -n lib%{name}-%{soname} -p /sbin/ldconfig

%postun -n lib%{name}-%{soname} -p /sbin/ldconfig

%files -n lib%{name}-%{soname}
%doc AUTHORS
%license COPYING
%{_libdir}/lib*.so.*

%files devel
%doc NEWS README THANKS ChangeLog TODO HACKING ROADMAP
%{_bindir}/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*

%changelog
