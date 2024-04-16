#
# spec file for package xone
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           xone
Version:        0.3+git50.58004bf
Release:        0
Summary:        Driver for Xbox One and Xbox Series X|S controllers
License:        GPL-2.0-only
Group:          System/Kernel
URL:            https://github.com/medusalix/xone
Source:         xone-%version.tar.xz
BuildRequires:  %kernel_module_package_buildreqs
BuildRequires:  xz
Requires:       xone-dongle-firmware

%kernel_module_package

%description
Driver for Xbox One and Xbox Series X|S controllers.

%package KMP
Summary:        Driver for Xbox One and Xbox Series X|S controllers

%description KMP
Driver for Xbox One and Xbox Series X|S controllers.

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
