#
# spec file
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


%if "@BUILD_FLAVOR@" == "kmp"
### macros for virtualbox-kmp ###
%define main_package 0
%define kmp_package 1
%define name_suffix kmp
%define dash -
%define package_summary Kernel modules for VirtualBox
%define package_group System/Kernel
%if %{undefined kernel_module_directory}
%define kernel_module_directory /lib/modules
%endif
%else
### macros for virtualbox main package ###
%define main_package 1
%define kmp_package 0
%define package_summary VirtualBox is an Emulator
%define package_group System/Emulators/PC
%define qt5ver %(rpm -q --queryformat %%{version} libQt5Core5|perl -ne '/(\\d+)\\.(\\d+)\\.(\\d+)?/&&printf "%%d%%02d%%02d\\n",$1,$2,$3')
#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
%if ! %{defined _distconfdir}
%define _distconfdir %{_sysconfdir}
%endif
# Do not provide libGL.so symbols - they are owned by Mesa already and this could potentially confuse rpm/zypp
%global __provides_exclude ^libE?GL.so.1.*$
# With 32-bit builds, the job limit cannot be larger than 2, otherwise the build runs out of memory.
# For 64-bit builds, no memory limit is reached when more jobs are run, but the builds crash with strange errors.
# For the above reasons, limit the number of jobs to 2.
%define _vbox_instdir %{_prefix}/lib/virtualbox
%define _udevrulesdir %{_prefix}/lib/udev/rules.d
%endif
# ********* If the VB version exceeds 6.1.x, notify the libvirt maintainer!!
Name:           virtualbox%{?dash}%{?name_suffix}
Version:        7.0.4
Release:        0
Summary:        %{package_summary}
# FIXME: use correct group or remove it, see "https://en.opensuse.org/openSUSE:Package_group_guidelines"
License:        GPL-2.0-or-later
# FIXME: use correct group or remove it, see "https://en.opensuse.org/openSUSE:Package_group_guidelines"
Group:          %{package_group}
URL:            https://www.virtualbox.org/
#
# so you don't need to repack virtualbox by hand, just add new release of VirtualBox-x.x.x.tar.bz2 and line below with
# script virtualbox-patch-source.sh will do the job :)
# WARNING: This is not a comment, but the real command to repack source
#%%(bash %%{_sourcedir}/virtualbox-patch-source.sh VirtualBox-%%{version}.tar.bz2)
Source0:        VirtualBox-%{version}-patched.tar.bz2
Source1:        UserManual.pdf
Source3:        virtualbox-60-vboxguest.rules
Source4:        virtualbox-default.virtualbox
Source5:        virtualbox-kmp-files
Source7:        virtualbox-kmp-preamble
Source8:        update-extpack.sh
Source9:        virtualbox-wrapper.sh
Source10:       virtualbox-LocalConfig.kmk
Source11:       virtualbox-60-vboxdrv.rules
Source12:       vboxclient.service
Source13:       vboxservice.service
Source14:       vboxdrv.service
Source15:       vboxadd-service.service
Source16:       vboxconfig.sh
Source17:       vboxguestconfig.sh
Source18:       fix_usb_rules.sh
Source19:       vboxdrv.sh
Source20:       README.autostart
Source21:       vboxweb-service.service
Source22:       vboxweb-service.sh
Source23:       vboxautostart-service.service
Source24:       vboxautostart-service.sh
Source25:       vboxclient.desktop
Source97:       README.build
Source98:       virtualbox-rpmlintrc
Source99:       virtualbox-patch-source.sh
#rework init scripts to fit suse needs
Patch1:         vbox-vboxdrv-init-script.diff
Patch2:         vbox-vboxadd-init-script.diff
#fix build : "Error 4001 - String must be entirely alphanumeric"
#with renaming we probably break some macosx functionality however ths is just quick fix
#see thread : http://lists.freebsd.org/pipermail/freebsd-acpi/2010-October/006795.html
Patch3:         vbox-smc-napa.diff
#deprecated old-style C++ service proxies and objects,we have to use soapcpp2 -z1 flag
Patch4:         vbox-deprec-gsoap-service-proxies.diff
#fix failed linking process during build - this patch is just quick workaround
Patch5:         vbox-gsoapssl-deps.diff
#PATCH-FIX-OPENSUSE implement messagebox (VBoxPermissionMessage app), which is displayed, when user
#try to start VirtualBox and is not member of vboxusers group
Patch6:         vbox-permissions_warning.diff
#PATCH-FIX-OPENSUSE Do not include build dates on binaries, makes build-compare happier
Patch7:         vbox-no-build-dates.diff
Patch8:         vbox-default-os-type.diff
# Disable the distributed versions of vboxdrv.sh and vboxadd.sh for security reasons.
Patch9:         security_fixes.patch
#disable update in vbox gui
Patch10:        vbox-disable-updates.diff
#use pie/fPIE for setuid binaries (bnc#743143)
Patch11:        vbox-fpie.diff
#smap issues on Haswell or Broadwell (boo#931461)
Patch12:        smap.diff
# Patch to build with Factory gcc5
Patch13:        gcc5-real-support.patch
# Patch to build with gnu sed correctly
Patch14:        virtualbox-sed-params.patch
# Patch to add code to explain USB Passthru
Patch16:        vbox-usb-warning.diff
# Patch to ensure that VirtualBoxVM is SUID
Patch17:        vbox-suid-warning.diff
# Fix symbol conflict between host and guest kmp
Patch18:        fix_conflict_between_host_and_guest.patch
# Fix change in kernel API for ttm_bo_move_memcpy()
Patch19:        modify_for_4_8_bo_move.patch
# Disable experimental and incomplete CLOUD_NET
Patch21:        turn_off_cloud_net.patch
# Fix rpmlint error for script /lib/usr/virtualbox/vboxshell.py
Patch22:        fixes_for_python.patch
# xpcom: Support up to python 3.10 -- https://www.virtualbox.org/changeset/90537/vbox + https://www.virtualbox.org/changeset/86623/vbox, thanks to Archlinux
Patch23:        vbox-python-py310.patch
# fix build of Python and dev package on openSUSE 11.3 (was vbox-detection.diff)
# use plain python3 interpreter of the distro (part of former switch_to_pyton3.4+.patch),
Patch24:        vbox-python-selection.patch
Patch25:        remove_vbox_video_build.patch
# Fixes for modified kernel in Leap 42.3
Patch26:        VirtualBox-5.2.10-xclient.patch
# Fixes for SLE12
Patch27:        fixes_for_sle12.patch
# Fixes for Qt5.13 on 32-bit systems
Patch28:        fixes_for_qt5.13.patch
# Fixes for openSUSE Leap 15.2
Patch29:        fixes_for_leap15.2.patch
# Fixes for kernel modules Makefile used at boot time
Patch30:        fixes_for_makefile.patch
# Fix build for Qt 5.15
Patch31:        fix-missing-includes-with-qt-5.15.patch
# Fix for changes in GSOAP 2.8.103
Patch32:        handle_gsoap_208103.patch
# Fix for struct file_operations backport in 15.3
Patch33:        fixes_for_leap15.3.patch
Patch34:        fix_kmp_build.patch
# Fix for backports to 15.5
Patch35:        fixes_for_leap15.5.patch
#
# Common BuildRequires for both virtualbox and virtualbox-kmp
BuildRequires:  %{kernel_module_package_buildreqs}
BuildRequires:  acpica
BuildRequires:  cmake-full
BuildRequires:  dwarves
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  kbuild >= 0.1.9998svn3101
BuildRequires:  libcap-devel
BuildRequires:  libcurl-devel
BuildRequires:  libopenssl-devel
BuildRequires:  libxslt-devel
BuildRequires:  module-init-tools
BuildRequires:  pam-devel
BuildRequires:  yasm
ExclusiveArch:  x86_64
%if 0%{?sle_version} != 120300
Source2:        VirtualBox.appdata.xml
%endif
### Requirements for virtualbox main package ###
%if %{main_package}
BuildRequires:  LibVNCServer-devel
BuildRequires:  SDL-devel
BuildRequires:  alsa-devel
#BuildRequires:  bin86
#BuildRequires:  dev86
BuildRequires:  device-mapper-devel
BuildRequires:  dmidecode
BuildRequires:  e2fsprogs-devel
BuildRequires:  fdupes
BuildRequires:  glibc-devel-static
BuildRequires:  glslang-devel
BuildRequires:  gsoap-devel >= 2.8.50
#BuildRequires:  infinipath-psm
BuildRequires:  java-devel >= 1.6.0
BuildRequires:  libelf-devel
BuildRequires:  libidl-devel
BuildRequires:  libopenssl-1_1-devel
BuildRequires:  libopus-devel
BuildRequires:  libqt5-linguist
BuildRequires:  libqt5-linguist-devel
BuildRequires:  libqt5-qtbase-devel
BuildRequires:  libqt5-qttools-devel
BuildRequires:  libqt5-qtx11extras-devel
BuildRequires:  libtpms-devel
BuildRequires:  libvpx-devel
BuildRequires:  libxslt-devel
BuildRequires:  libzio-devel
BuildRequires:  lzfse
BuildRequires:  lzfse-devel
BuildRequires:  pulseaudio-devel
BuildRequires:  python-rpm-macros
BuildRequires:  python3-devel
#BuildRequires:  sdl12_compat-devel
BuildRequires:  sed
BuildRequires:  systemd-rpm-macros
BuildRequires:  update-desktop-files
BuildRequires:  which
#BuildRequires:  xorg-x11
BuildRequires:  xorg-x11-server
#BuildRequires:  xorg-x11-server-sdk
#BuildRequires:  zlib-devel-static
BuildRequires:  pkgconfig(fontsproto)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(glx)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(randrproto)
BuildRequires:  pkgconfig(renderproto)
BuildRequires:  pkgconfig(resourceproto)
BuildRequires:  pkgconfig(scrnsaverproto)
BuildRequires:  pkgconfig(sdl)
BuildRequires:  pkgconfig(udev)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xau)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xdmcp)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(xf86driproto)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xineramaproto)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(xrandr)
Requires:       %{name}-kmp = %{version}
Requires(pre):  %fillup_prereq
Requires(pre):  permissions
Requires(pre):  shadow
Recommends:     %{name}-gui = %{version}
# package i4l-vbox from source package i4l-base shares the directory /etc/vbox
# with us, but with different owner.
Conflicts:      i4l-vbox
#rename from ose version:
Provides:       %{name}-ose = %{version}
Obsoletes:      %{name}-ose < %{version}
%{?systemd_ordering}
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_headers-devel
%else
BuildRequires:  boost-devel
%endif
%ifarch amd64 x86_64 ia32e em64t
BuildRequires:  gcc-32bit
BuildRequires:  gcc-c++-32bit
BuildRequires:  xorg-x11-libX11-devel-32bit
BuildRequires:  xorg-x11-libXext-devel-32bit
BuildRequires:  xorg-x11-libXmu-devel-32bit
BuildRequires:  xorg-x11-libXt-devel-32bit
%endif
%if ! 0%{?suse_version} > 1325
Requires(pre):  net-tools-deprecated
%endif
# end of main_package
%endif
### Requirements for virtualbox-kmp ###
%if %{kmp_package}
BuildRequires:  alsa-devel
BuildRequires:  libiptc-devel
BuildRequires:  libpulse-devel
BuildRequires:  libxml2-devel
Requires:       ca-certificates
Requires:       openSUSE-signkey-cert
%kernel_module_package -p %{SOURCE7} -n virtualbox -f %{SOURCE5} -x kdump um xen pae xenpae pv
# end of kmp_package
%endif
### Description and subpackages of virtualbox main package ###
%if %{main_package}
%description
VirtualBox is a hosted hypervisor for x86 computers. It supports the
creation and management of guest virtual machines running versions
and derivations of Windows, Linux, BSD, OS/2, Solaris, Haiku, OSx86
and others, and limited virtualization of macOS guests on Apple
hardware. VirtualBox is freely available as Open Source Software under
the terms of the GNU Public License (GPL).






















