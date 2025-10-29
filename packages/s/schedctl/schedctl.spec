#
# spec file for package schedctl
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


Name:           schedctl
Version:        1.0.2
Release:        0
Summary:        Linux eBPF sched_ext plug and play schedulers for fun and profit
License:        Apache-2.0
URL:            https://github.com/schedkit/schedctl
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang(API) >= 1.23
BuildRequires:  libbtrfs-devel
BuildRequires:  libgpgme-devel
Requires:       (podman or containerd)

%description
eBPF sched_ext plug and play containerized schedulers for fun and profit

%prep
%autosetup -a 1

%build
%ifnarch ppc64
export GOFLAGS="-buildmode=pie"
%endif
go build -ldflags='-s -X main.version=%{version}' -o=./schedctl main.go

%install
install -D -m 0755 %{name} "%{buildroot}/%{_bindir}/%{name}"

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
