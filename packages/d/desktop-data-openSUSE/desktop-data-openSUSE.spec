#
# spec file for package desktop-data-openSUSE
#
# Copyright (c) 2019 SUSE LLC.
# Copyright (c) 2018-2020 Stasiek Michalski <hellcp@opensuse.org>
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

%if 0%{?is_opensuse}
%define branding_version     %(rpm -q --queryformat '%%{VERSION}' branding-openSUSE)
%endif

Name:           desktop-data-openSUSE
Version:        15.2.20200107
Release:        0
Summary:        Shared Desktop Files for openSUSE
License:        GPL-2.0-or-later
URL:            https://github.com/openSUSE/desktop-data

Source:         desktop-data-%{version}.tar.xz
Source1:        %name.fillup
BuildArch:      noarch

PreReq:         %fillup_prereq

BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  perl-RPC-XML
BuildRequires:  update-desktop-files
BuildRequires:  wallpaper-branding
BuildRequires:  xdg-menu
BuildRequires:  xdg-utils
%if 0%{?is_opensuse}
BuildRequires:  branding-openSUSE
%endif

Requires:       hicolor-icon-theme
Requires:       xdg-utils
%if 0%{?is_opensuse}
Requires:       wallpaper-branding = %{branding_version}
%endif

Provides:       desktop-branding = %{version}
Provides:       desktop-data
Provides:       desktop-data-openSUSE-extra

Obsoletes:      desktop-data-openSUSE-extra

%description
This package contains shared desktop files, like the default
applications menu structure.

%prep
%setup -n desktop-data-%{version}

%build
# Keep build empty

%install
cp -a * %{buildroot}/
mkdir -p %{buildroot}%{_sysconfdir}/xdg/menus/applications-merged

# Update all desktop files
for i in %{buildroot}%{_datadir}/desktop-directories/*.directory
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
%{_fillupdir}/sysconfig.windowmanager-%name
%{_bindir}/call-browser
%{_bindir}/desktop-launch

%changelog
