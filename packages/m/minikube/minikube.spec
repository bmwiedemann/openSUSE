#
# spec file for package minikube
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           minikube
Version:        1.38.1
Release:        0
Summary:        Tool to run Kubernetes locally
License:        Apache-2.0
Group:          System/Management
URL:            https://github.com/kubernetes/minikube
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  bash-completion
BuildRequires:  fdupes
BuildRequires:  fish
BuildRequires:  git-core
BuildRequires:  libvirt-devel >= 1.2.14
BuildRequires:  zsh
BuildRequires:  zstd
BuildRequires:  golang(API) = 1.25
Recommends:     docker-machine-driver-kvm2
Recommends:     kubernetes-client
Recommends:     libvirt
Recommends:     libvirt-daemon-qemu
Recommends:     qemu-kvm
Recommends:     socat
ExcludeArch:    ppc64le s390x

# 1.38.0 removed the docker-machine-driver-kvm2 driver
Obsoletes:      docker-machine-driver-kvm2 < %{version}

%description
Minikube is a tool that allows running Kubernetes locally. Minikube
runs a single-node Kubernetes cluster inside a VM on your machine for
users looking to try out Kubernetes or develop with it day-to-day.

%package        bash-completion
Summary:        Minikube bash completion
Group:          System/Management
Requires:       bash
Requires:       bash-completion
Requires:       minikube = %{version}
Supplements:    (minikube and bash)
BuildArch:      noarch

%description    bash-completion
Optional bash completion for minikube.

%package        fish-completion
Summary:        Minikube fish completion
Group:          System/Management
Requires:       fish
Requires:       minikube = %{version}
Supplements:    (minikube and fish)
BuildArch:      noarch

%description    fish-completion
Optional fish completion for minikube.

%package        zsh-completion
Summary:        Minikube zsh completion
Group:          System/Management
Requires:       minikube = %{version}
Requires:       zsh
Supplements:    (minikube and zsh)
BuildArch:      noarch

%description    zsh-completion
Optional zsh completion for minikube.

%prep
%autosetup -p 1 -a 1

%build
export GOFLAGS="-buildmode=pie"
export GO_VERSION="$(go version | awk '{print $3}' | sed 's/go//g')"
%make_build out/minikube

%install
install -m 755 -d %{buildroot}%{_bindir}
install -p -m 755 -t %{buildroot}%{_bindir} out/minikube

%fdupes %{buildroot}%{_bindir}

# create the bash completion file
mkdir -p %{buildroot}%{_datarootdir}/bash-completion/completions/
%{buildroot}/%{_bindir}/%{name} completion bash > %{buildroot}%{_datarootdir}/bash-completion/completions/%{name}

# create the fish completion file
mkdir -p %{buildroot}%{_datarootdir}/fish/vendor_completions.d/
%{buildroot}/%{_bindir}/%{name} completion fish > %{buildroot}%{_datarootdir}/fish/vendor_completions.d/%{name}.fish

# create the zsh completion file
mkdir -p %{buildroot}%{_datarootdir}/zsh/site-functions/
%{buildroot}/%{_bindir}/%{name} completion zsh > %{buildroot}%{_datarootdir}/zsh/site-functions/_%{name}

%check
%{buildroot}/%{_bindir}/%{name} version
%{buildroot}/%{_bindir}/%{name} version | grep v%{version}

%files
%license LICENSE
%doc CHANGELOG.md CONTRIBUTING.md README.md
%{_bindir}/minikube

%files -n %{name}-bash-completion
%{_datadir}/bash-completion/completions/%{name}

%files -n %{name}-fish-completion
%{_datarootdir}/fish/vendor_completions.d/%{name}.fish

%files -n %{name}-zsh-completion
%{_datarootdir}/zsh/site-functions/_%{name}

%changelog
