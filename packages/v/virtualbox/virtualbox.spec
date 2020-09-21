#
# spec file for package virtualbox
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


%if "@BUILD_FLAVOR@" == "kmp"
### macros for virtualbox-kmp ###
%define main_package 0
%define kmp_package 1

%define name_suffix kmp
%define dash -
%define package_summary Kernel modules for VirtualBox
%define package_group System/Kernel
%else
### macros for virtualbox main package ###
%define main_package 1
%define kmp_package 0

%define package_summary VirtualBox is an Emulator
%define package_group System/Emulators/PC

%define qt5ver %(rpm -q --queryformat %%{version} libQt5Core5|perl -ne '/(\\d+)\\.(\\d+)\\.(\\d+)?/&&printf "%%d%%02d%%02d\\n",$1,$2,$3')

#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

# Use Python3 rather than Python2 by default
%define __python /usr/bin/python3

# In /usr/lib/rpm/macros, py_compile is hard-wired to use the command "python". I think
# this is a bug for which the work-around is to redefine that macro to use python3.
%define py_compile(O)  \
find %1 -name '*.pyc' -exec rm -f {} \\; \
python3 -c "import sys, os, compileall; br='%{buildroot}'; compileall.compile_dir(sys.argv[1], ddir=br and (sys.argv[1][len(os.path.abspath(br)):]+'/') or None)" %1 \
%{-O: \
find %1 -name '*.pyo' -exec rm -f {} \\; \
python3 -O -c "import sys, os, compileall; br='%{buildroot}'; compileall.compile_dir(sys.argv[1], ddir=br and (sys.argv[1][len(os.path.abspath(br)):]+'/') or None)" %1 \
}
# Do not provide libGL.so symbols - they are owned by Mesa already and this could potentially confuse rpm/zypp
%global __provides_exclude ^libE?GL.so.1.*$

# With 32-bit builds, the job limit cannot be larger than 2, otherwise the build runs out of memory.
# For 64-bit builds, no memory limit is reached when more jobs are run, but the builds crash with strange errors.
# For the above reasons, limit the number of jobs to 2.
%define _smp_mflags -j2

%define _vbox_instdir  %{_prefix}/lib/virtualbox
%define _udevrulesdir /usr/lib/udev/rules.d
%endif 

