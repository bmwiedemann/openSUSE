#
# spec file for package minikube
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


Name:           minikube
Version:        1.33.1
Release:        0
Summary:        Tool to run Kubernetes locally
License:        Apache-2.0
Group:          System/Management
URL:            https://github.com/kubernetes/minikube
Source0:        https://github.com/kubernetes/minikube/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
Source2:        %{name}-rpmlintrc
BuildRequires:  git-core
BuildRequires:  golang-github-jteeuwen-go-bindata
BuildRequires:  golang-packaging
BuildRequires:  libvirt-devel >= 1.2.14
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  wget
BuildRequires:  zstd
BuildRequires:  golang(API) = 1.22
Recommends:     docker-machine-driver-kvm2
Recommends:     kubernetes-client
Recommends:     libvirt
Recommends:     libvirt-daemon-qemu
Recommends:     qemu-kvm
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
BuildRequires:  bash
BuildRequires:  bash-completion
Requires:       bash
Requires:       bash-completion
Requires:       minikube = %{version}
Supplements:    (minikube and bash)
BuildArch:      noarch

%description    bash-completion
Optional bash completion for minikube.

%prep
%autosetup
tar -xf %{SOURCE1}
sed -i -e "s|GO111MODULE := on|GO111MODULE := off|" Makefile

%build
%{goprep} k8s.io/minikube
export GOPATH=%{_builddir}/go
cd $GOPATH/src/k8s.io/minikube
mkdir $GOPATH/bin
ln -s %{_bindir}/go-bindata $GOPATH/bin/go-bindata
export IN_DOCKER=0
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
git init
echo '*' > .gitignore
touch .dummy
git add -f .dummy .gitignore
d=$(date "-d@${SOURCE_DATE_EPOCH:-$(date +%%s)}" +"%%Y-%%m-%%d %%H:%%M:%%S")
GIT_COMMITTER_DATE="$d" git commit --date="$d" -m "trick hack/get_k8s_version.py"
%make_build out/minikube
%ifnarch i586
%ifarch aarch64
%make_build out/docker-machine-driver-kvm2-arm64
%else
%make_build out/docker-machine-driver-kvm2
%endif
%endif

%{_builddir}/go/src/k8s.io/minikube/out/%{name} completion bash > %{_builddir}/%{name}-bash-completions

%install
output_path="%{_builddir}/go/src/k8s.io/minikube/out/"
binaries=(minikube)
install -m 755 -d %{buildroot}%{_bindir}
install -p -m 755 -t %{buildroot}%{_bindir} ${output_path}/minikube
%ifnarch i586
install -p -m 755 -t %{buildroot}%{_bindir} ${output_path}/docker-machine-driver-kvm2*
%ifarch aarch64
# Add a symlink without '-arm64' suffix
pushd %{buildroot}%{_bindir}
ln -s docker-machine-driver-kvm2* docker-machine-driver-kvm2
popd
%endif
%endif

install -D -m 0644 %{_builddir}/%{name}-bash-completions \
    %{buildroot}%{_datadir}/bash-completion/completions/%{name}

%files
%license LICENSE
%doc CHANGELOG.md CONTRIBUTING.md README.md
%{_bindir}/minikube

%ifnarch i586
%files -n docker-machine-driver-kvm2
%license LICENSE
%{_bindir}/docker-machine-driver-kvm2*
%endif

%files bash-completion
%{_datadir}/bash-completion/completions/%{name}

%changelog
