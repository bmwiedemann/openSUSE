#
# spec file for package libyubikey
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define         sover 0
Name:           libyubikey
Version:        1.13
Release:        0
Summary:        Yubico's USB key low-level C library
License:        BSD-2-Clause
Group:          Productivity/Networking/Security
Url:            https://developers.yubico.com/
# a different tarball is available from github.  It will not build with this spec file
Source0:        https://developers.yubico.com/yubico-c/Releases/%{name}-%{version}.tar.gz
Source1:        https://developers.yubico.com/yubico-c/Releases/%{name}-%{version}.tar.gz.sig
Source2:        %{name}.keyring

%description
Low-level library for decrypting and parsing Yubikey One-Time Passwords
(OTP) in C.

%package -n %{name}%{sover}
Summary:        Yubico's USB key low-level C library
Group:          Productivity/Networking/Security

%description -n %{name}%{sover}
Low-level library for decrypting and parsing Yubikey One-Time Passwords
(OTP) in C.

%package        devel
Summary:        Yubico's USB key low-level C library
Group:          Development/Libraries/C and C++
Requires:       %{name}%{sover} = %{version}
Requires:       glibc-devel

%description devel
Low-level library for decrypting and parsing Yubikey One-Time Passwords
(OTP) in C.

%package        tools
Summary:        Tools to support Yubico's USB key low-level C library
Group:          Development/Libraries/C and C++

%description tools
Binary tools to support Yubico's Low-level library for decrypting and
parsing Yubikey One-Time Passwords (OTP) in C.

%prep
%setup -q

%build
%configure \
  --disable-silent-rules \
  --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%check
# path needs to be exported otherwise unit tests will fail
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:%{buildroot}%{_libdir}
make %{?_smp_mflags} check

%post -n %{name}%{sover} -p /sbin/ldconfig
%postun -n %{name}%{sover} -p /sbin/ldconfig

%files tools
%defattr(-,root,root,-)
%doc COPYING AUTHORS NEWS
%{_bindir}/modhex
%{_bindir}/ykgenerate
%{_bindir}/ykparse
%{_mandir}/man1/modhex.1%{ext_man}
%{_mandir}/man1/ykgenerate.1%{ext_man}
%{_mandir}/man1/ykparse.1%{ext_man}

%files -n %{name}%{sover}
%defattr(-,root,root,-)
%doc COPYING AUTHORS NEWS
%{_libdir}/libyubikey.so.%{sover}*

%files devel
%defattr(-,root,root,-)
%doc COPYING AUTHORS NEWS
%{_libdir}/libyubikey.so
%{_includedir}/yubikey.h

%changelog
