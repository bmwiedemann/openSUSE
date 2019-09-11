#
# spec file for package desktop-data-openSUSE
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2018 Stasiek Michalski <hellcp@opensuse.org>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
#
# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

%if 0%{?is_opensuse}
%define branding_version     %(rpm -q --queryformat '%%{VERSION}' branding-openSUSE)
%endif

Name:           desktop-data-openSUSE
Version:        15.1.20181213
Release:        0
Summary:        Shared Desktop Files for openSUSE
Url:            https://github.com/openSUSE/desktop-data
License:        GPL-2.0-or-later
Group:          System/GUI/Other

Source:         desktop-data-%{version}.tar.xz
Source1:        %name.fillup
BuildArch:      noarch

PreReq:         %fillup_prereq

BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  perl-RPC-XML
BuildRequires:  update-desktop-files
BuildRequires:  xdg-menu
BuildRequires:  xdg-utils
BuildRequires:  wallpaper-branding
%if 0%{?is_opensuse}
BuildRequires:  branding-openSUSE
%endif

Requires:       hicolor-icon-theme
Requires:       xdg-utils
# This is the default cursor theme we reference in /etc/sysconfig/windowmanager
Requires:       dmz-icon-theme-cursors
%if 0%{?is_opensuse}
Requires:       wallpaper-branding = %{branding_version}
%endif

Provides:       desktop-branding = %{version}
Provides:       desktop-data

%description
This package contains shared desktop files, like the default
applications menu structure and the default wallpaper.

%package extra
Summary:        Additional wallpapers
Group:          System/GUI/Other
Requires:       desktop-data-openSUSE
Enhances:       desktop-data-openSUSE

%description extra
This package contains additional wallpapers.

%prep
%setup -n desktop-data-%{version}

%build
# Keep build empty

%install
cp -a * %{buildroot}/
mkdir -p %{buildroot}%{_sysconfdir}/xdg/menus/applications-merged

# Update all desktop files
for i in %{buildroot}%{_datadir}/desktop-directories/*.directory %{buildroot}%{_datadir}/wallpapers/*.desktop
do
    %suse_update_desktop_file "$i"
done

# Define the default mouse cursor
mkdir -p %{buildroot}%{_fillupdir}/
install -m 0644 %SOURCE1 \
  %{buildroot}%{_fillupdir}/sysconfig.windowmanager-%name

# Make call-browser executable, symlink
mkdir -p %{buildroot}%{_bindir}
ln -snf xdg-open %{buildroot}%{_bindir}/call-browser
ln -snf xdg-open %{buildroot}%{_bindir}/desktop-launch

# Check duplicates
%fdupes %{buildroot}%{_datadir}/icons

%check
# Check if it's a valid menu
export XDG_DATA_DIRS=%{buildroot}%{_datadir}/
export XDG_CONFIG_DIRS=%{buildroot}%{_sysconfdir}/xdg/
xdg_menu --die-on-error --format readable

%post
%{fillup_only -an windowmanager}

%files
%dir %{_sysconfdir}/xdg/menus
%dir %{_sysconfdir}/xdg/menus/applications-merged
%config(noreplace) %{_sysconfdir}/xdg/menus/*.menu
%config %{_sysconfdir}/profile.d/desktop-data.*
%{_datadir}/desktop-*
%{_datadir}/icons/hicolor/*
%{_fillupdir}/sysconfig.windowmanager-%name
%{_bindir}/call-browser
%{_bindir}/desktop-launch

%files extra
%{_datadir}/gnome-background-properties/desktop-data-openSUSE-extra.xml
%{_datadir}/wallpapers/

%changelog
