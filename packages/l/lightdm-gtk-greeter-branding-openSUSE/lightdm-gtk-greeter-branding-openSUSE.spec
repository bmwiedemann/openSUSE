#
# spec file for package lightdm-gtk-greeter-branding-openSUSE
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2012 Guido Berhoerster <gber@opensuse.org>.
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


%define lightdm_gtk_greeter_version %(rpm -q --queryformat "%%{version}" lightdm-gtk-greeter)

Name:           lightdm-gtk-greeter-branding-openSUSE
Version:        2.0
Release:        0
Summary:        openSUSE branding of lightdm-gtk-greeter
License:        GPL-3.0-or-later
Group:          System/X11/Displaymanagers
Url:            https://launchpad.net/lightdm-gtk-greeter
Source0:        lightdm-gtk-greeter.conf
Source1:        lightdm-gtk-greeter-opensuse.png
BuildRequires:  lightdm
BuildRequires:  lightdm-gtk-greeter
# default background image
Requires:       wallpaper-branding
# default gtk3 theme
Requires:       gtk3-metatheme-adwaita
Requires:       lightdm-gtk-greeter = %{lightdm_gtk_greeter_version}
Provides:       lightdm-gtk-greeter-branding = %{lightdm_gtk_greeter_version}
Conflicts:      otherproviders(lightdm-gtk-greeter-branding)
Supplements:    packageand(lightdm-gtk-greeter:branding-openSUSE)
# switch to the upstream versioning scheme
Obsoletes:      lightdm-gtk-greeter-branding = 12.1
BuildArch:      noarch

%description
This package provides the openSUSE look and feel for lightdm-gtk-greeter.

%prep

%build
cp %{_defaultlicensedir}/lightdm-gtk-greeter/COPYING .

%install
install -D -p -m 644 %{SOURCE0} %{buildroot}%{_sysconfdir}/lightdm/lightdm-gtk-greeter.conf
install -D -p -m 644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/lightdm-gtk-greeter-opensuse.png

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%license COPYING
%config(noreplace) %{_sysconfdir}/lightdm/lightdm-gtk-greeter.conf
%{_datadir}/pixmaps/lightdm-gtk-greeter-opensuse.png

%changelog
