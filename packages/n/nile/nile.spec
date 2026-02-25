#
# spec file for package nile
#
# Copyright (c) 2025 SUSE LLC and contributors
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

Name:           nile
Version:        1.1.2
Release:        0
Summary:        Unofficial Amazon Games client
License:        GPL-3.0-only
URL:            https://github.com/imLinguin/nile.git
Source:         %{name}-%{version}.tar.xz
BuildRequires:  python3-PyInstaller
BuildRequires:  python3-json5 >= 0.9
BuildRequires:  python3-pip
BuildRequires:  python3-protobuf >= 4.0
BuildRequires:  python3-pycryptodome >= 3.0
BuildRequires:  python3-requests < 3.0}
BuildRequires:  python3-setuptools
%ifarch aarch64
ExclusiveArch: aarch64
%endif
%ifarch x86_64
ExclusiveArch: x86_64
%endif

%description
Nile aims to be CLI and GUI tool for managing and playing games from Amazon.

%prep
%setup -q

# Fixes pyproject and adds a data section.
cat >> pyproject.toml <<'PYEOF'
[tool.setuptools.packages.find]
where = ["."]
include = ["nile", "nile.*"]

[tool.setuptools.package-data]
"nile" = ["assets/**/*"]
PYEOF

%build
pyinstaller --onefile --name nile nile/cli.py

%install
install -Dm0755 dist/nile %{buildroot}/%{_bindir}/nile

%files
%license LICENSE*
%{_bindir}/nile

%changelog
