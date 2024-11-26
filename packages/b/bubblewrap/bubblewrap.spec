#
# spec file for package bubblewrap
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2024 Andreas Stieger <Andreas.Stieger@gmx.de>
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


Name:           bubblewrap
Version:        0.11.0
Release:        0
Summary:        Core execution tool for unprivileged containers
License:        LGPL-2.0-or-later
Group:          Productivity/Security
URL:            https://github.com/containers/bubblewrap
Source0:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source1:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.xz.asc
# https://www.pseudorandom.co.uk/2003/contact/
# 0x4DE8FF2A63C7CC90, fingerprint: DA98 F25C 0871 C49A 59EA FF2C 4DE8 FF2A 63C7 CC90
Source2:        %{name}.keyring
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  gcc
BuildRequires:  git
BuildRequires:  libcap-devel
BuildRequires:  libtool
BuildRequires:  libxslt
BuildRequires:  meson >= 0.49.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libselinux)

%description
Bubblewrap (%{_bindir}/bwrap) is a core execution engine for unprivileged
containers that works as a setuid binary on kernels without
user namespaces.

%package zsh-completion
Summary:        Zsh tab-completion for bubblewrap
Group:          System/Shells
Supplements:    (%{name} and zsh)

%description zsh-completion
This package provides zsh tab-completion for bubblewrap.

%prep
%autosetup -p1 -n %{name}-%{version}
sed -i '1d' completions/bash/bwrap
%if 0%{?suse_version} < 1500
sed -i '1s,%{_bindir}/env bash,/bin/bash,' demos/bubblewrap-shell.sh
sed -i '1s/env //' demos/userns-block-fd.py
%else
sed -i '1s/env //' demos/bubblewrap-shell.sh demos/userns-block-fd.py
%endif
sed -i '1s/env //' demos/flatpak-run.sh

%build
%meson
%meson_build

%install
%meson_install
find %{buildroot} -type f -name "*.la" -delete -print

%files
%license COPYING
%doc README.md demos
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/bwrap
%{_bindir}/bwrap
%{_mandir}/man1/*

%files zsh-completion
%license COPYING
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_bwrap

%changelog
