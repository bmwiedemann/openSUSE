#
# spec file for package 2ping
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define pythons python3

Name:           2ping
Version:        4.6.1
Release:        0
Summary:        Bi-directional ping utility
License:        MPL-2.0
URL:            https://www.finnie.org/software/2ping/
Source0:        https://github.com/rfinnie/2ping/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/rfinnie/2ping/releases/download/v%{version}/%{name}-%{version}.tar.gz.asc
Source2:        %{name}.keyring
Source3:        2ping.service
BuildRequires:  %{python_module distro}
BuildRequires:  %{python_module dnspython}
BuildRequires:  %{python_module netifaces}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pycryptodomex}
BuildRequires:  %{python_module pytest}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  systemd-rpm-macros
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

%package bash-completion
Summary:        Bash completion for 2ping
Group:          System/Shells
Requires:       %{name}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)

%description bash-completion
bash command line completion support for 2ping.

%prep
%autosetup

%build
%pyproject_wheel

%install
%pyproject_install

install -Dp -m 0644 %{SOURCE3} %{buildroot}%{_unitdir}/2ping.service
install -Dp -m 0644 doc/2ping.1 %{buildroot}%{_mandir}/man1/2ping.1
install -Dp -m 0644 doc/2ping.1 %{buildroot}%{_mandir}/man1/2ping6.1
install -Dp -m 0644 2ping.bash_completion %{buildroot}%{_datadir}/bash-completion/completions/2ping

# Fix python shebangs
%python3_fix_shebang

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
%license COPYING.md
%doc ChangeLog.md README.md
%{_bindir}/%{name}
%{_bindir}/%{name}6
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_mandir}/man1/%{name}6.1%{?ext_man}
%{_unitdir}/2ping.service
%{python3_sitelib}/*

%files bash-completion
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/%{name}

%changelog
