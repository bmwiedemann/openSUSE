#
# spec file for package grub2-theme-breeze
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%bcond_without released
Name:           grub2-theme-breeze
Version:        5.26.5
Release:        0
Summary:        Plasma branding for GRUB2's graphical console
License:        GPL-3.0-or-later
Group:          System/Boot
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/plasma/%{version}/breeze-grub-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/breeze-grub-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildArch:      noarch

%description
Plasma branding for the GRUB2's graphical console.

%prep
%setup -q -n breeze-grub-%{version}

%build

%install
  mkdir -p %{buildroot}/boot/grub2/themes/breeze/
  cp -a breeze %{buildroot}/boot/grub2/themes/breeze/

%files
%license LICENSES/*
%dir /boot/grub2
%dir /boot/grub2/themes
/boot/grub2/themes/breeze/

%changelog
