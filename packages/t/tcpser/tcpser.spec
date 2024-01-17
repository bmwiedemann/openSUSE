#
# spec file for package tcpser
#
# Copyright (c) 2020, Martin Hauke <mardnh@gmx.de>
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

Name:           tcpser
Version:        1.0rc12+git.20191116
Release:        0
Summary:        Serial to IP modem emulation program
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Other
URL:            https://github.com/FozzTexx/tcpser
Source:         %{name}-%{version}.tar.xz
Source1:        tcpser.1
Patch0:         tcpser-obey-cflags.patch

%description
TCPSER turns a PC serial port into an emulated Hayes compatible modem
that uses TCP/IP for incoming and outgoing connections. It can be
used to allow older applications and systems designed for modem use
to operate on the Internet. TCPSER supports all standard Hayes
commands, and understands extended and vendor proprietary commands
(though it does not implement many of them).
TCPSER can be used for both inbound and outbound connections.

The original source code can be found here:
http://www.jbrain.com/pub/linux/serial/
This forks changes are based upon the rc12 archive dated 11Mar09.
The author also fixed the bug with being unable to connect to real
telnet servers.

%prep
%setup -q
%patch0 -p1
sed -i 's/\r$//' CHANGES

%build
export CFLAGS="%{optflags}"
make %{?_smp_mflags}

%install
install -Dpm 0755 tcpser %{buildroot}/%{_bindir}/tcpser
install -Dpm 0644 %{SOURCE1} %{buildroot}/%{_mandir}/man1/tcpser.1

%files
%doc CHANGES README.md
%{_bindir}/tcpser
%{_mandir}/man1/tcpser.1%{?ext_man}

%changelog
