#
# spec file for package mkosi
#
# Copyright (c) 2024 SUSE LLC
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


%define pythons python3

Name:           mkosi
Version:        24.3
Release:        0
Summary:        Build bespoke OS Images
License:        LGPL-2.1-or-later
Group:          System/Management
URL:            https://github.com/systemd/mkosi
Source0:        https://github.com/systemd/mkosi/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        mkosi-initrd.conf
Source2:        mkosi-initrd-chroot.sh
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{pythons}
BuildRequires:  fdupes
BuildRequires:  pandoc
BuildRequires:  python-rpm-macros
Requires:       bubblewrap
Requires:       python3 >= 3.9
Requires:       zypper
Recommends:     btrfsprogs
Recommends:     cpio
Recommends:     dosfstools
Recommends:     dpkg
Recommends:     edk2-ovmf
Recommends:     gnupg
Recommends:     squashfs
Recommends:     tar
Recommends:     xz
Recommends:     zstd
BuildArch:      noarch
ExclusiveArch:  x86_64 aarch64

%description
A fancy wrapper around "dnf --installroot", "apt", "pacman", and "zypper" that
generates disk images with a number of bells and whistles.

Generated images are tailored to the purpose: GPT partitions,
systemd-boot or grub2, images for containers, VMs, initrd, and extensions.

mkosi can boot an image via QEMU or systemd-nspawn, or simply start a shell in
chroot, burn the image to a device, connect to a running VM via ssh, extract
logs and coredumps, and also serve an image over HTTP.

See https://mkosi.systemd.io/ for documentation.

%package initrd
Summary:        Build initrds locally using mkosi
Requires:       %{name} = %{version}-%{release}
Requires:       coreutils
Requires:       (%{name}-initrd-tukit if read-only-root-fs)

%description initrd
This package provides the mkosi-initrd wrapper to build initrds with mkosi
locally.

%package initrd-tukit
Summary:        Build initrds locally using mkosi with transactional updates
Requires:       %{name} = %{version}-%{release}
Requires:       read-only-root-fs

%description initrd-tukit
mkosi calls bwrap, and that does not work with transactional updates, so this
package provides a special mkosi-initrd wrapper to support building initrds on
transactional systems.

%prep
%autosetup -p1

%build
tools/make-man-page.sh
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}/%{$python_sitelib}/mkosi

mkdir -p %{buildroot}%{_mandir}/man1
cp %{buildroot}%{python3_sitelib}/mkosi/resources/mkosi.1* %{buildroot}%{_mandir}/man1/
cp %{buildroot}%{python3_sitelib}/mkosi/initrd/resources/mkosi-initrd.1* %{buildroot}%{_mandir}/man1/

# Install mkosi-initrd conf
mkdir -p %{buildroot}%{_prefix}/lib/mkosi-initrd
install -m 644 %{SOURCE1} %{buildroot}%{_prefix}/lib/mkosi-initrd/mkosi.conf
mkdir -p %{buildroot}%{_sysconfdir}/mkosi-initrd

# Install the tukit script
mkdir -p %{buildroot}%{_prefix}/libexec/mkosi-initrd
install -m 744 %{SOURCE2} %{buildroot}%{_prefix}/libexec/mkosi-initrd/mkosi-initrd-chroot.sh

%post initrd
if [ ! -e %{_sysconfdir}/mkosi-initrd/mkosi.conf ]; then
    cat >> %{_sysconfdir}/mkosi-initrd/mkosi.conf<<EOF
# Write here your own configuration.
# See man mkosi(1) for details.
[Content]
#ExtraTrees=
#KernelModulesInclude=
#KernelModulesExclude=
EOF
fi

%posttrans initrd-tukit
# mkosi runs in a sandbox, and for that purpose it relies on bubblewrap. The
# problem is transactional-update chroots to a snapshot, and bubblewrap does not
# work there because it requires pivot_root:
# https://github.com/containers/bubblewrap/issues/135
# The issue is quite old, there is even a PR trying to fall back to chroot if
# pivot_root fails (https://github.com/containers/bubblewrap/pull/595), but
# apparently bubblewrap upstream is not trying to fix this.
# The workaround implemented in mkosi-initrd-chroot.sh was proposed by the main
# mkosi upstream maintainer:
# https://github.com/containers/bubblewrap/issues/592#issuecomment-2243087731
mv %{_bindir}/mkosi-initrd %{_prefix}/libexec/mkosi-initrd
ln -s %{_prefix}/libexec/mkosi-initrd/mkosi-initrd-chroot.sh %{_bindir}/mkosi-initrd

%preun initrd-tukit
rm -f %{_prefix}/libexec/mkosi-initrd/mkosi-initrd

%check
%pytest

%files
%doc mkosi.md README.md
%license LICENSE
%{_bindir}/mkosi
%{_mandir}/man1/mkosi.1*
%{python3_sitelib}/mkosi
%{python3_sitelib}/mkosi-%{version}.dist-info

%files initrd
%{_bindir}/mkosi-initrd
%{_mandir}/man1/mkosi-initrd.1*
%dir %{_prefix}/lib/mkosi-initrd
%{_prefix}/lib/mkosi-initrd/mkosi.conf
%dir %{_sysconfdir}/mkosi-initrd

%files initrd-tukit
%dir %{_prefix}/libexec/mkosi-initrd
%{_prefix}/libexec/mkosi-initrd/mkosi-initrd-chroot.sh

%changelog
