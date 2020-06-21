#
# spec file for package sipsak
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


Name:           sipsak
Version:        0.9.7
Release:        0
Summary:        SIP Swiss Army Knife
License:        GPL-2.0-only
Group:          Productivity/Telephony/SIP/Utilities
URL:            https://github.com/nils-ohlmeier/sipsak
Source:         https://github.com/nils-ohlmeier/sipsak/releases/download/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(check)
BuildRequires:  pkgconfig(libcares)
BuildRequires:  pkgconfig(openssl)

%description
Sipsak is a small command line tool for developers and administrators
of Session Initiation Protocol (SIP) applications. It can be used for
some simple tests on SIP applications and devices, including sending
OPTIONS requests, sending text files with SIP requests, traceroute,
user location test, flooding test, etc

%prep
%setup -q

%build
export CFLAGS="%optflags -fcommon"
%configure
%make_build

%install
%make_install

%check
%make_build check

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/sipsak
%{_mandir}/man1/sipsak.1%{?ext_man}

%changelog
