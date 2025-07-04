#
# spec file for package arandr
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2012 Pascal Bleser <pascal.bleser@opensuse.org>
# Copyright (c) 2013,2019 B1 Systems GmbH, Vohburg, Germany <seife+obs@b1-systems.com>
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


%define pythons python3
Name:           arandr
Version:        0.1.11
Release:        0
Summary:        Visual Front End for XRandR
License:        GPL-3.0-only
URL:            https://christian.amsuess.com/tools/arandr/
Source:         http://christian.amsuess.com/tools/arandr/files/%{name}-%{version}.tar.gz
Patch1:         arandr-fix_desktop_icon.patch
Patch2:         reproducible.patch
BuildRequires:  %{python_module base}
BuildRequires:  %{python_module docutils}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  gobject-introspection
BuildRequires:  make
Requires:       python3-gobject
Requires:       python3-gobject-Gdk
Requires:       python3-pycairo
Requires:       xorg-x11
BuildArch:      noarch

%description
ARandR is designed to provide a simple visual front end for XRandR. Relative
monitor positions are shown graphically and can be changed in a drag-and-drop
way.

%prep
%autosetup -p0

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{python3_sitelib}/screenlayout

# removed obsolete suse_update_desktop_file
#suse_update_desktop_file -r "${name}" Settings DesktopSettings
# all it did was this, which doesn't look substantial
#-Categories=Settings;HardwareSettings;
#+Categories=Settings;DesktopSettings;

%find_lang "%{name}"

chmod 0755 "%{buildroot}%{_bindir}"/*

%files -f "%{name}.lang"
%license COPYING
%doc ChangeLog NEWS README TODO
%{_bindir}/%{name}
%{_bindir}/unxrandr
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_mandir}/man1/unxrandr.1%{?ext_man}
%{python3_sitelib}/screenlayout/
%{python3_sitelib}/arandr-%{version}.dist-info

%changelog
