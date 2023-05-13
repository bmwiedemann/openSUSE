#
# spec file for package gasket-driver
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
# Please submit bugfixes or comments via https://bugs.opensuse.org/

#===
# Packaging Notes:
#
# For information on building KMPs see:
# https://documentation.suse.com/sbp/all/single-html/SBP-KMP-Manual-SLE12SP2
# https://en.opensuse.org/Kernel_Module_Packages
#
# For information on `sysusers` macros used to create the `apex` group see:
# https://en.opensuse.org/openSUSE:Packaging_guidelines#Users_and_Groups
#---

# The following directive ensures the package will build correctly on OBS if it
# builds locally without problems. See:
# https://en.opensuse.org/openSUSE:Build_Service_Tips_and_Tricks#Permission_denied_errors
#
# norootforbuild

Name:           gasket-driver
Version:        1.0.18
Release:        0
Summary:        The Coral Gasket Driver allows usage of the Coral EdgeTPU on Linux systems
License:        GPL-2.0-only
Group:          System/Kernel
URL:            https://github.com/google/gasket-driver
Source0:        %{name}-%{version}.tar.xz
Source1:        group.conf
Source2:        preamble
Source3:        gasket-driver-rpmlintrc
BuildRequires:  %kernel_module_package_buildreqs
BuildRequires:  sysuser-tools
BuildRequires:  pesign-obs-integration
Requires:       %{name}-kmp
%sysusers_requires

# The dma-buf symbols used by this driver were moved into their own `DMA_BUF`
# module namespace in kernel 5.16. Consequently, the upstream source conditionally
# imports the `DMA_BUF` module namespace if the kernel version is >= 5.16.
# This patch removes that condition, allowing this module to be built for kernels
# that have backported the `DMA_BUF` namespace changes.
# See:
# https://github.com/google/gasket-driver/pull/10
# https://github.com/google/gasket-driver/commit/a87c105c14e826dafd4b25c36fa7c7c657a7ad03.patch
# PATCH-FIX-OPENSUSE fix-for-backported-dma-buf-ns.patch gh#google/gasket-driver!10
Patch0: fix-for-backported-dma-buf-ns.patch

# This directive instructs the build service to temporarily save the project's
# certificate as %%_sourcedir/_projectcert.crt. See:
# https://github.com/openSUSE/pesign-obs-integration
# https://documentation.suse.com/sbp/all/html/SBP-KMP-Manual/index.html#sec-signing-module-object
# https://documentation.suse.com/sbp/all/html/SBP-KMP-Manual/index.html#sec-appendix-a1
#
# needssslcertforbuild
#
# Having included the above directive, using the `-c` flag below will cause
# the "ueficert" package to get built. `%%_sourcedir` must be prefixed as the
# working dir is changed before the build service attempts to source the certificate.
%kernel_module_package -p preamble -c %_sourcedir/_projectcert.crt

%description
The Coral Gasket Driver allows usage of the Coral EdgeTPU on Linux systems.
The driver contains two modules: 
- Gasket (Google ASIC Software, Kernel Extensions, and Tools) is a top level driver
  for lightweight communication with Google ASICs.
- Apex refers to the EdgeTPU v1.

# This magic "KMP" subpackage is documented in 
# https://en.opensuse.org/Kernel_Module_Packages#Specfile_mechanisms
%package KMP
Summary:        Gasket Driver kernel modules  
Group:          System/Kernel

%description KMP
The Linux Kernel Module Package for the Coral Gasket Driver.

%prep
%setup -q
mkdir -p obj

# The `DMA_BUF` module namespace has been backported to the 5.14 kernel used
# in Leap 15.5, so apply the relevant patch. 
%if 0%{?sle_version} == 150500
%patch0 -p1
%endif

%build
# Build the kernel modules.
for flavor in %flavors_to_build; do
       rm -rf obj/$flavor
       cp -r src obj/$flavor
       make -C %{kernel_source $flavor} modules M=$PWD/obj/$flavor
done
# Generate content to be used by the `%%pre` scriptlet.
%sysusers_generate_pre %{SOURCE1} group group.conf

# Execute the system group scriptlet generated at build time.
%pre -f group.pre

%install
# Install the kernel modules.
export INSTALL_MOD_PATH=%{buildroot}
export INSTALL_MOD_DIR=updates
for flavor in %flavors_to_build; do
       make -C %{kernel_source $flavor} modules_install M=$PWD/obj/$flavor
done
# Install the system group used by the driver. 
mkdir -p %{buildroot}%{_sysusersdir}
install -m 0644 %{SOURCE1} -D %{buildroot}%{_sysusersdir}/group-apex.conf
# Install the udev rules defined in the module source.
install -D -m 644 debian/gasket-dkms.udev %buildroot%{_udevrulesdir}/70-apex.rules

# These env vars are used by the `pesign-obs-integration` package when signing
# the modules for Secure Boot.
export BRP_PESIGN_FILES='*.ko'
export BRP_PESIGN_COMPRESS_MODULE="xz"

%files
%license LICENSE
%doc README.md CONTRIBUTING.md
%{_sysusersdir}/group-apex.conf
%{_udevrulesdir}/70-apex.rules

%changelog

