#
# spec file for package k8s-sidecar
#
# Copyright (c) 2021 SUSE LLC
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


%define import_path github.com/kiwigrid/k8s-sidecar

Name:           k8s-sidecar
Version:        0.1.144
Release:        0
Summary:        Collect kubernetes cluster configmaps and store it
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/kiwigrid/k8s-sidecar
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       python3
Requires:       python3-kubernetes
Requires:       python3-requests

%description
Collect kubernetes cluster configmaps with a specified label and store the included files in an local folder.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{_datadir}/%{name}
for file in $(find sidecar/*.py -type f); do
  install -D -m 0644 $file %{buildroot}%{_datadir}/%{name}/$file
done

%files
%defattr(-,root,root)
%doc README.md
%license LICENSE
%{_datadir}/%{name}

%changelog
