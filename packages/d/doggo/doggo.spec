#
# spec file for package doggo
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


Name:           doggo
Version:        1.0.4
Release:        0
Summary:        CLI tool and API server DNS client implemented in Go
License:        GPL-3.0-only
Group:          Productivity/Networking/DNS/Utilities
URL:            https://github.com/mr-karan/doggo
Source0:        %{name}-%{version}.tar
Source1:        vendor.tar.xz
BuildRequires:  golang(API) >= 1.22
Recommends:     %{name}-bash-completion
Suggests:       %{name}-fish-completion
Suggests:       %{name}-zsh-completion

%description
doggo is a modern command-line DNS client (like dig) implemented in Go.
It outputs information in a neat concise manner and supports protocols
like DoH, DoT, DoQ, and DNSCrypt as well.

%package web
Summary:        Web UI for %{name}
Group:          Productivity/Networking/DNS/Utilities
Supplements:    %{name}

%description web
HTTP server for %{name} that provides a web browser UI for making DNS queries

%package bash-completion
Summary:        bash completion for %{name}
Group:          System/Shells
Supplements:    (%{name} and bash)
BuildArch:      noarch

%description bash-completion
bash completion scripts for %{name}

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
# build separate binary providing web interface
go build -o %{name}-web ./web/

%install
install -d %{buildroot}%{_bindir}
install -D %{name} %{buildroot}%{_bindir}/%{name}
install -D %{name} %{buildroot}%{_bindir}/%{name}-web

# Completions
./%{name} completions bash > %{name}.bash
install -Dm644 %{name}.bash %{buildroot}%{_datadir}/bash-completions/completions/%{name}
./%{name} completions fish > %{name}.fish
install -Dm644 %{name}.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/%{name}.fish
./%{name} completions zsh > %{name}.zsh
install -Dm644 %{name}.zsh %{buildroot}%{_datadir}/zsh/site-functions/_%{name}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%files web
%doc config-api-sample.toml
%{_bindir}/%{name}-web

%files fish-completion
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/%{name}.fish

%files zsh-completion
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_%{name}

%files bash-completion
%dir %{_datadir}/bash-completions
%dir %{_datadir}/bash-completions/completions
%{_datadir}/bash-completions/completions/%{name}

%changelog
