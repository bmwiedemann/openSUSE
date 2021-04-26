#
# spec file for package deepin-desktop-schemas
#
# Copyright (c) 2021 SUSE LINUX GmbH, Nuernberg, Germany.
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

Name:           deepin-desktop-schemas
Version:        5.9.5
Release:        0
Summary:        GSettings deepin desktop-wide schemas
License:        GPL-3.0+
URL:            https://github.com/linuxdeepin/deepin-desktop-schemas
Source0:        https://github.com/linuxdeepin/deepin-desktop-schemas/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         use-override-tool-in-system-default.patch
Group:          System/GUI/Other
BuildRequires:  deepin-override-tool
BuildRequires:  python3
BuildRequires:  glib2-tools
Requires:       dconf
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
deepin-desktop-schemas contains a collection of GSettings schemas for
settings shared by various components of a desktop.

%package -n deepin-desktop-schemas-branding-upstream
Summary:        Upstream Branding of the Deepin Desktop Environment
Requires:       deepin-desktop-schemas
Conflicts:      otherproviders(deepin-desktop-schemas-branding)
Provides:       deepin-desktop-schemas-branding = %{version}
Supplements:    packageand(deepin-desktop-schemas:branding-upstream)

%description -n deepin-desktop-schemas-branding-upstream
This package provides the upstream definition for Deepin Desktop GSchemas.

%prep
%autosetup -p1
sed -i 's|backgrounds/default_background.jpg|wallpapers/openSUSEdefault/contents/images/1920x1080.jpg|g' \
    overrides/common/com.deepin.wrap.gnome.desktop.override
sed -i '/display-mode/s|fashion|efficient|' overrides/common/desktop/dock.override

%build
make %{?_smp_mflags}

%install
%make_install

%files
%defattr(-,root,root,-)
%doc README.md CHANGELOG.md
%license LICENSE
%{_datadir}/glib-2.0/schemas/*
%{_datadir}/deepin-appstore
%{_datadir}/deepin-app-store
%{_datadir}/%{name}
%exclude %{_datadir}/glib-2.0/schemas/com.deepin.dde.appearance.gschema.xml
%exclude %{_datadir}/glib-2.0/schemas/com.deepin.dde.dock.gschema.xml
%exclude %{_datadir}/glib-2.0/schemas/com.deepin.dde.desktop.gschema.xml

%files -n deepin-desktop-schemas-branding-upstream
%defattr(-,root,root,-)
%{_datadir}/glib-2.0/schemas/com.deepin.dde.appearance.gschema.xml
%{_datadir}/glib-2.0/schemas/com.deepin.dde.dock.gschema.xml
%{_datadir}/glib-2.0/schemas/com.deepin.dde.desktop.gschema.xml

%changelog
