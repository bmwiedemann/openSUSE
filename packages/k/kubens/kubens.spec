#
# spec file for package kubens
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


Name:           kubens
Version:        0.9.4
Release:        0
Summary:        Faster way to switch between clusters and namespaces in kubectl
License:        Apache-2.0
URL:            https://github.com/ahmetb/kubectx
Source:         kubectx-%{version}.tar.gz
BuildArch:      noarch

%description
kubens is a utility to switch between Kubernetes namespaces.

USAGE:
  kubens                    : list the namespaces
  kubens <NAME>             : change the active namespace
  kubens -                  : switch to the previous namespace
  kubens -c, --current      : show the current namespace

%prep
%setup -q -n kubectx-%{version}

%build
sed -i '/^#!/ s/env\ bash/bash/' %{name}

%install
# Install the script.
install -D -m 0755 %{name} "%{buildroot}/%{_bindir}/%{name}"

%files
%defattr(-,root,root)
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
