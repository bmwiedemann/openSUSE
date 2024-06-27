#
# spec file for package kubernetes
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


# baseversion - base minor version (n) of kubernetes for this package
%define baseversion 1.30

# baseversionminus1 - previous base minor (n-1) version of kubernetes
%define baseversionminus1 1.29
# versionminus1 - full previous base minor (n-1) version of kubernetes, including point revision
%define versionminus1 1.29.6

# baseversionminus2 - previous base minor (n-2) version of kubernetes
%define baseversionminus2 1.28
# versionminus2 - full previous base minor (n-2) version of kubernetes, including point revision
%define versionminus2 1.28.11

# baseversionminus3 - previous base minor (n-3) version of kubernetes
%define baseversionminus3 1.27
# versionminus3 - full previous base minor (n-3) version of kubernetes, including point revision
%define versionminus3 1.27.15


# etcdversion - version of etcd
%define etcdversion 3.5.12
# etcdversionminus1 - version of etcd for versionminus1
%define etcdversionminus1 3.5.12
# etcdversionminus2 - version of etcd for versionminus2
%define etcdversionminus2 3.5.12
# etcdversionminus3 - version of etcd for versionminus3
%define etcdversionminus3 3.5.12


# corednsversion - version of coredns
%define corednsversion 1.11.1
# corednsversionminus1 - version of coredns for versionminus1
%define corednsversionminus1 1.11.1
# corednsversionminus2 - version of coredns for versionminus2
%define corednsversionminus2 1.10.1
# corednsversionminus3 - version of coredns for versionminus3
%define corednsversionminus3 1.10.1

Name:           kubernetes
Version:        1.30.2
Release:        0
Summary:        Container Scheduling and Management
License:        Apache-2.0
Group:          System/Management
URL:            http://kubernetes.io
Source:         README.packaging
ExcludeArch:    %{ix86} s390 ppc64 %arm

%description
Kubernetes is a system for automating deployment, scaling, and
management of containerized applications.

It groups containers that make up an application into logical units
for management and discovery.

# packages for containerized control plane

%package apiserver
Summary:        Kubernetes apiserver for container image
Group:          System/Management
Requires:       kubernetes%{baseversion}-apiserver = %{version}

%description apiserver
This subpackage contains the kube-apiserver binary for Kubic images

%package controller-manager
Summary:        Kubernetes controller-manager for container image
Group:          System/Management
Requires:       kubernetes%{baseversion}-controller-manager = %{version}

%description controller-manager
This subpackage contains the kube-controller-manager binary for Kubic images

%package scheduler
Summary:        Kubernetes scheduler for container image
Group:          System/Management
Requires:       kubernetes%{baseversion}-scheduler = %{version}

%description scheduler
This subpackage contains the kube-scheduler binary for Kubic images

%package proxy
Summary:        Kubernetes proxy for container image
Group:          System/Management
Requires:       kubernetes%{baseversion}-proxy = %{version}

%description proxy
This subpackage contains the kube-proxy binary for Kubic images

# packages for containerised control plane relative to Kubernetes minor version (n-1)

%package apiserver-minus1
Summary:        Kubernetes apiserver for container image
Group:          System/Management
Version:        %{versionminus1}
Requires:       kubernetes%{baseversionminus1}-apiserver

%description apiserver-minus1
This subpackage contains the kube-apiserver binary for Kubic images

%package controller-manager-minus1
Summary:        Kubernetes controller-manager for container image
Group:          System/Management
Version:        %{versionminus1}
Requires:       kubernetes%{baseversionminus1}-controller-manager

%description controller-manager-minus1
This subpackage contains the kube-controller-manager binary for Kubic images

%package scheduler-minus1
Summary:        Kubernetes scheduler for container image
Group:          System/Management
Version:        %{versionminus1}
Requires:       kubernetes%{baseversionminus1}-scheduler

%description scheduler-minus1
This subpackage contains the kube-scheduler binary for Kubic images

%package proxy-minus1
Summary:        Kubernetes proxy for container image
Group:          System/Management
Version:        %{versionminus1}
Requires:       kubernetes%{baseversionminus1}-proxy
%description proxy-minus1
This subpackage contains the kube-proxy binary for Kubic images

# packages for containerised control plane relative to Kubernetes minor version (n-2)

%package apiserver-minus2
Summary:        Kubernetes apiserver for container image
Group:          System/Management
Version:        %{versionminus2}
Requires:       kubernetes%{baseversionminus2}-apiserver

%description apiserver-minus2
This subpackage contains the kube-apiserver binary for Kubic images

%package controller-manager-minus2
Summary:        Kubernetes controller-manager for container image
Group:          System/Management
Version:        %{versionminus2}
Requires:       kubernetes%{baseversionminus2}-controller-manager

%description controller-manager-minus2
This subpackage contains the kube-controller-manager binary for Kubic images

%package scheduler-minus2
Summary:        Kubernetes scheduler for container image
Group:          System/Management
Version:        %{versionminus2}
Requires:       kubernetes%{baseversionminus2}-scheduler

%description scheduler-minus2
This subpackage contains the kube-scheduler binary for Kubic images

%package proxy-minus2
Summary:        Kubernetes proxy for container image
Group:          System/Management
Version:        %{versionminus2}
Requires:       kubernetes%{baseversionminus2}-proxy

%description proxy-minus2
This subpackage contains the kube-proxy binary for Kubic images

# packages for containerised control plane relative to Kubernetes minor version (n-3)

%package apiserver-minus3
Summary:        Kubernetes apiserver for container image
Group:          System/Management
Version:        %{versionminus3}
Requires:       kubernetes%{baseversionminus3}-apiserver