##########################################

%package qt
Summary:        Qt GUI part for %{name}
Group:          System/Emulators/PC
Requires(pre):  %{name} = %{version}
Requires(pre):  permissions
Provides:       %{name}-gui = %{version}
#this is needed during update to trigger installing qt subpackage
#http://en.opensuse.org/openSUSE:Upgrade_dependencies_explanation#Splitting_and_Merging
Provides:       %{name}-ose:%{_vbox_instdir}/VirtualBox.so
#rename from "ose" version:
Provides:       %{name}-ose-qt = %{version}
Obsoletes:      %{name}-ose-qt < %{version}

%description qt
This package contains the code for the GUI used to control VMs.






















#########################################

%package websrv
Summary:        WebService GUI part for %{name}
Group:          System/Emulators/PC
Requires:       %{name} = %{version}
Requires:       sysvinit-tools
Provides:       %{name}-gui = %{version}
Obsoletes:      %{name}-vboxwebsrv < %{version}

%description websrv
The VirtualBox web server is used to control headless VMs using a browser.























###########################################
%package guest-tools
Summary:        VirtualBox guest tools
Group:          System/Emulators/PC
Requires:       %{name}-kmp = %{version}
Requires:       libnotify-tools
# for /usr/lib/virtualbox/vboxadd-service
Requires:       which
Supplements:    modalias(pci:v000080EEd0000CAFEsv*sd*bc*sc*i*)
#rename from "ose" version:
Provides:       %{name}-ose-guest-tools = %{version}
Obsoletes:      %{name}-ose-guest-tools < %{version}
Obsoletes:      virtualbox-guest-x11 < %{version}
Obsoletes:      xorg-x11-driver-virtualbox-ose < %{version}
%if ! 0%{?suse_version} > 1325
Requires(pre):  net-tools-deprecated
%endif

