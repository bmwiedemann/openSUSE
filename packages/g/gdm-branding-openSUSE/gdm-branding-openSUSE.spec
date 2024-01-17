#
# spec file for package gdm-branding-openSUSE
#
# Copyright (c) 2023 SUSE LLC
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


%define gdm_version %(rpm -q --qf '%%{version}' gdm)
Name:           gdm-branding-openSUSE
Version:        15.1
Release:        0
Summary:        The GNOME Display Manager -- openSUSE default configuration
License:        GPL-2.0-or-later
Group:          System/GUI/GNOME
URL:            http://projects.gnome.org/gdm/
Source99:       gdm-branding-openSUSE-rpmlintrc
# For directory ownership:
BuildRequires:  gdm
# To be in sync with upstream defaults, do branding as a patch for upstream file.
# WARNING: As this package conflicts with gdm-branding-openSUSE, you cannot
#          reuse build root. You have to build in a clean build root every time!
BuildRequires:  gdm-branding-upstream
%if 0%{?sle_version} >= 120300
BuildRequires:  sed
%endif
BuildRequires:  distribution-logos-openSUSE-Tumbleweed
Requires:       distribution-logos
Requires:       gdm
Supplements:    (gdm and branding-openSUSE)
Conflicts:      gdm-branding
Provides:       gdm-branding
BuildArch:      noarch

%description
The GNOME Display Manager is a system service that is responsible for
providing graphical log-ins and managing local and remote displays.

This package provides the openSUSE default configuration for gdm.

%prep
cp -a %{_sysconfdir}/gdm/custom.conf .

%build

%install
mkdir -p %{buildroot}%{_datadir}/gdm/greeter/images/
install -d %{buildroot}%{_sysconfdir}/gdm
install -m0644 custom.conf %{buildroot}%{_sysconfdir}/gdm/custom.conf
%if (!0%{?is_opensuse} && 0%{?sle_version} >= 120300) || (0%{?is_opensuse} && 0%{?sle_version} <= 150400 && 0%{?sle_version} >= 120300)
sed -i -e "s/\[daemon\]/\[daemon\]\nInitialSetupEnable=False/g" %{buildroot}%{_sysconfdir}/gdm/custom.conf
%endif
ln -sf %{_datadir}/pixmaps/distribution-logos/light-inline.svg %{buildroot}%{_datadir}/gdm/greeter/images/distributor.svg

%files
%config(noreplace) %{_sysconfdir}/gdm/custom.conf
%{_datadir}/gdm/greeter/images/distributor.svg
%dir %{_datadir}/gdm/greeter/images/

%changelog
