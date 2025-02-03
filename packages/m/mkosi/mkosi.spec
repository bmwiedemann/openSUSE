#
# spec file for package mkosi
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


%define pythons python3

Name:           mkosi
Version:        25.3
Release:        0
Summary:        Build bespoke OS Images
License:        LGPL-2.1-or-later
Group:          System/Management
URL:            https://github.com/systemd/mkosi
Source0:        https://github.com/systemd/mkosi/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        mkosi-initrd.conf
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{pythons}
BuildRequires:  fdupes
%ifarch x86_64 aarch64
BuildRequires:  pandoc
%endif
BuildRequires:  python-rpm-macros
Requires:       distribution-gpg-keys
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
# pandoc is arch specific, so noarch will not work
#BuildArch:      noarch

%description
A fancy wrapper around "dnf --installroot", "apt", "pacman", and "zypper" that
generates disk images with a number of bells and whistles.

Generated images are tailored to the purpose: GPT partitions,
systemd-boot or grub2, images for containers, VMs, initrd, and extensions.

mkosi can boot an image via QEMU or systemd-nspawn, or simply start a shell in
chroot, burn the image to a device, connect to a running VM via ssh, extract
logs and coredumps, and also serve an image over HTTP.

See https://mkosi.systemd.io/ for documentation.

%package addon
Summary:        Build addons locally for unified kernel images using mkosi
Requires:       %{name} = %{version}-%{release}
Requires:       coreutils

%description addon
This package provides the mkosi-addon wrapper to build PE addons containing
customizations for unified kernel images specificto the running or local
system.

%package initrd
Summary:        Build initrds locally using mkosi
Requires:       %{name} = %{version}-%{release}
Requires:       coreutils

%description initrd
This package provides the mkosi-initrd wrapper to build initrds with mkosi
locally.

%prep
%autosetup -p1

%build
%ifarch x86_64 aarch64
tools/make-man-page.sh
%endif
%pyproject_wheel
bin/mkosi completion bash > mkosi.bash

%install
%pyproject_install
%python_expand %fdupes %{buildroot}/%{$python_sitelib}/mkosi

%ifarch x86_64 aarch64
# Install man pages
mkdir -p %{buildroot}%{_mandir}/man1
cp %{buildroot}%{python3_sitelib}/mkosi/resources/man/mkosi.1* \
    %{buildroot}%{_mandir}/man1/
cp %{buildroot}%{python3_sitelib}/mkosi/resources/man/mkosi-addon.1* \
    %{buildroot}%{_mandir}/man1/
cp %{buildroot}%{python3_sitelib}/mkosi/resources/man/mkosi-initrd.1* \
    %{buildroot}%{_mandir}/man1/
cp %{buildroot}%{python3_sitelib}/mkosi/resources/man/mkosi-sandbox.1* \
    %{buildroot}%{_mandir}/man1/
%endif

# Install bash completions
install -m 644 -D mkosi.bash \
    %{buildroot}%{_datadir}/bash-completion/completions/mkosi

# Create configuration directories for mkosi-initrd
mkdir -p %{buildroot}%{_prefix}/lib/mkosi-initrd
install -m 644 %{SOURCE1} %{buildroot}%{_prefix}/lib/mkosi-initrd/mkosi.conf
mkdir -p %{buildroot}%{_sysconfdir}/mkosi-initrd

%post initrd
if [ ! -e %{_sysconfdir}/mkosi-initrd/mkosi.conf ]; then
    cat >> %{_sysconfdir}/mkosi-initrd/mkosi.conf<<EOF
# Write here your own configuration.
# See man mkosi(1) for details.
#[Content]
#ExtraTrees=
#KernelModulesInclude=
#KernelModulesExclude=
EOF
fi

%check
%pytest

%files
%doc mkosi.md README.md
%license LICENSES
%{_bindir}/mkosi
%{_bindir}/mkosi-sandbox
%ifarch x86_64 aarch64
%{_mandir}/man1/mkosi.1*
%{_mandir}/man1/mkosi-sandbox.1*
%endif
%{python3_sitelib}/mkosi
%{python3_sitelib}/mkosi-%{version}.dist-info
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/mkosi

%files addon
%{_bindir}/mkosi-addon
%ifarch x86_64 aarch64
%{_mandir}/man1/mkosi-addon.1*
%endif

%files initrd
%{_bindir}/mkosi-initrd
%ifarch x86_64 aarch64
%{_mandir}/man1/mkosi-initrd.1*
%endif
%dir %{_prefix}/lib/mkosi-initrd
%{_prefix}/lib/mkosi-initrd/mkosi.conf
%dir %{_sysconfdir}/mkosi-initrd

%changelog
