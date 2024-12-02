#
# spec file for package 2ping
#
# Copyright (c) 2024 SUSE LLC
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
Version:        4.5.1+20241102
Release:        0
Summary:        Bi-directional ping utility
License:        MPL-2.0
URL:            https://www.finnie.org/software/2ping/
Source0:        %{name}-%{version}.tar.xz
Source2:        %{name}.keyring
Patch0:         harden_2ping.service.patch
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-devel >= 3.6
BuildRequires:  python3-distro
BuildRequires:  python3-dnspython
BuildRequires:  python3-netifaces
BuildRequires:  python3-pycryptodomex
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools
BuildRequires:  systemd-rpm-macros
Requires:       python3 >= 3.6
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
%python3_build

%install
%python3_install
install -Dp -m 0644 2ping.service %{buildroot}%{_unitdir}/2ping.service
install -Dp -m 0644 doc/2ping.1 %{buildroot}%{_mandir}/man1/2ping.1
install -Dp -m 0644 doc/2ping.1 %{buildroot}%{_mandir}/man1/2ping6.1

mkdir -p %{buildroot}%{_sbindir}
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rc2ping

# Fix python shebangs
%python3_fix_shebang

# create symlinks for man pages
%fdupes -s %{buildroot}%{_mandir}
# create hardlinks for the rest
%fdupes %{buildroot}%{_prefix}

%check
py.test -v

%pre
%service_add_pre 2ping.service

%post
%service_add_post 2ping.service

%preun
%service_del_preun 2ping.service

%postun
%service_del_postun 2ping.service

%files
%license COPYING.md
%doc ChangeLog.md README.md
%{_bindir}/%{name}
%{_bindir}/%{name}6
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_mandir}/man1/%{name}6.1%{?ext_man}
%{_sbindir}/rc%{name}
%{_unitdir}/2ping.service
%{python3_sitelib}/*

%changelog
