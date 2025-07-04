#
# spec file for package kiwi
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
#
# Please submit bugfixes or comments via:
#
#       https://github.com/OSInside/kiwi/issues
#

# If they aren't provided by a system installed macro, define them
%{!?_defaultdocdir: %global _defaultdocdir %{_datadir}/doc}

%if 0%{?suse_version} && 0%{?suse_version} < 1600
%global __python3 /usr/bin/python3.11
%global python3_pkgversion 311
%else
%{!?__python3: %global __python3 /usr/bin/python3}
%{!?python3_pkgversion:%global python3_pkgversion 3}
%endif

%if %{undefined python3_sitelib}
%if "%{_vendor}" == "debbuild"
%global python3_sitelib %(%{__python3} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")
%else
%global python3_sitelib %(%{__python3} -c "import sysconfig; print(sysconfig.get_path('platlib'))")
%endif
%endif

%if %{undefined python3_version}
%global python3_version %(%{__python3} -Esc "import sys; sys.stdout.write('{0.major}.{0.minor}'.format(sys.version_info))")
%endif

%if %{undefined python3_version_nodots}
%global python3_version_nodots %(%{__python3} -Esc "import sys; sys.stdout.write('{0.major}{0.minor}'.format(sys.version_info))")
%endif

%if 0%{?debian} || 0%{?ubuntu}
%global is_deb 1
%global pygroup python
%global sysgroup admin
%global develsuffix dev
%else
%global pygroup Development/Languages/Python
%global sysgroup System/Management
%global develsuffix devel
%endif

Name:           python-kiwi
Version:        10.2.26
Provides:       kiwi-schema = 8.1
Release:        0
Url:            https://github.com/OSInside/kiwi
Summary:        KIWI - Appliance Builder Next Generation
License:        GPL-3.0-or-later
%if "%{_vendor}" == "debbuild"
# Needed to set Maintainer in output debs
Packager:       Marcus Schaefer <marcus.schaefer@suse.com>
%endif
Group:          %{pygroup}
Source0:        %{name}.tar.gz
Source1:        %{name}-rpmlintrc
# SUSE-specific patches (1001+)
## PATCH-FIX-OPENSUSE kiwi-revert-bls-default-for-suse.patch -- temporary until opensuse has bls
Patch1001:      kiwi-revert-bls-default-for-suse.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?fedora} || 0%{?suse_version}
BuildRequires:  fdupes
%endif
%if 0%{?suse_version}
BuildRequires:  shadow
%endif
%if 0%{?debian} || 0%{?ubuntu}
BuildRequires:  passwd
%endif
# Main build requirements
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  python%{python3_pkgversion}-%{develsuffix} >= 3.9
BuildRequires:  python%{python3_pkgversion}-build
BuildRequires:  python%{python3_pkgversion}-installer
BuildRequires:  python%{python3_pkgversion}-poetry-core >= 1.2.0
BuildRequires:  python%{python3_pkgversion}-wheel
# doc build requirements
%if ! (0%{?fedora} >= 41 || 0%{?rhel} >= 10)
BuildRequires:  python%{python3_pkgversion}-docopt >= 0.6.2
%else
BuildRequires:  python%{python3_pkgversion}-docopt-ng
%endif
%if 0%{?debian} || 0%{?ubuntu}
# only because of debbuild
BuildRequires:  python%{python3_pkgversion}-setuptools
%endif
BuildRequires:  python%{python3_pkgversion}-lxml
BuildRequires:  python%{python3_pkgversion}-requests
BuildRequires:  python%{python3_pkgversion}-simplejson
%if 0%{?suse_version}
BuildRequires:  python%{python3_pkgversion}-Sphinx
%else
BuildRequires:  python%{python3_pkgversion}-sphinx
%endif
%if 0%{?debian} || 0%{?ubuntu}
BuildRequires:  python%{python3_pkgversion}-sphinx-rtd-theme
BuildRequires:  python%{python3_pkgversion}-yaml
%else
BuildRequires:  python%{python3_pkgversion}-sphinx_rtd_theme
BuildRequires:  python%{python3_pkgversion}-PyYAML
%endif

%description
The KIWI Image System provides an operating system image builder
for Linux supported hardware platforms as well as for virtualization
and cloud systems like Xen, KVM, VMware, EC2 and more.

