#
# spec file for package deepin-branding-openSUSE
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2017 Hillwood Yang <hillwood@opensuse.org>
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

%define deepin_desktop_schemas_version %(rpm -q --queryformat '%%{VERSION}' deepin-desktop-schemas)
%define deepin_launcher_version %(rpm -q --queryformat '%%{VERSION}' deepin-launcher)

Name:           deepin-branding-openSUSE
Version:        15.0
Release:        0
Summary:        openSUSE Branding of the Deepin Desktop Environment
License:        GPL-2.0+
URL:            https://github.com/linuxdeepin
Group:          System/GUI/Other
Source0:        deepin-launcher.svg
Source1:        com.deepin.dde.appearance.gschema.xml
Source2:        com.deepin.dde.desktop.gschema.xml
Source3:        com.deepin.dde.dock.gschema.xml
BuildRequires:  deepin-desktop-schemas
BuildRequires:  deepin-launcher
BuildRequires:  deepin-icon-theme
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package provides the openSUSE look and feel for the deepin desktop environment.

%package -n deepin-desktop-schemas-branding-openSUSE
Summary:        openSUSE Branding of the Deepin Desktop Environment
Requires:       deepin-desktop-schemas
Conflicts:      otherproviders(deepin-desktop-schemas-branding)
Provides:       deepin-desktop-schemas-branding = %{deepin_desktop_schemas_version}
Supplements:    packageand(deepin-desktop-schemas:branding-openSUSE)

%description -n deepin-desktop-schemas-branding-openSUSE
This package provides the openSUSE definition for Deepin Desktop GSchemas.

%package -n deepin-launcher-branding-openSUSE
Summary:        openSUSE Branding of the Deepin Launcher
Requires:       deepin-launcher
Conflicts:      otherproviders(deepin-launcher-schemas-branding)
Provides:       deepin-launcher-branding = %{deepin_launcher_version}
Supplements:    packageand(deepin-launcher:branding-openSUSE)

%description -n deepin-launcher-branding-openSUSE
This package provides the openSUSE Logo for the deepin-launcher

%prep

%build

%install
install -d %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
install -d %{buildroot}%{_datadir}/glib-2.0/schemas/
install -m 0644 %{SOURCE1} %{SOURCE2} %{SOURCE3} %{buildroot}%{_datadir}/glib-2.0/schemas/

pushd %{_datadir}/icons/bloom/places
ICON=`ls`
popd
for i in $ICON
do
    install -d %{buildroot}%{_datadir}/icons/bloom/places/$i/
    install -m 0644 %{SOURCE0} %{buildroot}%{_datadir}/icons/bloom/places/$i/
    install -d %{buildroot}%{_datadir}/icons/bloom-dark/places/$i/
    install -m 0644 %{SOURCE0} %{buildroot}%{_datadir}/icons/bloom-dark/places/$i/
done


%files -n deepin-desktop-schemas-branding-openSUSE
%defattr(-,root,root,-)
%{_datadir}/glib-2.0/schemas/*.xml

%files -n deepin-launcher-branding-openSUSE
%defattr(-,root,root,-)
%{_datadir}/icons/bloom
%{_datadir}/icons/bloom-dark

%changelog
