#
# spec file for package kompose
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


Name:           kompose
Version:        1.19.0
Release:        0
Summary:        Go from Docker Compose to Kubernetes
License:        Apache-2.0
Group:          Development/Tools/Other
URL:            http://kompose.io
Source0:        %{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM kompose-make-pie.patch sweiberg@suse.com -- use pie to fix lint-warning
Patch1:         kompose-make-pie.patch
BuildRequires:  git
BuildRequires:  go >= 1.6
BuildRequires:  make
# necessary for SLE15, Leap 15, Tumbleweed and some archs (no problem for other releases as well)
BuildRequires:  python3-PyYAML
#!BuildIgnore:  python2-PyYAML

%define GONS github.com/kubernetes
%define SRCDIR src/%{GONS}/%{name}

%description
kompose is a tool to help users who are familiar with docker-compose move to Kubernetes. kompose takes a Docker Compose file and translates it into Kubernetes resources. kompose is a convenience tool to go from local Docker development to managing your application with Kubernetes. Transformation of the Docker Compose format to Kubernetes resources manifest may not be exact, but it helps tremendously when first deploying an application on Kubernetes.

%prep
%setup -q
%patch1 -p1
mkdir -p %{SRCDIR}
cd %{SRCDIR}
tar xf %{S:0} --strip 1

%build
export GOPATH=$(pwd)
make %{?_smp_mflags} bin

%install
mkdir -p %{buildroot}/%{_bindir}
install -m 0755 %{name} %{buildroot}/%{_bindir}/

%post
%postun

%files
%{_bindir}/%{name}
%license LICENSE
%doc CHANGELOG.md README.md

%changelog
