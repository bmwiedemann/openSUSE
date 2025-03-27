#
# spec file for package hid-tmff2
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


Name:           hid-tmff2
Version:        0.0.1+git0.a9312ea
Release:        0
Summary:        Driver for Thrustmaster wheels
License:        GPL-2.0-or-later
Group:          System/Kernel
URL:            https://github.com/Kimplul/hid-tmff2
Source0:        %name-%version.tar.xz
Source1:        preamble
Source2:        blacklist-hid-thrustmaster.conf
BuildRequires:  %kernel_module_package_buildreqs
BuildRequires:  xz
Requires:       hid-tmff2-kmp

%kernel_module_package -n %name -p %_sourcedir/preamble

%description
Linux kernel module for Thrustmaster T300RS, T248, and (experimental support) TX and TS-XV wheels.

%prep
%autosetup -p1
set -- *
mkdir source
mv "$@" source/
mkdir obj

%build
for flavor in %flavors_to_build; do
        rm -rf "obj/$flavor"
        cp -r source "obj/$flavor"
        %make_build -C %{kernel_source $flavor} modules M="$PWD/obj/$flavor"
done

%install
export INSTALL_MOD_PATH="%buildroot"
export INSTALL_MOD_DIR=updates
for flavor in %flavors_to_build; do
        %make_install -C %{kernel_source $flavor} modules_install M="$PWD/obj/$flavor"
done

# udev rules
install -Dm 0644 -t "%buildroot%_modprobedir" %SOURCE2
install -Dm 0644 -t "%buildroot%_udevrulesdir" source/udev/99-thrustmaster.rules

%files
%_modprobedir/blacklist-hid-thrustmaster.conf
%_udevrulesdir/99-thrustmaster.rules

%changelog
