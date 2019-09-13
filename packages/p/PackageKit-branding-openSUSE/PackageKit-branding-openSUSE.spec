#
# spec file for package PackageKit-branding-openSUSE
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


%define         build_openSUSE 1
%define         build_SLED 0
%define packagekit_version %(rpm -q --qf '%%{version}' PackageKit)
# Do not edit this auto generated file! Edit PackageKit-branding.spec.in.
Name:           PackageKit-branding-openSUSE
Version:        42.1
Release:        0
Summary:        Simple software installation management software -- openSUSE default configuration
License:        GPL-2.0-or-later
Group:          System/Daemons
URL:            http://packagekit.org/
Source0:        COPYING
Source1:        PackageKit-branding-ZYpp.conf
# PATCH-FEATURE-OPENSUSE PackageKit-branding-vendor.patch vuntz@opensuse.org -- Update the Vendor.conf file with distro-specific data
Patch0:         PackageKit-branding-vendor.patch
# PATCH-FEATURE-OPENSUSE PackageKit-branding-default-config.patch vuntz@opensues.org -- Change some default configuration
Patch1:         PackageKit-branding-default-config.patch
BuildRequires:  PackageKit >= 1.0.1
# To be in sync with upstream defaults, do branding as a patch for upstream file.
# WARNING: As this package conflicts with PackageKit-branding-openSUSE, you cannot
#          reuse build root. You have to build in a clean build root every time!
BuildRequires:  PackageKit-branding-upstream >= 1.0.1
Requires:       PackageKit = %{packagekit_version}
Supplements:    packageand(PackageKit:branding-openSUSE)
Conflicts:      PackageKit-branding
Provides:       PackageKit-branding = %{packagekit_version}
BuildArch:      noarch

%description
PackageKit is a system designed to make installing and updating
software on your computer easier.  The primary design goal is to unify
all the software graphical tools used in different distributions, and
use some of the latest technology like PolicyKit to make the process
suck less.

This package provides the openSUSE default configuration for
PackageKit.

%prep
cp -a %{SOURCE0} .
cp -a %{_sysconfdir}/PackageKit/* .
%patch0
%patch1 -p1

%build

%install
install -d %{buildroot}%{_sysconfdir}/PackageKit
# Do the loop this way to make sure we don't forget about any configuration file
for conf in %{_sysconfdir}/PackageKit/*; do
    case "$conf" in
        %{_sysconfdir}/PackageKit/events)
            # skip this, it's not something we brand
            ;;
        *)
            install -m0644 `basename $conf` %{buildroot}%{_sysconfdir}/PackageKit/
            ;;
    esac
done
install -m0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/PackageKit/ZYpp.conf

%files
%license COPYING

%config(noreplace) %{_sysconfdir}/PackageKit/PackageKit.conf
%{_sysconfdir}/PackageKit/Vendor.conf
%config(noreplace) %{_sysconfdir}/PackageKit/ZYpp.conf

%changelog
