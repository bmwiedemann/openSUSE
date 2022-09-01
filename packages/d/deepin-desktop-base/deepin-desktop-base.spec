#
# spec file for package deepin-desktop-base
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


%define _version 2022.07.26

Name:           deepin-desktop-base
Version:        20.6
Release:        0
Summary:        Base component for Deepin
License:        GPL-3.0-or-later
Group:          System/GUI/Other
URL:            https://github.com/linuxdeepin/deepin-desktop-base
Requires:       distribution-logos
Source0:        https://github.com/linuxdeepin/deepin-desktop-base/archive/%{_version}/%{name}-%{_version}.tar.gz
# PATCH-FIX-OPENSUSE do-not-installl-os-version.patch hillwood@opensuse.org - Don't install deepin os information
Patch0:         do-not-installl-os-version.patch
# PATCH-FIX-OPENSUSE add-suse-info.patch hillwood@opensuse.org - Use openSUSE information
Patch1:         add-suse-info.patch
Patch2:         desktop-version-fallback.patch

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

%build
%make_build

%install
%make_install
install -Dm644 distribution.info %{buildroot}%{_datadir}/deepin/
%ifarch ppc ppc64 ppc64le s390 s390x
install -d %{buildroot}%{_datadir}/deepin-manual/manual-assets/application/
%endif

# Make a symlink for deepin-version
ln -sfv %{_datadir}/deepin/desktop-version %{buildroot}/etc/deepin-version

%files
%doc CHANGELOG.md
%license LICENSE
%config(noreplace) %{_sysconfdir}/appstore.json
%{_sysconfdir}/*-version
%dir %{_datadir}/deepin/
%ifarch ppc ppc64 ppc64le s390 s390x
%dir %{_datadir}/deepin-manual/
%dir %{_datadir}/deepin-manual/manual-assets
%dir %{_datadir}/deepin-manual/manual-assets/application
%endif
%{_datadir}/deepin/distribution.info
%{_datadir}/deepin/*-version
%dir %{_datadir}/distro-info
%dir %{_datadir}/i18n
%{_datadir}/i18n/i18n_dependent.json
%{_datadir}/i18n/language_info.json

%changelog