%description guest-tools
VirtualBox guest addition tools.






















###########################################

%package -n python3-%{name}
Summary:        Python bindings for %{name}
Group:          Development/Libraries/Python
Requires:       %{name} = %{version}
#rename from "ose" version:
Provides:       python3-%{name} = %{version}-%{release}
Obsoletes:      python-%{name} < %{version}-%{release}
Obsoletes:      python2-%{name} < %{version}-%{release}
Obsoletes:      python3-%{name} < %{version}-%{release}
Provides:       python3-%{name}-ose = %{version}
Obsoletes:      python-%{name}-ose < %{version}
Obsoletes:      python2-%{name}-ose < %{version}
Obsoletes:      python3-%{name}-ose < %{version}

%description -n python3-%{name}
Python XPCOM bindings to %{name}. Used e.g. by vboxgtk package.






















###########################################

%package devel
Summary:        Devel files for %{name}
Group:          Development/Libraries/Other
Requires:       %{name} = %{version}
Requires:       python3-%{name} = %{version}
#rename from "ose" version:
Provides:       %{name}-ose-devel = %{version}
Obsoletes:      %{name}-ose-devel < %{version}

%description devel
Development file for %{name}






















###########################################

%package host-source
Summary:        Source files for %{name} host kernel modules
Group:          Development/Sources
Requires:       %{name} = %{version}
Requires:       gcc
Requires:       kernel-devel
Requires:       libelf-devel
Requires:       make
BuildArch:      noarch

%description host-source
Source files for %{name} host kernel modules
These can be built for custom kernels using
sudo %{_sbindir}/vboxconfig

%package guest-source
Summary:        Source files for %{name} guest kernel modules
Group:          Development/Sources
Requires:       gcc
Requires:       kernel-devel
Requires:       libelf-devel
Requires:       make
BuildArch:      noarch

%description guest-source
Source files for %{name} guest kernel modules
These can be built for custom kernels using
sudo %{_sbindir}/vboxguestconfig






















###########################################

%package guest-desktop-icons
Summary:        Icons for guest desktop files
Group:          System/Emulators/PC
Requires:       %{name} = %{version}
Recommends:     %{name}-gui = %{version}
BuildArch:      noarch

%description guest-desktop-icons
This package contains icons for guest desktop files that were created on the desktop.






















###########################################

%package vnc
Summary:        VNC desktop sharing
Group:          System/Emulators/PC
Requires:       %{name} = %{version}

%description vnc
Virtual Network Computing (VNC) is a graphical desktop sharing system that uses the Remote Frame Buffer
protocol (RFB) to remotely control another computer. When this optional feature is desired, it is installed
as an "extpack" for VirtualBox. The implementation is licensed under GPL.
###########################################
# main_package
%endif

### Description of virtualbox-kmp ###
%if %{kmp_package}
%description
This package contains the kernel-modules that VirtualBox uses to create or run virtual machines.
# kmp_package
%endif

%prep
%setup -q -n VirtualBox-%{version}
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
# Adjustments that are version dependent
%patch27 -p1
# Handle the 32-bit changes needed for Qt 5.13
%ifarch %{ix86} && 0%{?qt5ver} >= 51300
%patch28 -p1
%endif
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%if 0%{?sle_version} == 150300 && 0%{?is_opensuse}
# Patch for Leap 15.3
%patch33 -p1
%endif
%patch34 -p1
%if 0%{?sle_version} == 150500 && 0%{?is_opensuse}
%patch35 -p1
%endif

### Documents for virtualbox main package ###
%if %{main_package}
#copy user manual
cp %{SOURCE1} UserManual.pdf
#copy README.build
cp %{SOURCE97} README.build
#copy kbuild config
cp %{SOURCE10} LocalConfig.kmk
#copy autostart doc
cp %{SOURCE20} README.autostart
# main_package
%endif

#
##########################
####workaround kmk_sed --v
#instead of kmk_sed use /usr/bin/sed because of bug http://svn.netlabs.org/kbuild/ticket/112,
#but we have to create wrapper which will handle --append and --output options which are not provided by /usr/bin/sed
cat >> kmk_sed <<EOF
#!/usr/bin/bash
while [ "\$#" != "0" ]; do
	pass=\${pass}" \$1"
	[ "\$1" == "-e" ] && shift && pass=\${pass}" '\$1'"
	shift
done
eval "sed \$(echo "\$pass" | sed -e "s/--output=/>/g;s/--append=/>/g;s/--output/>/g;s/--append/>>/g");"
EOF
chmod +x ./kmk_sed
echo "SED = $RPM_BUILD_DIR/VirtualBox-%{version}/kmk_sed"  >> LocalConfig.kmk
####workaround kmk_sed --^
##########################
#
# fix build of vboxvideo kernel module: replace relative drm include path with absolute include path
sed -i 's:include/drm:%{_prefix}/src/linux/include/drm:' src/VBox/Additions/linux/drm/Makefile.module.kms

### %%build, %%install, and %%file sections for virtualbox ###
%if %{main_package}
%build
# Disable LTO - Link Time Optimization
	%define _lto_cflags %{nil}
	#ensure we don't ever use them
rm -rf src/libs/{libpng-*,libxml2-*,libxslt-*,zlib-*,boost-*}

#	--disable-kmods		don't build Linux kernel modules -  but use SUSE specific way see few lines under
# NOT an autoconf ceonfigure macro
./configure \
    --enable-vnc \
    --enable-vde \
    --disable-kmods \
    --with-linux="%{_prefix}" \
    --disable-java \
    --disable-docs \
    --enable-webservice \
    --with-makeself=%{_bindir}/true

# configure actually warns we should source env.sh (which seems like it could influence the build...)
source ./env.sh

#
#  	VBOX_PATH_PACKAGE_DOCS set propper path for link to pdf in .desktop file
# 	VBOX_WITH_REGISTRATION_REQUEST= VBOX_WITH_UPDATE_REQUEST= just disable some functionality in gui
echo "build basic parts"
    %{_bindir}/kmk %{?_smp_mflags} \
    VBOX_GCC_WERR= \
    VBOX_USE_SYSTEM_XORG_HEADERS=1 \
    VBOX_WITH_REGISTRATION_REQUEST= VBOX_WITH_UPDATE_REQUEST= \
    TOOL_YASM_AS=yasm \
    VBOX_BUILD_PUBLISHER=_SUSE \
    TOOL_GCC3_CFLAGS="%{optflags}" TOOL_GCC3_CXXFLAGS="%{optflags}" \
    VBOX_GCC_OPT="%{optflags}"

