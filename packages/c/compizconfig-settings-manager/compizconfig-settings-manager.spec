#
# spec file for package compizconfig-settings-manager
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define _rev    1c1b988479082609fb5ca1103a7120ac
%define _name   ccsm
Name:           compizconfig-settings-manager
Version:        0.8.18
Release:        0
Summary:        Settings Manager for Compiz (CCSM)
License:        GPL-2.0-or-later
URL:            https://gitlab.com/compiz/ccsm
Source:         https://gitlab.com/compiz/ccsm/uploads/%{_rev}/%{_name}-%{version}.tar.xz
BuildRequires:  gettext
BuildRequires:  gobject-introspection-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
BuildRequires:  python-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-ccm = %{version}
Provides:       %{_name} = 0.8
BuildArch:      noarch

%description
Compiz Config and Settings tool (CCSM).

%lang_package

%package -n compizconfig-settings-manager-common
Summary:        Settings Manager for Compiz -- Common files
BuildArch:      noarch

%description -n compizconfig-settings-manager-common
Common files for the Compiz Config and Settings tool (CCSM).

%package -n python3-ccm
Summary:        CompizConfig Manager Backend
Requires:       compiz < 0.9
Requires:       compizconfig-settings-manager-common
Requires:       python3-cairo
Requires:       python3-compizconfig < 0.9
Requires:       python3-gobject
Requires:       python3-gobject-Gdk
Requires:       python3-gobject-cairo
Requires:       python3-xml
Obsoletes:      python-ccm < 0.8.14

%description -n python3-ccm
The backend to Compiz Config Manager.

%prep
%setup -q -n %{_name}-%{version}

%build
%py3_build \
  --prefix=%{_prefix}

%install
%py3_install
%find_lang %{_name}

%files
%license COPYING
%doc NEWS
%{_bindir}/%{_name}
%dir %{_datadir}/compiz/
%{_datadir}/compiz/icons/
%{_datadir}/applications/%{_name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{_name}.*
%{_datadir}/metainfo/%{_name}.appdata.xml

%files lang -f %{_name}.lang

%files -n compizconfig-settings-manager-common
%{_datadir}/%{_name}/

%files -n python3-ccm
%{python3_sitelib}/ccm/
%{python3_sitelib}/%{_name}*

%changelog
