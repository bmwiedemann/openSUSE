#
# spec file for package sersniff
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           sersniff
Version:        0.0.5
Release:        0
Summary:        A simple program to tunnel/sniff between 2 serial ports
License:        GPL-2.0-only
Group:          System/Libraries
URL:            https://www.earth.li/projectpurple/progs/sersniff.html
Source0:        https://www.earth.li/projectpurple/files/%{name}-%{version}.tar.gz

%description
This program was written to aid with the decoding of the protocol
used by serial communication. It has support for sniffing a TCP
connection or between a serial port and a TCP port.

%prep
%setup -q -b 0

%build
%make_build CFLAGS="%{optflags}"

%install
install -Dpm 0755 %{name} \
  %{buildroot}%{_bindir}/%{name}
install -Dpm 0644 %{name}.8 \
  %{buildroot}%{_mandir}/man8/%{name}.8

%files
%license LICENSE
%doc README HISTORY TODO
%{_bindir}/sersniff
%{_mandir}/man8/sersniff.8%{?ext_man}

%changelog