echo "build VNC extension pack"
# tar must use GNU, not POSIX, format here
sed -i 's/tar /tar --format=gnu /' src/VBox/ExtPacks/VNC/Makefile.kmk
kmk -C src/VBox/ExtPacks/VNC packing

%install
#################################
echo "create directory structure"
#################################
install -d -m 755 %{buildroot}%{_sbindir}
install -d -m 755 %{buildroot}%{_prefix}/lib
install -d -m 755 %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_sbindir}
install -d -m 755 %{buildroot}%{_datadir}/virtualbox/nls
install -d -m 755 %{buildroot}%{_datadir}/pixmaps
install -d -m 755 %{buildroot}%{_datadir}/applications
install -d -m 755 %{buildroot}%{_vbox_instdir}/sdk/bindings/xpcom
install -d -m 755 %{buildroot}%{_vbox_instdir}/components
install -d -m 755 %{buildroot}%{_libdir}/dri
install -d -m 755 %{buildroot}%{_libdir}/xorg/modules/drivers
install -d -m 755 %{buildroot}%{_libdir}/xorg/modules/input
install -d -m 755 %{buildroot}%{_sysconfdir}/default
install -d -m 755 %{buildroot}%{_sysconfdir}/init.d
install -d %{buildroot}%{_unitdir}
install -d %{buildroot}%{_unitdir}/multi-user.target.wants
install -d -m 755 %{buildroot}%{_sysconfdir}/vbox
install -d -m 755 %{buildroot}%{_sysconfdir}/vbox/autostart.d
install -d -m 755 %{buildroot}%{_udevrulesdir}
install -d -m 755 %{buildroot}%{_sysconfdir}/X11/xinit/xinitrc.d

###########################################
echo "entering guest-tools install section"
###########################################
install -m 755 out/linux.*/release/bin/additions/VBoxControl %{buildroot}%{_bindir}
install -m 755 out/linux.*/release/bin/additions/VBoxService %{buildroot}%{_sbindir}/VBoxService
install -m 755 out/linux.*/release/bin/additions/mount.vboxsf %{buildroot}%{_sbindir}/mount.vboxsf
install -m 744 src/VBox/Additions/linux/installer/vboxadd-service.sh %{buildroot}%{_vbox_instdir}/vboxadd-service
install -d %{buildroot}%{_userunitdir}
# udev rule for guest (virtualbox-guest-tools)
install -m 644 %{SOURCE3}			%{buildroot}%{_udevrulesdir}/90-vboxguest.rules
install -p -m 0644 -D %{SOURCE12} %{buildroot}%{_unitdir}/vboxclient.service
install -p -m 0644 -D %{SOURCE13} %{buildroot}%{_unitdir}/vboxservice.service
# /media is used for auto-mounting of shared folders
#VBoxClient daemon (support for clipboard,autoresize,seamless windows)
install -m 755 out/linux.*/release/bin/additions/VBoxClient	%{buildroot}%{_bindir}
install -m 755 out/linux.*/release/bin/additions/VBoxDRMClient	%{buildroot}%{_bindir}
# install init script which start VBoxClient daemon (support for clipboard,autoresize,seamless windows)
install -m 755 src/VBox/Additions/x11/Installer/98vboxadd-xclient %{buildroot}%{_sysconfdir}/X11/xinit/xinitrc.d/
install -d %{buildroot}%{_sysconfdir}/xdg/autostart/
install -m 644 %{SOURCE25} %{buildroot}%{_sysconfdir}/xdg/autostart/vboxclient.desktop
%if 0%{?suse_version} > 1320 || 0%{?sle_version} == 120300
install -d -m 755 %{buildroot}/media
%endif

###########################################
echo "entering VNC extension install section"
###########################################
pushd out/linux.*/release/packages/
mkdir -p "%{buildroot}%{_datadir}/virtualbox/extensions/"
install -D -m 644 VNC-*.vbox-extpack "%{buildroot}%{_datadir}/virtualbox/extensions/VNC-%{version}.vbox-extpack"
popd

##############################################
echo "entering virtualbox(-qt) install section"
##############################################
# copy the main files to %%{_vbox_instdir}
pushd out/linux.*/release/bin
install -m 755 VBoxManage 			%{buildroot}%{_vbox_instdir}
install -m 755 VBoxHeadless 			%{buildroot}%{_vbox_instdir}
install -m 755 VBoxSDL 				%{buildroot}%{_vbox_instdir}
install -m 755 VBoxNetNAT			%{buildroot}%{_vbox_instdir}
install -m 755 VBoxAutostart			%{buildroot}%{_vbox_instdir}
install -m 755 VBoxVolInfo			%{buildroot}%{_vbox_instdir}
install -m 755 vboxshell.py			%{buildroot}%{_vbox_instdir}
install -m 755 VBoxBalloonCtrl			%{buildroot}%{_vbox_instdir}
install -m 755 webtest				%{buildroot}%{_vbox_instdir}
install -m 755 VBoxDTrace			%{buildroot}%{_vbox_instdir}
install -m 755 VBoxDbg.so			%{buildroot}%{_vbox_instdir}
install -m 755 VBoxDbg.so			%{buildroot}%{_vbox_instdir}
install -m 755 VBoxDxVk.so			%{buildroot}%{_vbox_instdir}
install -m 755 UICommon.so			%{buildroot}%{_vbox_instdir}
install -m 755 vboximg-mount			%{buildroot}%{_vbox_instdir}
# create links to vbox tools in PATH - they could be usefull for controlling vbox from command line
ln -s %{_vbox_instdir}/VBoxManage		%{buildroot}%{_bindir}/VBoxManage
ln -s %{_vbox_instdir}/VBoxHeadless 		%{buildroot}%{_bindir}/VBoxHeadless
ln -s %{_vbox_instdir}/VBoxSDL			%{buildroot}%{_bindir}/VBoxSDL
ln -s %{_vbox_instdir}/vboximg-mount		%{buildroot}%{_bindir}/vboximg-mount
install -m 755 VBoxSVC 				%{buildroot}%{_vbox_instdir}
install -m 755 VBoxXPCOMIPCD 			%{buildroot}%{_vbox_instdir}
install -m 755 VBoxExtPackHelperApp		%{buildroot}%{_vbox_instdir}
install -m 755 VBoxTestOGL			%{buildroot}%{_vbox_instdir}
install -m 755 VBoxPermissionMessage		%{buildroot}%{_vbox_instdir}
install -m 755 VBoxSUIDMessage			%{buildroot}%{_vbox_instdir}
install -m 755 VBoxUSB_DevRules			%{buildroot}%{_vbox_instdir}
install -m 755 VBoxNetDHCP			%{buildroot}%{_vbox_instdir}
install -m 755 VBoxNetAdpCtl			%{buildroot}%{_vbox_instdir}
install -m 755 VirtualBox			%{buildroot}%{_vbox_instdir}/VirtualBox6
install -m 755 VirtualBoxVM			%{buildroot}%{_vbox_instdir}
# compatibility symlink in order to keep old desktop links functional
ln -s %{_vbox_instdir}/VirtualBoxVM		%{buildroot}%{_vbox_instdir}/VirtualBox
install -m 755 VBoxEFI*.fd			%{buildroot}%{_vbox_instdir}
install -m 755 VBoxSysInfo.sh			%{buildroot}%{_vbox_instdir}
install -m 644 *.so		 		%{buildroot}%{_vbox_instdir}
install -m 644 *.r0 				%{buildroot}%{_vbox_instdir}
install -m 644 components/*			%{buildroot}%{_vbox_instdir}/components/
# install languages
install -m 644 nls/*				%{buildroot}%{_datadir}/virtualbox/nls/
# install kmp src
mkdir -p %{buildroot}%{_usrsrc}/kernel-modules/virtualbox
mkdir -p %{buildroot}%{_usrsrc}/kernel-modules/additions
tar jcf %{buildroot}%{_usrsrc}/kernel-modules/additions/guest_src.tar.bz2 additions/src
cp -a src %{buildroot}%{_usrsrc}/kernel-modules/virtualbox
install -m 644 %{SOURCE11}			%{buildroot}%{_udevrulesdir}/60-vboxdrv.rules
popd

# install desktop file
install -m 644 out/linux.*/release/bin/virtualbox.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
%suse_update_desktop_file			%{buildroot}%{_datadir}/applications/%{name}.desktop 'System Emulator'

