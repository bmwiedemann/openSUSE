#
# spec file for package 2ping
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


%define skip_python2 1
Name:           2ping
Version:        4.5
Release:        0
Summary:        Bi-directional ping utility
License:        GPL-2.0-or-later
URL:            https://www.finnie.org/software/2ping/
Source0:        http://www.finnie.org/software/2ping/%{name}-%{version}.tar.gz
Source1:        http://www.finnie.org/software/2ping/%{name}-%{version}.tar.gz.asc
Source2:        %{name}.keyring
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module distro}
BuildRequires:  %{python_module dnspython}
BuildRequires:  %{python_module netifaces}
BuildRequires:  %{python_module pycryptodomex}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  systemd-rpm-macros
Requires:       python >= 3.5
Recommends:     python3-distro
Recommends:     python3-dnspython
Recommends:     python3-netifaces
Recommends:     python3-pycryptodomex
BuildArch:      noarch
%{?systemd_requires}

%description
2ping is a bi-directional ping utility. It uses 3-way pings (akin to TCP SYN,
SYN/ACK, ACK) and after-the-fact state comparison between a 2ping listener and
a 2ping client to determine which direction packet loss occurs.

%prep
%autosetup

%build
%python_build

%install
%python_install
install -Dp -m 0644 2ping.service %{buildroot}%{_unitdir}/2ping.service
install -Dp -m 0644 doc/2ping.1 %{buildroot}%{_mandir}/man1/2ping.1
install -Dp -m 0644 doc/2ping.1 %{buildroot}%{_mandir}/man1/2ping6.1

mkdir -p %{buildroot}%{_sbindir}
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rc2ping

# create symlinks for man pages
%fdupes -s %{buildroot}%{_mandir}
# create hardlinks for the rest
%fdupes %{buildroot}%{_prefix}

%check
%pytest

%pre
%service_add_pre 2ping.service

%post
%service_add_post 2ping.service

%preun
%service_del_preun 2ping.service

%postun
%service_del_postun 2ping.service

%files
%license COPYING
%doc ChangeLog README.md
%{_bindir}/%{name}
%{_bindir}/%{name}6
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_mandir}/man1/%{name}6.1%{?ext_man}
%{_sbindir}/rc%{name}
%{_unitdir}/2ping.service
%{python3_sitelib}/*

%changelog
