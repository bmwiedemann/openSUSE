#
# spec file for package go-containerregistry
#
# Copyright (c) 2022 SUSE LLC
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
# nodebuginfo


%global goipath github.com/google/go-containerregistry
Name:           go-containerregistry
Version:        0.12.0
Release:        0
Summary:        Container Library and tools for working with container registries
License:        Apache-2.0
Group:          System/Management
URL:            https://github.com/google/go-containerregistry
Source:         https://github.com/google/go-containerregistry/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang-packaging
BuildRequires:  golang(API) = 1.17
Conflicts:      distribution-registry

%description
This is a golang library for working with container registries.

%package -n crane
Summary:        CLI tool for interacting with remote images and registries
Group:          System/Management

%description -n crane
Useful tips and things you can do with crane and other standard tools.

List files in an image
crane export registry.opensuse.org/opensuse/tumbleweed - | tar -tvf - | less

Export a file from an image
crane export registry.opensuse.org/opensuse/tumbleweed -  | tar -0xf - etc/passwd

Diff two configs
diff -u <(crane config busybox:1.32 | jq) <(crane config busybox:1.33 | jq)

Diff two manifests
diff -u <(crane manifest busybox:1.32 | jq) <(crane manifest busybox:1.33 | jq)

Diff filesystem contents
diff -u \
   <(crane export gcr.io/kaniko-project/executor:v1.6.0-debug - | tar -tvf - | sort) \
   <(crane export gcr.io/kaniko-project/executor:v1.7.0-debug - | tar -tvf - | sort)

%package -n gcrane
Summary:        GCR-specific variant of crane
Group:          System/Management

%description -n gcrane
crane is a GCR-specific variant of crane that has richer output for the ls
subcommand and some basic garbage collection support.

%prep
%setup -qa1
%autopatch -p1

%build
%{goprep} %{goipath}

export CGO_ENABLED=0

%{gobuild} -mod vendor ./...

%install
%{goinstall}
# "only one tool per thing" SLE15 policy conflicts
%if 0%{?suse_version} && %{?suse_version} < 1550
rm -v %{buildroot}/%{_bindir}/{registry,help}
%endif

%if %{?suse_version} > 1500
%files
%license LICENSE
%doc README.md
%{_bindir}/registry
%exclude %{_bindir}/help
%endif

%files -n crane
%license LICENSE
%{_bindir}/crane

%files -n gcrane
%license LICENSE
%{_bindir}/gcrane

%changelog