%if 0%{?sle_version} != 120300
# install appstream file
mkdir -p %{buildroot}%{_datadir}/metainfo
install -m 644 %{SOURCE2}			%{buildroot}%{_datadir}/metainfo/%{name}.appdata.xml
%endif

# create a menu entry
install -m 644 out/linux.*/release/bin/VBox.png %{buildroot}%{_datadir}/pixmaps/virtualbox.png
# install config with session shutdown defs
install -m 644 %{SOURCE4}			%{buildroot}%{_sysconfdir}/default/virtualbox
#install wrapper script
install -m 644 %{SOURCE9}			%{buildroot}%{_bindir}/VirtualBox
install -m 644 %{SOURCE8}			%{buildroot}%{_bindir}/update-extpack.sh
# Service files to load kernel modules on boot
install -m 0644 %{SOURCE14}                     %{buildroot}%{_unitdir}/vboxdrv.service
ln -s -f %{_sbindir}/service			%{buildroot}%{_sbindir}/rcvboxdrv
install -m 0644 %{SOURCE15}                     %{buildroot}%{_unitdir}/vboxadd-service.service
install -m 0755 %{SOURCE16}			%{buildroot}%{_sbindir}/vboxconfig
install -m 0755 %{SOURCE17}			%{buildroot}%{_sbindir}/vboxguestconfig
install -m 0755 %{SOURCE18}			%{buildroot}%{_sbindir}/vbox-fix-usb-rules.sh
install -m 0755 %{SOURCE19}			%{buildroot}%{_vbox_instdir}/vboxdrv.sh
install -m 0644 %{SOURCE21}			%{buildroot}%{_unitdir}/vboxweb-service.service
install -m 0755 %{SOURCE22}			%{buildroot}%{_vbox_instdir}/vboxweb-service.sh
install -m 0644 %{SOURCE23}			%{buildroot}%{_unitdir}/vboxautostart-service.service
ln -s -f %{_sbindir}/service                    %{buildroot}%{_sbindir}/rcvboxautostart
install -m 0755 %{SOURCE24}                     %{buildroot}%{_vbox_instdir}/vboxautostart-service.sh
# Init scripts to start virtualbox during boot
ln -sf %{_unitdir}/vboxdrv.service		%{buildroot}%{_unitdir}/multi-user.target.wants/vboxdrv.service
ln -sf %{_unitdir}/vboxadd-service.service	%{buildroot}%{_unitdir}/multi-user.target.wants/vboxadd-service.service
ln -sf %{_unitdir}/vboxautostart-service.service        %{buildroot}%{_unitdir}/multi-user.target.wants/vboxautostart-service.service

# config file for vboxdrv and vboxweb
install -d -m 755 %{buildroot}%{_sysconfdir}/vbox
# install -d -m 775 %{buildroot}%{_sysconfdir}/vbox/autostart.d
echo -e "#settings for vboxwebsrn\nVBOXWEB_USER=root" > %{buildroot}%{_sysconfdir}/vbox/vbox.cfg
# config file for vboxautostart
cat > %{buildroot}%{_sysconfdir}/vbox/autostart.cfg << EOF
default_policy = deny
# Create an entry for each user allowed to use autostart
myusername = {
allow = true
}

EOF
# install udev helper script for creating usb devices
install -m 0755 -D src/VBox/Installer/linux/VBoxCreateUSBNode.sh %{buildroot}%{_vbox_instdir}/VBoxCreateUSBNode.sh
######################################################
echo "entering python-virtualbox install section"
######################################################
pushd out/linux.*/release/bin/sdk/installer
VBOX_INSTALL_PATH=%{_vbox_instdir} python3 vboxapisetup.py install --prefix=%{_prefix} --root=%{buildroot}
popd
install -d -m 755 %{buildroot}%{_vbox_instdir}/sdk/bindings/xpcom
cp -r out/linux.*/release/bin/sdk/bindings/xpcom/python %{buildroot}%{_vbox_instdir}/sdk/bindings/xpcom
%py3_compile %{buildroot}%{_vbox_instdir}/sdk/bindings/xpcom/python

######################################################
echo "entering virtualbox-devel install section"
######################################################
cp -r out/linux.*/release/bin/sdk/bindings/auth %{buildroot}%{_vbox_instdir}/sdk/bindings

pushd out/linux.*/release/bin/sdk/bindings/xpcom
cp -r include %{buildroot}%{_vbox_instdir}/sdk/bindings/xpcom
cp -r idl %{buildroot}%{_vbox_instdir}/sdk/bindings/xpcom
cp -r samples %{buildroot}%{_vbox_instdir}/sdk/bindings/xpcom
popd

cp out/linux.*/release/bin/sdk/bindings/VirtualBox.xidl %{buildroot}%{_vbox_instdir}/sdk/bindings

######################################################
echo "entering virtualbox-websrv install section"
######################################################
pushd out/linux.*/release/bin
install -m 755 vboxwebsrv %{buildroot}%{_vbox_instdir}
install -m 755 webtest %{buildroot}%{_vbox_instdir}
popd
ln -sf %{_unitdir}/vboxweb-service.service %{buildroot}%{_unitdir}/multi-user.target.wants/vboxweb-service.service

#
######################################################
echo "entering virtualbox-guest-desktop-icons install section"
######################################################
install -d -m 755	%{buildroot}%{_datadir}/pixmaps/virtualbox

