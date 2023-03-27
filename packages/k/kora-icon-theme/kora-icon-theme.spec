#
# spec file for package kora-icon-theme
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

Name:               kora-icon-theme
Version:            1.5.6
Release:            0
Summary:            SVG icon theme suitable for every desktop environment (dark and light versions, HiDPI support)
License:            GPL-3.0
URL:                https://github.com/bikass/kora
Source0:            kora-%{version}.tar.gz
BuildArch:          noarch
BuildRequires:      fdupes
Requires(post):     gtk3-tools

%description
Kora is an SVG icon theme with lots of new icons for GNU/Linux operating systems.

To make them display properly, you may need to update the icon cache. A script is included.

Different versions available:
kora - for dark themes with dark panel
kora-light - for light themes with dark panel (depends on Kora)
kora-light-panel - for light themes with light panel (depends on Kora and Kora-light)
kora-pgrey - theme with grey folder colors (depends on Kora)

%prep
%setup -q -n kora-%{version}

%build
# Nothing to do here

%install
%fdupes %{buildroot}
# Delete useless files from source folder
rm -f "kora/create-new-icon-theme.cache.sh"
rm -f "kora/icon-theme.cache"
rm -f "kora-light/create-new-icon-theme.cache.sh"
rm -f "kora-light/icon-theme.cache"
rm -f "kora-light-panel/create-new-icon-theme.cache.sh"
rm -f "kora-light-panel/icon-theme.cache"
rm -f "kora-pgrey/create-new-icon-theme.cache.sh"
rm -f "kora-pgrey/icon-theme.cache"

# Install icons
mkdir -p %{buildroot}/usr/share/icons
cp -dr --no-preserve=mode "kora" %{buildroot}/usr/share/icons/kora
cp -dr --no-preserve=mode "kora-light" %{buildroot}/usr/share/icons/kora-light
cp -dr --no-preserve=mode "kora-light-panel" %{buildroot}/usr/share/icons/kora-light-panel
cp -dr --no-preserve=mode "kora-pgrey" %{buildroot}/usr/share/icons/kora-pgrey

# Install license
mkdir -p %{buildroot}/usr/share/licenses/%{name}
cp -p "LICENSE" %{buildroot}/usr/share/licenses/%{name}

%files
%doc README.md
%license LICENSE
/usr/share/icons/kora
/usr/share/icons/kora-light
/usr/share/icons/kora-light-panel
/usr/share/icons/kora-pgrey

%changelog
