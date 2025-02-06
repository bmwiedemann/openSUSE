#
# spec file for package minikube
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


Name:           minikube
Version:        1.35.0
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
BuildRequires:  golang(API) = 1.23
Recommends:     docker-machine-driver-kvm2
Recommends:     kubernetes-client
Recommends:     libvirt
Recommends:     libvirt-daemon-qemu
Recommends:     qemu-kvm
Recommends:     socat
ExcludeArch:    ppc64le s390x

%description
Minikube is a tool that allows running Kubernetes locally. Minikube
runs a single-node Kubernetes cluster inside a VM on your machine for
users looking to try out Kubernetes or develop with it day-to-day.

# vendor/github.com/libvirt/libvirt-go/domain_events.go:334: type [1073741824]_Ctype_struct__virDomainEventGraphicsSubjectIdentity too large
%ifnarch i586 %{arm}
%package -n docker-machine-driver-kvm2
Summary:        KVM driver for docker-machine
Group:          System/Management

%description -n docker-machine-driver-kvm2
KVM driver for docker-machine which is using libvirt for setting up
virtual machines with Docker.
%endif

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
%make_build out/minikube
%ifnarch i586
%ifarch aarch64
# do not use make, as it would skip due to
# https://github.com/kubernetes/minikube/issues/19959
go build \
	-buildvcs=false \
	-installsuffix "static" \
	-ldflags="-X k8s.io/minikube/pkg/drivers/kvm.version=v%{version} -X k8s.io/minikube/pkg/drivers/kvm.gitCommitID=v%{version}" \
	-tags "libvirt_without_lxc" \
	-o out/docker-machine-driver-kvm2-arm64 k8s.io/minikube/cmd/drivers/kvm
%else
%make_build out/docker-machine-driver-kvm2
%endif
%endif

%install
install -m 755 -d %{buildroot}%{_bindir}
install -p -m 755 -t %{buildroot}%{_bindir} out/minikube
%ifnarch i586
install -p -m 755 -t %{buildroot}%{_bindir} out/docker-machine-driver-kvm2*
%ifarch aarch64
# Add a symlink without '-arm64' suffix
pushd %{buildroot}%{_bindir}
ln -s docker-machine-driver-kvm2* docker-machine-driver-kvm2
popd
%endif
%endif

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
%{buildroot}/%{_bindir}/%{name} version | grep v%{version}

%files
%license LICENSE
%doc CHANGELOG.md CONTRIBUTING.md README.md
%{_bindir}/minikube

%ifnarch i586
%files -n docker-machine-driver-kvm2
%license LICENSE
%{_bindir}/docker-machine-driver-kvm2*
%endif

%files -n %{name}-bash-completion
%{_datadir}/bash-completion/completions/%{name}

%files -n %{name}-fish-completion
%{_datarootdir}/fish/vendor_completions.d/%{name}.fish

%files -n %{name}-zsh-completion
%{_datarootdir}/zsh/site-functions/_%{name}

%changelog