%package -n kiwi-systemdeps-core
Summary:        KIWI - Core host system dependencies
Group:          %{sysgroup}
Provides:       kiwi-image-tbz-requires = %{version}-%{release}
Obsoletes:      kiwi-image-tbz-requires < %{version}-%{release}
%if "%{_vendor}" != "debbuild"
Provides:       kiwi-image:tbz
%endif
%if 0%{?fedora} >= 42
Provides:       kiwi-image:enclave
Requires:       eif_build
%endif
# tools conditionally used by kiwi
%if 0%{?fedora} || 0%{?rhel} >= 8
Recommends:     gnupg2
Recommends:     apt
Recommends:     dpkg
%endif
%if 0%{?suse_version}
Recommends:     gpg2
%if 0%{?suse_version} >= 1650
Recommends:     dnf
%endif
%endif
# package managers required by distro
%if 0%{?fedora} || 0%{?rhel} >= 8 || 0%{?suse_version} >= 1650
Provides:       kiwi-packagemanager:microdnf
Requires:       microdnf
%endif
%if 0%{?fedora} >= 41
Requires:       dnf5
Requires:       dnf5-plugins
Provides:       kiwi-packagemanager:dnf5
%else
%if 0%{?fedora} || 0%{?rhel} || 0%{?suse_version} >= 1650
Requires:       dnf
Provides:       kiwi-packagemanager:dnf
Provides:       kiwi-packagemanager:dnf4
Provides:       kiwi-packagemanager:yum
%endif
%endif
%if 0%{?fedora} >= 26 || 0%{?suse_version}
Requires:       zypper
Provides:       kiwi-packagemanager:zypper
%endif
%if 0%{?debian} || 0%{?ubuntu}
Requires:       apt
Requires:       dpkg
Requires:       gnupg
%endif
# tools required by kiwi
Requires:       mtools
Requires:       rsync
Requires:       tar >= 1.2.7
Requires:       cpio
Requires:       lsof
Requires:       openssl

%description -n kiwi-systemdeps-core
This metapackage installs the necessary system dependencies
to run KIWI.

%package -n kiwi-systemdeps-containers
Summary:        KIWI - host requirements for OCI container images
Group:          %{sysgroup}
Provides:       kiwi-image-docker-requires = %{version}-%{release}
Obsoletes:      kiwi-image-docker-requires < %{version}-%{release}
%if "%{_vendor}" != "debbuild"
Provides:       kiwi-image:docker
Provides:       kiwi-image:oci
%endif
%if 0%{?suse_version}
Requires:       umoci
%else
Requires:       buildah
%endif
Requires:       skopeo

%description -n kiwi-systemdeps-containers
Host setup helper to pull in all packages required/useful on
the build host to build OCI container images

%package -n kiwi-systemdeps-containers-wsl
Summary:        KIWI - host requirements for WSL container images
Group:          %{sysgroup}
Provides:       kiwi-image-wsl-requires = %{version}-%{release}
Obsoletes:      kiwi-image-wsl-requires < %{version}-%{release}
%if "%{_vendor}" != "debbuild"
Provides:       kiwi-image:appx
Provides:       kiwi-image:wsl
%endif
%if 0%{?suse_version}
Requires:       fb-util-for-appx
%endif
%if 0%{?fedora} || 0%{?rhel}
Requires:       appx-util
%endif

%description -n kiwi-systemdeps-containers-wsl
Host setup helper to pull in all packages required/useful on
the build host to build WSL container images

%package -n kiwi-systemdeps-iso-media
Summary:        KIWI - host requirements for live and install iso images
Group:          %{sysgroup}
Provides:       kiwi-image-iso-requires = %{version}-%{release}
Obsoletes:      kiwi-image-iso-requires < %{version}-%{release}
%if "%{_vendor}" != "debbuild"
Provides:       kiwi-image:iso
%endif
%if 0%{?suse_version}
Requires:       checkmedia
%else
Requires:       isomd5sum
%endif
Requires:       xorriso
Requires:       kiwi-systemdeps-core = %{version}-%{release}
Requires:       kiwi-systemdeps-filesystems = %{version}-%{release}
Requires:       kiwi-systemdeps-bootloaders = %{version}-%{release}

%description -n kiwi-systemdeps-iso-media
Host setup helper to pull in all packages required/useful on
the build host to build live and install iso images.