# ********* If the VB version exceeds 6.1.x, notify the libvirt maintainer!!
Name:           virtualbox%{?dash}%{?name_suffix}
Version:        6.1.14
Release:        0
Summary:        %{package_summary}
License:        GPL-2.0-or-later
Group:          %{package_group}
URL:            http://www.virtualbox.org/
#
# so you don't need to repack virtualbox by hand, just add new release of VirtualBox-x.x.x.tar.bz2 and line below with
# script virtualbox-patch-source.sh will do the job :)
# WARNING: This is not a comment, but the real command to repack source
#%%(bash %%{_sourcedir}/virtualbox-patch-source.sh VirtualBox-%%{version}.tar.bz2)
Source0:        VirtualBox-%{version}-patched.tar.bz2
Source1:        UserManual.pdf
%if 0%{?sle_version} != 120300 
Source2:        VirtualBox.appdata.xml
%endif
Source3:        virtualbox-60-vboxguest.rules
Source4:        virtualbox-default.virtualbox
Source5:        virtualbox-kmp-files
Source7:        virtualbox-kmp-preamble
Source8:        update-extpack.sh
Source9:        virtualbox-wrapper.sh
Source10:       virtualbox-LocalConfig.kmk
Source11:       virtualbox-60-vboxdrv.rules
Source14:       vboxdrv.service
Source15:       vboxadd-service.service
Source16:       vboxconfig.sh
Source17:       vboxguestconfig.sh
Source18:       fix_usb_rules.sh
Source19:       vboxdrv.sh
Source20:       README.autostart
Source21:       vboxweb-service.service
Source22:       vboxweb-service.sh
Source23:       vboxautostart.service
Source24:       vboxautostart.sh
Source97:       README.build
Source98:       virtualbox-rpmlintrc
Source99:       virtualbox-patch-source.sh
#rework init scripts to fit suse needs
Patch1:         vbox-vboxdrv-init-script.diff
Patch2:         vbox-vboxadd-init-script.diff
#fix build : "Error 4001 - String must be entirely alphanumeric"
#with renaming we probably break some macosx functionality however ths is just quick fix
#see thread : http://lists.freebsd.org/pipermail/freebsd-acpi/2010-October/006795.html
Patch6:         vbox-smc-napa.diff
#fix build of Python and dev package on openSUSE 11.3
Patch8:         vbox-python-detection.diff
#deprecated old-style C++ service proxies and objects,we have to use soapcpp2 -z1 flag
Patch9:         vbox-deprec-gsoap-service-proxies.diff
#fix failed linking process during build - this patch is just quick workaround
Patch10:        vbox-gsoapssl-deps.diff
#PATCH-FIX-OPENSUSE implement messagebox (VBoxPermissionMessage app), which is displayed, when user
#try to start VirtualBox and is not member of vboxusers group
Patch99:        vbox-permissions_warning.diff
#PATCH-FIX-OPENSUSE Do not include build dates on binaries, makes build-compare happier
Patch100:       vbox-no-build-dates.diff
Patch101:       vbox-default-os-type.diff
# Disable the distributed versions of vboxdrv.sh and vboxadd.sh for security reasons.
Patch102:       security_fixes.patch
#disable update in vbox gui
Patch103:       vbox-disable-updates.diff
#use pie/fPIE for setuid binaries (bnc#743143)
Patch104:       vbox-fpie.diff
#smap issues on Haswell or Broadwell (boo#931461)
Patch105:       smap.diff
# Patch to build with Factory gcc5
Patch106:       gcc5-real-support.patch
# Patch to build with gnu sed correctly
Patch107:       virtualbox-sed-params.patch
# Patch to use snprintf correcty and not overflow dst buffer
Patch108:       virtualbox-snpritnf-buffer-overflow.patch
# Patch to add code to explain USB Passthru
Patch109:       vbox-usb-warning.diff
# Patch to ensure that VirtualBoxVM is SUID
Patch110:       vbox-suid-warning.diff
# Fix symbol conflict between host and guest kmp
Patch111:       fix_conflict_between_host_and_guest.patch
# Fix change in kernel API for ttm_bo_move_memcpy()
Patch112:       modify_for_4_8_bo_move.patch
# Remove all mention of _smp_mflags
Patch113:       vbox_remove_smp_mflags.patch
# Disable experimental and incomplete CLOUD_NET
Patch114:       turn_off_cloud_net.patch
# Fix for missing include needed for server 1.19
Patch116:       Fix_for_server_1.19.patch
# Fix invalid use of internal headers
Patch118:       internal-headers.patch
# Fix rpmlint error for script /lib/usr/virtualbox/vboxshell.py
Patch120:       fixes_for_python.patch
# Fix build for Qt 5.11
Patch122:       fixes_for_Qt5.11.patch
# Switch to Python 3.4+
Patch123:       switch_to_python3.4+.patch
# Use build parameters to control video driver problems
Patch125:       remove_vbox_video_build.patch
# fix library search
Patch128:       fix_lib_search.patch
# Fixes for modified kernel in Leap 42.3
Patch130:       fixes_for_Leap42.3.patch
# Fixes for SLE12
Patch131:       fixes_for_sle12.patch
# Fixes for Qt5.13 on 32-bit systems
Patch132:       fixes_for_qt5.13.patch
# Fixes for openSUSE Leap 15.2
Patch133:       fixes_for_leap15.2.patch
# Fixes for kernel modules Makefile used at boot time
Patch134:       fixes_for_makefile.patch
# Fix build for Qt 5.15
Patch135:       fix-missing-includes-with-qt-5.15.patch
# Fix builds with GCC10
Patch136:       fixes_for_gcc10.patch
# Fix for changes in GSOAP 2.8.103
Patch137:       handle_gsoap_208103.patch
# Fixes for kernel 5.9
Patch138:       fixes_for_5.9.patch
Patch999:       virtualbox-fix-ui-background-color.patch
#

