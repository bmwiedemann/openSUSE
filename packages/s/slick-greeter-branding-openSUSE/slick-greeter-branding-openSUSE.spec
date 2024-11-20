#
# spec file for package slick-greeter-branding-openSUSE
#
# Copyright (c) 2024 SUSE LLC
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


%define lightdm_slick_greeter_version %(rpm -q --queryformat "%%{version}" lightdm-slick-greeter)
Name:           slick-greeter-branding-openSUSE
Version:        1.0
Release:        0
Summary:        openSUSE branding of slick-greeter
License:        GPL-3.0-only
Group:          System/X11/Displaymanagers
URL:            https://github.com/linuxmint/slick-greeter
Source1:        slick-greeter-branding.gschema.override.in
BuildRequires:  lightdm
BuildRequires:  lightdm-slick-greeter
BuildRequires:  lightdm-slick-greeter-branding-upstream
BuildRequires:  pkgconfig
BuildRequires:  wallpaper-branding-openSUSE
BuildRequires:  pkgconfig(glib-2.0)
BuildArch:      noarch

%description
This package provides the openSUSE look and feel for
slick-greeter.

%package -n lightdm-slick-greeter-branding-openSUSE
Summary:        openSUSE branding of lightdm-slick-greeter
Group:          System/X11/Displaymanagers
Requires:       adwaita-icon-theme
Requires:       cantarell-fonts
Requires:       gtk3-metatheme-adwaita
Requires:       lightdm-slick-greeter = %{lightdm_slick_greeter_version}
Requires:       wallpaper-branding-openSUSE
Supplements:    (lightdm-slick-greeter and branding-openSUSE)
Conflicts:      lightdm-slick-greeter-branding
Provides:       lightdm-slick-greeter-branding = %{lightdm_slick_greeter_version}
%glib2_gsettings_schema_requires

%description -n lightdm-slick-greeter-branding-openSUSE
This package provides the openSUSE look and feel for
lightdm-slick-greeter.

%prep
%setup -q -c -T
cp -f %{SOURCE1} slick-greeter-branding.gschema.override.in

%build
cp %{_defaultlicensedir}/lightdm-slick-greeter/COPYING .

bg="%{_datadir}/wallpapers/openSUSEdefault/contents/images/default.png"
sed -e "s|@@WALLPAPER_URI@@|$bg|" \
  slick-greeter-branding.gschema.override.in > \
  slick-greeter-branding.gschema.override

%install
install -Dpm 0644 slick-greeter-branding.gschema.override \
  %{buildroot}%{_datadir}/glib-2.0/schemas/20_slick-greeter-branding.gschema.override

%if 0%{?suse_version} <= 1500
%post -n lightdm-slick-greeter-branding-openSUSE
%glib2_gsettings_schema_post

%postun -n lightdm-slick-greeter-branding-openSUSE
%glib2_gsettings_schema_postun
%endif

%check

%files -n lightdm-slick-greeter-branding-openSUSE
%license COPYING
%{_datadir}/glib-2.0/schemas/20_slick-greeter-branding.gschema.override

%changelog
