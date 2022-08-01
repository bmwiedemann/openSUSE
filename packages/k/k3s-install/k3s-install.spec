#
# spec file for package k3s-install
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


Name:           k3s-install
Version:        1.24.3+k3s1
Release:        0
Summary:        Installer for k3s optimised for openSUSE MicroOS
License:        Apache-2.0
Group:          System/Management
URL:            https://k3s.io
Source0:        https://github.com/k3s-io/k3s/archive/v%{version}.tar.gz#/k3s-%{version}.tar.gz
Requires:       iptables
Requires:       k3s-selinux
Conflicts:      cri-tools
Conflicts:      kubectl
Conflicts:      kubernetes-client
Conflicts:      kubernetes-client-provider

%description
Based on the official upstream k3s install.sh, this k3s-install
package provides a curated, MicroOS-optimised, securely delivered
alternative to running a script directly from the internet.

k3s is a container orchestration system for automating application
deployment, scaling, and management. It is a Kubernetes-compliant
distribution that differs from the original Kubernetes (colloquially
"k8s") in that:

  * Legacy, alpha, or non-default features are removed.
  * Most in-tree plugins (cloud providers and storage plugins) were
    removed, since they can be replaced with out-of-tree addons.
  * sqlite3 is the default storage mechanism.
    etcd3 is still available, but not the default.
  * There is a new launcher that handles a lot of the complexity of
    TLS and options.

%prep
%autosetup -p1 -n k3s-%(echo %{version} | tr '+' '-')

%build

%install
mkdir -p %{buildroot}%{_bindir}
install -p -m 755 install.sh %{buildroot}%{_bindir}/k3s-install

%files
%license LICENSE
%doc README.md
%{_bindir}/k3s-install

%changelog