%package -n kiwi-systemdeps-bootloaders
Summary:        KIWI - host requirements for configuring bootloaders
%if 0%{?suse_version}
%ifarch x86_64
Requires:       grub2-x86_64-efi
%endif
%ifarch %{ix86} x86_64
Recommends:     gfxboot
%endif
%endif
%if 0%{?fedora} || 0%{?rhel}
%ifarch x86_64
Requires:       grub2-efi-x64
%endif
%endif
%ifarch %arm aarch64
%if 0%{?fedora} || 0%{?rhel}
Requires:       uboot-tools
%endif
%if 0%{?suse_version}
Requires:       u-boot-tools
%endif
%endif
%ifarch s390 s390x
%if 0%{?fedora} || 0%{?rhel}
Requires:       s390utils
%else
Requires:       s390-tools
%if ! (0%{?debian} || 0%{?ubuntu})
Requires:       grub2
%endif
%endif
%endif
Requires:       kiwi-systemdeps-core = %{version}-%{release}

%description -n kiwi-systemdeps-bootloaders
Host setup helper to pull in all packages required/useful on
the build host for configuring bootloaders on images.

%package -n kiwi-systemdeps-filesystems
Summary:        KIWI - host requirements for filesystems
Group:          %{sysgroup}
Provides:       kiwi-image-pxe-requires = %{version}-%{release}
Obsoletes:      kiwi-image-pxe-requires < %{version}-%{release}
Provides:       kiwi-filesystem-requires = %{version}-%{release}
Obsoletes:      kiwi-filesystem-requires < %{version}-%{release}
%if "%{_vendor}" != "debbuild"
Provides:       kiwi-image:pxe
Provides:       kiwi-image:kis
%if ! (0%{?rhel} >= 8)
Provides:       kiwi-filesystem:btrfs
%endif
Provides:       kiwi-filesystem:ext2
Provides:       kiwi-filesystem:ext3
Provides:       kiwi-filesystem:ext4
Provides:       kiwi-filesystem:squashfs
Provides:       kiwi-filesystem:xfs
%if ! (0%{?suse_version} && 0%{?suse_version} <= 1600)
Provides:       kiwi-filesystem:erofs
Provides:       kiwi-image:erofs
%endif
%endif
Requires:       dosfstools
Requires:       e2fsprogs
Requires:       xfsprogs
%if ! (0%{?suse_version} && 0%{?suse_version} <= 1600)
Requires:       erofs-utils
%endif
%if 0%{?suse_version}
Requires:       btrfsprogs
%else
%if ! (0%{?rhel} >= 8)
Requires:       btrfs-progs
%endif
%endif
%if 0%{?suse_version}
Requires:       squashfs
%else
Requires:       squashfs-tools
%endif
%if "%{_vendor}" == "debbuild"
Requires:       qemu-utils
%else
%if 0%{?suse_version}
Requires:       qemu-tools
%else
Requires:       qemu-img
%endif
%endif
Requires:       kiwi-systemdeps-core = %{version}-%{release}

%description -n kiwi-systemdeps-filesystems
Host setup helper to pull in all packages required/useful on
the build host to build filesystem images

%package -n kiwi-systemdeps-disk-images
Summary:        KIWI - host requirements for disk images
Group:          %{sysgroup}
Provides:       kiwi-image-oem-requires = %{version}-%{release}
Obsoletes:      kiwi-image-oem-requires < %{version}-%{release}
Provides:       kiwi-image-vmx-requires = %{version}-%{release}
Obsoletes:      kiwi-image-vmx-requires < %{version}-%{release}
%if "%{_vendor}" != "debbuild"
Provides:       kiwi-image:oem
Provides:       kiwi-image:vmx
%endif
Requires:       kiwi-systemdeps-filesystems = %{version}-%{release}
Requires:       kiwi-systemdeps-bootloaders = %{version}-%{release}
Requires:       kiwi-systemdeps-iso-media = %{version}-%{release}
%if 0%{?suse_version} >= 1650
Requires:       binutils
Requires:       glibc-gconv-modules-extra
%endif
%if 0%{?suse_version}
Requires:       gptfdisk
%else
Requires:       gdisk
%endif
Requires:       lvm2
Requires:       parted
Requires:       kpartx
Requires:       cryptsetup
Requires:       mdadm
Requires:       util-linux
# lsblk is part of util-linux-systemd on openSUSE
%if 0%{?suse_version}
Requires:       util-linux-systemd
%endif