%description apiserver-minus3
This subpackage contains the kube-apiserver binary for Kubic images

%package controller-manager-minus3
Summary:        Kubernetes controller-manager for container image
Group:          System/Management
Version:        %{versionminus3}
Requires:       kubernetes%{baseversionminus3}-controller-manager

%description controller-manager-minus3
This subpackage contains the kube-controller-manager binary for Kubic images

%package scheduler-minus3
Summary:        Kubernetes scheduler for container image
Group:          System/Management
Version:        %{versionminus3}
Requires:       kubernetes%{baseversionminus3}-scheduler

%description scheduler-minus3
This subpackage contains the kube-scheduler binary for Kubic images

%package proxy-minus3
Summary:        Kubernetes proxy for container image
Group:          System/Management
Version:        %{versionminus3}
Requires:       kubernetes%{baseversionminus3}-proxy

%description proxy-minus3
This subpackage contains the kube-proxy binary for Kubic images

# packages for running on hosts/clients

%package kubelet
Summary:        Kubernetes kubelet daemon
Group:          System/Management
Requires:       kubernetes%{baseversion}-kubelet = %{VERSION}

%description kubelet
Manage a cluster of Linux containers as a single system to accelerate Dev and simplify Ops.
kubelet daemon

%package kubeadm
Summary:        Kubernetes kubeadm bootstrapping tool
Group:          System/Management
Requires:       kubernetes%{baseversion}-kubeadm = %{VERSION}
Requires:       kubernetes%{baseversion}-kubelet
Requires:       kubernetes%{baseversionminus1}-kubelet

%description kubeadm
Manage a cluster of Linux containers as a single system to accelerate Dev and simplify Ops.
kubeadm bootstrapping tool

%package client
Summary:        Kubernetes client tools
Group:          System/Management
Requires:       kubernetes%{baseversion}-client = %{VERSION}

%description client
Kubernetes client tools like kubectl.

# etcd package relative to k8s base minor version (n)

%package etcd
Summary:        Kubernetes etcd daemon for container images
Group:          System/Management
Version:        %{etcdversion}
Requires:       etcd-for-k8s%{baseversion}

%description etcd
This subpackage contains the etcd binary for Kubic images

# etcd package relative to k8s base minor version (n-1)

%package etcd-minus1
Summary:        Kubernetes etcd daemon for container images
Group:          System/Management
Version:        %{etcdversionminus1}
Requires:       etcd-for-k8s%{baseversionminus1}

%description etcd-minus1
This subpackage contains the etcd binary for Kubic images

# etcd package relative to k8s base minor version (n-2)

%package etcd-minus2
Summary:        Kubernetes etcd daemon for container images
Group:          System/Management
Version:        %{etcdversionminus2}
Requires:       etcd-for-k8s%{baseversionminus2}

%description etcd-minus2
This subpackage contains the etcd binary for Kubic images

# etcd package relative to k8s base minor version (n-3)

%package etcd-minus3
Summary:        Kubernetes etcd daemon for container images
Group:          System/Management
Version:        %{etcdversionminus3}
Requires:       etcd-for-k8s%{baseversionminus3}

%description etcd-minus3
This subpackage contains the etcd binary for Kubic images

# coredns package relative to k8s base minor version (n)

%package coredns
Summary:        Kubernetes coredns daemon for container images
Group:          System/Management
Version:        %{corednsversion}
Requires:       coredns-for-k8s%{baseversion}

%description coredns
This subpackage contains the coredns binary for Kubic images

# coredns package relative to k8s base minor version (n-1)

%package coredns-minus1
Summary:        Kubernetes coredns daemon for container images
Group:          System/Management
Version:        %{corednsversionminus1}
Requires:       coredns-for-k8s%{baseversionminus1}

%description coredns-minus1
This subpackage contains the coredns binary for Kubic images

# coredns package relative to k8s base minor version (n-2)

%package coredns-minus2
Summary:        Kubernetes coredns daemon for container images
Group:          System/Management
Version:        %{corednsversionminus2}
Requires:       coredns-for-k8s%{baseversionminus2}

%description coredns-minus2
This subpackage contains the coredns binary for Kubic images

# coredns package relative to k8s base minor version (n-3)

%package coredns-minus3
Summary:        Kubernetes coredns daemon for container images
Group:          System/Management
Version:        %{corednsversionminus3}
Requires:       coredns-for-k8s%{baseversionminus3}

%description coredns-minus3
This subpackage contains the coredns binary for Kubic images

%prep
#Not Needed

%build
echo "This is a dummy package to provide a dependency on supported kubernetes versions." > README

%install

%files apiserver
%doc README

%files controller-manager
%doc README

%files scheduler
%doc README

%files proxy
%doc README

%files etcd
%doc README

%files coredns
%doc README

%files apiserver-minus1
%doc README

%files controller-manager-minus1
%doc README

%files scheduler-minus1
%doc README

%files proxy-minus1
%doc README

%files etcd-minus1
%doc README

%files coredns-minus1
%doc README

%files apiserver-minus2
%doc README

%files controller-manager-minus2
%doc README

%files scheduler-minus2
%doc README

%files proxy-minus2
%doc README

%files etcd-minus2
%doc README

%files coredns-minus2
%doc README

%files apiserver-minus3
%doc README

%files controller-manager-minus3
%doc README

%files scheduler-minus3
%doc README

%files proxy-minus3
%doc README

%files etcd-minus3
%doc README

%files coredns-minus3
%doc README

%files kubelet
%doc README

%files kubeadm
%doc README

%files client
%doc README

%changelog
