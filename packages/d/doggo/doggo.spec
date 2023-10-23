#
# spec file for package doggo
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


Name:           doggo
Version:        0.5.7
Release:        0
Summary:        CLI tool and API server DNS client implemented in Go
License:        GPL-3.0
URL:            https://github.com/mr-karan/doggo
Source0:      	%{name}-%{version}.tar
Source1:		vendor.tar.xz
BuildRequires:  golang(API) >= 1.20
Suggests:       %{name}-fish-completion
Suggests:       %{name}-zsh-completion

%description
doggo is a modern command-line DNS client (like dig) implemented in Go.
It outputs information in a neat concise manner and supports protocols
like DoH, DoT, DoQ, and DNSCrypt as well.

%package fish-completion
Summary:        fish completion for %{name}
Group:          System/Shells
Supplements:    (%{name} and fish)
BuildArch:      noarch

%description fish-completion
fish completion scripts for %{name}

%package zsh-completion
Summary:        zsh completion for %{name}
Group:          System/Shells
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
zsh completion scripts for %{name}

%prep
%autosetup -a1

%build
%ifnarch ppc64
export GOFLAGS="-buildmode=pie"
%endif
go build ./cmd/%{name}
go build ./cmd/api

%install
install -d %{buildroot}%{_bindir}
install -D %{name} %{buildroot}%{_bindir}/%{name}
install -D api %{buildroot}%{_bindir}/%{name}-api
install -Dm644 completions/%{name}.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/%{name}.fish
install -Dm644 completions/%{name}.zsh %{buildroot}%{_datadir}/zsh/site-functions/_%{name}

%files
%license LICENSE
%doc README.md
%doc config-api-sample.toml
%{_bindir}/%{name}
%{_bindir}/%{name}-api

%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions

%files fish-completion
%{_datadir}/fish/vendor_completions.d/%{name}.fish

%files zsh-completion
%{_datadir}/zsh/site-functions/_%{name}

%changelog
