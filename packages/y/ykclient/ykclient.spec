#
# spec file for package ykclient
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           ykclient
Version:        2.15
Release:        0
Summary:        Online validation of Yubikey OTPs
License:        BSD-2-Clause
Group:          Productivity/Networking/Security
Url:            https://developers.yubico.com/
Source0:        https://developers.yubico.com/yubico-c-client/Releases/ykclient-%{version}.tar.gz
Source1:        https://developers.yubico.com/yubico-c-client/Releases/ykclient-%{version}.tar.gz.sig
BuildRequires:  curl-devel
BuildRequires:  help2man
BuildRequires:  pkgconfig
Requires:       libykclient3 = %{version}
Provides:       yubico-c-client = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This project implements online validation of Yubikey OTPs.
It is written in C and provides a shared library for use by other software.

%package -n libykclient3
Summary:        Online validation of Yubikey OTPs
Group:          Productivity/Networking/Security

%description -n libykclient3
This project implements online validation of Yubikey OTPs.
It is written in C and provides a shared library for use by other software.

%package -n libykclient-devel
Summary:        Online validation of Yubikey OTPs
Group:          Development/Languages/C and C++
Requires:       glibc-devel
Requires:       libykclient3 = %{version}

%description -n libykclient-devel
This project implements online validation of Yubikey OTPs.·
It is written in C and provides a shared library for use by other software.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
rm -rf %{buildroot}%{_libdir}/libykclient.la

%post -n libykclient3 -p /sbin/ldconfig

%postun -n libykclient3 -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc ChangeLog README COPYING
%{_bindir}/ykclient
%{_mandir}/man1/ykclient.1.gz

%files -n libykclient3
%defattr(-,root,root)
%{_libdir}/libykclient.so.*

%files -n libykclient-devel
%defattr(-,root,root)
%{_includedir}/ykclient.h
%{_includedir}/ykclient_errors.h
%{_includedir}/ykclient_server_response.h
%{_includedir}/ykclient_version.h
%{_libdir}/libykclient.so

%changelog
