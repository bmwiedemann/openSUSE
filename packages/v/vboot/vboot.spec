#
# spec file for package vboot
#
# Copyright (c) 2020 SUSE LLC
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


%define major_version 78
%define minor_version 12499
Name:           vboot
Version:        %{major_version}.%{minor_version}
Release:        0
Summary:        Chromium vboot
License:        BSD-3-Clause
Group:          Development/Tools/Other
URL:            https://git.chromium.org/git/chromiumos/platform/vboot_reference.git
# Source:         https://chromium.googlesource.com/chromiumos/platform/vboot_reference.git/+archive/release-R%{major_version}-%{minor_version}.B.tar.gz
Source:         release-R%{major_version}-%{minor_version}.B.tar.gz
# Disable static builds
Patch1:         fix_Makefile.patch
Patch2:         Fix-arch-detection-for-armv6.patch
Patch3:         reproducible.patch
Patch4:         fix_vboot_version.patch
BuildRequires:  gcc-c++
BuildRequires:  libgnutls-devel
BuildRequires:  libuuid-devel
BuildRequires:  libyaml-devel
BuildRequires:  python
BuildRequires:  trousers-devel
BuildRequires:  xz-devel
ExcludeArch:    ppc ppc64 ppc64le riscv64

%description
VBoot contains verified boot reference implementation and
helper tools for Chrome OS devices.

%prep
%setup -q -c
%patch1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
export CFLAGS="-D_GNU_SOURCE %{optflags}"
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}%{_prefix}
install -d -m 755 %{buildroot}/%{_datadir}/%{name}/devkeys/
cp -ar tests/devkeys/* %{buildroot}/%{_datadir}/%{name}/devkeys/

rm -f %{buildroot}%{_prefix}/default/vboot_reference
rm -f %{buildroot}%{_prefix}/lib/pkgconfig/vboot_host.pc

%files
%doc README LICENSE
%{_bindir}/chromeos-tpm-recovery
%{_bindir}/cgpt
%{_bindir}/common_minimal.sh
%{_bindir}/crossystem
%{_bindir}/dev_debug_vboot
%{_bindir}/dev_make_keypair
%{_bindir}/dumpRSAPublicKey
%{_bindir}/dump_fmap
%{_bindir}/dump_kernel_config
%{_bindir}/enable_dev_usb_boot
%{_bindir}/futility
%{_bindir}/gbb_flags_common.sh
%{_bindir}/gbb_utility
%{_bindir}/get_gbb_flags.sh
%{_bindir}/load_kernel_test
%{_bindir}/make_dev_firmware.sh
%{_bindir}/make_dev_ssd.sh
%{_bindir}/pad_digest_utility
%{_bindir}/resign_firmwarefd.sh
%{_bindir}/set_gbb_flags.sh
%{_bindir}/signature_digest_utility
%{_bindir}/tpm-nvsize
%{_bindir}/tpmc
%{_bindir}/vbutil_firmware
%{_bindir}/vbutil_kernel
%{_bindir}/vbutil_key
%{_bindir}/vbutil_keyblock
%{_bindir}/vbutil_what_keys
%{_bindir}/verify_data
%{_datadir}/%{name}

%changelog
