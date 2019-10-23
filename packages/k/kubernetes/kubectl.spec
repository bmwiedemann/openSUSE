#
# spec file for package kubectl
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%{!?tmpfiles_create:%global tmpfiles_create systemd-tmpfiles --create}
# baseversion - version of kubernetes for this package
%define baseversion 1.16
Name:           kubectl
Version:        %{baseversion}.2
Release:        0
Summary:        Kubectl (Kubernetes client tools)
License:        Apache-2.0
Group:          System/Management
URL:            http://kubernetes.io
Source:         kubernetes-%{version}.tar.xz
Source2:        genmanpages.sh
Source28:       kubernetes.obsinfo
Source30:       kubectl-rpmlintrc
BuildRequires:  bash-completion
BuildRequires:  fdupes
BuildRequires:  git
BuildRequires:  go-go-md2man
# Kubernetes 1.16.1 requires at least go 1.12.10 (see changelog)
BuildRequires:  golang(API) = 1.12
BuildRequires:  go >= 1.12.10
BuildRequires:  golang(github.com/jteeuwen/go-bindata)
BuildRequires:  golang-packaging
BuildRequires:  rsync
BuildRequires:  systemd-rpm-macros
Requires:       bash-completion
# Conflict with kubernetes-client which already provides kubectl but as a link
# to hyperkube, provided by kubernetes-common
Conflicts:      kubernetes-client
ExcludeArch:    %{ix86} s390
%{go_nostrip}
%{go_provides}

%description
Kubectl (Kubernetes client tool). This package contains only the kubectl tool so
it can be distributed and installed without any other kubernetes package.

It groups containers that make up an application into logical units
for management and discovery.

%prep
%setup -q -n kubernetes-%{version}
%{goprep} github.com/kubernetes/kubernetes

%build
# This is fixing bug bsc#1065972
export KUBE_GIT_COMMIT=$(grep "commit:" %{SOURCE28} | cut -d ":" -f2 | tr -d " ")
# KUBE_GIT_TREE_STATE="clean" indicates no changes since the git commit id
# KUBE_GIT_TREE_STATE="dirty" indicates source code changes after the git commit id
export KUBE_GIT_TREE_STATE="clean"
export KUBE_GIT_VERSION=v%{version}

# https://bugzilla.redhat.com/show_bug.cgi?id=1392922#c1
%ifarch ppc64le
export GOLDFLAGS='-linkmode=external'
%endif
make %{?_smp_mflags} WHAT="cmd/hyperkube cmd/kubeadm test/e2e/e2e.test"
make %{?_smp_mflags} ginkgo

# The majority of the documentation has already been moved into
# http://kubernetes.io/docs/admin, and most of the files stored in the `docs`
# directory simply point there. That being said, some of the files are actual
# man pages, but they have to be generated with `hack/generate-docs.sh`. So,
# let's do that and run `genmanpages.sh`.
./hack/generate-docs.sh || true
pushd docs
cp %{SOURCE2} genmanpages.sh
bash genmanpages.sh
popd

%install

%ifarch ppc64le aarch64
output_path="_output/local/go/bin"
%else
output_path="_output/local/bin/linux/%{go_arch}"
%endif

install -m 755 -d %{buildroot}%{_bindir}

cp ${output_path}/hyperkube %{buildroot}%{_bindir}/kubectl

# install the bash completion
install -d -m 0755 %{buildroot}%{_datadir}/bash-completion/completions/
%{buildroot}%{_bindir}/kubectl completion bash > %{buildroot}%{_datadir}/bash-completion/completions/kubectl

# cleanup before copying dirs...
rm -f hack/.linted_packages
find .    -name '.gitignore' -type f -delete
find hack -name '*.sh.orig' -type f -delete
find hack -name '.golint_*' -type f -delete

# install manpages
install -d %{buildroot}%{_mandir}/man1
install -p -m 644 docs/man/man1/kubectl* %{buildroot}%{_mandir}/man1
%fdupes -s %{buildroot}

%files
%doc README.md CONTRIBUTING.md
%license LICENSE
%{_mandir}/man1/kubectl.1%{?ext_man}
%{_mandir}/man1/kubectl-*
%{_bindir}/kubectl
%{_datadir}/bash-completion/completions/kubectl

%changelog
