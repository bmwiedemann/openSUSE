%define _buildshell /bin/bash

%define sbver   1.16.3_3_g3d33c746

%define srcdir %{_builddir}/%buildsubdir
%define blddir %srcdir/build

%define build_x86_firmware 0
%define build_ppc_firmware 0
%define build_opensbi_firmware 0
%define kvm_available 0
%define legacy_qemu_kvm 0
%define force_fit_virtio_pxe_rom 1

%define with_xen 0%{!?_without_xen:1}

%if "%{?distribution}" == ""
%define distro private-build
%else
%define distro %{distribution}
%endif

# Items to exclude in ALP-based products
%if 0%{?suse_version} == 1600
%define with_xen 0
%endif

%bcond_with system_membarrier
%bcond_with malloc_trim

%bcond_with chkqtests

%if 0%{?suse_version} > 1600
# canokey is an openSUSE thing, not a SLE one
%ifarch x86_64
%bcond_without canokey
%else
%bcond_with canokey
%endif
%endif

%if 0%{?suse_version} > 1600
# XDP seems not to be there in SLE...
%bcond_without xdp
%else
%bcond_with xdp
%endif

%ifarch %ix86 x86_64
%bcond_without vmsr_helper
%else
%define vmsr_helper 0
%endif

# Make it possible to build without spice (for SLE/Leap Micro)
%bcond_without spice

# We do not have the stuff needed to compile rutabaga support.
# If/when we want to do it, we can check how it's done here:
#  https://src.fedoraproject.org/rpms/qemu/c/deeb9357cb751df21c566fd8408936cfb034d43b?branch=rawhide
%define has_rutabaga_gfx 0

%define has_virtiofsd 1
# Upstream virtiofsd does not even build on 32 bit systems
%ifarch %ix86 %arm
%define has_virtiofsd 0
%endif

# non-x86 archs still seem to have some issues with Link Time Optimization
%ifnarch %ix86 x86_64
%define _lto_cflags %{nil}
%endif

%ifarch aarch64
%define qemu_arch aarch64
%endif
%ifarch %arm
%define qemu_arch arm
%endif
%ifarch %ix86
%define qemu_arch i386
%endif
%ifarch ppc64
%define qemu_arch ppc64
%endif
%ifarch ppc
%define qemu_arch ppc
%endif
%ifarch ppc64le
%define qemu_arch ppc64le
%endif
%ifarch riscv64
%define qemu_arch riscv64
%endif
%ifarch s390x
%define qemu_arch s390x
%endif
%ifarch x86_64
%define qemu_arch x86_64
%endif

%define generic_qemu_description \
QEMU provides full machine emulation and cross architecture usage. It closely\
integrates with KVM and Xen virtualization, allowing for excellent performance.\
Many options are available for defining the emulated environment, including\
traditional devices, direct host device access, and interfaces specific to\
virtualization.

