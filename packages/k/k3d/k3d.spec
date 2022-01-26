# spec file for package k3d
#
# Copyright (c) 2021 Orville Q. Song <orville@anislet.dev>
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

%global k3s_tag     v1.21.7-k3s1

%global provider        github
%global provider_tld    com
%global project         rancher
%global repo            k3d
%global provider_prefix %{provider}.%{provider_tld}/%{project}
%global import_path     %{provider_prefix}/%{repo}

Name:           k3d
Version:        5.2.2
Release:        0
Summary:        Little helper to run Rancher Lab's k3s in Docker
License:        MIT
Group:          System/Management
URL:            https://github.com/rancher/k3d
Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}-vendor.tar.xz
BuildRequires:  golang-packaging
BuildRequires:  golang(API) >= 1.16

%description
k3d is a little helper to run Rancher Lab's k3s in Docker.

%package bash-completion
Summary:        Bash completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Supplements:    (%{name} and bash)
BuildArch:      noarch

%description bash-completion
Bash command line completion support for %{name}.

%package fish-completion
Summary:        Fish completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Supplements:    (%{name} and fish)
BuildArch:      noarch

%description fish-completion
Fish command line completion support for %{name}.

%package zsh-completion
Summary:        Zsh completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
Zsh command line completion support for %{name}.

%{go_nostrip}
%{go_provides}

%prep
%setup -q -n %{name}-%{version}
%setup -a1 %{SOURCE1}

%build
%goprep .
mkdir -p vendor/%{provider_prefix}
ln -s . vendor/%{import_path}
%gobuild -ldflags "-s -w -X github.com/rancher/k3d/v5/version.Version=v%{version} -X github.com/rancher/k3d/v5/version.K3sVersion=%{k3s_tag}" .

# Generate completion files
go run -v -p 4 -x -mod=vendor . completion bash > %{name}.bash
go run -v -p 4 -x -mod=vendor . completion zsh > %{name}.zsh
go run -v -p 4 -x -mod=vendor . completion fish > %{name}.fish

%install
%goinstall

# Install comletion files
install -D -m0644 %{name}.zsh %{buildroot}%{_datadir}/zsh/site-functions/_%{name}
install -D -m0644 %{name}.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/%{name}.fish
install -D -m0644 %{name}.bash %{buildroot}%{_datadir}/bash-completion/completions/%{name}

%files
%defattr(-,root,root)
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%files bash-completion
%dir %{_datadir}/bash-completion/
%{_datadir}/bash-completion/completions/

%files fish-completion
%dir %{_datadir}/fish/
%{_datadir}/fish/vendor_completions.d/

%files zsh-completion
%dir %{_datadir}/zsh/
%{_datadir}/zsh/site-functions/

%changelog
