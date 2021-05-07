#
# spec file for package onioncat
#
# Copyright (c) 2021 SUSE LLC
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


Name:           onioncat
Version:        0.3.8
Release:        0
Summary:        VPN adapter for Tor and I2P
License:        GPL-3.0-only
URL:            https://www.onioncat.org/
Source0:        https://github.com/rahra/onioncat/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  libtool
Requires:       tor

%description
OnionCat creates a transparent IP layer on top of Tor's hidden services. It
transmits any kind of IP-based data transparently through the Tor network on a
location hidden basis. You can think of it as a point-to-multipoint VPN between
hidden services.

%prep
%autosetup

%build
autoreconf -fvi
%configure --docdir=%{_docdir}/%{name}
%make_build

%install
%make_install

%files
%license COPYING
%doc AUTHORS ChangeLog GitLog README.md
%doc %{_docdir}/%{name}/
%{_bindir}/ocat
%{_mandir}/man1/ocat.1%{?ext_man}

%changelog