pushd src/VBox/Frontends/VirtualBox/images
for icon in os_*.png; do
  install -m 644 "$icon" %{buildroot}%{_datadir}/pixmaps/virtualbox/"$icon";
done
popd
#
######################################################
# run fdupes
######################################################
#run fdupes because we lost link for virtualbox/components directory
%fdupes %{buildroot}/%{_vbox_instdir}
#also some translation files are duplicated
%fdupes %{buildroot}/%{_datadir}/virtualbox/nls
#also some icon files are duplicated
%fdupes %{buildroot}/%{_datadir}/pixmaps/virtualbox

#
#
######################################################
# scriptlets - pre
######################################################

%pre
getent group vboxusers >/dev/null || groupadd -r vboxusers
%service_add_pre vboxdrv.service
%service_add_pre vboxautostart-service.service

%pre guest-tools
# Add groups for seamless mode and shared folders:
getent group vboxguest >/dev/null || groupadd -r vboxguest
getent group vboxsf >/dev/null || groupadd -r vboxsf
%if 0%{?suse_version} <= 1500
getent group vboxvideo >/dev/null || groupadd -r vboxvideo
%endif
%service_add_pre vboxadd-service.service

%pre websrv
%service_add_pre vboxweb-service.service

#######################################################
# scriptlets - post
#######################################################

