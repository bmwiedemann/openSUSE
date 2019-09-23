#
# spec file for package libtiger
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2016 Bjørn Lie, Bryne, Norway.
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

%define _sover  5

Name:           libtiger
Version:        0.3.4
Release:        0
License:        LGPL-2.1+
Summary:        Rendering library for Kate streams using Pango and Cairo
Url:            http://libtiger.googlecode.com
Group:          Development/Libraries/C and C++
## Git Url:     https://git.xiph.org/?p=users/oggk/tiger.git
Source:         http://libtiger.googlecode.com/files/libtiger-%{version}.tar.gz
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(kate) >= 0.2.0
BuildRequires:  pkgconfig(pangocairo) >= 1.16
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Libtiger is a rendering library for Kate streams using Pango and Cairo.
More information about Kate streams may be found at 
http://wiki.xiph.org/index.php/OggKate

%package -n     libtiger%{_sover}
Summary:        Rendering library for Kate streams using Pango and Cairo
Group:          System/Libraries

%description -n libtiger%{_sover}
Libtiger is a rendering library for Kate streams using Pango and Cairo.
More information about Kate streams may be found at 
http://wiki.xiph.org/index.php/OggKate

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       libtiger%{_sover} = %{version}-%{release}

%description    devel
This package contains libraries and header files for developing
applications that use libtiger.

%prep
%setup -q

%build
%configure \
	--disable-static \
	--disable-doc
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} %{?_smp_mflags}
find  %{buildroot}%{_libdir} -name '*.la' -delete -print

# Fix timestamps change
touch -r include/tiger/tiger.h.in %{buildroot}%{_includedir}/tiger/tiger.h

%post -n libtiger%{_sover} -p /sbin/ldconfig

%postun -n libtiger%{_sover} -p /sbin/ldconfig

%files -n libtiger%{_sover}
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog README
%{_libdir}/libtiger.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/tiger/
%{_libdir}/*.so
%{_libdir}/pkgconfig/tiger.pc

%changelog
