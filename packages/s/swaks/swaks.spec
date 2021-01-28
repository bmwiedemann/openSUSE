#
# spec file for package swaks
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           swaks
Version:        20201014.0
Release:        0
Summary:        Swiss Army Knife for SMTP
License:        GPL-2.0-only
Group:          Productivity/Networking/Email/Clients
URL:            http://jetmore.org/john/code/swaks/
Source:         http://jetmore.org/john/code/swaks/files/swaks-%{version}.tar.gz
Requires:       perl-Net-SSLeay
BuildArch:      noarch

%description
Swaks is a scriptable, transaction-oriented SMTP test
tool. Features include:

* SMTP extensions including TLS, authentication, pipelining, and
  XCLIENT
* Protocols including SMTP, ESMTP, and LMTP
* Transports including UNIX-domain sockets, internet-domain sockets
  (IPv4 and IPv6), and pipes to spawned processes
* Completely scriptable configuration, with option specification via
  environment variables, configuration files, and command line

%prep
%autosetup -p1 

%build

%install
install -D -m 0755 swaks %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%license LICENSE.txt
%doc README.txt doc/*.txt

%changelog
