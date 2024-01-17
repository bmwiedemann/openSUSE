#
# spec file for package mate-tweak
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


%define _name   mate_tweak
Name:           mate-tweak
Version:        22.10.0
Release:        0
Summary:        MATE desktop tweak tool
License:        GPL-2.0-or-later
Group:          System/GUI/Other
URL:            https://github.com/ubuntu-mate/mate-tweak
Source:         https://github.com/ubuntu-mate/mate-tweak/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE mate-tweak-use-matemenu.patch sor.alexei@meowr.ru -- Layouts are patched to use mate-menu instead of mintMenu or gnome-main-menu.
Patch0:         mate-tweak-use-matemenu.patch
BuildRequires:  Mesa-demo-x
BuildRequires:  dconf
BuildRequires:  fdupes
BuildRequires:  gobject-introspection-devel
BuildRequires:  intltool
BuildRequires:  python3
BuildRequires:  python3-configobj
BuildRequires:  python3-distutils-extra
BuildRequires:  python3-gobject
BuildRequires:  python3-psutil
BuildRequires:  python3-setproctitle
BuildRequires:  python3-setuptools
BuildRequires:  update-desktop-files
Requires:       Mesa-demo-x
Requires:       dconf
Requires:       mate-panel
Requires:       python3-configobj
Requires:       python3-distro
Requires:       python3-gobject
Requires:       python3-gobject-Gdk
Requires:       python3-psutil
Requires:       python3-setproctitle
# For privilege granting.
Requires:       xdg-utils
Recommends:     mate-applet-indicator
Suggests:       mate-hud
BuildArch:      noarch

%description
Configures some aspects of the MATE desktop not exposed via the
MATE Control Centre applets.

Settings that can be handled via MATE Tweak:
 * Show/hide standard desktop icons.
 * Panel fine-tuning (icon visibility, in menus and on buttons,
   icon size, button labelling, contex menus, etc.).
 * Window manager fine-tuning.

%lang_package

%prep
%autosetup -p1
# Make world a bit simpler.
sed -i "s/'pkexec', '/'xdg-su', '-c /g" %{name}
sed -i '/polkit/d' setup.py

%build
%py3_build

%install
%py3_install

# Give gi-find-deps.sh a bait.
ln -s %{_bindir}/%{name} %{buildroot}%{_prefix}/lib/%{name}/%{name}.py

rm %{buildroot}%{python3_sitelib}/setup.py
%py3_compile %{buildroot}%{python3_sitelib}/

%fdupes %{buildroot}%{python3_sitelib}/
%find_lang %{name}

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_bindir}/marco-*
%{_prefix}/lib/%{name}/
%{python3_sitelib}/%{_name}-*
%pycache_only %{python3_sitelib}/__pycache__
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/marco-*.desktop
%{_mandir}/man?/%{name}.?%{?ext_man}
%{_mandir}/man?/*-no-composite.?%{?ext_man}
%{_mandir}/man?/marco-glx.?%{?ext_man}
%{_mandir}/man?/marco-xr_glx_hybrid.?%{?ext_man}
%{_mandir}/man?/marco-xrender.?%{?ext_man}

%files lang -f %{name}.lang

%changelog
