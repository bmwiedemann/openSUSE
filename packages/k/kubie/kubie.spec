#
# spec file for package kubie
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


%global rustflags '-Clink-arg=-Wl,-z,relro,-z,now'

Name:           kubie
Version:        0.23.1
Release:        0
Summary:        A Kubernetes context switcher
License:        Zlib
URL:            https://github.com/sbstp/kubie
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.xz
Recommends:     fzf
BuildRequires:  cargo
BuildRequires:  rust >= 1.67.0

%description
kubie offers context switching, namespace switching and prompt modification in a
way that makes each shell independent from others. It also has support for
split configuration files, meaning it can load Kubernetes contexts from
multiple files. You can configure the paths where kubie will look for
contexts, see the settings section.

%package -n %{name}-bash-completion
Summary:        Bash Completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description -n %{name}-bash-completion
Bash command line completion support for %{name}.

%package -n %{name}-fish-completion
Summary:        Fish Completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Supplements:    (%{name} and fish)
BuildArch:      noarch

%description -n %{name}-fish-completion
Fish command line completion support for %{name}.

%prep
%autosetup -a1

%build
RUSTFLAGS=%{rustflags} cargo build --release --no-default-features

%install
RUSTFLAGS=%{rustflags} cargo install --root=%{buildroot}%{_prefix} --path .

# copy bash completion file
install -D -m 644 ./completion/kubie.bash %{buildroot}%{_datarootdir}/bash-completion/completions/%{name}

# copy fish completion file
install -D -m 644 ./completion/kubie.fish %{buildroot}%{_datarootdir}/fish/vendor_completions.d/%{name}.fish

# remove residue crate files
rm %{buildroot}%{_prefix}/.crates.toml
rm -f %{buildroot}%{_prefix}/.crates2.json

%files
%license LICENSE
%{_bindir}/%{name}

%files -n %{name}-bash-completion
%dir %{_datarootdir}/bash-completion/completions/
%{_datarootdir}/bash-completion/completions/%{name}

%files -n %{name}-fish-completion
%dir %{_datarootdir}/fish
%dir %{_datarootdir}/fish/vendor_completions.d
%{_datarootdir}/fish/vendor_completions.d/%{name}.fish

%changelog