%description -n kiwi-systemdeps-disk-images
Host setup helper to pull in all packages required/useful on
the build host to build disk images

%package -n kiwi-systemdeps-image-validation
Summary:        KIWI - host requirements for handling image descriptions better
Group:          %{sysgroup}
%if 0%{?fedora} || 0%{?rhel} >= 8 || 0%{?suse_version} || 0%{?debian} || 0%{?ubuntu}
Recommends:     jing
%endif
%if 0%{?fedora} || 0%{?rhel} >= 8 || 0%{?suse_version}
Requires:       python%{python3_pkgversion}-solv
%endif
%if ! (0%{?rhel} && 0%{?rhel} < 8)
Recommends:     python%{python3_pkgversion}-anymarkup-core
%endif

%description -n kiwi-systemdeps-image-validation
Host setup helper to pull in all packages required/useful on
the build host to handling image descriptions better. This also
includes reading of image descriptions for different markup
languages

%package -n kiwi-systemdeps
Summary:        KIWI - Host system dependencies
Group:          %{sysgroup}
Requires:       kiwi-systemdeps-core = %{version}-%{release}
Requires:       kiwi-systemdeps-bootloaders = %{version}-%{release}
%if 0%{?fedora} || 0%{?rhel} || 0%{?suse_version}
# None of the container build tools are available in Debian/Ubuntu
Requires:       kiwi-systemdeps-containers = %{version}-%{release}
Requires:       kiwi-systemdeps-containers-wsl = %{version}-%{release}
%endif
Requires:       kiwi-systemdeps-filesystems = %{version}-%{release}
Requires:       kiwi-systemdeps-disk-images = %{version}-%{release}
Requires:       kiwi-systemdeps-iso-media = %{version}-%{release}
%if 0%{?fedora} || 0%{?suse_version}
Requires:       kiwi-systemdeps-image-validation = %{version}-%{release}
%endif

%description -n kiwi-systemdeps
Host setup helper to pull in all packages required/useful to
leverage all functionality in KIWI.

# python3-kiwi
%package -n python%{python3_pkgversion}-kiwi
Summary:        KIWI - Appliance Builder Next Generation
Group:          %{pygroup}
%if "%{python3_pkgversion}" == "3"
%if 0%{?suse_version}
Provides:       python%{python3_version_nodots}-kiwi = %{version}-%{release}
%else
Provides:       python%{python3_version}-kiwi = %{version}-%{release}
%endif
%endif
Obsoletes:      python2-kiwi
Conflicts:      python2-kiwi
Conflicts:      kiwi-man-pages < %{version}
Requires:       screen
Requires:       file
Requires:       sed
Requires:       bash
Requires:       python%{python3_pkgversion} >= 3.9
%if 0%{?ubuntu} || 0%{?debian}
Requires:       python%{python3_pkgversion}-yaml
%else
Requires:       python%{python3_pkgversion}-PyYAML
%endif
Requires:       python%{python3_pkgversion}-simplejson
%if ! (0%{?fedora} >= 41 || 0%{?rhel} >= 10)
Requires:       python%{python3_pkgversion}-docopt
%else
Requires:       python%{python3_pkgversion}-docopt-ng
%endif
Requires:       python%{python3_pkgversion}-lxml
Requires:       python%{python3_pkgversion}-requests
Requires:       python%{python3_pkgversion}-xmltodict
%if ! (0%{?rhel} && 0%{?rhel} < 8)
Recommends:     kiwi-man-pages
%endif
%if "%{_vendor}" == "debbuild"
# Avoid issues with not being able to use magic Provides
Requires:       kiwi-systemdeps = %{version}-%{release}
%else
# Only require core dependencies, and allow OBS to pull the rest through magic Provides
Requires:       kiwi-systemdeps-core = %{version}-%{release}
%if ! 0%{?el7}
# Retain default expectation for local installations
Recommends:     kiwi-systemdeps = %{version}-%{release}
%endif
%endif

%description -n python%{python3_pkgversion}-kiwi
Python 3 library of the KIWI Image System. Provides an operating system
image builder for Linux supported hardware platforms as well as for
virtualization and cloud systems like Xen, KVM, VMware, EC2 and more.

