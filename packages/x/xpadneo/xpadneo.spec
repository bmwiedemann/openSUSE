#
# spec file for package xpadneo
#
# Copyright (c) 2024 SUSE LLC
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
# needssslcertforbuild


Name:           xpadneo
Version:        0.9.7
Release:        0
Summary:        Driver for Xbox Wireless Controller
License:        GPL-3.0-only
URL:            https://github.com/atar-axis/xpadneo
Source0:        https://github.com/atar-axis/xpadneo/archive/v%{version}.tar.gz#/%name-%version.tar.gz
Source1:        preamble
BuildRequires:  %{kernel_module_package_buildreqs}
BuildRequires:  pesign-obs-integration
Requires:       xpadneo-kmp
%kernel_module_package -n %{name} -x debug -x trace -c %{_sourcedir}/_projectcert.crt -p %{_sourcedir}/preamble

%description
Advanced Linux Driver for Xbox One Wireless Controller (shipped with Xbox One S)

%prep
%autosetup
set -- hid-xpadneo/*
mkdir source
mv "$@" source/
mkdir obj

%build
for flavor in %{flavors_to_build}; do
    rm -rf obj/$flavor
    cp -r source obj/$flavor
    make -C %{kernel_source $flavor} modules M=$PWD/obj/$flavor/src
done

%install
export INSTALL_MOD_PATH=$RPM_BUILD_ROOT
export INSTALL_MOD_DIR=updates
for flavor in %{flavors_to_build}; do
    make -C %{kernel_source $flavor} modules_install M=$PWD/obj/$flavor/src
done

# The BRP_PESIGN_FILES variable must be set to a space separated list of
# directories or patterns matching files that need to be signed.  E.g., packages
# that include firmware files would set BRP_PESIGN_FILES='*.ko /lib/firmware'
export BRP_PESIGN_FILES='*.ko'

# modprobe aliases
install -Dm0644 -t "%{buildroot}/usr/lib/modprobe.d" source/etc-modprobe.d/*

# udev rules
install -Dm0644 -t "%{buildroot}/usr/lib/udev/rules.d" source/etc-udev-rules.d/*

%files
/usr/lib/modprobe.d/xpadneo.conf
/usr/lib/udev/rules.d/60-xpadneo.rules
/usr/lib/udev/rules.d/70-xpadneo-disable-hidraw.rules

%changelog
