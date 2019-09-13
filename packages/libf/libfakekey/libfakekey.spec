#
# spec file for package libfakekey
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


%define lname   libfakekey0
Name:           libfakekey
Version:        0.1
Release:        0
Summary:        Library for converting characters to X key-presses
License:        LGPL-2.1+
Group:          System/GUI/Other
Url:            https://yoctoproject.org/tools-resources/projects/matchbox
Source:         http://downloads.yoctoproject.org/releases/matchbox/%{name}/%{version}/%{name}-%{version}.tar.bz2
# PATCH-FIX-UPSTREAM 0001-add-return.patch nmo.marques@gmail.com -- Add missing return.
Patch0:         0001-add-return.patch
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(xtst)

%description
libfakekey is a simple library for converting UTF-8 characters into
'fake' X key-presses.

%package -n %{lname}
Summary:        Library for converting characters to X key-presses
Group:          System/Libraries

%description -n %{lname}
libfakekey is a simple library for converting UTF-8 characters into
'fake' X key-presses.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries/Other
Requires:       %{lname} = %{version}

%description devel
The libfakekey-devel package contains libraries and header files for
developing applications that use libfakekey.

%prep
%setup -q
%patch0 -p1

%build
%configure --disable-static
make %{?_smp_mflags} AM_LDFLAGS=-lX11

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{lname} -p /sbin/ldconfig

%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%defattr(-,root,root)
%doc COPYING
%{_libdir}/libfakekey.so.*

%files devel
%defattr(-,root,root)
%{_includedir}/fakekey/
%{_libdir}/libfakekey.so
%{_libdir}/pkgconfig/libfakekey.pc

%changelog