# Common BuildRequires for both virtualbox and virtualbox-kmp
BuildRequires:  %{kernel_module_package_buildreqs}
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

### Requirements for virtualbox main package ###
%if %{main_package}
BuildRequires:  LibVNCServer-devel
BuildRequires:  SDL-devel
BuildRequires:  acpica
BuildRequires:  alsa-devel
BuildRequires:  bin86
BuildRequires:  infinipath-psm
BuildRequires:  systemd-rpm-macros
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_headers-devel
%else
BuildRequires:  boost-devel
%endif
BuildRequires:  dev86
BuildRequires:  device-mapper-devel
BuildRequires:  dmidecode
BuildRequires:  e2fsprogs-devel
BuildRequires:  fdupes
BuildRequires:  glibc-devel-static
BuildRequires:  gsoap-devel >= 2.8.50
BuildRequires:  java-devel >= 1.6.0
BuildRequires:  libelf-devel
BuildRequires:  libidl-devel
BuildRequires:  libopus-devel
BuildRequires:  libqt5-linguist
BuildRequires:  libqt5-qtbase-devel
BuildRequires:  libqt5-qtx11extras-devel
BuildRequires:  libvpx-devel
BuildRequires:  libxslt-devel
BuildRequires:  libzio-devel
BuildRequires:  pulseaudio-devel
BuildRequires:  python3-devel
BuildRequires:  sed
BuildRequires:  update-desktop-files
BuildRequires:  which
BuildRequires:  xorg-x11
BuildRequires:  xorg-x11-server
BuildRequires:  xorg-x11-server-sdk
BuildRequires:  zlib-devel-static
BuildRequires:  pkgconfig(fontsproto)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(randrproto)
BuildRequires:  pkgconfig(renderproto)
BuildRequires:  pkgconfig(resourceproto)
BuildRequires:  pkgconfig(scrnsaverproto)
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
%ifarch amd64 x86_64 ia32e em64t
BuildRequires:  gcc-32bit
BuildRequires:  gcc-c++-32bit
BuildRequires:  xorg-x11-libX11-devel-32bit
BuildRequires:  xorg-x11-libXext-devel-32bit
BuildRequires:  xorg-x11-libXmu-devel-32bit
BuildRequires:  xorg-x11-libXt-devel-32bit
%endif
%{?systemd_requires}
# package i4l-vbox from source package i4l-base shares the directory /etc/vbox
# with us, but with different owner.
Conflicts:      i4l-vbox
Requires:       %{name}-kmp = %{version}
Requires(post): sysvinit(syslog)
Requires(pre):  permissions
%if ! 0%{?suse_version} > 1325
Requires(pre):  net-tools-deprecated
%endif
Requires(pre):  shadow
Requires(pre):  %fillup_prereq
Recommends:     %{name}-gui = %{version}
#rename from ose version:
Provides:       %{name}-ose = %{version}
Obsoletes:      %{name}-ose < %{version}
# end of main_package
%endif

### Requirements for virtualbox-kmp ###
%if %{kmp_package}
BuildRequires:  libxml2-devel
%(sed -e '/^Provides: multiversion(kernel)/d' %{_prefix}/lib/rpm/kernel-module-subpackage > %{_builddir}/virtualbox-kmp-template)
%kernel_module_package -t %{_builddir}/virtualbox-kmp-template -p %{SOURCE7} -n virtualbox -f %{SOURCE5} -x kdump um xen pae xenpae pv
Obsoletes:      virtualbox-guest-kmp
Obsoletes:      virtualbox-host-kmp
# end of kmp_package
%endif

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExclusiveArch:  x86_64

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
Provides:       %{name}-ose:%{_prefix}/lib/virtualbox/VirtualBox.so
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
Provides:       %{name}-gui = %{version}
Obsoletes:      %{name}-vboxwebsrv

%description websrv
The VirtualBox web server is used to control headless VMs using a browser.
#########################################

