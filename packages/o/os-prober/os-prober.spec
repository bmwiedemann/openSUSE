#
# spec file for package os-prober
#
# Copyright (c) 2022 SUSE LLC
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


Name:           os-prober
Version:        1.81
Release:        0
Summary:        Probes disks on the system for installed operating systems
License:        GPL-2.0-or-later
Group:          System/Boot
URL:            https://salsa.debian.org/installer-team/os-prober
Source0:        https://salsa.debian.org/installer-team/os-prober/-/archive/%{version}/%{name}-%{version}.tar.bz2
Source1:        COPYING-note.txt
# move newns binary outside of os-prober subdirectory, so that debuginfo
# can be automatically generated for it
Patch0:         os-prober-newnsdirfix.patch
# PATCH-FIX-OPENSUSE: Fix spelling of SUSE aj@suse.de
Patch1:         os-prober-SUSE.patch
# PATCH-FIX-OPENSUSE: Fix parsing of grub.cfg [bnc#796919]
Patch3:         os-prober-1.49-fix-grub2.cfg-parsing.patch
# PATCH-FIX-OPENSUSE: Use correct name for grub2-mount
Patch5:         os-prober-1.49-grub2-mount.patch
# PATCH-FIX-OPENSUSE: Probe also unpartitioned Linux MD devices (bnc#811006)
Patch7:         os-prober-probe-MD-devices.patch
# PATCH-FIX-OPENSUSE: Detect linux secure boot entries too (bnc#810912)
Patch8:         os-prober-linux-secure-boot.patch
# PATCH-FIX-OPENSUSE: btrfs support from Fedora (rediffed)
Patch9:         os-prober-btrfsfix.patch
# PATCH-FIX-OPENSUSE: difference between upstream and our previous scripts
Patch10:        os-prober-EFI-openSUSEfy.patch
# PATCH-FIX-OPENSUSE: accept ESP on IMSM MD raid (bnc#818871)
Patch11:        os-prober-accept-ESP-on-IMSM.patch
# PATCH-FIX-OPENSUSE: don't modprobe all file system modules and don't test mount on unknown partition (bnc#851722)
Patch12:        os-prober-dont-load-all-fs-module-and-dont-test-mount.patch
# PATCH-FIX-OPENSUSE: fix os-prober entries for distro on btrfs root-fs not created (bnc#846003)
Patch13:        os-prober-fix-btrfs-subvol-mounted-tests.patch
# PATCH-FIX-SLE: fix os-prober creates many unusuable entries on multipath disk (bnc#875327)
Patch14:        os-prober-skip-part-on-multipath.patch
# PATCH-FIX-SLE: fix os-prober fails to detect other SLES12 installation (bsc#892364)
Patch17:        Improve-btrfs-handling-on-os-probing-for-grub2.patch
# PATCH-FIX-SLE: fix os-prober mount error, no such file or directory (bsc#931955)
Patch18:        os-prober-btrfs-absolute-subvol.patch
# PATCH-FIX-OPENSUSE: also skip legacy grub if /boot/grub2/grub.cfg is present
Patch19:        os-prober-40grub-check-grub2.patch
# PATCH-FIX-OPENSUSE: detect os on default subvolume in snapshot (bsc#954225)
Patch21:        os-prober-btrfs-snapshot-detection.patch
# PATCH-FIX-OPENSUSE: os-prober update broke Linux detection (bsc#957018)
Patch22:        os-prober-btrfs-always-detect-default.patch
# PATCH-FIX-OPENSUSE: y2base runs at 100% cpu busy from beginning in installation of files to completion (bsc#953987)
Patch23:        os-prober-linux-distro-avoid-expensive-ld-file-test.patch
# PATCH-FIX-OPENSUSE: Leap does not recognize Tumbleweed any more (bsc#997465)
Patch24:        os-prober-linux-distro-parse-os-release.patch
# PATCH-FIX-OPENSUSE: Windows 10 is not listed in the grub menu (bsc#1076779)
Patch25:        os-prober-05efi-blkid.patch
# PATCH-FIX-OPENSUSE: os-prober unconditionally pulls btrfsprogs (boo#1118279)
Patch27:        os-prober-make-btrfsprogs-optional.patch
# PATCH-FIX-OPENSUSE: os-prober isn't compatible with transactional update (boo#1125729)
# PATCH-FIX-OPENSUSE: os-prober deletes subvolume on btrfs disk (boo#1130669)
Patch28:        os-prober-use-tmp-over-var-lib-for-transient-files.patch
# PATCH-FIX-OPENSUSE: Two TW selections is shown in GRUB after installing system with multi-device Btrfs (bsc#1142858)
Patch29:        os-prober-btrfs-multiple-device.patch
# PATCH-FIX-OPENSUSE: 40grub2: debug messages (bsc#1101735)
Patch30:        os-prober-disable-debug.patch
Requires:       /bin/grep
Requires:       /bin/sed
Requires:       /sbin/modprobe
Requires:       coreutils
Requires:       udev
Requires:       util-linux
Recommends:     dmraid
Suggests:       lvm2
Suggests:       btrfsprogs
%if 0%{?suse_version} >= 1315
# For logger utility
Requires:       util-linux-systemd
%endif

%description
This package detects other OSes available on a system and outputs the results
in a generic machine-readable format. Support for new OSes and Linux
distributions can be added easily.

%prep
%autosetup -p1
cp %{SOURCE1} .
find . -name \*.orig -delete

%build
make %{?_smp_mflags} CC="gcc" CFLAGS="%{optflags}"

%install
install -m 0755 -d %{buildroot}%{_bindir}
# See also boo#1125729, we no longer use /var/lib/os-prober for runtime
# temporary files, but to keep compatible with upstream runtime we still keep
# it in place.
install -m 0755 -d %{buildroot}%{_localstatedir}/lib/%{name}

install -m 0755 -p os-prober linux-boot-prober %{buildroot}%{_bindir}
install -m 0755 -Dp newns %{buildroot}%{_prefix}/lib/newns
install -m 0644 -Dp common.sh %{buildroot}%{_datadir}/%{name}/common.sh

%ifarch m68k
ARCH=m68k
%endif
%ifarch ppc ppc64
ARCH=powerpc
%endif
%ifarch sparc sparc64
ARCH=sparc
%endif
%ifarch %ix86 x86_64
ARCH=x86
%endif

for probes in os-probes os-probes/mounted os-probes/init \
              linux-boot-probes linux-boot-probes/mounted; do
        install -m 755 -d %{buildroot}%{_prefix}/lib/$probes
        cp -a $probes/common/* %{buildroot}%{_prefix}/lib/$probes
        if [ -e "$probes/$ARCH" ]; then
                cp -a $probes/$ARCH/* %{buildroot}%{_prefix}/lib/$probes
        fi
done
if [ "$ARCH" = x86 ]; then
        install -m 755 -p os-probes/mounted/powerpc/20macosx \
            %{buildroot}%{_prefix}/lib/os-probes/mounted
fi

%files
%defattr(-,root,root,-)
%doc README TODO debian/copyright debian/changelog COPYING-note.txt
%{_bindir}/*
%{_prefix}/lib/linux-boot-probes
%{_prefix}/lib/newns
%{_prefix}/lib/os-probes
%{_datadir}/%{name}
%{_localstatedir}/lib/%{name}

%changelog
