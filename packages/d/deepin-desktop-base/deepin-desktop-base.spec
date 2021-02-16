
# spec file for package deepin-desktop-base
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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

%define _version 2020.12.09
%define system_version %(rpm -q --queryformat '%%{VERSION}' openSUSE-release)
%if 0%{?suse_version} > 1500 
%define system_branch Tumbleweed
%else
%define system_branch Leap
%endif

Name:           deepin-desktop-base
Version:        20.1
Release:        0
Summary:        Base component for Deepin
License:        GPL-3.0+
URL:            https://github.com/linuxdeepin/deepin-desktop-base
Source0:        https://github.com/linuxdeepin/deepin-desktop-base/archive/%{_version}/%{name}-%{_version}.tar.gz
# PATCH-FIX-OPENSUSE do-not-installl-os-version.patch hillwood@opensuse.org - Don't install deepin os information
Patch0:         do-not-installl-os-version.patch
Group:          System/GUI/Other
# BuildRequires:  openSUSE-release
Requires:       qt5integration
# Recommends:     deepin-wallpapers

%description
This package provides some components for the Deepin desktop environment:
Deepin logo, desktop version, login screen background image, and
language information.

%prep
%autosetup -p1 -n %{name}-%{_version}

# Remove Deepin distro's lsb-release
# Don't override systemd timeouts
# Remove apt-specific templates
sed -i -E '/lsb-release|systemd|apt/d' Makefile

# Fix data path
sed -i 's|/usr/lib|%{_datadir}|' Makefile

# Set openSUSE version information
# sed -i 's|@@VERSION@@|branch version|g; s|Desktop||g; s|桌面版||g' files/suse-version.in
# sed -i "s|branch|%{system_branch}|g; s|version|%{system_version}|g" files/suse-version.in

%build
%make_build

%install
%make_install

# Make a symlink for deepin-version
ln -sfv %{_datadir}/deepin/desktop-version %{buildroot}/etc/deepin-version
# ln -sfv %{_datadir}/deepin/suse-version %{buildroot}/etc/suse-version

%files
%doc CHANGELOG.md
%license LICENSE
%config(noreplace) %{_sysconfdir}/appstore.json
%{_sysconfdir}/*-version
%dir %{_datadir}/deepin/
%{_datadir}/deepin/*-version
%{_datadir}/deepin/uos_logo.svg
%dir %{_datadir}/distro-info
%dir %{_datadir}/i18n
%{_datadir}/i18n/i18n_dependent.json
%{_datadir}/i18n/language_info.json
%dir %{_datadir}/plymouth
%{_datadir}/plymouth/deepin-logo.png

%changelog
