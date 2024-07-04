#
# spec file for package istioctl
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


%define __arch_install_post export NO_BRP_STRIP_DEBUG=true

Name:           istioctl
Version:        1.22.2
Release:        0
Summary:        CLI for the istio servic mesh in Kubernetes
License:        Apache-2.0
URL:            https://github.com/istio/istio
Source:         istio-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  fdupes
BuildRequires:  go >= 1.22

%description
The istioctl tool is a configuration command line utility that allows service operators to debug and diagnose their Istio service mesh deployments. The Istio project also includes two helpful scripts for istioctl that enable auto-completion for Bash and ZSH. Both of these scripts provide support for the currently available istioctl commands.

%package -n %{name}-bash-completion
Summary:        Bash Completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description -n %{name}-bash-completion
Bash command line completion support for %{name}.

%package -n %{name}-zsh-completion
Summary:        Zsh Completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description -n %{name}-zsh-completion
zsh command line completion support for %{name}.

%prep
%setup -q -n istio-%{version}
%setup -q -T -D -a1 -n istio-%{version}

%build
go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags="-X istio.io/pkg/version.buildVersion=%{version} -X istio.io/pkg/version.buildArch=${GOARCH} -X istio.io/pkg/version.buildOS=linux" \
   -o bin/%{name} ./istioctl/cmd/istioctl

%install
# Install the binary.
install -D -m 0755 bin/%{name} "%{buildroot}/%{_bindir}/%{name}"

# copy the sample files
mkdir -p %{buildroot}%{_docdir}/%{name}
cp -vr samples %{buildroot}%{_docdir}/%{name}
rm -f %{buildroot}%{_docdir}/%{name}/samples/bookinfo/src/reviews/.gitignore
rm -f %{buildroot}%{_docdir}/%{name}/samples/bookinfo/src/reviews/reviews-wlpcfg/shared/.gitkeep
rm -f %{buildroot}%{_docdir}/%{name}/samples/wasm_modules/header_injector/.gitignore
%fdupes %{buildroot}%{_docdir}/%{name}/samples/

# create the bash completion file
mkdir -p %{buildroot}%{_datarootdir}/bash-completion/completions
%{buildroot}/%{_bindir}/%{name} completion bash > %{buildroot}%{_datarootdir}/bash-completion/completions/%{name}

# create the zsh completion file
mkdir -p %{buildroot}%{_datarootdir}/zsh_completion.d
%{buildroot}/%{_bindir}/%{name} completion zsh > %{buildroot}%{_datarootdir}/zsh_completion.d/_%{name}

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_docdir}/%{name}

%files -n %{name}-bash-completion
%dir %{_datarootdir}/bash-completion/completions/
%{_datarootdir}/bash-completion/completions/%{name}

%files -n %{name}-zsh-completion
%defattr(-,root,root)
%dir %{_datarootdir}/zsh_completion.d/
%{_datarootdir}/zsh_completion.d/_%{name}

%changelog
