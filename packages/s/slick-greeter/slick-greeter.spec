#
# spec file for package slick-greeter
#
# Copyright (c) 2022 SUSE LLC
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


%define _name   lightdm-slick-greeter
Name:           slick-greeter
Version:        1.5.9
Release:        0
Summary:        The slick-looking login screen application
License:        CC-BY-SA-3.0 AND GPL-3.0-only
Group:          System/X11/Displaymanagers
URL:            https://github.com/linuxmint/slick-greeter
Source:         https://github.com/linuxmint/slick-greeter/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# Some documentation for people writing branding packages, shipped in the branding-upstream package.
Source1:        README.GSettings-overrides
# PATCH-FEATURE-OPENSUSE slick-greeter-gtk-3.20.patch -- Restore GTK+ 3.20 support.
Patch0:         slick-greeter-gtk-3.20.patch
BuildRequires:  gnome-common
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.24
BuildRequires:  pkgconfig(cairo-ft)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gdk-x11-3.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(liblightdm-gobject-1) >= 1.12.0
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)

%description
The slick-looking greeter (login screen) application.
It is implemented as a LightDM greeter.

%package -n %{_name}
Summary:        The slick-looking login screen application
Group:          System/X11/Displaymanagers
Requires:       lightdm
Requires:       numlockx
Requires(post): update-alternatives
Requires(postun):update-alternatives
Recommends:     %{_name}-lang
Provides:       lightdm-greeter
%glib2_gsettings_schema_requires

%description -n %{_name}
The slick-looking greeter (login screen) application.
It is implemented as a LightDM greeter.

%lang_package -n %{_name}

%package -n %{_name}-branding-upstream
Summary:        Upstream branding of %{_name}
Group:          System/X11/Displaymanagers
Requires:       %{_name} = %{version}
Requires:       gnome-icon-theme
Requires:       gtk3-metatheme-adwaita
Requires:       ubuntu-fonts
Supplements:    (%{_name} and branding-upstream)
Conflicts:      %{_name}-branding
Provides:       %{_name}-branding = %{version}
BuildArch:      noarch
#BRAND: A /usr/share/glib-2.0/schemas/$NAME.gschema.override file can
#BRAND: be used to override the default value for GSettings keys. See
#BRAND: README.GSettings-overrides for more details. The branding
#BRAND: package should then have proper Requires for features changed
#BRAND: with such an override file.

%description -n %{_name}-branding-upstream
This package provides the upstream look and feel for
lightdm-slick-greeter.

%prep
%setup -q
cp -a %{SOURCE1} .
%patch0 -p1

%build
NOCONFIGURE=1 gnome-autogen.sh
%configure
%make_build

%install
%make_install
%find_lang %{name}

%if 0%{?suse_version} >= 1320
mkdir -p %{buildroot}%{_sysconfdir}/alternatives/
touch %{buildroot}%{_sysconfdir}/alternatives/lightdm-default-greeter.desktop
ln -s %{_sysconfdir}/alternatives/lightdm-default-greeter.desktop \
  %{buildroot}%{_datadir}/xgreeters/lightdm-default-greeter.desktop
%endif

%post -n %{_name}
update-alternatives --install \
  %{_datadir}/xgreeters/lightdm-default-greeter.desktop \
  lightdm-default-greeter.desktop \
  %{_datadir}/xgreeters/%{name}.desktop \
  10
%if 0%{?suse_version} < 1500
%glib2_gsettings_schema_post
%endif

%postun -n %{_name}
if [ "$1" = 0 ]; then
    update-alternatives --remove \
      lightdm-default-greeter.desktop \
      %{_datadir}/xgreeters/%{name}.desktop
fi
%if 0%{?suse_version} < 1500
%glib2_gsettings_schema_postun
%endif

%files -n %{_name}
%license COPYING
%doc README.md
%{_sbindir}/%{name}
%{_bindir}/%{name}-set-keyboard-layout
%{_bindir}/%{name}-check-hidpi
%{_datadir}/%{name}/
%dir %{_datadir}/xgreeters/
%{_datadir}/xgreeters/%{name}.desktop
%if 0%{?suse_version} >= 1320
%{_datadir}/xgreeters/lightdm-default-greeter.desktop
%else
%ghost %attr(0644,root,root) %{_datadir}/xgreeters/lightdm-default-greeter.desktop
%endif
%ghost %attr(0644,root,root) %{_sysconfdir}/alternatives/lightdm-default-greeter.desktop
%{_datadir}/glib-2.0/schemas/*%{name}.gschema.xml
%{_mandir}/man8/%{name}.8%{?ext_man}
%{_mandir}/man1/%{name}-set-keyboard-layout.1%{?ext_man}
%{_mandir}/man1/%{name}-check-hidpi.1%{?ext_man}

%files -n %{_name}-lang -f %{name}.lang

%files -n %{_name}-branding-upstream
%doc README.GSettings-overrides

%changelog
