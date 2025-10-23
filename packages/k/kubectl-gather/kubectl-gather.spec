#
# spec file for package kubectl-gather
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           kubectl-gather
Version:        0.11.0
Release:        0
Summary:        Kubectl plugin to gather data about your cluster
License:        Apache-2.0
URL:            https://github.com/nirs/kubectl-gather
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang(API) >= 1.25

%description
This is a kubectl plugin for gathering data about your cluster that may help to
debug issues.

Kubernetes is big and complicated, and when something breaks it is hard to tell
which info is needed for debugging. Even if you known which resources or logs
are needed, it is hard to get the data manually. When working with multiple
related clusters gathering the right data from the right cluster is even
harder.

The kubectl gather tool makes it easy to gather data quickly from multiple
clusters with a single command. It gathers all resources from all clusters. It
also gather related data such as pods logs, on for specific cases, external
logs stored on the nodes. The data is stored in a local directory, one file per
resource, making it easy to navigate and inspect using standard tools. If you
know what you want to gather, it is much faster and consume fraction of the
storage to gather only specific namespaces from all clusters.

%package -n %{name}-bash-completion
Summary:        Bash Completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description -n %{name}-bash-completion
Bash command line completion support for %{name}.

%prep
%autosetup -p 1 -a 1

%build
go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags=" \
   -X github.com/nirs/kubectl-gather/pkg/gather.Image=quay.io/nirsof/gather:v%{version} \
   -X github.com/nirs/kubectl-gather/pkg/gather.Version=v%{version}" \
   -o bin/%{name}

%install
# Install the binary.
install -D -m 0755 bin/%{name} %{buildroot}/%{_bindir}/%{name}

# bash completion script
install -D -m 0755 kubectl_complete-gather %{buildroot}/%{_bindir}/kubectl_complete-gather

%check
%{buildroot}/%{_bindir}/%{name} --version | grep v%{version}

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%files -n %{name}-bash-completion
%{_bindir}/kubectl_complete-gather

%changelog
