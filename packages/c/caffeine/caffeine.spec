#
# spec file for package caffeine
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2011 Malcolm J Lewis <malcolmlewis@opensuse.org>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%if %{suse_version} == 1315 && ! 0%{?is_opensuse}
%define __requires_exclude typelib\\(AppIndicator3\\)
%endif

Name:           caffeine
Version:        2.8.3
Release:        0
Summary:        Utility to inhibit screensaver and sleep modes
License:        GPL-3.0+ and LGPL-3.0+
Group:          System/GUI/GNOME
Url:            https://launchpad.net/caffeine
Source0:        https://launchpad.net/ubuntu/+archive/primary/+files/%{name}_%{version}.orig.tar.gz
# PATCH-FIX-UPSTREAM caffeine-fix-desktop-file-semicolon-trailing-character p.drouand@gmail.com -- Fix missing semicolon in Keywords entries.
Patch1:         caffeine-fix-desktop-file-semicolon-trailing-character.patch
BuildRequires:  fdupes
# For typelib() Requires
BuildRequires:  gobject-introspection
BuildRequires:  hicolor-icon-theme
BuildRequires:  python3-devel
BuildRequires:  update-desktop-files
Requires:       python3-xdg
Requires:       python3-xlib
Provides:       %{name}-lang = %{version}
Obsoletes:      %{name}-lang < %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Caffeine is a status bar application able to temporarily prevent the
activation of both the screensaver and the "sleep" powersaving mode.

%prep
%setup -q -n %{name}
%patch1 -p1

%build
python3 setup.py build

%install
python3 setup.py install -O1 --prefix=%{_prefix} --root=%{buildroot}
%suse_update_desktop_file -G Caffeine -r -u %{buildroot}%{_datadir}/applications/caffeine.desktop Utility TrayIcon
%suse_update_desktop_file -G Caffeine -r -u %{buildroot}%{_sysconfdir}/xdg/autostart/%{name}.desktop Utility TrayIcon
%find_lang %{name}-indicator
# Remove ubuntu icons for now
rm -rf %{buildroot}%{_datadir}/icons/ubuntu-mono-dark

%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun

%files -f %{name}-indicator.lang
%defattr(-,root,root)
%doc COPYING COPYING.LESSER README
%{_bindir}/caffein*
%{python3_sitelib}/ewmh*
%{python3_sitelib}/__pycache__/ewmh*
%{python3_sitelib}/caffeine-%{version}-py%{py3_ver}.egg-info
%{_datadir}/caffeine-indicator
%{_datadir}/applications/caffeine*.desktop
%{_datadir}/icons/*/*/*/caffeine*
%{_datadir}/pixmaps/caffeine.*
%{_mandir}/man?/caffein*%{?ext_man}
%{_sysconfdir}/xdg/autostart/caffeine.desktop

%changelog
