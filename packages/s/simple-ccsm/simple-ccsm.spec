#
# spec file for package simple-ccsm
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define _rev    c7b6d3ccd61a65e81125ddb8627d55f6
Name:           simple-ccsm
Version:        0.8.16
Release:        0
Summary:        Simple settings manager for Compiz
License:        GPL-2.0-or-later
Group:          System/X11/Utilities
URL:            https://gitlab.com/compiz/simple-ccsm
Source:         https://gitlab.com/compiz/simple-ccsm/uploads/%{_rev}/%{name}-%{version}.tar.xz
BuildRequires:  compiz < 0.9
BuildRequires:  fdupes
BuildRequires:  gobject-introspection-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
BuildRequires:  libcompizconfig < 0.9
BuildRequires:  python3-devel
BuildRequires:  update-desktop-files
Requires:       compiz < 0.9
Requires:       compiz-plugins < 0.9
Requires:       compiz-plugins-main < 0.9
Requires:       python3-cairo
Requires:       python3-ccm < 0.9
Requires:       python3-ccm >= 0.8.12
Requires:       python3-compizconfig < 0.9
Requires:       python3-gobject
Requires:       python3-gobject-cairo
Recommends:     %{name}-lang
Recommends:     compiz-plugins-extra < 0.9
# simple-ccsm-kde was last used in openSUSE 11.3.
Provides:       %{name}-kde = %{version}
Obsoletes:      %{name}-kde < %{version}
Provides:       ccsm = 0.8
BuildArch:      noarch
%if 0%{?suse_version} >= 1500 || 0%{?sle_version} >= 120200
Requires:       python3-gobject-Gdk
%endif

%description
Compiz settings manager focused on simplicity for an end-user.

%lang_package

%prep
%setup -q

%build
python3 setup.py build \
  --prefix=%{_prefix}    \
  --enableDesktopEffects

%install
python3 setup.py install \
  --root=%{buildroot} \
  --prefix=%{_prefix}

mv %{buildroot}%{_datadir}/{metainfo,appdata}/
%fdupes %{buildroot}%{_datadir}/
%suse_update_desktop_file -N "Desktop Effects" %{name}
%find_lang simple-ccsm

%if 0%{?suse_version} < 1500
%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun
%endif

%files
%license COPYING
%doc AUTHORS NEWS README.md
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{python3_sitelib}/simple_ccsm-*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%dir %{_datadir}/appdata/
%{_datadir}/appdata/%{name}.appdata.xml

%files lang -f %{name}.lang

%changelog
