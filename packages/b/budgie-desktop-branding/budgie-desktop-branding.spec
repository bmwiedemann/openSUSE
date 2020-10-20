#
# spec file for package budgie-desktop-branding
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2020 Callum Farmer <callumjfarmer13@gmail.com>
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
%if !0%{?is_backports}
%define nsuffix openSUSE
%define isnot SLE
%else
%define nsuffix SLE
%define isnot openSUSE
%endif

Name:           budgie-desktop-branding
Version:        20201017.1
Release:        0
Summary:        Branding of the Budgie Desktop Environment
Group:          System/GUI/Other
License:        GPL-2.0-only AND CC-BY-SA-3.0
URL:            https://github.com/gmbr3/budgie-desktop-branding
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  meson
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  hicolor-icon-theme

%description
This package provides the look and feel for the Budgie
desktop environment.

%package %{nsuffix}
Summary:        %{nsuffix} branding of the Budgie Desktop Environment
Requires:       budgie-desktop
Supplements:    (budgie-desktop and branding-%{nsuffix})
Conflicts:      budgie-desktop-branding
Provides:       budgie-desktop-branding = %{version}
BuildArch:      noarch
# Best themes/icons for Budgie in openSUSE
Recommends:     wallpaper-branding-%{nsuffix}
Recommends:     gtk3-metatheme-greybird-geeko
Recommends:     adwaita-icon-theme
# Recommend openSUSE favourited packages
Recommends:     gnome-terminal
Recommends:     yast2-control-center
Recommends:     firefox

%description %{nsuffix}
This package provides the %{nsuffix} look and feel for the Budgie
desktop environment.

%package upstream
Summary:        Upstream branding of the Budgie Desktop Environment
Requires:       budgie-desktop
Supplements:    (budgie-desktop and branding-upstream)
Conflicts:      budgie-desktop-branding
Provides:       budgie-desktop-branding = %{version}
Recommends:     gnome-backgrounds
Recommends:     gtk3-metatheme-greybird
Recommends:     adwaita-icon-theme
BuildArch:      noarch

%description upstream
This package provides the upstream look and feel for the Budgie
desktop environment.


%prep
%setup -q -n budgie-desktop-branding-%{version}

%build
%meson -Dversion=%{nsuffix},upstream
%meson_build

%install
%meson_install
%if !0%{?is_backports} && 0%{?suse_version} < 1550
sed -e 's-5120x3200-3840x2400-g' -i %{buildroot}%{_datadir}/glib-2.0/schemas/21_budgie_gnome_settings_%{nsuffix}.gschema.override
%endif
%if 0%{?is_backports} && 0%{?sle_version} < 150300
sed -e 's-5120x2880-1920x1200-g' -i %{buildroot}%{_datadir}/glib-2.0/schemas/21_budgie_gnome_settings_%{nsuffix}.gschema.override
%endif
%if 0%{?is_backports} && 0%{?suse_version} < 1550
sed -e 's-png-jpg-g' -i %{buildroot}%{_datadir}/glib-2.0/schemas/21_budgie_gnome_settings_%{nsuffix}.gschema.override
%endif

%files %{nsuffix}
%license LICENSE LICENSE.CC-BY-SA-3.0
%doc README.md
%{_datadir}/glib-2.0/schemas/21_budgie_gnome_settings_%{nsuffix}.gschema.override
%{_datadir}/icons/hicolor/scalable/apps/budgie-%{nsuffix}-distributor-logo.svg

%files upstream
%license LICENSE LICENSE.CC-BY-SA-3.0
%doc README.md
%{_datadir}/glib-2.0/schemas/21_budgie_gnome_settings_upstream.gschema.override

%changelog
