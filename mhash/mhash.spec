#
# spec file for package mhash
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           mhash
Version:        0.9.9.9
Release:        0
Summary:        A Library for Working with Strong Hashes
License:        GPL-2.0+
Group:          Development/Libraries/C and C++
Url:            http://mhash.sourceforge.net/
Source:         http://sourceforge.net/projects/%{name}/files/%{name}/%{version}/%{name}-%{version}.tar.bz2
Patch0:         %{name}-%{version}-shared.diff
# PATCH-FIX-UPSTREAM fix-for-upstream-sources.patch sourceforge#2908478
Patch1:         mhash_remove_premature_free.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The mhash library provides an easy way to access strong hashes, such as
MD5, SHA1, and other algorithms.

%package -n lib%{name}2
Summary:        A Library for Working with Strong Hashes
Group:          System/Libraries
Provides:       %{name} = %{version}
Obsoletes:      %{name} < %{version}

%description -n lib%{name}2
The mhash library provides an easy way to access strong hashes, such as
MD5, SHA1, and other algorithms.

%package devel
Summary:        Header Files for mhash Library
Group:          Development/Libraries/C and C++
Requires:       lib%{name}2 = %{version}
Provides:       %{name}:%{_includedir}/%{name}.h

%description devel
The mhash library provides an easy way to access strong hashes such as
MD5, SHA1, and other algorithms.

%prep
%setup -q
%patch0
%patch1 -p1

%build
autoreconf --force --install
%configure \
	--with-pic \
	--disable-static

make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
# useless .la file 
rm %{buildroot}%{_libdir}/lib%{name}.la

%check
make %{?_smp_mflags} check

%post -n lib%{name}2 -p /sbin/ldconfig

%postun -n lib%{name}2 -p /sbin/ldconfig

%files -n lib%{name}2
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog NEWS README THANKS TODO
%{_libdir}/libmhash.so.*

%files devel
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog NEWS README THANKS TODO
%doc doc/skid2-authentication doc/example.c
%doc %{_mandir}/man?/*
%{_includedir}/*
%{_libdir}/libmhash.so

%changelog
