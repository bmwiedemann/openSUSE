#
# spec file for package gnu-netcat
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           gnu-netcat
Version:        0.7.1
Release:        0
Summary:        GNU variant of universal network utility
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Other
Url:            http://netcat.sourceforge.net
Source0:        http://sourceforge.net/projects/netcat/files/netcat/%{version}/netcat-%{version}.tar.bz2
Source1:        http://netcat.sourceforge.net/signatures/netcat-%{version}.tar.bz2.asc
Source2:        %{name}.keyring
Conflicts:      netcat-openbsd

%description
Netcat is a networking utility which reads and writes data across
network connections. It is a "back-end" tool that can be used
directly or driven by other programs and scripts. It is also a
network debugging and exploration tool, since it can create a number
of connection types. It provides the following main features:

  * Outbound and inbound connections, TCP or UDP, to or from any ports.
  * Tunneling mode which allows also tunneling such as UDP to
    TCP, with the possibility of specifying all network parameters (source
    port/interface, listening port/interface, and the remote host allowed to
    connect to the tunnel.
  * Built-in port-scanning capabilities, with randomizer.
  * Advanced usage options, such as buffered send-mode (one line every N
    seconds), and hexdump (to stderr or to a specified file) of trasmitted and
    received data.
  * Optional RFC854 telnet codes parser and responder.

%prep
%setup -q -n netcat-%{version}

%build
%configure --disable-static --disable-silent-rules
make %{?_smp_mflags}

%install
%make_install
%find_lang netcat

%post
%install_info --info-dir=%{_infodir} %{_infodir}/netcat.info.gz

%postun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/netcat.info.gz

%files -f netcat.lang
%license COPYING
%doc ChangeLog README
%{_bindir}/*
%{_infodir}/netcat.info%{?ext_info}
%{_mandir}/*/*

%changelog
