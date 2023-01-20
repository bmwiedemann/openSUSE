#
# spec file for package mirror-registry
#
# Copyright (c) 2023 SUSE LLC
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


Name:           mirror-registry
Version:        1.3
Release:        0
Summary:        Tool helping to mirror a registry to a private one
License:        Apache-2.0
URL:            https://github.com/thkukuk/mirror-registry
Source:         %{name}-%{version}.tar.xz
Requires:       skopeo >= 0.1.39
BuildRequires:  golang(API) >= 1.18
ExcludeArch:    s390 %{ix86}

%description
mirror-registry will analyse a remote registry and create a yaml file with all containers and tags matching a regex to sync with skopeo to a private registry. While this tool understands the architecture flag for containers, skopeo does not really use this information yet. If a repository contains multi-arch containers, it will fail if there is no container for the architecture it is running on, else it will use the architecture which it is running on.

%prep
%setup -q

%build
make build

%install
install -d -p %{buildroot}%{_bindir}
install -p -m 0755 bin/mirror-registry %{buildroot}%{_bindir}

%files
%license LICENSE
%doc README.md
%{_bindir}/mirror-registry

%changelog
