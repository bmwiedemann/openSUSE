#
# spec file for package hexyl
#
# Copyright (c) 2026 SUSE LLC and contributors
# Copyright (c) 2022-2026, Martin Hauke <mardnh@gmx.de>
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


Name:           hexyl
Version:        0.17.0
Release:        0
Summary:        A command-line hex viewer
License:        Apache-2.0 OR MIT
Group:          Development/Tools/Other
#Git-Clone:     https://github.com/sharkdp/hexyl.git
URL:            https://github.com/sharkdp/hexyl
Source:         https://github.com/sharkdp/hexyl/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.xz
BuildRequires:  cargo-packaging
BuildRequires:  pandoc

%description
hexyl is a simple hex viewer for the terminal. It uses a colored output
to distinguish different categories of bytes (NUL bytes, printable
ASCII characters, ASCII whitespace characters, other ASCII characters
and non-ASCII).

%prep
%autosetup -p 1 -a 1

%build
%{cargo_build}
pandoc --standalone --to man ./doc/hexyl.1.md -o hexyl.1

%check
%{cargo_test}

%install
cargo install --no-track --root=%{buildroot}%{_prefix} --path .
install -Dm 0644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1
%{buildroot}%{_bindir}/%{name} --completion bash > %{name}.bash
install -Dm 0644 %{name}.bash %{buildroot}%{_datadir}/bash-completion/completions/%{name}

%files
%license LICENSE-APACHE LICENSE-MIT
%doc CHANGELOG.md README.md
%{_bindir}/hexyl
%{_datadir}/bash-completion/completions/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