%package guest-x11
Summary:        VirtualBox X11 drivers for mouse and video
Group:          System/X11/Servers/XF86_4
Requires:       %{name}-kmp = %{version}
Supplements:    modalias(xorg-x11-server:pci:v000080EEd0000BEEFsv*sd*bc*sc*i*)
#rename from xorg-x11-driver-virtualbox-ose:
Provides:       xorg-x11-driver-virtualbox-ose = %{version}
Obsoletes:      xorg-x11-driver-virtualbox-ose < %{version}

%description guest-x11
This package contains X11 guest utilities and X11 guest mouse and video drivers
###########################################

%package guest-tools
Summary:        VirtualBox guest tools
Group:          System/Emulators/PC
Requires:       %{name}-kmp = %{version}
Supplements:    modalias(pci:v000080EEd0000BEEFsv*sd*bc*sc*i*)
#rename from "ose" version:
Provides:       %{name}-ose-guest-tools = %{version}
Obsoletes:      %{name}-ose-guest-tools < %{version}
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
sudo /sbin/vboxconfig

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
sudo /sbin/vboxguestconfig
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
%patch6 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch99 -p1
%patch100 -p1
%patch101 -p1
%patch102 -p1
%patch103 -p1
%patch104 -p1
%patch105 -p1
%patch106 -p1
%patch107 -p1
%patch108 -p1
%patch109 -p1
%patch110 -p1
%patch111 -p1
%patch112 -p1
%patch113 -p1
%patch114 -p1
%patch116 -p1
%patch118 -p1
%patch120 -p1
%patch122 -p1
%patch123 -p1
%patch125 -p1
%patch128 -p1
# Adjustments that are version dependent
%if 0%{?sle_version} == 120300 && 0%{?is_opensuse} 
# Patch for Leap 42.3
%patch130 -p1
%endif
%patch131 -p1
# Handle the 32-bit changes needed for Qt 5.13
%ifarch %ix86 && 0%{?qt5ver} >= 51300
%patch132 -p1
%endif
%patch133 -p1
%patch134 -p1
%patch135 -p1
%patch136 -p1
%patch137 -p1
%patch138 -p1
# make VB UI background colors look sane again
%patch999 -p1

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
#!/bin/bash
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
sed -i 's:include/drm:/usr/src/linux/include/drm:' src/VBox/Additions/linux/drm/Makefile.module.kms

### %%build, %%install, and %%file sections for virtualbox ###
%if %{main_package}
%build
# Disable LTO - Link Time Optimization
%define _lto_cflags %{nil}
#ensure we don't ever use them
rm -rf src/libs/{libpng-*,libxml2-*,libxslt-*,zlib-*,boost-*}

#	--disable-kmods		don't build Linux kernel modules -  but use SUSE specific way see few lines under
# NOT an autoconf configure macro
./configure \
    --ose \
    --enable-vnc \
    --enable-vde \
    --disable-kmods \
    --with-linux="/usr" \
    --disable-java \
    --disable-docs \
    --enable-webservice \
    --with-makeself=/bin/true

# configure actually warns we should source env.sh (which seems like it could influence the build...)
source ./env.sh

#
#  	VBOX_PATH_PACKAGE_DOCS set propper path for link to pdf in .desktop file
# 	VBOX_WITH_REGISTRATION_REQUEST= VBOX_WITH_UPDATE_REQUEST= just disable some functionality in gui
echo "build basic parts"
    %{_bindir}/kmk %_smp_mflags \
    VBOX_GCC_WERR= \
    KBUILD_VERBOSE=2 \
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
pushd out/linux.*/release/packages/
mkdir -p "%{buildroot}%{_datadir}/virtualbox/extensions/"
install -D -m 644 VNC-*.vbox-extpack "%{buildroot}%{_datadir}/virtualbox/extensions/VNC-%{version}.vbox-extpack"
popd
install -D -m 644 "COPYING" "%{buildroot}%{_datadir}/licenses/LICENSE.vnc"

%install
#################################
echo "create directory structure"
#################################
install -d -m 755 %{buildroot}/sbin
install -d -m 755 %{buildroot}/lib
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
install -d -m 755 %{buildroot}%{_udevrulesdir}
install -d -m 755 %{buildroot}%{_sysconfdir}/X11/xinit/xinitrc.d

