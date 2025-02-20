#
# spec file for package kubectl-browse-pvc
#
# Copyright (c) 2025 SUSE LLC
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


%define executable_name kubectl-browse_pvc

Name:           kubectl-browse-pvc
Version:        1.2.0
Release:        0
Summary:        Kubectl plugin for browsing PVCs on the command line
License:        MIT
URL:            https://github.com/clbx/kubectl-browse-pvc
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go1.22

%description
I constantly found myself spinning up dummy pods to exec into them so I could
browse a PVC, this takes a few steps out of creating dummy pods to check out
the contents of a PVC.

Usage

`kubectl browse-pvc -n <namespace> <pvc-name>`

On an unbound PVC. The tool spins up a pod that mounts the PVC and then execs
into it allowing you to modify the contents of the PVC. The Job finishes and
cleans up the pod when you disconnect.

%prep
%autosetup -a 1 -p 1
mv vendor ./src/

%build
%ifarch s390x i586 riscv64
CGO_ENABLED=1 \
%else
CGO_ENABLED=0 \
%endif
cd src/
go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags="-X main.Version=v%{version}" \
   -o ../bin/%{executable_name} .

%install
# Install the binary.
install -D -m 0755 bin/%{executable_name} %{buildroot}/%{_bindir}/%{executable_name}

%check

%files
%doc README.md
%license LICENSE
%{_bindir}/%{executable_name}

%changelog
