%define _buildshell /bin/bash

%define sbver   1.16.3_3_ga95067eb

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

%define generic_qemu_description \
QEMU provides full machine emulation and cross architecture usage. It closely\
integrates with KVM and Xen virtualization, allowing for excellent performance.\
Many options are available for defining the emulated environment, including\
traditional devices, direct host device access, and interfaces specific to\
virtualization.

