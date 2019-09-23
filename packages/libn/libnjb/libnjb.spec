#
# spec file for package libnjb
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

# norootforbuild


Name:           libnjb
BuildRequires:  libtool libusb-devel zlib-devel
Url:            http://libnjb.sourceforge.net
License:        BSD-3-Clause
Group:          Development/Libraries/Other
Version:        2.2.7
Release:        1
Summary:        Nomad Jukebox API
Source:         %{name}-%{version}.tar.gz
Patch:          libnjb-no_m4_dir.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       dbus-1

%description
Nomad Jukebox API

%package -n libnjb5
License:        BSD-3-Clause
Summary:        Nomad Jukebox API
Group:          Development/Libraries/Other
Requires:       %{name} = %{version}

%description -n libnjb5
Nomad Jukebox API

%package devel
License:        BSD-3-Clause
Group:          Development/Libraries/Other
AutoReqProv:    on
Summary:        Nomad Jukebox API
Requires:       %{name} = %{version}
Requires:       libusb-devel

%description devel
Nomad Jukebox API

%prep
%setup -q
%patch

%build
autoreconf -fiv
%configure --program-prefix=njb- --disable-static --with-pic
%{__make} %{?jobs:-j%jobs}

%install
make install DESTDIR=$RPM_BUILD_ROOT
rm %{buildroot}%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post -n libnjb5 -p /sbin/ldconfig

%postun -n libnjb5 -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc AUTHORS FAQ README LICENSE
%{_bindir}/njb-*

%files -n libnjb5
%defattr (-, root, root)
%{_libdir}/libnjb.so.*

%files devel
%defattr(-,root,root)
%{_libdir}/libnjb.so
%{_prefix}/include/libnjb.h
%{_libdir}/pkgconfig/libnjb.pc

%changelog
