#
# spec file for package bpfmon
#
# Copyright (c) 2023 SUSE LLC
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


Name:           bpfmon
Version:        2.51
Release:        0
Summary:        Traffic monitor for BPF expression/iptables rule
License:        GPL-2.0-or-later
URL:            https://github.com/bbonev/bpfmon/
Source:         %{url}releases/download/v%{version}/bpfmon-%{version}.tar.xz
Source2:        %{url}releases/download/v%{version}/bpfmon-%{version}.tar.xz.asc
Source3:        https://raw.githubusercontent.com/bbonev/bpfmon/v%{version}/debian/upstream/signing-key.asc#/%{name}.keyring
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libpcap)
BuildRequires:  pkgconfig(yascreen)

%description
While tcpdump shows what packets are going through the
network, bpfmon will show how much in terms
of bytes per second and packets per second in a
nice pseudo-graphical terminal interface.

bpfmon also supports monitoring an iptables rule that
is selected by command line option or selected from a
menu.

%prep
%autosetup -p1

%build
export CFLAGS="%{optflags}"
%make_build PREFIX=%{_usr}

%install
%make_install PREFIX=%{_usr}
install -D -m 0644 -t %{buildroot}%{_mandir}/man8 bpfmon.8

%files
%license LICENSE
%doc README.md
%{_sbindir}/bpfmon
%{_mandir}/man8/bpfmon.8%{?ext_man}

%changelog
