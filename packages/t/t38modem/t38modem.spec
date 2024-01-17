#
# spec file for package t38modem
#
# Copyright (c) 2022 SUSE LLC
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


Name:           t38modem
Version:        4.6.0
Release:        0
Summary:        T.38 for OpenH323 (modem-compatible interface for IP telephony)
License:        MPL-1.1
Group:          Productivity/Telephony/H323/Servers
URL:            https://github.com/T38Modem/t38modem

Source:         https://github.com/T38Modem/t38modem/archive/v%version.tar.gz
Patch1:         0001-build-resolve-compiler-warnings-and-errors-with-ptli.patch
BuildRequires:  gcc-c++
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libsrtp2)
BuildRequires:  pkgconfig(opal) >= 3.18.6
BuildRequires:  pkgconfig(ptlib) >= 2.18.6

%description
This package contains a modem interface for IP telephony using the
H.323 and T.38 protocol standards. It implements a 'tty' interface
which resembles a FAX modem. A sample HylaFAX setup is also provided.

%prep
%autosetup -p1

%build
make CFLAGS="%optflags" CXXFLAGS="%optflags" %{?_smp_mflags}

%install
b="%buildroot"
mkdir -p "$b/%_sbindir"
cp -a t38modem "$b/%_sbindir/"

%files
%doc ReadMe.txt
%doc HylaFAX/config.ttyx
%_sbindir/t38modem

%changelog
