#
# spec file for package hello-kubic
#
# Copyright (c) 2017, 2019 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           hello-kubic
Version:        1.0
Release:        0
Summary:        A mini webserver showing a hello kubic page
License:        Apache-2.0
Group:          System/Management
Url:            https://github.com/thkukuk/hello-kubic
Source:         %{name}-%{version}.tar.xz
BuildRequires:  golang-packaging
BuildRequires:  golang(API) >= 1.12
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExcludeArch:    s390 %ix86

%description
hello-kubic is a mini webserver with a "Hello Kubic" webpage
containing some informations about the running system, container
or pod.

%package k8s-yaml
Summary:        Kubernetes yaml file to run hello-kubic container
Group:          System/Management
BuildArch:      noarch

%description k8s-yaml
This package contains the yaml file requried to download and run the
hello-kubic container in a kubernetes cluster.

hello-kubic is a mini webserver with a "Hello Kubic" webpage
containing some informations about the running pod.

%prep
%setup -q

%build
make build

%install
mkdir -p %{buildroot}%{_bindir}
install -m 0755 bin/hello-kubic %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/hello-kubic
cp -av webpage/* %{buildroot}%{_datadir}/hello-kubic/

# Install provided yaml file to download and run the hello-kubic container
mkdir -p %{buildroot}%{_datadir}/k8s-yaml/hello-kubic
install -m 0644 yaml/hello-kubic.yaml %{buildroot}%{_datadir}/k8s-yaml/hello-kubic/hello-kubic.yaml

%files
%defattr(-,root,root)
%license LICENSE
%{_bindir}/hello-kubic
%{_datadir}/hello-kubic

%files k8s-yaml
%dir %{_datarootdir}/k8s-yaml
%dir %{_datarootdir}/k8s-yaml/hello-kubic
%{_datarootdir}/k8s-yaml/hello-kubic/hello-kubic.yaml

%changelog