%post
/sbin/ldconfig
#setup our sysconfig file /etc/sysconfig/vbox
%set_permissions %{_vbox_instdir}/VBoxNetNAT
%set_permissions %{_vbox_instdir}/VBoxNetDHCP
%set_permissions %{_vbox_instdir}/VBoxNetAdpCtl
%set_permissions %{_vbox_instdir}/VBoxHeadless
%service_add_post vboxdrv.service
%service_add_post vboxautostart-service.service
# add new autostart stuff to the existing default config, if missing
grep -q VBOXAUTOSTART %{_sysconfdir}/default/virtualbox || {
    cat >> %{_sysconfdir}/default/virtualbox << EOF
#
# -------------------------------------------------------------------------------------------------
# Autostart
# -------------------------------------------------------------------------------------------------
VBOXAUTOSTART_DB=%{_sysconfdir}/vbox/autostart.d
VBOXAUTOSTART_CONFIG=%{_sysconfdir}/vbox/autostart.cfg

EOF
}
for entry in %{_sysconfdir}/vbox/*.start
do
        user=$(basename "$entry" .start)
        [ "$user" = "*" ] && break
	mv %{_sysconfdir}/vbox/user.start %{_sysconfdir}/vbox/autostart.d/.
done

%post qt
%set_permissions %{_vbox_instdir}/VirtualBoxVM
%set_permissions %{_vbox_instdir}/VBoxSDL

%verifyscript
%verify_permissions -e %{_vbox_instdir}/VBoxNetNAT
%verify_permissions -e %{_vbox_instdir}/VBoxNetDHCP
%verify_permissions -e %{_vbox_instdir}/VBoxNetAdpCtl
%verify_permissions -e %{_vbox_instdir}/VBoxHeadless

%verifyscript qt
%verify_permissions -e %{_vbox_instdir}/VirtualBoxVM
%verify_permissions -e %{_vbox_instdir}/VBoxSDL

%post guest-tools
%service_add_post vboxadd-service.service
%service_add_post vboxclient.service
%service_add_post vboxservice.service

%post websrv
%service_add_post vboxweb-service.service

%post vnc
EXTPACK="%{_datadir}/virtualbox/extensions/VNC-%{version}.vbox-extpack"
ACCEPT="$(tar --to-stdout -xf "${EXTPACK}" ./ExtPack-license.txt | sha256sum | head --bytes=64)"
VBoxManage extpack install --replace "${EXTPACK}" --accept-license="${ACCEPT}" > /dev/null

#######################################################
# scriptlets preun
#######################################################

%preun
%stop_on_removal vboxautostart-service
%stop_on_removal vboxdrv
%service_del_preun vboxautostart-service.service
%service_del_preun vboxdrv.service
exit 0

%preun guest-tools
%stop_on_removal vboxadd-service
%stop_on_removal vboxadd
%service_del_preun vboxadd-service.service
%systemd_preun vboxclient.service
%systemd_preun vboxservice.service
exit 0

%preun websrv
%stop_on_removal vboxweb-service
%service_del_preun vboxweb-service.service
exit 0

#######################################################
# scriptlets postun
#######################################################

%postun
/sbin/ldconfig
%restart_on_update vboxdrv
%restart_on_update vboxautostart-service
# immediately restarting virtualbox may not work. As such wait for the next reboot to restart
%if ! %{defined service_del_postun_without_restart}
export DISABLE_RESTART_ON_UPDATE=yes
%service_del_postun vboxautostart-service.service
%service_del_postun vboxdrv.service
%else
%service_del_postun_without_restart vboxautostart-service.service
%service_del_postun_without_restart vboxdrv.service
%endif

%postun guest-tools
%restart_on_update vboxadd
%restart_on_update vboxadd-service
%service_del_postun vboxadd-service.service
%service_del_postun vboxclient.service
%service_del_postun vboxservice.service

%postun websrv
%restart_on_update vboxweb-service
%service_del_postun vboxweb-service.service
#
#######################################################

%files
%doc README.autostart UserManual.pdf README.build
%{_bindir}/VBoxManage
%{_bindir}/VBoxHeadless
%{_bindir}/VBoxSDL
%{_bindir}/vboximg-mount
%dir %{_vbox_instdir}
%{_vbox_instdir}/VBoxAutostart
%{_vbox_instdir}/VBoxBalloonCtrl
%{_vbox_instdir}/VBoxDTrace
%{_vbox_instdir}/VBoxNetNAT
%{_vbox_instdir}/VBoxVolInfo
%{_vbox_instdir}/vboxshell.py
%{_vbox_instdir}/VBoxSysInfo.sh
%{_vbox_instdir}/VBoxDD2.so
%{_vbox_instdir}/VBoxDD.so
%{_vbox_instdir}/VBoxDDU.so
%{_vbox_instdir}/VBoxGuestControlSvc.so
%{_vbox_instdir}/VBoxGuestPropSvc.so
%{_vbox_instdir}/VBoxHeadless.so
%{_vbox_instdir}/VBoxNetDHCP.so
%{_vbox_instdir}/VBoxNetNAT.so
%{_vbox_instdir}/VBoxRT.so
%{_vbox_instdir}/VBoxSharedFolders.so
%{_vbox_instdir}/VBoxVMM.so
%{_vbox_instdir}/VBoxXPCOMC.so
%{_vbox_instdir}/VBoxXPCOM.so
%{_vbox_instdir}/VBox*.r0
%{_vbox_instdir}/VMMR0.r0
%{_vbox_instdir}/VBoxEFI*.fd
%{_vbox_instdir}/VBoxManage
%{_vbox_instdir}/VBoxSVC
%{_vbox_instdir}/VBoxXPCOMIPCD
%{_vbox_instdir}/VBoxExtPackHelperApp
%{_vbox_instdir}/vboximg-mount
%{_vbox_instdir}/DbgPlugInDiggers.so
%{_vbox_instdir}/VBoxAuth.so
%{_vbox_instdir}/VBoxAuthSimple.so
%{_vbox_instdir}/VBoxDragAndDropSvc.so
%{_vbox_instdir}/VBoxVMMPreload.so
#todo:double check - if this file should be assigned to the host side
%{_vbox_instdir}/VBoxDxVk.so
%{_vbox_instdir}/UICommon.so
%{_vbox_instdir}/VBoxHostChannel.so
%dir %{_vbox_instdir}/components
%{_vbox_instdir}/components/*.so
%{_vbox_instdir}/components/*.xpt
%dir %{_datadir}/virtualbox
%config %{_sysconfdir}/default/virtualbox
%dir %{_prefix}/lib/virtualbox
%dir %{_unitdir}
%dir %{_unitdir}/multi-user.target.wants
%{_prefix}/lib/virtualbox/vboxdrv.sh
%{_prefix}/lib/virtualbox/vboxautostart-service.sh
%{_unitdir}/vboxdrv.service
%{_unitdir}/vboxautostart-service.service
%{_unitdir}/multi-user.target.wants/vboxweb-service.service
%{_unitdir}/multi-user.target.wants/vboxdrv.service
%{_unitdir}/multi-user.target.wants/vboxautostart-service.service
%{_sbindir}/rcvboxdrv
%{_sbindir}/rcvboxautostart
%{_sbindir}/vboxconfig
#rules fixing script is in /usr/sbin
%attr(0755,root,root) %{_sbindir}/vbox-fix-usb-rules.sh
%{_vbox_instdir}/VBoxCreateUSBNode.sh
%verify(not mode) %attr(0755,root,vboxusers) %{_vbox_instdir}/VBoxNetNAT
%verify(not mode) %attr(0755,root,vboxusers) %{_vbox_instdir}/VBoxNetDHCP
%verify(not mode) %attr(0755,root,vboxusers) %{_vbox_instdir}/VBoxNetAdpCtl
%verify(not mode) %attr(0755,root,vboxusers) %{_vbox_instdir}/VBoxHeadless
%dir %{_sysconfdir}/vbox
%dir %{_sysconfdir}/vbox/autostart.d
%attr(755,root,root) %{_sysconfdir}/vbox
%attr(1770,root,vboxusers) %{_sysconfdir}/vbox/autostart.d
%config %attr(644,root,vboxusers) %{_sysconfdir}/vbox/vbox.cfg
%config %attr(644,root,vboxusers) %{_sysconfdir}/vbox/autostart.cfg

%files qt
%attr(0755,root,vboxusers) %{_vbox_instdir}/VBoxPermissionMessage
%attr(0755,root,vboxusers) %{_vbox_instdir}/VBoxSUIDMessage
%attr(0755,root,vboxusers) %{_vbox_instdir}/VBoxUSB_DevRules
%attr(0755,root,vboxusers) %{_vbox_instdir}/VirtualBox6
%verify(not mode) %attr(0750,root,vboxusers) %{_vbox_instdir}/VirtualBoxVM
%verify(not mode) %attr(0755,root,vboxusers) %{_vbox_instdir}/VBoxSDL
%{_vbox_instdir}/VirtualBox
#wrapper script is in bindir
%attr(0755,root,root) %{_bindir}/VirtualBox
%attr(0755,root,root) %{_bindir}/update-extpack.sh
#ldd shows libQt* dependency
%{_vbox_instdir}/VBoxTestOGL
#qm's translations
%{_datadir}/virtualbox/nls
%{_vbox_instdir}/VBoxSVGA3D.so
%{_vbox_instdir}/VirtualBoxVM.so
%{_vbox_instdir}/VBoxDbg.so
%{_bindir}/VBoxSDL
%{_vbox_instdir}/VBoxSDL.so
%{_vbox_instdir}/VBoxKeyboard.so
%{_vbox_instdir}/VBoxSharedClipboard.so
%{_datadir}/pixmaps/virtualbox.png
%{_datadir}/applications/%{name}.desktop
%if 0%{?sle_version} != 120300
%{_datadir}/metainfo/%{name}.appdata.xml
%endif
%{_udevrulesdir}/60-vboxdrv.rules

%files guest-tools
%{_bindir}/VBoxControl
%{_sbindir}/VBoxService
%{_sbindir}/vboxguestconfig
%{_sbindir}/mount.vboxsf
%{_udevrulesdir}/90-vboxguest.rules
%{_vbox_instdir}/vboxadd-service
%{_unitdir}/vboxadd-service.service
%{_unitdir}/multi-user.target.wants/vboxadd-service.service
%dir %{_libdir}/xorg/modules/drivers
%dir %{_libdir}/xorg/modules/input
%dir %{_libdir}/dri/
%dir %{_sysconfdir}/X11
%dir %{_sysconfdir}/X11/xinit
%dir %{_sysconfdir}/X11/xinit/xinitrc.d
%{_bindir}/VBoxClient
%{_bindir}/VBoxDRMClient
%{_sysconfdir}/X11/xinit/xinitrc.d/98vboxadd-xclient
%{_unitdir}/vboxclient.service
%{_unitdir}/vboxservice.service
%dir %{_sysconfdir}/xdg
%dir %{_sysconfdir}/xdg/autostart
%{_sysconfdir}/xdg/autostart/vboxclient.desktop
%if 0%{?suse_version} > 1320 || 0%{?sle_version} == 120300
%dir /media
%endif

%files -n python3-%{name}
%dir %{_vbox_instdir}/sdk
%dir %{_vbox_instdir}/sdk/bindings
%dir %{_vbox_instdir}/sdk/bindings/xpcom
%{_vbox_instdir}/sdk/bindings/xpcom/python
%{_vbox_instdir}/VBoxPython*.so
%{python3_sitelib}/vboxapi-1.0-*.egg-info
%{python3_sitelib}/vboxapi/

%files devel
%dir %{_vbox_instdir}/sdk
%dir %{_vbox_instdir}/sdk/bindings
%dir %{_vbox_instdir}/sdk/bindings/xpcom
%{_vbox_instdir}/sdk/bindings/VirtualBox.xidl
%{_vbox_instdir}/sdk/bindings/xpcom/idl
%{_vbox_instdir}/sdk/bindings/xpcom/include
%{_vbox_instdir}/sdk/bindings/xpcom/samples
%{_vbox_instdir}/sdk/bindings/auth

%files host-source
%dir %{_usrsrc}/kernel-modules
%{_usrsrc}/kernel-modules/virtualbox

%files guest-source
%dir %{_usrsrc}/kernel-modules
%dir %{_usrsrc}/kernel-modules/additions
%{_usrsrc}/kernel-modules/additions/guest_src.tar.bz2

%files websrv
%{_unitdir}/vboxweb-service.service
%{_vbox_instdir}/vboxweb-service.sh
%{_vbox_instdir}/webtest
%{_vbox_instdir}/vboxwebsrv

%files guest-desktop-icons
%dir %{_datadir}/pixmaps/virtualbox
%{_datadir}/pixmaps/virtualbox/*.png

%files vnc
%license COPYING
%dir %{_datadir}/virtualbox/extensions
%{_datadir}/virtualbox/extensions/VNC-%{version}.vbox-extpack

# main_package
%endif

### %%build and %%install sections of virtualbox-kmp ###
%if %{kmp_package}
%build
# Disable LTO - Link Time Optimization
%define _lto_cflags %{nil}
#ensure we don't ever use them
rm -rf src/libs/{libpng-*,libxml2-*,libxslt-*,zlib-*,boost-*}

# Craft LocalConfig.kmk
echo "
VBOX_GCC_OPT                   := %{optflags}
VBOX_GCC_WERR                  :=
VBOX_BUILD_PUBLISHER           := _SUSE

VBOX_OSE                       := 1
VBOX_WITH_DOCS                 :=
VBOX_WITHOUT_LINUX_TEST_BUILDS := 1
VBOX_WITH_TESTCASES            :=
SDK_VBOX_LIBXML2_DEFS          := _REENTRANT
SDK_VBOX_LIBXML2_INCS          := %{_includedir}/libxml2
SDK_VBOX_LIBXML2_LIBS          := xml2
SDK_VBOX_OPENSSL_INCS          :=
SDK_VBOX_OPENSSL_LIBS          := ssl crypto
SDK_VBOX_BLD_OPENSSL_LIBS      := ssl crypto
SDK_VBOX_LIBCURL_INCS          :=
SDK_VBOX_LIBCURL_LIBS          := curl
" > LocalConfig.kmk

COMMON_KMK_FLAGS="
	KBUILD_VERBOSE=2 \
	KBUILD_TARGET=linux \
	BUILD_TARGET=linux \
"
# Build additions to export the source code of vbox{guest,sf,video} to
# out/linux.*/release/bin/additions/src/
%{_bindir}/kmk %{?_smp_mflags} \
	${COMMON_KMK_FLAGS} \
	VBOX_WITH_X11_ADDITIONS= \
	VBOX_ONLY_ADDITIONS=1