###########################################
echo "entering guest-tools install section"
###########################################
install -m 755 out/linux.*/release/bin/additions/VBoxControl %{buildroot}%{_bindir}/VBoxControl
install -m 755 out/linux.*/release/bin/additions/VBoxService %{buildroot}%{_sbindir}/VBoxService
install -m 755 out/linux.*/release/bin/additions/mount.vboxsf %{buildroot}/sbin/mount.vboxsf
install -m 744 src/VBox/Additions/linux/installer/vboxadd-service.sh %{buildroot}%{_vbox_instdir}/vboxadd-service
# udev rule for guest (virtualbox-guest-tools)
install -m 644 %{SOURCE3}			%{buildroot}%{_udevrulesdir}/60-vboxguest.rules
# /media is used for auto-mounting of shared folders
%if 0%{?suse_version} > 1320 || 0%{?sle_version} == 120300
install -d -m 755 %{buildroot}/media
%endif
#
##############################################################
echo "entering guest-x11 install section"
##############################################################
pushd out/linux.*/release/bin/additions/
#VBoxClient daemon (support for clipboard,autoresize,seamless windows)
install -m 755 VBoxClient	%{buildroot}%{_bindir}
popd
# install init script which start VBoxClient daemon (support for clipboard,autoresize,seamless windows)
install -m 755 src/VBox/Additions/x11/Installer/98vboxadd-xclient %{buildroot}%{_sysconfdir}/X11/xinit/xinitrc.d/vboxadd-xclient.sh

##############################################
echo "entering virtualbox(-qt) install section"
##############################################
# copy the main files to %%{_vbox_instdir}
pushd out/linux.*/release/bin
install -m 755 VBoxManage 			%{buildroot}%{_vbox_instdir}
install -m 755 VBoxHeadless 			%{buildroot}%{_vbox_instdir}
install -m 755 VBoxSDL 				%{buildroot}%{_vbox_instdir}
install -m 755 VBoxTunctl 			%{buildroot}%{_vbox_instdir}
install -m 755 VBoxNetNAT			%{buildroot}%{_vbox_instdir}
install -m 755 VBoxAutostart			%{buildroot}%{_vbox_instdir}
install -m 755 VBoxVolInfo			%{buildroot}%{_vbox_instdir}
install -m 755 vboxshell.py			%{buildroot}%{_vbox_instdir}
install -m 755 VBoxBalloonCtrl			%{buildroot}%{_vbox_instdir}
install -m 755 webtest				%{buildroot}%{_vbox_instdir}
install -m 755 VBoxDTrace			%{buildroot}%{_vbox_instdir}
install -m 755 VBoxDbg.so			%{buildroot}%{_vbox_instdir}
install -m 755 VBoxDbg.so			%{buildroot}%{_vbox_instdir}
install -m 755 UICommon.so			%{buildroot}%{_vbox_instdir}
# create links to vbox tools in PATH - they could be usefull for controlling vbox from command line
ln -s %{_vbox_instdir}/VBoxManage		%{buildroot}%{_bindir}/VBoxManage
ln -s %{_vbox_instdir}/VBoxHeadless 		%{buildroot}%{_bindir}/VBoxHeadless
ln -s %{_vbox_instdir}/VBoxSDL			%{buildroot}%{_bindir}/VBoxSDL
ln -s %{_vbox_instdir}/VBoxTunctl		%{buildroot}%{_bindir}/VBoxTunctl
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
rm components/VBoxREM.so
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
install -m 0755 %{SOURCE16}			%{buildroot}/sbin/vboxconfig
install -m 0755 %{SOURCE17}			%{buildroot}/sbin/vboxguestconfig
install -m 0755 %{SOURCE18}			%{buildroot}/sbin/vbox-fix-usb-rules.sh
install -m 0755 %{SOURCE19}			%{buildroot}%{_vbox_instdir}/vboxdrv.sh
install -m 0644 %{SOURCE21}			%{buildroot}%{_unitdir}/vboxweb-service.service
install -m 0755 %{SOURCE22}			%{buildroot}%{_vbox_instdir}/vboxweb-service.sh
install -m 0644 %{SOURCE23}			%{buildroot}%{_unitdir}/vboxautostart.service
ln -s -f %{_sbindir}/service                    %{buildroot}%{_sbindir}/rcvboxautostart
install -m 0755 %{SOURCE24}                     %{buildroot}%{_vbox_instdir}/vboxautostart.sh
# Init scripts to start virtualbox during boot
ln -sf %{_unitdir}/vboxdrv.service		%{buildroot}%{_unitdir}/multi-user.target.wants/vboxdrv.service
ln -sf %{_unitdir}/vboxadd-service.service	%{buildroot}%{_unitdir}/multi-user.target.wants/vboxadd-service.service
ln -sf %{_unitdir}/vboxautostart.service        %{buildroot}%{_unitdir}/multi-user.target.wants/vboxautostart.service

