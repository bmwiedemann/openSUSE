#
# spec file for package kubectx
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


Name:           kubectx
Version:        0.9.5
Release:        0
Summary:        Faster way to switch between clusters and namespaces in kubectl
License:        Apache-2.0
URL:            https://github.com/ahmetb/kubectx
Source:         kubectx-%{version}.tar.gz
BuildRequires:  go >= 1.13
BuildArch:      noarch

%description
kubectx is a utility to manage and switch between kubectl(1) contexts.

%prep
%setup -q

%build
sed -i '/^#!/ s/env\ bash/bash/' %{name}

%install
# Install the script.
install -D -m 0755 %{name} "%{buildroot}/%{_bindir}/%{name}"

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
