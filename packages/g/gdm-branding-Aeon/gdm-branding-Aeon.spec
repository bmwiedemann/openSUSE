#
# spec file for package gdm-branding-Aeon
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define gdm_version %(rpm -q --qf '%%{version}' gdm)
Name:           gdm-branding-Aeon
Version:        20240324
Release:        0
Summary:        The GNOME Display Manager -- openSUSE Aeon default configuration
License:        GPL-2.0-or-later
Group:          System/GUI/GNOME
Url:            http://projects.gnome.org/gdm/
Source99:       gdm-branding-Aeon-rpmlintrc
# For directory ownership:
BuildRequires:  gdm
# To be in sync with upstream defaults, do branding as a patch for upstream file.
# WARNING: As this package conflicts with gdm-branding-openSUSE, you cannot
#          reuse build root. You have to build in a clean build root every time!
BuildRequires:  gdm-branding-upstream
BuildRequires:  distribution-logos-openSUSE-Aeon
Requires:       gdm
Requires:       distribution-logos
Conflicts:      gdm-branding
Provides:       gdm-branding
Conflicts:      gdm-branding-MicroOS
Provides:       gdm-branding-MicroOS
BuildArch:      noarch

%description
The GNOME Display Manager is a system service that is responsible for
providing graphical log-ins and managing local and remote displays.

This package provides the openSUSE Aeon default configuration for gdm.

%prep
cp -a %{_sysconfdir}/gdm/custom.conf .

%build

%install
mkdir -p %{buildroot}%{_datadir}/gdm/greeter/images/
install -d %{buildroot}%{_sysconfdir}/gdm
install -m0644 custom.conf %{buildroot}%{_sysconfdir}/gdm/custom.conf
ln -sf %{_datadir}/pixmaps/distribution-logos/light-inline.svg %{buildroot}%{_datadir}/gdm/greeter/images/distributor.svg

%files
%config(noreplace) %{_sysconfdir}/gdm/custom.conf
%{_datadir}/gdm/greeter/images/distributor.svg
%dir %{_datadir}/gdm/greeter/images/

%changelog
