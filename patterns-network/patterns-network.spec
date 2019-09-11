#
# spec file for package patterns-openSUSE
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


%bcond_with betatest

Name:           patterns-network
Version:        20170319
Release:        0
Summary:        Patterns for Installation (Network)
License:        MIT
Group:          Metapackages
Url:            https://github.com/openSUSE/patterns
Source0:        %{name}-rpmlintrc
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  patterns-rpm-macros


%description
This is an internal package that is used to create the patterns as part
of the installation source setup.  Installation of this package does
not make sense.

This particular package contains the Network patterns.

################################################################################

%package network_admin
%pattern_serverfunctions
Summary:        Network Administration
Group:          Metapackages
Provides:       pattern() = network_admin
Provides:       pattern-icon() = pattern-web-devel
Provides:       pattern-order() = 2940
Provides:       pattern-visible()
Requires:       pattern() = basesystem

Recommends:     nmap
Recommends:     quagga
Recommends:     tcpdump
Recommends:     whois
Recommends:     wireshark
Recommends:     arpwatch
Recommends:     iftop
Recommends:     nagios
Recommends:     mtr
Suggests:       mrtg
Suggests:       openvpn
Suggests:       opie
Suggests:       kismet
Suggests:       iptraf-ng
Suggests:       privoxy
Suggests:       pptpd
Suggests:       wondershaper
Suggests:       krb5
Suggests:       qinternet

%description network_admin
Tools for administering and debugging networks.

%files network_admin
%dir %{_defaultdocdir}/patterns
%{_defaultdocdir}/patterns/network_admin.txt


################################################################################

%prep

%build

%install
mkdir -p %{buildroot}/%{_defaultdocdir}/patterns
echo 'This file marks the pattern network_admin to be installed.' >%{buildroot}/%{_defaultdocdir}/patterns/network_admin.txt

%changelog