%if "%{_vendor}" != "debbuild"
%ifarch %{ix86} x86_64
%package -n kiwi-pxeboot
Summary:        KIWI - PXE boot structure
Requires:       syslinux
%if 0%{?fedora} || 0%{?rhel}
Requires(pre):  shadow-utils
%else
Requires(pre):  shadow
%endif
%if 0%{?suse_version} >= 1550
Requires(pre):  user(tftp)
%endif
License:        GPL-3.0-or-later
Group:          %{sysgroup}

%description -n kiwi-pxeboot
This package contains the basic PXE directory structure which is
needed to serve kiwi built images via PXE.
%endif
%endif

%package -n dracut-kiwi-lib
Summary:        KIWI - Dracut kiwi Library
%if 0%{?fedora} || 0%{?rhel} || 0%{?suse_version} || 0%{?debian}
# Ubuntu 16.04 OBS environments refuse to set up due to
# initramfs-tools / dracut conflict and initramfs-tools is required
# to set up the build environment...
BuildRequires:  dracut
%endif
Requires:       bc
Requires:       cryptsetup
%if 0%{?fedora} || 0%{?rhel} || 0%{?ubuntu} >= 1804 || 0%{?debian} >= 9
%if 0%{?rhel} && 0%{?rhel} < 8
Requires:       btrfs-progs
%else
Recommends:     btrfs-progs
%endif
Requires:       gdisk
Requires:       dracut-network
%else
%if 0%{?debian} || 0%{?ubuntu}
Recommends:     btrfs-tools
Requires:       gdisk
%else
Requires:       btrfsprogs
Requires:       gptfdisk
%endif
%endif
Requires:       coreutils
Requires:       e2fsprogs
Requires:       grep
Requires:       lvm2
Requires:       mdadm
Requires:       util-linux
# lsblk is part of util-linux-systemd on openSUSE
%if 0%{?suse_version}
Requires:       util-linux-systemd
%endif
Requires:       xfsprogs
Requires:       dialog
Requires:       pv
Requires:       curl
%if 0%{?debian} || 0%{?ubuntu}
Requires:       xz-utils
Requires:       dmsetup
%else
Requires:       xz
Requires:       device-mapper
%endif
%ifarch s390 s390x
%if 0%{?fedora} || 0%{?rhel}
Requires:       s390utils
%else
Requires:       s390-tools
%endif
Requires:       parted
%endif
License:        GPL-3.0-or-later
Group:          %{sysgroup}

%description -n dracut-kiwi-lib
This package contains a collection of methods to provide a library
for tasks done in other kiwi dracut modules

%package -n dracut-kiwi-oem-repart
Summary:        KIWI - Dracut module for oem(repart) image type
%if 0%{?fedora} || 0%{?rhel} || 0%{?suse_version} || 0%{?debian}
# Ubuntu 16.04 OBS environments refuse to set up due to
# initramfs-tools / dracut conflict and initramfs-tools is required
# to set up the build environment...
BuildRequires:  dracut
%endif
Requires:       dracut-kiwi-lib = %{version}-%{release}
License:        GPL-3.0-or-later
Group:          %{sysgroup}

%description -n dracut-kiwi-oem-repart
This package contains the kiwi-repart dracut module which is
used to repartition the oem disk image to the current disk
geometry according to the setup in the kiwi image configuration

%package -n dracut-kiwi-oem-dump
Summary:        KIWI - Dracut module for oem(install) image type
%if 0%{?fedora} || 0%{?rhel} || 0%{?suse_version} || 0%{?debian}
# Ubuntu 16.04 OBS environments refuse to set up due to
# initramfs-tools / dracut conflict and initramfs-tools is required
# to set up the build environment...
BuildRequires:  dracut
%endif
Requires:       dracut-kiwi-lib = %{version}-%{release}
Requires:       kexec-tools
Requires:       gawk
Requires:       kpartx
License:        GPL-3.0-or-later
Group:          %{sysgroup}

%description -n dracut-kiwi-oem-dump
This package contains the kiwi-dump and kiwi-dump-reboot dracut
modules which is used to install an oem image onto a target disk.
It implements a simple installer which allows for user selected
target disk or unattended installation to target. The source of
the image to install could be either from media(CD/DVD/USB) or
from remote

