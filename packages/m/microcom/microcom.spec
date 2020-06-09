#
# spec file for package microcom
#
# Copyright (c) 2020 SUSE LLC
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


Name:           microcom
Version:        2019.01.0
Release:        0
Summary:        Minimalistic terminal program
License:        GPL-2.0-only
Group:          System/Console
URL:            https://github.com/pengutronix/microcom.git
Source0:        https://github.com/pengutronix/microcom/releases/download/v%{version}/%{name}-%{version}.tar.xz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  readline-devel

%description
microcom is a minimalistic terminal program for communicating with devices over
a serial connection (e.g. embedded systems, switches, modems). It features
connection via RS232 serial interfaces (including setting of transfer rates) as
well as in "Telnet mode" as specified in [RFC 2217].

[RFC 2217]: https://tools.ietf.org/html/rfc2217

%prep
%setup -q

%build
autoreconf -i
%configure
%make_build

%install
%make_install 

%files
%{_mandir}/man1/microcom.1%{?ext_man}
%license COPYING
%{_bindir}/microcom

%changelog
