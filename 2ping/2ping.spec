#
# spec file for package 2ping
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


Name:           2ping
Version:        4.3
Release:        0
Summary:        Bi-directional ping utility
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Diagnostic
URL:            http://www.finnie.org/software/2ping/
Source0:        http://www.finnie.org/software/2ping/%{name}-%{version}.tar.gz
Source1:        http://www.finnie.org/software/2ping/%{name}-%{version}.tar.gz.asc
Source2:        %{name}.keyring
BuildRequires:  fdupes
BuildRequires:  python3-base
BuildRequires:  python3-setuptools
Requires:       python >= 3.4
# A bit tricky but should do it
Provides:       %{name} = 1397618874.f2c20471488c
Obsoletes:      %{name} = 1397618874.f2c20471488c
BuildArch:      noarch

%description
2ping is a bi-directional ping utility. It uses 3-way pings (akin to TCP SYN,
SYN/ACK, ACK) and after-the-fact state comparison between a 2ping listener and
a 2ping client to determine which direction packet loss occurs.

%prep
%setup -q

%build
%{py3_build}

%install
%{py3_install}
install -d -m 0755 %{buildroot}%{_mandir}/man1
install -m 0644 doc/2ping.1 %{buildroot}%{_mandir}/man1/2ping.1
install -m 0644 doc/2ping.1 %{buildroot}%{_mandir}/man1/2ping6.1

# create symlinks for man pages
%fdupes -s %{buildroot}/%{_mandir}
# create hardlinks for the rest
%fdupes %{buildroot}/%{_prefix}

%check
python3 setup.py test

%files
%license COPYING
%doc ChangeLog README doc/2ping-protocol-examples.py doc/2ping.md doc/2ping-protocol.md
%{_bindir}/2ping
%{_bindir}/2ping6
%{_mandir}/man1/2ping.1%{?ext_man}
%{_mandir}/man1/2ping6.1%{?ext_man}
%{python3_sitelib}/*

%changelog
