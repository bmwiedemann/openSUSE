#
# spec file for package bat-extras
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


Name:           bat-extras
Version:        2023.03.21
Release:        0
Summary:        Extra scripts for bat
License:        MIT
BuildArch:      noarch
Group:          Productivity/File utilities
URL:            https://github.com/eth-p/bat-extras
Source:         https://github.com/eth-p/bat-extras/archive/v%{version}.tar.gz
Requires:       bash
Requires:       bat
Recommends:     delta
Recommends:     entr
Recommends:     ripgrep

%description
Bash scripts that integrate bat with various command line tools.

%prep
%setup -q -n %{name}-%{version}

%build

%install
./build.sh --install --manuals --prefix=%{buildroot}%{_prefix}
sed -i "s@/usr/bin/env bash@/bin/bash@" %{buildroot}%{_bindir}/*
install -Dm 0644 -t %{buildroot}%{_mandir}/man1 man/*

%files
%defattr(-, root, root)
%license LICENSE.md
%{_mandir}/man1/*
%doc README.md
%{_bindir}/*

%changelog
