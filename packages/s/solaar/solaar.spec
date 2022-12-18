#
# spec file for package solaar
#
# Copyright (c) 2022 SUSE LLC
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


%{?!python_module:%define python_module() python3-%{**}}
%define pythons python3
%define skip_python2 1
%define skip_python36 1
Name:           solaar
Version:        1.1.8
Release:        0
Summary:        Linux devices manager for the Logitech Unifying Receiver
License:        GPL-2.0-or-later
Group:          Hardware/Other
URL:            https://pwr-solaar.github.io/Solaar
Source0:        Solaar-%{version}.tar.gz
#PATCH-FIX-OPENSUSE solaar-fix-desktop-categories.patch malcolmlewis@opensuse.org -- Fix desktop categories as per openSUSE desktop file specification.
Patch0:         solaar-fix-desktop-categories.patch
#
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module evdev}
BuildRequires:  %{python_module gobject-Gdk}
BuildRequires:  %{python_module gobject}
BuildRequires:  %{python_module hid-parser}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module python-xlib}
BuildRequires:  %{python_module pyudev}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module typing_extensions}
#
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  python-rpm-macros
BuildRequires:  typelib-1_0-Gtk-3_0
BuildRequires:  update-desktop-files
Requires:       python3-PyYAML
%if 0%{?suse_version} <= 1500
Requires:       python3-dataclasses
%endif
Requires:       python3-evdev
Requires:       python3-gobject
Requires:       python3-gobject-Gdk
Requires:       python3-hid-parser
Requires:       python3-psutil
Requires:       python3-python-xlib
Requires:       python3-pyudev
Requires:       python3-typing_extensions
#
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
sed -i 's#%{_bindir}/env python##' lib/solaar/gtk.py lib/solaar/tasks.py
%python_build

%install
%python_install
%fdupes %{buildroot}%{python3_sitelib}
%fdupes -s %{buildroot}%{_datadir}
%suse_update_desktop_file %{buildroot}%{_datadir}/applications/%{name}.desktop

install -d 0755 %{buildroot}%{_udevrulesdir}
install -m 0644 rules.d/42-logitech-unify-permissions.rules %{buildroot}%{_udevrulesdir}/42-logitech-unify-permissions.rules

ln -s solaar %{buildroot}%{_bindir}/solaar-cli

%posttrans udev
# This is needed to apply permissions to existing devices when the package is
# installed.
%{_bindir}/udevadm trigger --subsystem-match=hidraw --action=add

%files
%doc ChangeLog.md COPYRIGHT README.md Release_Notes.md
%license COPYING
%{_bindir}/%{name}
%{_bindir}/%{name}-cli
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/solaar.svg
%{_datadir}/metainfo/io.github.pwr_solaar.solaar.metainfo.xml
%{python_sitelib}/hidapi
%{python_sitelib}/logitech_receiver
%{python_sitelib}/keysyms
%{python_sitelib}/solaar
%{python_sitelib}/solaar-*

%files udev
%{_udevrulesdir}/42-logitech-unify-permissions.rules

%files doc
%doc docs/*

%changelog