%package -n dracut-kiwi-live
Summary:        KIWI - Dracut module for iso(live) image type
%if 0%{?fedora} || 0%{?rhel} || 0%{?suse_version} || 0%{?debian}
# Ubuntu 16.04 OBS environments refuse to set up due to
# initramfs-tools / dracut conflict and initramfs-tools is required
# to set up the build environment...
BuildRequires:  dracut
%endif
Requires:       dialog
Requires:       xfsprogs
Requires:       e2fsprogs
Requires:       util-linux
# lsblk is part of util-linux-systemd on openSUSE
%if 0%{?suse_version}
Requires:       util-linux-systemd
%endif
%if 0%{?debian} || 0%{?ubuntu}
Requires:       dmsetup
Requires:       dracut-network
%endif
%if 0%{?fedora} || 0%{?rhel}
Requires:       device-mapper
Requires:       dracut-network
%endif
%if 0%{?suse_version}
Requires:       device-mapper
%endif
Requires:       dracut
License:        GPL-3.0-or-later
Group:          %{sysgroup}

%description -n dracut-kiwi-live
This package contains the kiwi-live dracut module which is used
for booting iso(live) images built with KIWI

%package -n dracut-kiwi-overlay
Summary:        KIWI - Dracut module for vmx(+overlay) image type
%if 0%{?fedora} || 0%{?rhel} || 0%{?suse_version} || 0%{?debian}
# Ubuntu 16.04 OBS environments refuse to set up due to
# initramfs-tools / dracut conflict and initramfs-tools is required
# to set up the build environment...
BuildRequires:  dracut
%endif
Requires:       dracut-kiwi-lib = %{version}-%{release}
Requires:       dracut
License:        GPL-3.0-or-later
Group:          %{sysgroup}

%description -n dracut-kiwi-overlay
This package contains the kiwi-overlay dracut module which is used
for booting vmx images built with KIWI and configured to use an
overlay root filesystem

%package -n dracut-kiwi-verity
Summary:        KIWI - Dracut module for disk with embedded verity metadata
%if 0%{?fedora} || 0%{?rhel} || 0%{?suse_version} || 0%{?debian}
# Ubuntu 16.04 OBS environments refuse to set up due to
# initramfs-tools / dracut conflict and initramfs-tools is required
# to set up the build environment...
BuildRequires:  dracut
%endif
Requires:       dracut-kiwi-lib = %{version}-%{release}
Requires:       dracut
BuildRequires:  gcc
License:        GPL-3.0-or-later
Group:          %{sysgroup}

%description -n dracut-kiwi-verity
This package contains the kiwi-verity dracut module which is used
for booting oem images built with KIWI and configured to use an
embedded verity metadata block via the embed_verity_metadata
type attribute

%package -n kiwi-man-pages
Summary:        KIWI - manual pages
License:        GPL-3.0-or-later
Group:          %{sysgroup}

%description -n kiwi-man-pages
Provides manual pages to describe the kiwi commands

%package -n kiwi-bash-completion
Summary:        Bash Completion for kiwi-ng
Requires:       bash-completion
Requires:       python%{python3_pkgversion}-kiwi = %{version}
%if ! (0%{?debian} || 0%{?ubuntu})
Supplements:    (%{name} and bash-completion)
%endif
BuildArch:      noarch

%description -n kiwi-bash-completion
Bash command line completion support for python-kiwi - completion
of subcommands, parameters and keywords for the kiwi-ng command.

%prep
%setup -q -n kiwi-%{version}

%if 0%{?suse_version}
# Temporarily revert grub-bls default to false for SUSE distributions
%patch -P 1001 -p1
%endif

# Temporarily switch things back to docopt for everything but Fedora 41+
# FIXME: Drop this hack as soon as we can...
%if ! (0%{?fedora} >= 41 || 0%{?rhel} >= 10)
sed -e 's/docopt-ng.*/docopt = ">=0.6.2"/' -i pyproject.toml
%endif

# Drop shebang for kiwi/xml_parse.py, as we don't intend to use it
# as an independent script
sed -e "s|#!/usr/bin/env python||" -i kiwi/xml_parse.py

# Build documentation
make -C doc man

# Build application wheel
%{__python3} -m build --no-isolation --wheel

