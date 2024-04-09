#
# spec file for package oath-toolkit
#
# Copyright (c) 2024 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%{!?_pam_moduledir: %define _pam_moduledir /%{_lib}/security}
Name:           oath-toolkit
Version:        2.6.11
Release:        0
Summary:        Toolkit for one-time password authentication systems
License:        GPL-3.0-or-later AND LGPL-2.1-or-later
Group:          Productivity/Networking/Security
URL:            https://www.nongnu.org/oath-toolkit/
Source:         https://download-mirror.savannah.gnu.org/releases/%{name}/%{name}-%{version}.tar.gz
Source1:        https://download-mirror.savannah.gnu.org/releases/%{name}/%{name}-%{version}.tar.gz.sig
Source99:       %{name}.keyring
BuildRequires:  bison
BuildRequires:  gengetopt
BuildRequires:  libgcrypt-devel
BuildRequires:  libtool
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gtk-doc)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(xmlsec1)

%description
The OATH Toolkit makes it possible to build one-time password
authentication systems. It contains shared libraries, command line
tools and a PAM module. Supported technologies include the
event-based HOTP algorithm (RFC4226) and the time-based TOTP algorithm
(RFC6238). OATH stands for Open AuTHentication, which is the
organization that specify the algorithms. For managing secret key
files, the Portable Symmetric Key Container (PSKC) format described in
RFC6030 is supported.

%package -n pam_oath
Summary:        PAM module for pluggable login authentication for OATH
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Security

%description -n pam_oath
The OATH Toolkit makes it possible to build one-time password
authentication systems.

This subpackage contains a module to integrate OATH into PAM.

%package -n     liboath0
Summary:        Library for Open AuTHentication (OATH) HOTP support
License:        LGPL-2.1-or-later
Group:          System/Libraries
Requires:       %{name}-xml >= %{version}

%description -n liboath0
The OATH Toolkit makes it possible to build one-time password
authentication systems. Supported technologies include the
event-based HOTP algorithm (RFC4226) and the time-based TOTP algorithm
(RFC6238).

%package        xml
Summary:        XML data files needed by liboath
License:        GPL-3.0-or-later AND LGPL-2.1-or-later
Group:          Productivity/Networking/Security
BuildArch:      noarch

%description xml
The OATH Toolkit makes it possible to build one-time password
authentication systems. It contains shared libraries, command line
tools and a PAM module. Supported technologies include the
event-based HOTP algorithm (RFC4226) and the time-based TOTP algorithm
(RFC6238). OATH stands for Open AuTHentication, which is the
organization that specify the algorithms. For managing secret key
files, the Portable Symmetric Key Container (PSKC) format described in
RFC6030 is supported.

%package -n     liboath-devel
Summary:        Development files for the Open AuTHentication (OATH) HOTP support library
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       liboath0 = %{version}

%description -n liboath-devel
The OATH Toolkit makes it possible to build one-time password
authentication systems.

This subpackage contains the header files for the HOTP/TOTP library.

%package -n     libpskc0
Summary:        Library for Portable Symmetric Key Container
License:        LGPL-2.1-or-later
Group:          System/Libraries

%description -n libpskc0
The OATH Toolkit makes it possible to build one-time password
authentication systems.

For managing secret key files, the Portable Symmetric Key Container
(PSKC) format described in RFC6030 is supported.

%package -n     libpskc-devel
Summary:        Development files for the Portable Symmetric Key Container library
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libpskc0 = %{version}

%description -n libpskc-devel
The OATH Toolkit makes it possible to build one-time password
authentication systems.

For managing secret key files, the Portable Symmetric Key Container
(PSKC) format described in RFC6030 is supported.

This subpackage contains the headers for this library.

%prep
%setup -q

%build
autoreconf -fiv
%configure  \
  --with-pam-dir=%{_pam_moduledir} \
  --with-libgcrypt \
  --disable-silent-rules \
  --disable-static
# Only SLE and openSUSE >= 15.0 are using rpm >= 4.12
# See https://en.opensuse.org/openSUSE:Build_system_recipes#automake
%if 0%{?sle_version} >= 150000
%make_build
%else
make %{?_smp_mflags}
%endif

%install
%make_install
mv COPYING COPYING.summary
find %{buildroot} -type f -name "*.la" -delete -print

%post -n liboath0 -p /sbin/ldconfig
%postun -n liboath0 -p /sbin/ldconfig
%post -n libpskc0 -p /sbin/ldconfig
%postun -n libpskc0 -p /sbin/ldconfig

%files
%license COPYING.summary
%doc ChangeLog NEWS README
%license oathtool/COPYING
%{_bindir}/oathtool
%{_mandir}/man1/oathtool.*
%{_bindir}/pskctool
%{_mandir}/man1/pskctool.*

%files -n pam_oath
%doc pam_oath/README
%license pam_oath/COPYING
%{_pam_moduledir}/pam_oath.so

%files -n liboath0
%license liboath/COPYING
%{_libdir}/liboath.so.*

%files xml
%{_datadir}/xml/pskc/

%files -n liboath-devel
%{_libdir}/liboath.so
%{_includedir}/liboath/
%{_libdir}/pkgconfig/liboath.pc
%doc %{_datadir}/gtk-doc/html/liboath
%{_mandir}/man3/oath_*

%files -n libpskc0
# there's no COPYING for libpskc, but it's LGPL, like liboath
%doc libpskc/README
%license liboath/COPYING
%{_libdir}/libpskc.so.*

%files -n libpskc-devel
%{_libdir}/libpskc.so
%{_includedir}/pskc/
%{_libdir}/pkgconfig/libpskc.pc
%doc %{_datadir}/gtk-doc/html/libpskc
%{_mandir}/man3/pskc_*

%changelog