# The following kmk commands are used to extract the source of
# vbox{drv,netflt,netadp} without building the whole virtualbox
# program.

# 1. build src/bldprogs/ to get bin2c and VBoxTpG
%{_bindir}/kmk %{?_smp_mflags} -C src/bldprogs/ \
	${COMMON_KMK_FLAGS} \
	VBOX_ONLY_EXTPACKS=1

# 2. build src/VBox/HostDrivers/ with VBOX_ONLY_EXTPACKS=1 to
#    get SUPR3.a for src/VBox/Runtime/
%{_bindir}/kmk %{?_smp_mflags} -C src/VBox/HostDrivers/ \
	${COMMON_KMK_FLAGS} \
	VBOX_ONLY_EXTPACKS=1

# 3. build src/VBox/Runtime/ with VBOX_ONLY_BUILD=1 to get
#    VBoxRt.so for src/VBox/HostDrivers/Support/
%{_bindir}/kmk %{?_smp_mflags} -C src/VBox/Runtime/ \
	${COMMON_KMK_FLAGS} \
	VBOX_ONLY_BUILD=1

# 4. build src/VBox/HostDrivers/ to export the source of
#    host kernel modules to out/linux.*/release/bin/src/
%{_bindir}/kmk %{?_smp_mflags} -C src/VBox/HostDrivers/ \
	${COMMON_KMK_FLAGS}
#
# build kernel modules for guest and host (check novel-kmp package as example)
# host  modules : vboxdrv,vboxnetflt,vboxnetadp
# guest modules : vboxguest,vboxsf,vboxvideo
echo "build kernel modules"
for vbox_module in out/linux.*/release/bin/src/vbox{drv,netflt,netadp} \
           out/linux.*/release/bin/additions/src/vbox{guest,sf,video}; do
    #get the module name from path
    module_name=$(basename "$vbox_module")

    # go through the all flavors (desktop,default ...)
    for flavor in %{flavors_to_build}; do
	# delete old build dir for sure
	rm -rf modules_build_dir/${module_name}_${flavor}

	if [ "$module_name" = "vboxdrv" -o \
	     "$module_name" = "vboxguest" ] ; then
	    SYMBOLS=""
	fi
	# create build directory for specific flavor
        mkdir -p modules_build_dir/$flavor

	# copy sources which will be used to build vbox module in last step
	cp -r $vbox_module/ modules_build_dir/$flavor/

	# copy vboxdrv (for host) module symbols which are used by vboxnetflt and vboxnetadp km's:
	if [ "$module_name" = "vboxnetflt" -o \
	     "$module_name" = "vboxnetadp" ] ; then
	    cp $PWD/modules_build_dir/$flavor/vboxdrv/Module.symvers	\
		  $PWD/modules_build_dir/$flavor/$module_name
	    SYMBOLS="$PWD/modules_build_dir/$flavor/vboxdrv/Module.symvers"
	fi
        # copy vboxguest (for guest) module symbols which are used by vboxsf and vboxvideo km's:
	if [ "$module_name" = "vboxsf" -o \
	     "$module_name" = "vboxvideo" ] ; then
	    cp $PWD/modules_build_dir/$flavor/vboxguest/Module.symvers \
		$PWD/modules_build_dir/$flavor/$module_name
	    SYMBOLS="$PWD/modules_build_dir/$flavor/vboxguest/Module.symvers"
	fi
	# build the module for the specific flavor
	%make_build -j4 -C %{_prefix}/src/linux-obj/%{_target_cpu}/$flavor %{?linux_make_arch} modules \
		M=$PWD/modules_build_dir/$flavor/$module_name KBUILD_EXTRA_SYMBOLS="$SYMBOLS" V=1
    done
done

%install
export INSTALL_MOD_PATH=%{buildroot}
export INSTALL_MOD_DIR=extra
#to install modules we use here similar steps like in build phase, go through all the modules :
for module_name in vbox{drv,netflt,netadp,guest,sf,video}
do
	#and through all flavors
	for flavor in %{flavors_to_build}; do
    	    make -C %{_prefix}/src/linux-obj/%{_target_cpu}/$flavor modules_install M=$PWD/modules_build_dir/$flavor/$module_name
    	done
done
# kmp_package
%endif

%changelog
