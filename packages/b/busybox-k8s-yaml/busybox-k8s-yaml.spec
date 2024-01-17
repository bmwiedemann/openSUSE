#
# spec file for package busybox-k8s-yaml
#
# Copyright (c) 2020 SUSE LLC
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


Name:           busybox-k8s-yaml
Version:        1.0
Release:        0
Summary:        K8s yaml file to deploy busybox
License:        MIT
Source0:        busybox.yaml
Source1:        LICENSE
BuildArch:      noarch

%description
K8s yaml file to deploy busybox on a kubernetes cluster.

%prep

%build
cp %{SOURCE1} .

%install
mkdir -p %{buildroot}%{_datadir}/k8s-yaml/busybox
install -m 644 %{SOURCE0} %{buildroot}%{_datadir}/k8s-yaml/busybox/

%files
%dir %{_datadir}/k8s-yaml
%{_datadir}/k8s-yaml/busybox
%license LICENSE

%changelog