%install
# Install application
%{__python3} -m installer --destdir %{buildroot} %{?is_deb:--no-compile-bytecode} dist/*.whl

%if 0%{?is_deb}
# Fix where files were installed
mv %{buildroot}%{_prefix}/local/* %{buildroot}%{_prefix}
mv %{buildroot}%{_prefix}/lib/python3* %{buildroot}%{_prefix}/lib/python3
%endif

# Install man-pages, completion and kiwi default configuration
make buildroot=%{buildroot}/ python=%{__python3} install

# Install dracut modules
make buildroot=%{buildroot}/ python=%{__python3} install_dracut

# Install documentation README / LICENSE
make buildroot=%{buildroot}/ docdir=%{_defaultdocdir}/ python=%{__python3} install_package_docs

# Create symlinks for correct binaries
ln -sr %{buildroot}%{_bindir}/kiwi-ng %{buildroot}%{_bindir}/kiwi
ln -sr %{buildroot}%{_bindir}/kiwi-ng %{buildroot}%{_bindir}/kiwi-ng-3

%if "%{_vendor}" != "debbuild"
# kiwi pxeboot directory structure to be packed in kiwi-pxeboot
%ifarch %{ix86} x86_64
for i in KIWI pxelinux.cfg image upload boot; do \
    mkdir -p %{buildroot}/srv/tftpboot/$i ;\
done
%endif
%endif

%if 0%{?fedora} || 0%{?suse_version}
%fdupes %{buildroot}/srv/tftpboot
%endif

%if "%{_vendor}" != "debbuild" && 0%{?suse_version} < 1550
%ifarch %{ix86} x86_64
%pre -n kiwi-pxeboot
#============================================================
# create user and group tftp if they does not exist
if ! /usr/bin/getent group tftp >/dev/null; then
    %{_sbindir}/groupadd -r tftp
fi
if ! /usr/bin/getent passwd tftp >/dev/null; then
    %{_sbindir}/useradd -c "TFTP account" -d /srv/tftpboot -G tftp -g tftp \
        -r -s /bin/false tftp
fi
%endif
%endif

%files -n kiwi-systemdeps-core
# Empty metapackage

%files -n kiwi-systemdeps-bootloaders
# Empty metapackage

%files -n kiwi-systemdeps-containers
# Empty metapackage

%files -n kiwi-systemdeps-containers-wsl
# Empty metapackage

%files -n kiwi-systemdeps-iso-media
# Empty metapackage

%files -n kiwi-systemdeps-filesystems
# Empty metapackage

%files -n kiwi-systemdeps-disk-images
# Empty metapackage

%files -n kiwi-systemdeps-image-validation
# Empty metapackage

%files -n kiwi-systemdeps
# Empty metapackage

%files -n python%{python3_pkgversion}-kiwi
%dir %{_defaultdocdir}/python-kiwi
%dir %{_usr}/share/kiwi
%{_bindir}/kiwi
%{_bindir}/kiwi-ng
%{_bindir}/kiwi-ng-3*
%{python3_sitelib}/kiwi*
%{_usr}/share/kiwi/xsl_to_v74/
%{_defaultdocdir}/python-kiwi/LICENSE
%{_defaultdocdir}/python-kiwi/README

%files -n kiwi-bash-completion
%{_usr}/share/bash-completion/completions/kiwi-ng

%files -n kiwi-man-pages
%config %_sysconfdir/kiwi.yml
%doc %{_mandir}/man8/*

%files -n dracut-kiwi-lib
%{_usr}/lib/dracut/modules.d/99kiwi-lib

%files -n dracut-kiwi-oem-repart
%{_usr}/lib/dracut/modules.d/90kiwi-repart

%files -n dracut-kiwi-oem-dump
%{_usr}/lib/dracut/modules.d/90kiwi-dump
%{_usr}/lib/dracut/modules.d/99kiwi-dump-reboot

%files -n dracut-kiwi-live
%{_usr}/lib/dracut/modules.d/90kiwi-live

%files -n dracut-kiwi-overlay
%{_usr}/lib/dracut/modules.d/90kiwi-overlay

%files -n dracut-kiwi-verity
%{_usr}/lib/dracut/modules.d/80kiwi-verity
%{_bindir}/kiwi-parse-verity

%if "%{_vendor}" != "debbuild"
%ifarch %{ix86} x86_64
%files -n kiwi-pxeboot
%if 0%{?suse_version} < 1550
%dir %attr(0755,tftp,tftp) /srv/tftpboot
%endif
%dir /srv/tftpboot/KIWI
%dir /srv/tftpboot/pxelinux.cfg
%dir /srv/tftpboot/image
%dir /srv/tftpboot/upload
%dir /srv/tftpboot/boot
%endif
%endif

%changelog