# config file for vboxdrv and vboxweb
install -d -m 755 %{buildroot}%{_sysconfdir}/vbox
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
%py_compile %{buildroot}%{_vbox_instdir}/sdk/bindings/xpcom/python

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
%service_add_pre vboxautostart.service

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
%service_add_post vboxautostart.service
# add new autostart stuff to the existing default config, if missing
grep -q VBOXAUTOSTART /etc/default/virtualbox || {
    cat >> /etc/default/virtualbox << EOF
#
# -------------------------------------------------------------------------------------------------
# Autostart
# -------------------------------------------------------------------------------------------------
VBOXAUTOSTART_DB=/etc/vbox
VBOXAUTOSTART_CONFIG=/etc/vbox/autostart.cfg

EOF
}

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

%post websrv
%service_add_post vboxweb-service.service

%post vnc
EXTPACK="/usr/share/virtualbox/extensions/VNC-%{version}.vbox-extpack"
ACCEPT="$(tar --to-stdout -xf "${EXTPACK}" ./ExtPack-license.txt | sha256sum | head --bytes=64)"
VBoxManage extpack install --replace "${EXTPACK}" --accept-license="${ACCEPT}" > /dev/null

#######################################################
# scriptlets preun
#######################################################

%preun
%stop_on_removal vboxautostart
%stop_on_removal vboxdrv
%service_del_preun vboxautostart.service
%service_del_preun vboxdrv.service
exit 0

%preun guest-tools
%stop_on_removal vboxadd-service
%stop_on_removal vboxadd
%service_del_preun vboxadd-service.service
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
%restart_on_update vboxautostart
# immediately restarting virtualbox may not work. As such wait for the next reboot to restart
%if ! %{defined service_del_postun_without_restart}
export DISABLE_RESTART_ON_UPDATE=yes
%service_del_postun vboxautostart.service
%service_del_postun vboxdrv.service
%else
%service_del_postun_without_restart vboxautostart.service
%service_del_postun_without_restart vboxdrv.service
%endif

%postun guest-tools
%restart_on_update vboxadd
%restart_on_update vboxadd-service
%service_del_postun vboxadd-service.service

%postun websrv
%restart_on_update vboxweb-service
%service_del_postun vboxweb-service.service
#
#######################################################

