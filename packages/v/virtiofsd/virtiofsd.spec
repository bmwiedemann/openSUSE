#
# spec file for package virtiofsd
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Version:        1.14.0
Release:        0
Summary:        A vhost-user virtio-fs device backend written in Rust
Group:          Development/Libraries/Rust
License:        Apache-2.0
URL:            https://gitlab.com/virtio-fs/virtiofsd
Source0:        %{name}-%{version}.tar.xz
Source1:        vendor.tar.zst
Source2:        50-virtiofsd.json
Patch0:         update-time-0.3.47.patch
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

# Special checks for making sure that bsc#1257912 (CVE-2026-25727)
# has been correctly handled.
TIME_VERSION=$(awk '/^name = "time"/{flag=1} flag && /^version =/{print $3; exit}' Cargo.lock | tr -d '"')
MIN_TIME_VERSION="0.3.47"
HIGHEST=$(printf "%s\n%s" "$MIN_TIME_VERSION" "$TIME_VERSION" | sort -V | tail -n1)
if [ "$HIGHEST" != "$TIME_VERSION" ]; then
    echo "=== ERROR! bsc#1257912 (CVE-2026-25727) not handled properly."
    echo " The time crate is at version $TIME_VERSION. It must be at least $MIN_TIME_VERSION."
    echo " Check the changelog of the patch update-time-0.3.47.patch and follow the instructions"
    exit 1
fi

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
