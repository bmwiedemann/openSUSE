#
# spec file for package kompose
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


Name:           kompose
Version:        1.34.0
Release:        0
Summary:        Go from Docker Compose to Kubernetes
License:        Apache-2.0
Group:          Development/Tools/Other
URL:            https://kompose.io
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  golang-packaging
BuildRequires:  golang(API) >= 1.22
# necessary for SLE15, Leap 15, Tumbleweed and some archs (no problem for other releases as well)
BuildRequires:  python3-PyYAML
#!BuildIgnore:  python2-PyYAML

%description
kompose is a tool to help users who are familiar with docker-compose move to Kubernetes. kompose takes a Docker Compose file and translates it into Kubernetes resources. kompose is a convenience tool to go from local Docker development to managing your application with Kubernetes. Transformation of the Docker Compose format to Kubernetes resources manifest may not be exact, but it helps tremendously when first deploying an application on Kubernetes.

%package bash-completion
Summary:        Bash Completion for %{name}
Group:          System/Shells
Requires:       bash-completion
Supplements:    (%{name} and bash)
BuildArch:      noarch

%description bash-completion
The official bash completion script for %{name}, generated during the build.

%prep
%autosetup -a 1

%build
%ifarch ppc64
go build \
   -mod=vendor \
   -tags extended
%else
go build \
   -mod=vendor \
   -tags extended \
   -buildmode=pie
%endif

%install
# Install the binary.
install -D -m 0755 %{name} "%{buildroot}/%{_bindir}/%{name}"

# Build the bash autocomplete file
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions/
%{buildroot}/%{_bindir}/%{name} completion bash > %{name}-autocomplete.sh

# Install the bash autocomplete file
install -Dm 644 %{name}-autocomplete.sh %{buildroot}%{_datadir}/bash-completion/completions/%{name}

%check

%files
%{_bindir}/%{name}
%license LICENSE
%doc README.md

%files bash-completion
%{_datadir}/bash-completion

%changelog
