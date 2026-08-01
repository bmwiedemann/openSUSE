#
# spec file for package nbox
#
# Copyright (c) 2026, Martin Hauke <mardnh@gmx.de>
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


Name:           nbox
Version:        0.14.0
Release:        0
Summary:        Terminal UI and CLI for NetBox
License:        Apache-2.0 OR MIT
URL:            https://github.com/lance0/nbox
#Git-Clone:     https://github.com/lance0/nbox.git
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
Source2:        https://github.com/lance0/nbox/releases/download/v%{version}/nbox-completions.tar.gz
BuildRequires:  cargo-packaging
Recommends:     bash-completion

%description
Terminal UI, CLI, and MCP server for NetBox.
Fast search, IPAM lookups, and device context.

%prep
%autosetup -p 1 -a 1
tar xzvf %{SOURCE2}

%build
%{cargo_build}

%install
%{cargo_install}
install -Dm0644 completions/nbox.bash %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -Dm0644 completions/man/*.1 -t %{buildroot}%{_mandir}/man1/

%check
%{cargo_test}

%files
%license LICENSE-APACHE LICENSE-MIT
%doc CHANGELOG.md README.md
%{_bindir}/nbox
%{_datadir}/bash-completion/completions/%{name}
%{_mandir}/man1/*.1%{?ext_man}

%changelog
