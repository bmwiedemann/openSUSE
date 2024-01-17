#
# spec file for package nss-shared-helper
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
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



Name:           nss-shared-helper
Version:        1.0.10
Release:        1
License:        LGPL-2.1+
Summary:        Helper functions for sharing NSS database
Group:          Development/Libraries/C and C++
Source0:        nss-shared-helper-%{version}.tar.bz2
Source1:        baselibs.conf
Url:            http://www.rosenauer.org/hg/libnsssharedhelper/
BuildRequires:  mozilla-nss-devel
BuildRequires:  pkg-config
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This library provides helper functions for programs that want to share
an NSS crypto database.

%define debug_package_requires libnsssharedhelper0 = %{version}-%{release}

%package -n libnsssharedhelper0
License:        LGPL-2.1+
Summary:        Helper functions for sharing NSS database
Group:          Development/Libraries/C and C++

%description -n libnsssharedhelper0
This library provides helper functions for programs that want to share
an NSS crypto database.

%package devel
License:        LGPL-2.1+
Summary:        Development libraries for nss-shared-helper
Group:          Development/Libraries/C and C++
Requires:       libnsssharedhelper0 = %{version}
Requires:       mozilla-nss-devel

%description devel
Header and library files for helpers meant to enable sharing of NSS
crypto database.

%prep
%setup -n nss-shared-helper-%{version}

%build
%configure
make %{?_smp_mflags};

%install
%makeinstall
# We don't want to ship the .a and .la files
rm %{buildroot}/%{_libdir}/*.*a

%clean
rm -rf %{buildroot}

%files -n libnsssharedhelper0
%defattr(-, root, root, -)
%{_libdir}/libnsssharedhelper.so.*
%doc COPYING

%files devel
%defattr(-,root,root,-)
%{_includedir}/nss-shared-helper
%{_libdir}/libnsssharedhelper.so
%{_libdir}/pkgconfig/nss-shared-helper.pc

%post -n libnsssharedhelper0 -p /sbin/ldconfig

%postun -n libnsssharedhelper0 -p /sbin/ldconfig

%changelog
