#
# spec file for package rfcat
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2017, Martin Hauke <mardnh@gmx.de>
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


%define rfcat_group rfcat
Name:           rfcat
Version:        0.0.0.git1554316953.d960f01
Release:        0
Summary:        The swiss army knife of subGHz
License:        BSD-2-Clause
Group:          Productivity/Hamradio/Other
URL:            https://github.com/atlas0fd00m/rfcat
# Refreshed version of https://github.com/3553x/rfcat/commit/8b2ad00da6b25b188b6800aeea3cc811243a8c15.patch
Patch0:         avoid-pyside.patch
Source:         %{name}-%{version}.tar.xz
BuildRequires:  git-core
BuildRequires:  pkgconfig
BuildRequires:  python-devel
BuildRequires:  python-future >= 0.17.1
BuildRequires:  python-numpy
BuildRequires:  python-qt5
BuildRequires:  python-setuptools
BuildRequires:  python-usb
# for rfcat_bootloader
BuildRequires:  python-pyserial
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(udev)
Requires:       %{name}-udev
# Unfortunately this isnt automatically detected.
Requires:       libusb-1_0-0
Requires:       python-future >= 0.17.1
Requires:       python-numpy
Requires:       python-qt5
Requires:       python-usb
# for rfcat_bootloader
Requires:       python-pyserial
BuildArch:      noarch

%description
RfCat allows you to control the wireless transceiver from an interactive
Python shell or your own program running on your computer.

%package udev
Summary:        Udev rules for rfcat
Group:          Hardware/Other
Requires(pre):  shadow

%description udev
Udev rules for rfcat.

%prep
%setup -q
%patch0 -p1

# Remove files that may be problematic from a license point of view
rm -f firmware/cc1111_vcom.c
rm -f firmware/cc1111_vcomdesc.c
rm -f firmware/include/cc1111_vcom.h
# HACK: set udev group to rfcat
sed -i 's|GROUP="dialout"|GROUP="rfcat"|g' etc/udev/rules.d/20-rfcat.rules

# Loosen pins to allow use of higher version rpms
sed -i 's/==/>=/g' setup.py

# PySide2 is replaced with qt5
sed -i '/PySide2>=[0-9.]*/d' setup.py

# Declared dependency on Python package libusb seems incorrect.
# Likely it refers to system libusb.
# Anyway, that isnt packaged in openSUSE yet, so dont inject it into
# runtime dependencies.
sed -i '/libusb/d' setup.py

# These are a mix of python and ipython interpreters in the hashbang,
# but residing inside the site-packages and they have relative imports
# making them not executable as-is.
sed -i '1{/#!/d}' rflib/*.py

%build
python setup.py build

%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot}
install -Dpm0644 etc/udev/rules.d/20-rfcat.rules %{buildroot}%{_udevrulesdir}/20-rfcat.rules

%check
# use setuptools instead of distutils only during testing.
sed -i 's/distutils.core/setuptools/' setup.py
python setup.py test

%pre udev
getent group %{rfcat_group} >/dev/null || groupadd -r %{rfcat_group}

%post udev
%udev_rules_update

%postun udev
%udev_rules_update

%files
%license LICENSE
%doc README.md README.immesniff
%{_bindir}/rfcat
%{_bindir}/rfcat_bootloader
%{_bindir}/rfcat_msfrelay
%{_bindir}/rfcat_server
%{python_sitelib}/rflib
%{python_sitelib}/vstruct
%{python_sitelib}/rfcat-1.0.1-py%{py_ver}.egg-info

%files udev
%{_udevrulesdir}/20-rfcat.rules

%changelog
