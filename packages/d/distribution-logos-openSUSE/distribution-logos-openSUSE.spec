#
# spec file for package distribution-logos-openSUSE
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2021 Sasi Olin <hellcp@opensuse.org>.
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


Name:           distribution-logos-openSUSE
Version:        20250203
Release:        0
Summary:        Logos for openSUSE Distros
License:        CC-BY-SA-4.0
URL:            https://github.com/openSUSE/distribution-logos
# updated via "osc service manualrun"
Source:         distribution-logos-%{version}.tar.zst
BuildRequires:  hicolor-icon-theme
BuildRequires:  zstd
BuildArch:      noarch

%description
Logos for openSUSE Distributions

%if 0%{?sle_version} || 0%{?suse_version} == 1600
%package Leap
Summary:        Logos for openSUSE Leap
Conflicts:      distribution-logos
Obsoletes:      distribution-logos
Provides:       distribution-logos
Removepathpostfixes: .Leap
BuildArch:      noarch

%description Leap
Logos for openSUSE Leap

%package LeapMicro
Summary:        Logos for openSUSE Leap Micro
Conflicts:      distribution-logos
Obsoletes:      distribution-logos
Provides:       distribution-logos
Removepathpostfixes: .LeapMicro
BuildArch:      noarch

%description LeapMicro
Logos for openSUSE Leap Micro

%else

%package Tumbleweed
Summary:        Logos for openSUSE Tumbleweed
Conflicts:      distribution-logos
Obsoletes:      distribution-logos
Provides:       distribution-logos
Removepathpostfixes: .Tumbleweed
BuildArch:      noarch

%description Tumbleweed
Logos for openSUSE Tumbleweed

%package Slowroll
Summary:        Logos for openSUSE Slowroll
Conflicts:      distribution-logos
Obsoletes:      distribution-logos
Provides:       distribution-logos
Removepathpostfixes: .Slowroll
BuildArch:      noarch

%description Slowroll
Logos for openSUSE Slowroll

%package Kubic
Summary:        Logos for openSUSE Kubic
Conflicts:      distribution-logos
Obsoletes:      distribution-logos
Provides:       distribution-logos
Removepathpostfixes: .Kubic
BuildArch:      noarch

%description Kubic
Logos for openSUSE Kubic

%package MicroOS
Summary:        Logos for openSUSE MicroOS
Conflicts:      distribution-logos
Obsoletes:      distribution-logos
Provides:       distribution-logos
Removepathpostfixes: .MicroOS
BuildArch:      noarch

%description MicroOS
Logos for openSUSE MicroOS

%package Aeon
Summary:        Logos for openSUSE Aeon
Conflicts:      distribution-logos
Obsoletes:      distribution-logos
Provides:       distribution-logos
Removepathpostfixes: .Aeon
BuildArch:      noarch

%description Aeon
Logos for openSUSE Aeon

%package Kalpa
Summary:        Logos for openSUSE Kalpa
Conflicts:      distribution-logos
Obsoletes:      distribution-logos
Provides:       distribution-logos
Removepathpostfixes: .Kalpa
BuildArch:      noarch

%description Kalpa
Logos for openSUSE Kalpa


%endif

%package icons
Summary:        Icons with distribution logos
Requires:       distribution-logos
Conflicts:      systemd-icon-branding-openSUSE
Provides:       systemd-icon-branding
Obsoletes:      systemd-icon-branding-openSUSE < 84.87.20210910
Provides:       systemd-icon-branding-openSUSE = 84.87.20210910
BuildArch:      noarch

%description icons
Icons with openSUSE distribution logos.

%prep
%setup -q -n distribution-logos-%{version}

%build
# Skip build

%install
export NO_BRP_STALE_LINK_ERROR=yes
mkdir -p %{buildroot}%{_datadir}/pixmaps/distribution-logos
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/{scalable,symbolic}/apps
%if 0%{?sle_version} || 0%{?suse_version} == 1600
for distro in Leap LeapMicro; do \
%else
for distro in Tumbleweed Slowroll Kubic MicroOS Aeon Kalpa; do \
%endif
for file in `ls ${distro}`; do \
cp -r ${distro}/${file} %{buildroot}%{_datadir}/pixmaps/distribution-logos/${file}.${distro}; \
done; \
cp -r ${distro}/square-hicolor.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/distributor-logo-${distro}.svg; \
cp -r ${distro}/square-symbolic.svg %{buildroot}%{_datadir}/icons/hicolor/symbolic/apps/distributor-logo-${distro}-symbolic.svg; \
done
ln -sf %{_datadir}/pixmaps/distribution-logos/square-hicolor.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/distributor-logo.svg
ln -sf %{_datadir}/pixmaps/distribution-logos/square-symbolic.svg %{buildroot}%{_datadir}/icons/hicolor/symbolic/apps/distributor-logo-symbolic.svg

%files
%dir %{_datadir}/pixmaps/distribution-logos

%if 0%{?sle_version} || 0%{?suse_version} == 1600
%files Leap
%{_datadir}/pixmaps/distribution-logos/*.Leap

%files LeapMicro
%{_datadir}/pixmaps/distribution-logos/*.LeapMicro

%else

%files Tumbleweed
%{_datadir}/pixmaps/distribution-logos/*.Tumbleweed

%files Slowroll
%{_datadir}/pixmaps/distribution-logos/*.Slowroll

%files Kubic
%{_datadir}/pixmaps/distribution-logos/*.Kubic

%files MicroOS
%{_datadir}/pixmaps/distribution-logos/*.MicroOS

%files Aeon
%{_datadir}/pixmaps/distribution-logos/*.Aeon

%files Kalpa
%{_datadir}/pixmaps/distribution-logos/*.Kalpa

%endif

%files icons
%{_datadir}/icons/hicolor/*

%changelog