%define disable_everything	\\\
 --audio-drv-list=		\\\
 --disable-af-xdp		\\\
 --disable-alsa			\\\
 --disable-asan			\\\
 --disable-attr			\\\
 --disable-auth-pam		\\\
 --disable-avx2			\\\
 --disable-avx512bw		\\\
 --disable-blkio		\\\
 --disable-block-drv-whitelist-in-tools	\\\
 --disable-bochs		\\\
 --disable-bpf			\\\
 --disable-brlapi		\\\
 --disable-bsd-user		\\\
 --disable-bzip2		\\\
 --disable-cap-ng		\\\
 --disable-capstone		\\\
 --disable-cfi			\\\
 --disable-cfi-debug		\\\
 --disable-cloop		\\\
 --disable-cocoa		\\\
 --disable-colo-proxy		\\\
 --disable-coreaudio		\\\
 --disable-coroutine-pool	\\\
 --disable-crypto-afalg		\\\
 --disable-curl			\\\
 --disable-curses		\\\
 --disable-dbus-display		\\\
 --disable-debug-graph-lock	\\\
 --disable-debug-info		\\\
 --disable-debug-mutex		\\\
 --disable-debug-remap		\\\
 --disable-debug-tcg		\\\
 --disable-dmg			\\\
 --disable-docs			\\\
 --disable-download		\\\
 --disable-dsound		\\\
 --disable-fdt			\\\
 --disable-fuse			\\\
 --disable-fuse-lseek		\\\
 --disable-gcrypt		\\\
 --disable-gettext		\\\
 --disable-gio			\\\
 --disable-glusterfs		\\\
 --disable-gnutls		\\\
 --disable-gtk			\\\
 --disable-gtk-clipboard	\\\
 --disable-guest-agent		\\\
 --disable-guest-agent-msi	\\\
 --disable-hv-balloon		\\\
 --disable-hvf			\\\
 --disable-iconv		\\\
 --disable-jack			\\\
 --disable-kvm			\\\
 --disable-l2tpv3		\\\
 --disable-libcbor		\\\
 --disable-libdaxctl		\\\
 --disable-libdw		\\\
 --disable-libiscsi		\\\
 --disable-libkeyutils		\\\
 --disable-libkeyutils 		\\\
 --disable-libnfs 		\\\
 --disable-libpmem 		\\\
 --disable-libssh 		\\\
 --disable-libudev 		\\\
 --disable-libusb 		\\\
 --disable-linux-aio 		\\\
 --disable-linux-io-uring 	\\\
 --disable-linux-user 		\\\
 --disable-lto 			\\\
 --disable-lzfse 		\\\
 --disable-lzo 			\\\
 --disable-malloc-trim 		\\\
 --disable-membarrier 		\\\
 --disable-module-upgrades 	\\\
 --disable-modules 		\\\
 --disable-mpath 		\\\
 --disable-multiprocess 	\\\
 --disable-netmap 		\\\
 --disable-nettle 		\\\
 --disable-numa 		\\\
 --disable-nvmm 		\\\
 --disable-opengl 		\\\
 --disable-oss 			\\\
 --disable-pa 			\\\
 --disable-parallels 		\\\
 --disable-pie 			\\\
 --disable-pipewire 		\\\
 --disable-pixman		\\\
 --disable-plugins		\\\
 --disable-png			\\\
 --disable-qcow1		\\\
 --disable-qed			\\\
 --disable-qom-cast-debug	\\\
 --disable-qpl			\\\
 --disable-rbd			\\\
 --disable-rdma			\\\
 --disable-relocatable		\\\
 --disable-replication		\\\
 --disable-rng-none		\\\
 --disable-rust			\\\
 --disable-rutabaga-gfx		\\\
 --disable-safe-stack		\\\
 --disable-sdl			\\\
 --disable-sdl-image		\\\
 --disable-seccomp		\\\
 --disable-selinux		\\\
 --disable-slirp		\\\
 --disable-slirp-smbd		\\\
 --disable-smartcard		\\\
 --disable-snappy		\\\
 --disable-sndio		\\\
 --disable-sparse		\\\
 --disable-spice		\\\
 --disable-spice-protocol	\\\
 --disable-strict-rust-lints	\\\
 --disable-strip		\\\
 --disable-system		\\\
 --disable-tcg			\\\
 --disable-tcg-interpreter	\\\
 --disable-tools		\\\
 --disable-tpm			\\\
 --disable-tsan			\\\
 --disable-u2f			\\\
 --disable-uadk			\\\
 --disable-ubsan		\\\
 --disable-usb-redir		\\\
 --disable-user			\\\
 --disable-vde			\\\
 --disable-vdi			\\\
 --disable-vhdx			\\\
 --disable-vhost-crypto		\\\
 --disable-vhost-kernel		\\\
 --disable-vhost-net		\\\
 --disable-vhost-user		\\\
 --disable-vhost-user-blk-server \\\
 --disable-vhost-vdpa		\\\
 --disable-virglrenderer	\\\
 --disable-virtfs 		\\\
 --disable-vnc			\\\
 --disable-vnc-jpeg 		\\\
 --disable-vnc-sasl		\\\
 --disable-vpc			\\\
 --disable-vte 			\\\
 --disable-vvfat		\\\
 --disable-werror		\\\
 --disable-whpx			\\\
 --disable-xen			\\\
 --disable-xen-pci-passthrough	\\\
 --disable-xkbcommon		\\\
 --disable-zstd			\\\
 --without-default-devices
