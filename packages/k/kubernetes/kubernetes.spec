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


# baseversion - version of kubernetes for this package
%define baseversion 1.18
# baseversionminus1 - previous version of kubernetes
%define baseversionminus1 1.17

Name:           kubernetes
Version:        1.18.2
Release:        0
Summary:        Container Scheduling and Management
License:        Apache-2.0
Group:          System/Management
URL:            http://kubernetes.io
Source:         README.packaging
ExcludeArch:    %{ix86} s390 ppc64

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

# packages for old containerised control plane

%package apiserver-minus1
Summary:        Kubernetes apiserver for container image
Group:          System/Management
Requires:       kubernetes%{baseversionminus1}-apiserver

%description apiserver-minus1
This subpackage contains the kube-apiserver binary for Kubic images

%package controller-manager-minus1
Summary:        Kubernetes controller-manager for container image
Group:          System/Management
Requires:       kubernetes%{baseversionminus1}-controller-manager

%description controller-manager-minus1
This subpackage contains the kube-controller-manager binary for Kubic images

%package scheduler-minus1
Summary:        Kubernetes scheduler for container image
Group:          System/Management
Requires:       kubernetes%{baseversionminus1}-scheduler

%description scheduler-minus1
This subpackage contains the kube-scheduler binary for Kubic images

%package proxy-minus1
Summary:        Kubernetes proxy for container image
Group:          System/Management
Requires:       kubernetes%{baseversionminus1}-proxy
%description proxy-minus1
This subpackage contains the kube-proxy binary for Kubic images

# packages for running on hosts/clients

%package kubelet
Summary:        Kubernetes kubelet daemon
Group:          System/Management
Requires:       kubernetes%{baseversion}-kubelet = %{version}

%description kubelet
Manage a cluster of Linux containers as a single system to accelerate Dev and simplify Ops.
kubelet daemon

%package kubeadm
Summary:        Kubernetes kubeadm bootstrapping tool
Group:          System/Management
Requires:       kubernetes%{baseversion}-kubeadm = %{version}
Requires:       kubernetes%{baseversionminus1}-kubelet

%description kubeadm
Manage a cluster of Linux containers as a single system to accelerate Dev and simplify Ops.
kubeadm bootstrapping tool

%package client
Summary:        Kubernetes client tools
Group:          System/Management
Requires:       kubernetes%{baseversion}-client = %{version}

%description client
Kubernetes client tools like kubectl.

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

%files apiserver-minus1
%doc README

%files controller-manager-minus1
%doc README

%files scheduler-minus1
%doc README

%files proxy-minus1
%doc README

%files kubelet
%doc README

%files kubeadm
%doc README

%files client
%doc README

%changelog
