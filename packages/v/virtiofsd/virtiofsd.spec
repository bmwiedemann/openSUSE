#
# spec file for package virtiofsd
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


%if 0%{?suse_version} > 1500
  %define _virtiofsd_libexecdir %{_libexecdir}
%else
  %define _virtiofsd_libexecdir %{_libexecdir}/%{name}
%endif

Name:           virtiofsd
Version:        1.13.0
Release:        0
Summary:        A vhost-user virtio-fs device backend written in Rust
Group:          Development/Libraries/Rust
License:        Apache-2.0
URL:            https://gitlab.com/virtio-fs/virtiofsd
Source0:        %{name}-%{version}.tar.xz
Source1:        vendor.tar.xz
Source2:        50-virtiofsd.json
BuildRequires:  cargo
BuildRequires:  cargo-packaging
BuildRequires:  libcap-ng-devel
BuildRequires:  libseccomp-devel
Conflicts:      qemu-tools < 8
ExcludeArch:    %ix86 %arm

%description
A vhost-user virtio-fs device backend written in Rust

%prep
%autosetup -a1
# Adjust libvirt/virtiofsd interop config file to handle differences in
# the definition of libexecdir macro on SLE and Tumbleweed (bsc#1219772)
sed -i 's#@@LIBEXECDIR@@#%{_virtiofsd_libexecdir}#' %{SOURCE2}

%build
%{cargo_build}

%install
mkdir -p %{buildroot}%{_virtiofsd_libexecdir}
install -D -p -m 0755 %{_builddir}/%{name}-%{version}/target/release/virtiofsd %{buildroot}%{_virtiofsd_libexecdir}/virtiofsd
install -D -p -m 0644 %{SOURCE2} %{buildroot}%{_datadir}/qemu/vhost-user/50-virtiofsd.json

%check
%{cargo_test}

%if  0%{?suse_version} > 1500
# transition from old subdirectory to single file: rpm can't replace a directory on upgrades, force delete
%pre
[ ! -d %{_libexecdir}/%{name} ] || rm -r %{_libexecdir}/%{name}
%endif

%files
%doc README.md
%{_libexecdir}/virtiofsd
%dir %{_datadir}/qemu
%dir %{_datadir}/qemu/vhost-user
%{_datadir}/qemu/vhost-user/50-virtiofsd.json

%changelog
