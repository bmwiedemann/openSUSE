#
# spec file for package xone
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

Name:           xone
Version:        0.4.11
Release:        0
Summary:        Driver for Xbox One and Xbox Series X|S controllers
License:        GPL-2.0-or-later
Group:          System/Kernel
URL:            https://github.com/dlundqvist/xone
Source0:        https://github.com/dlundqvist/xone/archive/refs/tags/v%version.tar.gz
Source1:        preamble
BuildRequires:  %kernel_module_package_buildreqs
BuildRequires:  systemd-rpm-macros
BuildRequires:  xz
Requires:       xone-dongle-firmware
Requires:       xone-kmp

%kernel_module_package -n %name -p %_sourcedir/preamble

%description
Linux kernel driver for Xbox One and Xbox Series X|S accessories.
it serves as a modern replacement for xpad, aiming to be
compatible with Microsoft's Game Input Protocol (GIP).

%prep
%autosetup -p1
set -- *
mkdir source
mv "$@" source/
mkdir obj

%build
for flavor in %flavors_to_build; do
	rm -Rf "obj/$flavor"
	cp -r source "obj/$flavor"
	# kernel's make install is picky about flags changing/being the same between %%build and %%install
	%make_build -C %{kernel_source $flavor} modules M="$PWD/obj/$flavor" KCFLAGS="-DDEBUG"
done

%install
export INSTALL_MOD_PATH="%buildroot"
export INSTALL_MOD_DIR=updates
for flavor in %flavors_to_build; do
	%make_build -C %{kernel_source $flavor} modules_install M="$PWD/obj/$flavor" KCFLAGS="-DDEBUG"
done

# modprobe aliases
mv source/install/modprobe.conf source/install/xone.conf
install -Dm0644 -t "%buildroot/%_modprobedir" source/install/xone.conf

%files
%_modprobedir/xone.conf

%changelog

