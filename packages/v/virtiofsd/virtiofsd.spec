#
# spec file for package virtiofsd
#
# Copyright (c) 2023 SUSE LLC
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


Name:           virtiofsd
Version:        1.6.1
Release:        0
Summary:        vhost-user virtio-fs device backend written in Rust
Group:          Development/Libraries/Rust
License:        Apache-2.0
URL:            https://gitlab.com/virtio-fs/virtiofsd
Source0:        %{name}-%{version}.tar.xz
Source1:        vendor.tar.xz
Source2:        cargo_config
BuildRequires:  cargo-packaging
BuildRequires:  libcap-ng-devel
BuildRequires:  libseccomp-devel
Conflicts:      qemu-tools < 8
ExcludeArch:    %ix86 %arm

%description
vhost-user virtio-fs device backend written in Rust

%files
%doc README.md
%{_libexecdir}/virtiofsd

%prep
%autosetup -a1
mkdir .cargo
cp %{SOURCE2} .cargo/config

%build
%{cargo_build}

%install
install -D -d -m 0755 %{buildroot}%{_libexecdir}
install -m 0755 %{_builddir}/%{name}-%{version}/target/release/virtiofsd %{buildroot}%{_libexecdir}/virtiofsd

%check
%{cargo_test}

%changelog
