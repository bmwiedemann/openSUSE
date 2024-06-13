#
# spec file for package python-usbsdmux
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


%define         skip_python2 1
%define         orig_name usbsdmux
Name:           python-usbsdmux
Version:        24.01.1
Release:        0
Summary:        Tool to control an usb-sd-mux from the command line
License:        LGPL-2.1-or-later
URL:            https://shop.linux-automation.com/index.php?route=product/product&product_id=50
Source0:        https://github.com/linux-automation/usbsdmux/archive/%{version}.tar.gz#/%{orig_name}-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(udev)
Requires:       %{orig_name}-udev
Requires(post): update-alternatives
Requires(postun): update-alternatives
%python_subpackages

%description
Tool to control USB-SD-mux hardware from linux-automation.com

Full manual is available at https://www.linux-automation.com/usbsdmux-M01/

%package -n %{orig_name}-udev
Summary:        Udev rules for usbsdmux

%description -n %{orig_name}-udev
Udev rules for usbsdmux

%prep
%setup -q -n %{orig_name}-%{version}

%build
%python_build

%install
%python_install
# Fix interpreter
%{python_expand # Fix all supported python version
for i in %{buildroot}%{$python_sitelib}/usbsdmux/*.py; do
    sed -i 's#%{_bindir}/env python3#%{_bindir}/python3#' $i
    chmod +x $i
done
}
%python_clone -a %{buildroot}%{_bindir}/usbsdmux
%python_clone -a %{buildroot}%{_bindir}/usbsdmux-configure
%python_clone -a %{buildroot}%{_bindir}/usbsdmux-service
# Install udev rules (and switch from 'plugdev' group to 'disk' group)
sed -i 's/plugdev/disk/' contrib/udev/99-usbsdmux.rules
mkdir -p %{buildroot}%{_udevrulesdir}
cp contrib/udev/99-usbsdmux.rules %{buildroot}%{_udevrulesdir}
# Run fdupes
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative usbsdmux
%python_install_alternative usbsdmux-configure
%python_install_alternative usbsdmux-service

%postun
%python_uninstall_alternative usbsdmux
%python_uninstall_alternative usbsdmux-configure
%python_uninstall_alternative usbsdmux-service

%post -n %{orig_name}-udev
%udev_rules_update

%postun -n %{orig_name}-udev
%udev_rules_update

%files %{python_files}
%doc README.rst
%license COPYING
%python_alternative %{_bindir}/usbsdmux
%python_alternative %{_bindir}/usbsdmux-configure
%python_alternative %{_bindir}/usbsdmux-service
%dir %{python_sitelib}/usbsdmux
%{python_sitelib}/usbsdmux/*
%{python_sitelib}/*.egg-info*

%files -n %{orig_name}-udev
%{_udevrulesdir}/*.rules

%changelog
