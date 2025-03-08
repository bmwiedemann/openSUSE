#
# spec file for package keylightd
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

Name:           framework-laptop
Version:        1+git20240915.6164bc3
Release:        0
Summary:        Kernel module to expose the LEDs and battery charge limits of Framework Laptops
License:        GPL-2.0-only
Group:          System/Kernel
URL:            https://github.com/DHowett/framework-laptop-kmod
Source:         %name-%version.tar.xz
BuildRequires:  %kernel_module_package_buildreqs

%kernel_module_package

%description
A kernel module that exposes the Framework Laptop (13, 16)'s battery charge limit and LEDs to userspace.

%package KMP
Summary:        Kernel module to expose the LEDs and battery charge limits of Framework Laptops

%description KMP
A kernel module that exposes the Framework Laptop (13, 16)'s battery charge limit and LEDs to userspace.

%prep
%autosetup -p1

%build
cd ../
for flavor in %flavors_to_build; do
	cp -a "%name-%version" "%name-$flavor-%version"
	cd "%name-$flavor-%version/"
	# kernel's make install is picky about flags changing/being the same between %%build and %%install
	%make_build -C "/usr/src/linux-obj/%_target_cpu/$flavor" M=$PWD KCFLAGS="-DDEBUG"
	cd -
done

%install
cd ../
for flavor in %flavors_to_build; do
	cd "%name-$flavor-%version/"
	%make_build -C "/usr/src/linux-obj/%_target_cpu/$flavor" M=$PWD KCFLAGS="-DDEBUG" \
		INSTALL_MOD_PATH="%buildroot" modules_install
	cd -
done

%changelog
