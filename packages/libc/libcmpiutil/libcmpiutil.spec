#
# spec file for package libcmpiutil
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


Name:           libcmpiutil
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  libxml2-devel
BuildRequires:  sblim-cmpi-devel
%if 0%{?fedora_version} || 0%{?centos_version} || 0%{?rhel_version} || 0%{?fedora} || 0%{?rhel}
BuildRequires:  pkgconfig
%else
%if 0%{?suse_version} < 920
BuildRequires:  pkgconfig
%else
BuildRequires:  pkg-config
%endif
%endif
Url:            http://libvirt.org/CIM/
Version:        0.5.7
Release:        0
Summary:        Library of utility functions for CMPI providers
License:        LGPL-2.1+
Group:          Development/Libraries/C and C++
Source:         %{name}-%{version}.tar.bz2
Patch1:         fix-arm.patch
Patch2:         0001-libcmpiutil-Fix-endianness-issues-in-embedded-object.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Libcmpiutil is a library of utility functions for CMPI providers.  The
goal is to reduce the amount of repetitive work done in most CMPI
providers by encapsulating common procedures with more "normal" APIs. 
This extends from operations like getting typed instance properties to
standardizing method dispatch and argument checking.



Authors:
--------
    Dan Smith <danms@us.ibm.com>

%package devel
Summary:        Library of utility functions for CMPI providers
Group:          Development/Libraries/C and C++
Requires:       sblim-cmpi-devel
%if 0%{?fedora_version} || 0%{?centos_version} || 0%{?rhel_version} || 0%{?fedora} || 0%{?rhel}
Requires:       pkgconfig
%else
%if 0%{?suse_version} < 920
Requires:       pkgconfig
%else
Requires:       pkg-config
%endif
%endif
Requires:       %{name} = %{version}-%{release}

%description devel
Libcmpiutil is a library of utility functions for CMPI providers.  The
goal is to reduce the amount of repetitive work done in most CMPI
providers by encapsulating common procedures with more "normal" APIs. 
This extends from operations like getting typed instance properties to
standardizing method dispatch and argument checking.


%prep
%setup -q
%ifarch %arm
%patch1 -p1
%endif
%patch2 -p1
chmod -x *.c *.y *.h *.l

%build
export CFLAGS="$RPM_OPT_FLAGS -fgnu89-inline"
%configure --enable-static=no
make

%install
%makeinstall
%{__rm} -f $RPM_BUILD_ROOT%{_libdir}/*.{a,la}

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files 
%defattr(-, root, root, -)
%doc doc/doxygen.conf doc/mainpage README COPYING
%{_libdir}/lib*.so.*

%files devel
%defattr(-, root, root, -)
%{_libdir}/lib*.so
%dir %{_includedir}/libcmpiutil
%{_includedir}/libcmpiutil/*.h
%{_libdir}/pkgconfig/libcmpiutil.pc
%doc doc/SubmittingPatches

%changelog
