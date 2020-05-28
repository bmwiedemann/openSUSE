#
# spec file for package kube-prometheus
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


Name:           kube-prometheus
Version:        0.4.0+git20200520.28332b4
Release:        0
Summary:        Manifests to use Prometheus to monitor Kubernetes
License:        Apache-2.0
URL:            https://github.com/coreos/kube-prometheus
Source0:        kube-prometheus-%{version}.tar.xz
Source1:        vendor.tar.xz
Source2:        update-vendor.sh
Source3:        kubic.jsonnet
BuildRequires:  gojsontoyaml
BuildRequires:  jsonnet
BuildArch:      noarch

%description
This repository collects Kubernetes manifests, Grafana dashboards, and Prometheus rules combined with documentation and scripts to provide easy to operate end-to-end Kubernetes cluster monitoring with Prometheus using the Prometheus Operator.

%package k8s-yaml
Summary:        Yaml file to deploy Prometheus to monitor Kubernetes

%description k8s-yaml
This package collects Kubernetes manifests, Grafana dashboards, and Prometheus rules combined with documentation and scripts to provide easy to operate end-to-end Kubernetes cluster monitoring with Prometheus using the Prometheus Operator.

To deploy:
# Create the namespace and CRDs, and then wait for them to be availble before creating the remaining resources
kubectl create -f %{_datadir}/k8s-yaml/kube-prometheus/setup
until kubectl get servicemonitors --all-namespaces ; do date; sleep 1; echo ""; done
kubectl create -f %{_datadir}/k8s-yaml/kube-prometheus/base

To teardown:
kubectl delete --ignore-not-found=true -f %{_datadir}/k8s-yaml/kube-prometheus/base -f %{_datadir}/k8s-yaml/kube-prometheus/setup

%package sources
Summary:        Sources for own manifests for Grafana and Prometheus
Requires:       gojsontoyaml
Requires:       jsonnet

%description sources
This package contains the "sources" to build kubernetes manifests with own
changes for Grafana dashboards and Prometheus.
To build new manifests, read the README.md and
run "./build.sh <name>.jsonnet".

%prep
%setup -q -a1

%build
cp %{SOURCE3} kubic.jsonnet
rm -rf manifests
./build.sh kubic.jsonnet
pushd manifests/setup
echo -e "apiVersion: kustomize.config.k8s.io/v1beta1\nkind: Kustomization\nresources:" > kustomization.yaml
for i in `ls *.yaml| grep -v kustomization.yaml | sort`; do
    echo "- $i" >> kustomization.yaml
done
popd
pushd manifests
echo -e "apiVersion: kustomize.config.k8s.io/v1beta1\nkind: Kustomization\nresources:" > kustomization.yaml
for i in `ls *.yaml| grep -v kustomization.yaml | sort`; do
    echo "- $i" >> kustomization.yaml
done
popd

%install
mkdir -p %{buildroot}%{_datadir}/k8s-yaml/kube-prometheus/setup
mkdir -p %{buildroot}%{_datadir}/k8s-yaml/kube-prometheus/base
cp -av manifests/setup/* %{buildroot}%{_datadir}/k8s-yaml/kube-prometheus/setup/
cp -av manifests/*.yaml %{buildroot}%{_datadir}/k8s-yaml/kube-prometheus/base/
# Instal the "sources"
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -a * %{buildroot}%{_datadir}/%{name}/
rm -rf %{buildroot}%{_datadir}/%{name}/{.git*,manifests,vendor}
sed -i -e 's|%{_bindir}/env bash|/bin/bash|g' %{buildroot}%{_datadir}/kube-prometheus/build.sh %{buildroot}%{_datadir}/kube-prometheus/hack/example-service-monitoring/{deploy,teardown} %{buildroot}%{_datadir}/kube-prometheus/test.sh %{buildroot}%{_datadir}/kube-prometheus/tests/e2e/travis-e2e.sh

%files k8s-yaml
%license LICENSE
%dir %{_datadir}/k8s-yaml
%dir %{_datadir}/k8s-yaml/kube-prometheus
%dir %{_datadir}/k8s-yaml/kube-prometheus/setup
%dir %{_datadir}/k8s-yaml/kube-prometheus/base
%{_datadir}/k8s-yaml/kube-prometheus/setup/*
%{_datadir}/k8s-yaml/kube-prometheus/base/*

%files sources
%{_datadir}/%{name}

%changelog
