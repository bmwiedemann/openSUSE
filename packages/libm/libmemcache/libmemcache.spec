#
# spec file for package libmemcache
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


%define library_name libmemcache0
Name:           libmemcache
Version:        1.4.0.rc2
Release:        0
Summary:        A client library for memcached
License:        BSD-3-Clause and MIT
Group:          Development/Libraries/C and C++
Url:            http://people.freebsd.org/~seanc/libmemcache/
Source:         http://people.freebsd.org/~seanc/libmemcache/%{name}/%{name}-%{version}.tar.bz2
Patch0:         libmemcache-1.4.0.rc2_gnusource.patch
Patch1:         libmemcache-1.4.0.rc2_gcc43_inline.patch
Patch2:         libmemcache-1.4.0.rc2_preserve_cflags.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
libmemcache implements a client for the superior memcached from Danga
Interactive.


%package -n %{library_name}
Summary:        A client library for memcached
Group:          Development/Libraries/C and C++

%description -n libmemcache0
libmemcache implements a client for the superior memcached from Danga
Interactive.

This package holds the shared libraries from libmemcache.

%package devel
Summary:        Development files for libmemcache
Group:          Development/Libraries/C and C++
Requires:       %{library_name} = %{version}

%description devel
libmemcache implements a client for the superior memcached from Danga
Interactive.

This package contains the development files for libmemcache.

%prep
%setup -q
%patch0
%patch1
%patch2
touch NEWS README AUTHORS

%build
autoreconf -fiv
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags} STRIP=true
rm %{buildroot}%{_libdir}/%{name}.*a

%post   -n %{library_name} -p /sbin/ldconfig

%postun -n %{library_name} -p /sbin/ldconfig

%files -n %{library_name}
%defattr(-,root,root)
%{_libdir}/%{name}.so.*
%doc COPYING ChangeLog

%files devel
%defattr(-,root,root)
%{_libdir}/%{name}.so
%{_includedir}/memcache*

%changelog
