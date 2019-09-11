#
# spec file for package fusion-icon
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           fusion-icon
Version:        0.2.4
Release:        0
Summary:        Tray icon to manage Compiz
License:        GPL-2.0+
Group:          System/GUI/Other
Url:            https://github.com/compiz-reloaded/fusion-icon
Source:         https://github.com/compiz-reloaded/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source1:        %{name}.1
BuildRequires:  fdupes
BuildRequires:  gobject-introspection-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  python3
BuildRequires:  update-desktop-files
Requires:       Mesa-demo-x
Requires:       python3-compizconfig
Requires:       python3-gobject
Requires:       python3-qt5
Requires:       xvinfo
Recommends:     compiz-gnome < 0.9
Suggests:       compizconfig-settings-manager < 0.9
BuildArch:      noarch
%if 0%{?suse_version} > 1320 || 0%{?sle_version} >= 120200
Requires:       python3-gobject-Gdk
%endif

%description
This package provides a tray icon that allows you to easily enable,
disable and restart Compiz, and change the currently used window
manager and/or window decorator.

%prep
%setup -q
cp -f %{SOURCE1} %{name}.1

%build
python3 setup.py build \
  --with-qt=5.0 --with-gtk=3.0

%install
python3 setup.py install \
  --root=%{buildroot} \
  --prefix=%{_prefix}

mv %{buildroot}%{_datadir}/{metainfo,appdata}/
install -Dpm 0644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1
%suse_update_desktop_file -r %{name} Utility DesktopUtility
%fdupes %{buildroot}%{python_sitelib}/

%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun

%files
%defattr(-,root,root)
%doc COPYING NEWS
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%dir %{_datadir}/appdata/
%{_datadir}/appdata/%{name}.appdata.xml
%{python3_sitelib}/FusionIcon/
%{python3_sitelib}/fusion_icon-*
%{_mandir}/man?/%{name}.?%{?ext_man}

%changelog
