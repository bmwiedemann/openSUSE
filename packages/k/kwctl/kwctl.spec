#
# spec file for package kwctl
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


Name:           kwctl
Version:        1.30.0
Release:        0
Summary:        The go-to CLI tool for Kubewarden users
License:        Apache-2.0
URL:            https://kubewarden.io/
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
BuildRequires:  cargo >= 1.74
BuildRequires:  zstd
ExclusiveArch:  %{rust_tier1_arches}

%description
kwctl is the go-to CLI tool for Kubewarden users.

Think of it as the docker CLI tool if you were working with containers.

As a policy author
- e2e testing of your policy. Test your policy against crafted Kubernetes
  requests, and ensure your policy behaves as you expect. You can even test
  context-aware policies, that require access to a running cluster.
- Embed metadata in your Wasm module, so the binary is annotated with the
  permissions it needs to execute.
- Publish policies to OCI registries.
- Generate initial ClusterAdmissionPolicy scaffolding for your policy.

As a cluster administrator
- Inspect remote policies. Given a policy in an OCI registry, or in an HTTP
  server, show all static information about the policy.
- Dry-run of a policy in your cluster. Test the policy against crafted
  Kubernetes requests, and ensure the policy behaves as you expect given the
  input data you provide. You can even test context-aware policies, that
  require access to a running cluster, also in a dry-run mode.
- Generate ClusterAdmissionPolicy scaffolding for a given policy.

%prep
%autosetup -p1 -a1

%build
%{cargo_build}

%install
install -D -m 0755 target/release/%{name} %{buildroot}%{_bindir}/%{name}

%check

%files
%license LICENSE
%doc README.md

%{_bindir}/%{name}

%changelog
