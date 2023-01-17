#
# spec file for package arandr
#
# Copyright (c) 2023 SUSE LLC
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


Name:           arandr
Version:        0.1.11
Release:        0
Summary:        Visual Front End for XRandR
License:        GPL-3.0-only
URL:            https://christian.amsuess.com/tools/arandr/
Source:         http://christian.amsuess.com/tools/arandr/files/%{name}-%{version}.tar.gz
Patch1:         arandr-fix_desktop_icon.patch
BuildRequires:  gobject-introspection
BuildRequires:  make
BuildRequires:  python3
BuildRequires:  python3-docutils
Requires:       python3-gobject
Requires:       python3-gobject-Gdk
Requires:       python3-pycairo
BuildRequires:  update-desktop-files
BuildArch:      noarch
%if 0%{?suse_version} >= 1220
Requires:       xrandr
%else
Requires:       xorg-x11
%endif

%description
ARandR is designed to provide a simple visual front end for XRandR. Relative
monitor positions are shown graphically and can be changed in a drag-and-drop
way.

%prep
%setup -q
%patch1

%build
python3 ./setup.py build

%install
python3 ./setup.py install \
    --prefix="%{_prefix}" \
    --root=%{buildroot}

%suse_update_desktop_file -r "%{name}" Settings DesktopSettings

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
%{python3_sitelib}/arandr-%{version}-py*.egg-info

%changelog