%files
%defattr(-, root, root)
%doc README.autostart UserManual.pdf README.build
%{_bindir}/VBoxManage
%{_bindir}/VBoxHeadless
%{_bindir}/VBoxTunctl
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
%{_vbox_instdir}/VBoxTunctl
%{_vbox_instdir}/VBoxXPCOMIPCD
%{_vbox_instdir}/VBoxExtPackHelperApp
%{_vbox_instdir}/DbgPlugInDiggers.so
%{_vbox_instdir}/VBoxAuth.so
%{_vbox_instdir}/VBoxAuthSimple.so
%{_vbox_instdir}/VBoxDragAndDropSvc.so
%{_vbox_instdir}/VBoxVMMPreload.so
#todo:double check - if this file should be assigned to the host side
%{_vbox_instdir}/UICommon.so
%{_vbox_instdir}/VBoxHostChannel.so
%dir %{_vbox_instdir}/components
%{_vbox_instdir}/components/*.so
%{_vbox_instdir}/components/*.xpt
%dir %{_datadir}/virtualbox
%config %{_sysconfdir}/default/virtualbox
%dir /usr/lib/virtualbox
%dir %{_unitdir}
%dir %{_unitdir}/multi-user.target.wants
/usr/lib/virtualbox/vboxdrv.sh
/usr/lib/virtualbox/vboxautostart.sh
%{_unitdir}/vboxdrv.service
%{_unitdir}/vboxautostart.service
%{_unitdir}/multi-user.target.wants/vboxdrv.service
%{_unitdir}/multi-user.target.wants/vboxautostart.service
%{_sbindir}/rcvboxdrv
%{_sbindir}/rcvboxautostart
/sbin/vboxconfig
%{_vbox_instdir}/VBoxCreateUSBNode.sh
%verify(not mode) %attr(0755,root,vboxusers) %{_vbox_instdir}/VBoxNetNAT
%verify(not mode) %attr(0755,root,vboxusers) %{_vbox_instdir}/VBoxNetDHCP
%verify(not mode) %attr(0755,root,vboxusers) %{_vbox_instdir}/VBoxNetAdpCtl
%verify(not mode) %attr(0755,root,vboxusers) %{_vbox_instdir}/VBoxHeadless
%dir %{_sysconfdir}/vbox
%attr(1775,root,vboxusers) %{_sysconfdir}/vbox
%config %attr(644,root,vboxusers) %{_sysconfdir}/vbox/vbox.cfg
%config %attr(644,root,vboxusers) %{_sysconfdir}/vbox/autostart.cfg

%files qt
%defattr(-, root, root)
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
#rules fixing script is in /sbin
%attr(0755,root,root) /sbin/vbox-fix-usb-rules.sh
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

%files guest-x11
%defattr(-, root, root)
%dir %{_libdir}/xorg/modules/drivers
%dir %{_libdir}/xorg/modules/input
%dir %{_libdir}/dri/
%{_bindir}/VBoxClient
%{_sysconfdir}/X11/xinit/xinitrc.d/vboxadd-xclient.sh

%files guest-tools
%defattr(-, root, root)
%{_bindir}/VBoxControl
%{_sbindir}/VBoxService
/sbin/vboxguestconfig
/sbin/mount.vboxsf
%{_udevrulesdir}/60-vboxguest.rules
%{_vbox_instdir}/vboxadd-service
%{_unitdir}/vboxadd-service.service
%{_unitdir}/multi-user.target.wants/vboxadd-service.service
%if 0%{?suse_version} > 1320 || 0%{?sle_version} == 120300
%dir /media
%endif

%files -n python3-%{name}
%defattr(-, root, root)
%dir %{_vbox_instdir}/sdk
%dir %{_vbox_instdir}/sdk/bindings
%dir %{_vbox_instdir}/sdk/bindings/xpcom
%{_vbox_instdir}/sdk/bindings/xpcom/python
%{_vbox_instdir}/VBoxPython*.so
%{python3_sitelib}/vboxapi-1.0-*.egg-info
%{python3_sitelib}/vboxapi/

%files devel
%defattr(-,root, root)
%dir %{_vbox_instdir}/sdk
%dir %{_vbox_instdir}/sdk/bindings
%dir %{_vbox_instdir}/sdk/bindings/xpcom
%{_vbox_instdir}/sdk/bindings/VirtualBox.xidl
%{_vbox_instdir}/sdk/bindings/xpcom/idl
%{_vbox_instdir}/sdk/bindings/xpcom/include
%{_vbox_instdir}/sdk/bindings/xpcom/samples
%{_vbox_instdir}/sdk/bindings/auth

%files host-source
%defattr(-,root, root)
%dir %{_usrsrc}/kernel-modules
%{_usrsrc}/kernel-modules/virtualbox

%files guest-source
%defattr(-,root, root)
%dir %{_usrsrc}/kernel-modules
%dir %{_usrsrc}/kernel-modules/additions
%{_usrsrc}/kernel-modules/additions/guest_src.tar.bz2

%files websrv
%defattr(-,root, root)
%{_unitdir}/vboxweb-service.service
%{_vbox_instdir}/vboxweb-service.sh
%{_vbox_instdir}/webtest
%{_vbox_instdir}/vboxwebsrv

%files guest-desktop-icons
%defattr(-,root, root)
%dir %{_datadir}/pixmaps/virtualbox
%{_datadir}/pixmaps/virtualbox/*.png

%files vnc
%defattr(-,root, root)
%dir %{_datadir}/virtualbox/extensions
%{_datadir}/virtualbox/extensions/VNC-%{version}.vbox-extpack
%dir %{_datadir}/licenses
%{_datadir}/licenses/LICENSE.vnc

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
SDK_VBOX_LIBXML2_INCS          := /usr/include/libxml2
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
# Architecture specific flags
%ifarch x86_64
COMMON_KMK_FLAGS+="
	KBUILD_TARGET_ARCH=amd64 \
	BUILD_TARGET_ARCH=amd64
"
%endif

# Build additions to export the source code of vbox{guest,sf,video} to
# out/linux.*/release/bin/additions/src/
%{_bindir}/kmk %_smp_mflags \
	${COMMON_KMK_FLAGS} \
	VBOX_WITH_X11_ADDITIONS= \
	VBOX_ONLY_ADDITIONS=1

