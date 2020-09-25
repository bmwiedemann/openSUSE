#
# spec file for package glib2
#
# Copyright (c) 2020 SUSE LLC
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


%define flavor @BUILD_FLAVOR@
%if "%{flavor}" == ""
%define branding_name %{nil}
ExclusiveArch:  %{nil}
%else
%define branding_name %{flavor}
%define dash -
%if "%{flavor}" == "SLE"
%define build_SLE 1
%else
%define build_openSUSE 1
%endif
%if (0%{?build_SLE} && 0%{?is_opensuse}) || (0%{?build_openSUSE} && ! 0%{?is_opensuse})
# Don't build SLE branding on openSUSE and vice-versa
ExclusiveArch:  %{nil}
%endif
%endif
%define gio_real_package %(rpm -q --qf '%%{name}' --whatprovides gio)
%define gio_version %(rpm -q --qf '%%{version}' %{gio_real_package})
Name:           glib2-branding%{?dash}%{branding_name}
Summary:        General-Purpose Utility Library -- %{branding_name} default configuration
License:        BSD-3-Clause
Group:          System/GUI/GNOME
URL:            http://www.gtk.org/
Source:         glib2-branding-gnome_defaults.conf
Source1:        glib2-branding-COPYING
Source2:        glib2-branding.gschema.override.in
# We need glib2-branding-upstream else, the call to SuSEconfig.glib2 fails
BuildRequires:  glib2-branding-upstream
BuildRequires:  glib2-devel
BuildRequires:  wallpaper-branding-%{branding_name}
BuildArch:      noarch
%if 0%{?build_openSUSE}
Version:        42.1
Release:        0
%else
Version:        15
Release:        0
%endif

%description
This package provides %{branding_name} defaults for settings stored with
GSettings and applications used by the MIME system.

%package -n gio-branding-%{branding_name}
Summary:        %{branding_name} definitions of default settings and applications
Group:          System/GUI/GNOME
Requires:       %{gio_real_package} = %{gio_version}
Recommends:     sound-theme-freedesktop
# For wallpaper
Recommends:     (wallpaper-branding-%{branding_name} if gnome-shell)
Supplements:    packageand(%{gio_real_package}:branding-%{branding_name})
Conflicts:      gio-branding
Provides:       glib2-branding-%{branding_name} = %{version}
Obsoletes:      glib2-branding-%{branding_name} < %{version}
Provides:       gio-branding = %{gio_version}
%glib2_gsettings_schema_requires
%if 0%{?build_SLE}
# Obsolete SLE11 packages to resolve file conflicts on sle11->sle12 upgrade
Obsoletes:      glib2-branding-SLED
Obsoletes:      glib2-branding-SLES
%endif

%description -n gio-branding-%{branding_name}
This package provides %{branding_name} defaults for settings stored with
GSettings and applications used by the MIME system.

%prep
%setup -q -T -c %{name}-%{version}
cp -a %{SOURCE0} gnome_defaults.conf
cp -a %{SOURCE1} COPYING
cp -a %{SOURCE2} glib2-branding.gschema.override.in

%build
test -f %{_datadir}/wallpapers/%{branding_name}-default.xml
sed "s,@@WALLPAPER_URI@@,file://%{_datadir}/wallpapers/%{branding_name}-default.xml,;s,@@LOCKSCREEN_URI@@,file://%{_datadir}/wallpapers/%{branding_name}-default-static-lockscreen.xml,"  glib2-branding.gschema.override.in > glib2-branding.gschema.override
#for sound theme
%if 0%{?build_openSUSE}
sed "s:@@IF_openSUSE@@::g" < glib2-branding.gschema.override | \
%if 0%{?sle_version}
    sed "s:@@IF_LEAP@@::g" | \
%endif
    grep -v ^@@IF_ > %{branding_name}-branding.gschema.override
%endif
%if 0%{?build_SLE}
sed "s:@@IF_SLE@@::g" < glib2-branding.gschema.override | grep -v ^@@IF_ > %{branding_name}-branding.gschema.override
%endif

%install
install -d %{buildroot}%{_sysconfdir}
install -m0644 gnome_defaults.conf %{buildroot}%{_sysconfdir}/
install -d %{buildroot}%{_datadir}/glib-2.0/schemas
install -m0644 %{branding_name}-branding.gschema.override %{buildroot}%{_datadir}/glib-2.0/schemas/

%files -n gio-branding-%{branding_name}
%license COPYING
%config (noreplace) %{_sysconfdir}/gnome_defaults.conf
%{_datadir}/glib-2.0/schemas/%{branding_name}-branding.gschema.override

%changelog
