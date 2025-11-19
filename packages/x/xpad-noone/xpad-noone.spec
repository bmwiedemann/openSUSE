# spec file for package xpad-noone
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

Name:           xpad-noone
Version:        0+git20251029.8e90367
Release:        0
Summary:        The original xpad kernel driver with support for Xbox One controllers removed
License:        GPL-2.0-or-later
Group:          System/Kernel
URL:            https://github.com/forkymcforkface/xpad-noone
Source0:        xpad-noone-%version.tar.xz
Source1:        preamble
BuildRequires:  %kernel_module_package_buildreqs
BuildRequires:  xz
Requires:       xone-dongle-firmware

%kernel_module_package -n %name -p %_sourcedir/preamble

%description
This is the original xpad kernel driver with support for Xbox One
controllers removed. If you are running the xone driver you will have
to replace the xpad kernel module with this one to retain the
functionality of Xbox and Xbox 360 controllers.

%prep
%autosetup -p1

%build
pushd ../
for flavor in %flavors_to_build; do
	cp -a "%name-%version" "%name-$flavor-%version"
	pushd "%name-$flavor-%version/"
	# kernel's make install is picky about flags changing/being the same between %%build and %%install
	%make_build -C "/usr/src/linux-obj/%_target_cpu/$flavor" M=$PWD KCFLAGS="-DDEBUG"
	popd
done

%install
pushd ../
for flavor in %flavors_to_build; do
	pushd "%name-$flavor-%version/"
	%make_build -C "/usr/src/linux-obj/%_target_cpu/$flavor" M=$PWD KCFLAGS="-DDEBUG" \
		INSTALL_MOD_PATH="%buildroot" modules_install
	popd
done

%changelog
