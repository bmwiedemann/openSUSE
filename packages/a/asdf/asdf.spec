#
# spec file for package asdf
#
# Copyright (c) 2025 SUSE LLC
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


Name:           asdf
Version:        0.19.0
Release:        0
Summary:        Extendable version manager
License:        MIT
URL:            https://github.com/asdf-vm/asdf
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang(API) >= 1.23
BuildRequires:  bash-completion
BuildRequires:  fish
BuildRequires:  zsh

%description
Extendable version manager with support for
Ruby, Node.js, Elixir, Erlang & more.

Manage multiple runtime versions with a single CLI tool,
extendable via plugins.

%package bash-completion
Summary:        Bash Completion for %{name}
Requires:       %{name} = %{version}
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion
Bash command line completion support for %{name}.

%package zsh-completion
Summary:        Zsh Completion for %{name}
Requires:       %{name} = %{version}
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
Zsh command line completion support for %{name}.

%package fish-completion
Summary:        Fish Completion for %{name}
Requires:       %{name} = %{version}
Supplements:    (%{name} and fish)
BuildArch:      noarch

%description fish-completion
Fish command line completion support for %{name}.

%prep
%autosetup -a 1

%build
%ifnarch ppc64
export GOFLAGS="-buildmode=pie"
%endif
go build -ldflags='-s -X main.version=%{version}' -o=./asdf ./cmd/asdf

%install
install -D -m 0755 %{name} "%{buildroot}/%{_bindir}/%{name}"
install -d %{buildroot}%{_datadir}/bash-completion/completions
%{buildroot}%{_bindir}/%{name} completion bash > %{buildroot}%{_datarootdir}/bash-completion/completions/%{name}
install -d %{buildroot}%{_datarootdir}/zsh/site-functions
%{buildroot}%{_bindir}/%{name} completion zsh > %{buildroot}%{_datarootdir}/zsh/site-functions/_%{name}
install -d %{buildroot}%{_datadir}/fish/vendor_completions.d
%{buildroot}%{_bindir}/%{name} completion fish > %{buildroot}%{_datadir}/fish/vendor_completions.d/%{name}.fish

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%files bash-completion
%defattr(-,root,root)
%{_datarootdir}/bash-completion/completions/%{name}

%files zsh-completion
%defattr(-,root,root)
%{_datarootdir}/zsh/site-functions/_%{name}

%files fish-completion
%defattr(-,root,root)
%{_datadir}/fish/vendor_completions.d/%{name}.fish

%changelog
