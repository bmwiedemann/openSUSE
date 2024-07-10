#
# spec file for package opentofu
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


%define executable_name tofu

Name:           opentofu
Version:        1.7.3
Release:        0
Summary:        Declaratively manage your cloud infrastructure
License:        MPL-2.0
Group:          System/Management
URL:            https://github.com/opentofu/opentofu
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
Source99:       opentofu-rpmlintrc
BuildRequires:  bash-completion
BuildRequires:  golang-packaging
BuildRequires:  golang(API) >= 1.21
# See: https://github.com/hashicorp/opentofu/issues/22807
ExcludeArch:    %{ix86} %{arm}

%description
Fork of Terraform

OpenTofu is an OSS tool for building, changing, and versioning infrastructure safely and efficiently. OpenTofu can manage existing and popular service providers as well as custom in-house solutions.

The key features of OpenTofu are:
- Infrastructure as Code: Infrastructure is described using a high-level configuration syntax. This allows a blueprint of your datacenter to be versioned and treated as you would any other code. Additionally, infrastructure can be shared and re-used.
- Execution Plans: OpenTofu has a "planning" step where it generates an execution plan. The execution plan shows what OpenTofu will do when you call apply. This lets you avoid any surprises when OpenTofu manipulates infrastructure.
- Resource Graph: OpenTofu builds a graph of all your resources, and parallelizes the creation and modification of any non-dependent resources. Because of this, OpenTofu builds infrastructure as efficiently as possible, and operators get insight into dependencies in their infrastructure.
- Change Automation: Complex changesets can be applied to your infrastructure with minimal human interaction. With the previously mentioned execution plan and resource graph, you know exactly what OpenTofu will change and in what order, avoiding many possible human errors.

%prep
%autosetup -p 1 -a 1

%build
go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags "-w -s -X github.com/opentofu/opentofu/version.dev=no -X github.com/opentofu/opentofu/version.Version=%{version}" \
   -o bin/%{executable_name} ./cmd/tofu

%install
# Install the binary.
install -D -m 0755 bin/%{executable_name} "%{buildroot}/%{_bindir}/%{executable_name}"
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions/
cat > %{buildroot}%{_datadir}/bash-completion/completions/%{executable_name} <<EOF
complete -C %{_bindir}/%{executable_name} %{executable_name}
EOF

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/%{executable_name}
%{_datadir}/bash-completion/completions/%{executable_name}

%changelog