# The following kmk commands are used to extract the source of
# vbox{drv,netflt,netadp} without building the whole virtualbox
# program.

# 1. build src/bldprogs/ to get bin2c and VBoxTpG
%{_bindir}/kmk %_smp_mflags -C src/bldprogs/ \
	${COMMON_KMK_FLAGS} \
	VBOX_ONLY_EXTPACKS=1

# 2. build src/VBox/HostDrivers/ with VBOX_ONLY_EXTPACKS=1 to
#    get SUPR3.a for src/VBox/Runtime/
%{_bindir}/kmk %_smp_mflags -C src/VBox/HostDrivers/ \
	${COMMON_KMK_FLAGS} \
	VBOX_ONLY_EXTPACKS=1

# 3. build src/VBox/Runtime/ with VBOX_ONLY_BUILD=1 to get
#    VBoxRt.so for src/VBox/HostDrivers/Support/
%{_bindir}/kmk %_smp_mflags -C src/VBox/Runtime/ \
	${COMMON_KMK_FLAGS} \
	VBOX_ONLY_BUILD=1

# 4. build src/VBox/HostDrivers/ to export the source of
#    host kernel modules to out/linux.*/release/bin/src/
%{_bindir}/kmk %_smp_mflags -C src/VBox/HostDrivers/ \
	${COMMON_KMK_FLAGS}
#
# build kernel modules for guest and host (check novel-kmp package as example)
# host  modules : vboxdrv,vboxnetflt,vboxnetadp
# guest modules : vboxguest,vboxsf vboxvideo (for Leap 15.1 and older)
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
	# copy vboxguest (for guest) module symbols which are used by vboxsf km:
       if [ "$module_name" = "vboxsf" -o \
            "$module_name" = "vboxvideo" ] ; then
           cp $PWD/modules_build_dir/$flavor/vboxguest/Module.symvers \
	          $PWD/modules_build_dir/$flavor/$module_name
	    SYMBOLS="$PWD/modules_build_dir/$flavor/vboxguest/Module.symvers"
	fi
	# build the module for the specific flavor
	make -j2 -C %{_prefix}/src/linux-obj/%{_target_cpu}/$flavor %{?linux_make_arch} modules \
		M=$PWD/modules_build_dir/$flavor/$module_name KBUILD_EXTRA_SYMBOLS="$SYMBOLS" V=1
    done
done

%install
export INSTALL_MOD_PATH=%{buildroot}
export INSTALL_MOD_DIR=extra
#to install modules we use here similar steps like in build phase, go through all the modules :
for module_name in vbox{drv,netflt,netadp,guest,sf,video}
do
	#and through the all flavors
	for flavor in %{flavors_to_build}; do
    	    make -C %{_prefix}/src/linux-obj/%{_target_cpu}/$flavor modules_install M=$PWD/modules_build_dir/$flavor/$module_name
    	done
done
# kmp_package
%endif

%changelog
