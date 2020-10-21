#
# spec file for package cert-manager
#
# Copyright (c) 2020 SUSE LLC, Nuernberg, Germany.
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

%define goipath github.com/jetstack/cert-manager

Name:           cert-manager
Version:        0.15.1
Release:        0
Summary:        Add-on for automatic provisioning of TLS certificates in Kubernetes
License:        Apache-2.0
Group:          System/Management
URL:            https://cert-manager.io
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang-packaging
BuildRequires:  golang(API) = 1.14

%description
cert-manager is a Kubernetes add-on to automate the management and issuance of
TLS certificates from various issuing sources.

It will ensure certificates are valid and up to date periodically, and attempt
to renew certificates at an appropriate time before expiry.

%package controller
Summary:        The controller for %{name}
Group:          System/Management
%description controller
The controller is the main component of cert-manager.

%package cainjector
Summary:        The CA injector for %{name}
Group:          System/Management
%description cainjector
The CA injector is responsible for injecting the CA bundle into the webhook’s
ValidatingWebhookConfiguration and MutatingWebhookConfiguration resources
in order to allow the Kubernetes API server to trust the webhook API server.

%package webhook
Summary:        The webhook for %{name}
Group:          System/Management
%description webhook
The webhook server provides dynamic admission control over cert-manager resources includes
ValidatingAdmissionWebhook, MutatingAdmissionWebhook, and CustomResourceConversionWebhook.

%prep
%setup -q -a1

%build
%goprep %{goipath}
export CGO_ENABLED=0
%gobuild -mod vendor cmd/controller
%gobuild -mod vendor cmd/cainjector
%gobuild -mod vendor cmd/webhook

%install
%goinstall
mv %{buildroot}/%{_bindir}/controller %{buildroot}/%{_bindir}/%{name}-controller
mv %{buildroot}/%{_bindir}/cainjector %{buildroot}/%{_bindir}/%{name}-cainjector
mv %{buildroot}/%{_bindir}/webhook %{buildroot}/%{_bindir}/%{name}-webhook

%files
%defattr(-,root,root)
%doc README.md
%license LICENSE
%files controller
%{_bindir}/%{name}-controller
%files cainjector
%{_bindir}/%{name}-cainjector
%files webhook
%{_bindir}/%{name}-webhook

%changelog
