#
# spec file for package yara-x
#
# Copyright (c) 2024-2026, Martin Hauke <mardnh@gmx.de>
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


Name:           yara-x
Version:        1.25.0
Release:        0
Summary:        A malware identification and classification tool
License:        BSD-3-Clause
Group:          System/Filesystems
URL:            https://virustotal.github.io/yara-x/
Source:         %{name}-%{version}.tar.xz
Source1:        vendor.tar.zst
BuildRequires:  cargo
BuildRequires:  cargo-packaging
BuildRequires:  rust >= 1.78.0

%description
YARA is a tool aimed at helping malware researchers to identify and classify
malware samples. With YARA you can create descriptions of malware families
based on textual or binary patterns contained on samples of those families.
Each description consists of a set of strings and a Boolean expression which
determines its logic.

%prep
%autosetup -p 1 -a 1

%build
%{cargo_build}

%install
#%%{cargo_install}
# cargo install with workspaces is still broken
# -> https://github.com/rust-lang/cargo/issues/7599
install -Dm 0755 target/release/yr %{buildroot}%{_bindir}/yr

# create and install bash-completion
install -d %{buildroot}%{_datadir}/bash-completion/completions/
./target/release/yr completion bash > %{buildroot}%{_datadir}/bash-completion/completions/%{name}

# install upstream man pages
install -d %{buildroot}%{_mandir}/man1
install -m 0644 cli/man/*.1 %{buildroot}%{_mandir}/man1/

%check
%ifnarch %{arm}
%{cargo_test}
%else
%{cargo_test} || true
%endif

%files
%license LICENSE
%doc README.md
%{_bindir}/yr
%{_datadir}/bash-completion/completions/%{name}
%{_mandir}/man1/yr*.1%{?ext_man}

%changelog
