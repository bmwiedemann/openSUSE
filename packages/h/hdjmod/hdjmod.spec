#
# spec file for package hdjmod
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2008-2017 Matthias Bach <marix@marix.org>
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


Name:           hdjmod
Version:        1.28
Release:        0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?suse_version} < 1120
BuildRequires:  %kernel_module_package_buildreq
BuildRequires:  module-init-tools
%else
BuildRequires:  %kernel_module_package_buildreqs
%endif
BuildRequires:  libelf-devel
Summary:        Support for Hercules DJ Devices
License:        GPL-2.0-or-later
Group:          System/Kernel
Url:            http://ts.hercules.com/ger/index.php?pg=view_files&gid=17&fid=62&pid=177&cid=1
Source0:        hdjmod-%{version}.tar.bz2
Source1:        preamble
# PATCH-FIX-UPSTREAM hdjmod_kernel_2.6.30.patch marix@marix.org -- Fix build on kernel 2.6.30 and newer
Patch0:         hdjmod_kernel_2.6.30.patch
# PATCH-FIX-UPSTREAM hdjmod_kernel_2.6.36.patch marix@marix.org -- Fix includes for kfree
Patch1:         hdjmod-kfree.patch
# PATCH-FIX-UPSTREAM hdjmod_kernel_2.6.36.patch marix@marix.org -- Fix build on kernel 2.6.36 and newer
Patch2:         hdjmod_kernel_2.6.36.patch.bz2
# PATCH-FIX-UPSTREAM hdjmod_kernel_2.6.37.patch marix@marix.org -- Fix build on kernel 2.6.37 and newer
Patch3:         hdjmod_kernel_2.6.37.patch
# PATCH-FIX-UPSTREAM hdjmod_kernel_2.6.39.patch marix@marix.org -- Fix build on kernel 2.6.39 and newer
Patch4:         hdjmod_kernel_2.6.39.patch
# PATCH-FIX-UPSTREAM hdjmod_fix_hotplug.patch [bnc#746358] marix@marix.org -- Don't load on hotplug of devices from other vendors
Patch5:         hdjmod_fix_hotplug.patch
# PATCH-FIX-UPSTREAM hdjmod_kernel_3.6.patch [bnc#783848] marix@marix.org -- Fix build on kernel 3.6 and newer
Patch6:         hdjmod_kernel_3.6.patch
# PATCH-FIX-UPSTREAM hdjmod_kernel_3.7.patch marix@marix.org -- Fix build on kernel 3.7 and newer
Patch7:         hdjmod_kernel_3.7.patch
# PATCH-FIX-UPSTREAM hdjmod_kernel_3.16.patch marix@marix.org -- Fix build on kernel 3.16 and newer
Patch8:         hdjmod_kernel_3.16.patch
# PATCH-FIX-UPSTREAM hdjmod_kernel_4.11.patch marix@marix.org -- Fix build on kernel 4.11 and newer
Patch9:         hdjmod_kernel_4.11.patch
# PATCH-FIX-UPSTREAM hdjmod_fix_buffer_overrun_in_device_name_handling.patch marix@marix.org -- Fix build on kernel 4.11 and newer
Patch10:        hdjmod_fix_buffer_overrun_in_device_name_handling.patch
# PATCH-FIX-UPSTREAM hdjmod_kernel_4.14.patch marix@marix.org -- Fix build on kernel 4.14 and newer
Patch11:        hdjmod_kernel_4.14.patch
# PATCH-FIX-UPSTREAM hdjmod_kernel_4.15.patch marix@marix.org -- Fix build on kernel 4.15 and newer
Patch12:        hdjmod_kernel_4.15.patch
# Fix build with kernel 5.0
Patch13:        hdjmod_kernel_5.0.patch

%suse_kernel_module_package -p%_sourcedir/preamble

%description
This is the Hercules DJ Series Kernel Module, which supports Hercules DJ Devices.

%prep
echo %flavors_to_build
%setup -q
%if 0%{?suse_version} >= 1120 || 0%{?sles_version} > 10
%patch0 -p1
%endif
%if 0%{?suse_version} >= 1140 || 0%{?sles_version} > 10
%patch2 -p1
%patch3 -F3 -p1
%patch4 -p1
%endif
%patch1 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p2
set -- *
mkdir source
mv "$@" source/
mkdir obj

%build
for flavor in %flavors_to_build; do
        rm -rf obj/$flavor
        cp -r source obj/$flavor
        make -C %{kernel_source $flavor} %{?linux_make_arch} modules M=$PWD/obj/$flavor
done

%install
export INSTALL_MOD_PATH=%{buildroot}
export INSTALL_MOD_DIR=updates
for flavor in %flavors_to_build; do
        make -C %{kernel_source $flavor} %{?linux_make_arch} modules_install M=$PWD/obj/$flavor
done

%changelog
