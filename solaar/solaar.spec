#
# spec file for package solaar
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


Name:           solaar
Version:        1.0.1
Release:        0
Summary:        Linux devices manager for the Logitech Unifying Receiver
License:        GPL-2.0-or-later
Group:          Hardware/Other
Url:            https://pwr-solaar.github.io/Solaar
Source0:        https://github.com/pwr/Solaar/archive/%{version}/%{name}-%{version}.tar.gz
#PATCH-FIX-OPENSUSE solaar-fix-desktop-categories.patch malcolmlewis@opensuse.org -- Fix desktop categories as per openSUSE desktop file specification.
Patch0:         solaar-fix-desktop-categories.patch
# https://github.com/pwr-Solaar/Solaar/pull/546
Patch1:         0001-Fix-reading-and-storing-DPI-in-config-settings.patch
#
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  python-rpm-macros
BuildRequires:  python3-setuptools
BuildRequires:  update-desktop-files
#
Requires:       python3-gobject
Requires:       python3-pyudev
Requires:       solaar-udev >= %{version}
Requires:       typelib-1_0-Gtk-3_0
#
Obsoletes:      solaar-cli < %{version}
Provides:       solaar-cli = %{version}
#
BuildArch:      noarch

%description
Solaar will detect all devices paired with your Unifying Receiver, and
at the very least display some basic information about them.

For some devices, extra settings (usually not available through the
standard Linux system configuration) are supported. For a full list of
supported devices and their features, see docs/devices.md.

%package        doc
Summary:        Documentation for %{name}
Group:          Documentation/Other

%description    doc
Solaar will detect all devices paired with your Unifying Receiver, and
at the very least display some basic information about them.

For some devices, extra settings (usually not available through the
standard Linux system configuration) are supported. For a full list of
supported devices and their features, see docs/devices.md.

%package        udev
Summary:        Udev rules for accessing Logitech Unifying Receiver
Group:          Hardware/Other
Requires:       udev
Conflicts:      solaar-cli < %{version}

%description    udev
Rules that users are able to access Logitech Unifying Receiver.

%prep
%autosetup -p1 -n Solaar-%{version}

# Fix desktop file installation
sed -i '/yield autostart_path/d' setup.py

%build
sed -i 's#/usr/bin/env python##' lib/solaar/gtk.py lib/solaar/tasks.py
%python3_build

%install
%python3_install
%fdupes %{buildroot}%{python3_sitelib}
%fdupes -s %{buildroot}%{_datadir}
%suse_update_desktop_file %{buildroot}%{_datadir}/applications/%{name}.desktop

install -d 0755 %{buildroot}%{_udevrulesdir}
install -m 0644 rules.d/42-logitech-unify-permissions.rules %{buildroot}%{_udevrulesdir}/42-logitech-unify-permissions.rules

rm %{buildroot}%{_bindir}/solaar-cli
ln -s solaar %{buildroot}%{_bindir}/solaar-cli

%files
%doc ChangeLog COPYRIGHT README.md
%license COPYING
%{_bindir}/%{name}
%{_bindir}/%{name}-cli
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/solaar.svg
%{python3_sitelib}/hidapi
%{python3_sitelib}/logitech_receiver
%{python3_sitelib}/solaar
%{python3_sitelib}/solaar-*

%files udev
%{_udevrulesdir}/42-logitech-unify-permissions.rules

%files doc
%defattr(-,root,root)
%doc docs/*

%changelog
