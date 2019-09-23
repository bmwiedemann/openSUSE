#
# spec file for package liblscp
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2012 Pascal Bleser <pascal.bleser@opensuse.org>
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

%define sover  6
Name:           liblscp
Version:        0.5.8
Release:        0
Summary:        LinuxSampler control protocol library
License:        LGPL-2.1+
Group:          Development/Libraries/C and C++
URL:            https://linuxsampler.org
Source:         https://download.linuxsampler.org/packages/liblscp-%{version}.tar.gz
Patch1:         liblscp-remove_build_timestamps.patch
BuildRequires:  pkgconfig

%description
liblscp is an implementation of the LinuxSampler control protocol,
proposed as a C language API.

%package -n liblscp%{sover}
Summary:        LinuxSampler Control Protocol Library
Group:          System/Libraries

%description -n liblscp%{sover}
liblscp is an implementation of the LinuxSampler control protocol,
proposed as a C language API.

%package -n liblscp-devel
Summary:        LinuxSampler Control Protocol Library
Group:          Development/Libraries/C and C++
Requires:       liblscp%{sover} = %{version}

%description -n liblscp-devel
liblscp is an implementation of the LinuxSampler control protocol,
proposed as a C language API.

%prep
%setup -q
%patch1

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -name "*.la" -type f -delete

%post   -n liblscp%{sover} -p /sbin/ldconfig
%postun -n liblscp%{sover} -p /sbin/ldconfig

%files -n liblscp%{sover}
%doc AUTHORS ChangeLog NEWS README TODO
%license COPYING
%{_libdir}/liblscp.so.%{sover}
%{_libdir}/liblscp.so.%{sover}.*

%files -n liblscp-devel
%{_includedir}/lscp
%{_libdir}/liblscp.so
%{_libdir}/pkgconfig/lscp.pc

%changelog
