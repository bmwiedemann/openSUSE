#
# spec file for package zoxide
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


%global rustflags '-Clink-arg=-Wl,-z,relro,-z,now'

Name:           zoxide
Version:        0.9.0
Release:        0
Summary:        A smarter cd command
License:        MIT
Group:          System/Console
URL:            https://github.com/ajeetdsouza/zoxide
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.xz
Source2:        cargo_config
BuildRequires:  cargo
BuildRequires:  rust >= 1.31

%description
zoxide is a smarter cd command, inspired by z and autojump. It remembers
which directories you use most frequently, so you can "jump" to them in
just a few keystrokes.

%prep
%autosetup -p1 -a1

install -d -m 0755 .cargo
cp %{SOURCE2} .cargo/config

%build
export RUSTFLAGS=%{rustflags}
cargo build --release %{?_smp_mflags}

%install
export RUSTFLAGS=%{rustflags}
RUSTFLAGS=%{rustflags} cargo install --path . --root=%{buildroot}%{_prefix} %{?_smp_mflags}

# install manpages
ls -la
install -Dpm 644 man/man1/%{name}*.1 -t %{buildroot}%{_mandir}/man1/

# install shell completions
install -Dpm 644 contrib/completions/%{name}.bash %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -Dpm 644 contrib/completions/_%{name} -t %{buildroot}%{_datadir}/zsh/site-functions/
install -Dpm 644 contrib/completions/%{name}.fish -t %{buildroot}/%{_datadir}/fish/vendor_completions.d/

# remove residue crate file
rm -f %{buildroot}%{_prefix}/.crates*

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*.1*
%{_datadir}/bash-completion/completions/%{name}
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_%{name}
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/%{name}.fish

%changelog
