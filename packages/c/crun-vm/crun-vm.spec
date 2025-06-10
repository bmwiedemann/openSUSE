#
# spec file for package crun-vm
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


Name:           crun-vm
Version:        0.3.0
Release:        0
Summary:        OCI Runtime that enables to run VM images
License:        GPL-2.0-or-later
URL:            https://github.com/containers/crun-vm
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
Patch0:         xorriso.patch
BuildRequires:  cargo-packaging
BuildRequires:  gzip
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libselinux)
%if 0%{?suse_version} > 1600
BuildRequires:  rubygem(ronn-ng)
%endif
Requires:       crun
Requires:       xorriso

%description
crun-vm is an OCI Runtime that enables Podman, Docker, and Kubernetes to run QEMU-compatible Virtual Machine (VM) images. This means you can:

    Run VMs as easily as you run containers.
    Manage containers and VMs together using the same standard tooling.

%prep
%autosetup -a1 -p1

%build
%{cargo_build}
%if 0%{?suse_version} >= 1600
%make_build out/crun-vm.1.gz
%endif

%install
install -Dm0755 ./target/release/%{name} %{buildroot}%{_bindir}/%{name}
%if 0%{?suse_version} >= 1600
%make_build DESTDIR=%{buildroot} PREFIX=%{_prefix} install-man
%endif

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%if 0%{?suse_version} >= 1600
%{_mandir}/man?/%{name}.?%{?ext_man}
%endif

%changelog
