#
# spec file for package python-magic-wormhole
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


%define modname magic_wormhole
Name:           python-magic-wormhole
Version:        0.17.0
Release:        0
Summary:        Tool for transferring files through a secure channel
License:        MIT
URL:            https://github.com/magic-wormhole/magic-wormhole
Source:         https://files.pythonhosted.org/packages/source/m/%{modname}/%{modname}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM https://github.com/magic-wormhole/magic-wormhole/pull/554 fix test under Twisted 24.10.0
Patch0:         twisted.patch
BuildRequires:  %{python_module Automat}
BuildRequires:  %{python_module PyNaCl}
BuildRequires:  %{python_module Twisted}
BuildRequires:  %{python_module attrs >= 19.2.0}
BuildRequires:  %{python_module autobahn}
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module cryptography}
BuildRequires:  %{python_module humanize}
BuildRequires:  %{python_module iterable-io >= 1.0.0}
BuildRequires:  %{python_module magic-wormhole-mailbox-server}
BuildRequires:  %{python_module magic-wormhole-transit-relay >= 0.3.1}
BuildRequires:  %{python_module noiseprotocol}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module spake2 >= 0.9}
BuildRequires:  %{python_module tqdm >= 4.13.0}
BuildRequires:  %{python_module txtorcon >= 18.0.2}
BuildRequires:  %{python_module versioneer}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module zipstream-ng >= 1.7.1}
BuildRequires:  %{pythons}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# Shell completions
BuildRequires:  bash-completion
BuildRequires:  fish
BuildRequires:  zsh
Requires:       python-Automat
Requires:       python-PyNaCl
Requires:       python-Twisted
Requires:       python-attrs >= 19.2.0
Requires:       python-autobahn
Requires:       python-click
Requires:       python-cryptography
Requires:       python-humanize
Requires:       python-iterable-io >= 1.0.0
Requires:       python-spake2 >= 0.9
Requires:       python-tqdm >= 4.13.0
Requires:       python-txtorcon >= 18.0.2
Requires:       python-zipstream-ng >= 1.7.1
Requires(post): update-alternatives
Requires(preun): update-alternatives
Suggests:       python-magic-wormhole-mailbox-server
Suggests:       python-magic-wormhole-transit-relay
Suggests:       python-noiseprotocol
BuildArch:      noarch
%python_subpackages

%description
This package provides a library and a command-line tool named wormhole,
which makes it possible to get arbitrary-sized files and directories from
one computer to another. The two endpoints are identified by using identical
"wormhole codes": in general, the sending machine generates and displays
the code, which must then be typed into the receiving machine.

%package -n %{name}-bash-completion
Summary:        Bash Completion for %{name}
Group:          System/Shells
Supplements:    (%{name} and bash-completion)
Requires:       bash-completion
Requires:       python3dist(magic-wormhole)
BuildArch:      noarch

%description -n %{name}-bash-completion
Bash command-line completion support for %{name}.

%package -n %{name}-fish-completion
Summary:        Fish Completion for %{name}
Group:          System/Shells
Supplements:    (%{name} and fish)
Requires:       fish
Requires:       python3dist(magic-wormhole)
BuildArch:      noarch

%description -n %{name}-fish-completion
Fish command-line completion support for %{name}.

%package -n %{name}-zsh-completion
Summary:        Zsh Completion for %{name}
Group:          System/Shells
Supplements:    (%{name} and zsh)
Requires:       zsh
Requires:       python3dist(magic-wormhole)
BuildArch:      noarch

%description -n %{name}-zsh-completion
Zsh command-line completion support for %{name}.

%prep
%autosetup -p1 -n %{modname}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/wormhole
install -Dm644 wormhole_complete.bash %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -Dm644 wormhole_complete.zsh %{buildroot}%{_datadir}/zsh/site-functions/_%{name}
install -Dm644 wormhole_complete.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/%{name}.fish
rm %{buildroot}/usr/wormhole_complete*

%check
%pytest src/wormhole/test

%post
%python_install_alternative wormhole

%postun
%python_uninstall_alternative wormhole

%files %python_files
%license LICENSE
%doc NEWS.md README.md
%python_alternative %{_bindir}/wormhole
%{python_sitelib}/wormhole
%{python_sitelib}/magic_wormhole-%{version}.dist-info

%files -n %{name}-bash-completion
%{_datadir}/bash-completion/*

%files -n %{name}-fish-completion
%{_datadir}/fish/*

%files -n %{name}-zsh-completion
%{_datadir}/zsh/*

%changelog
