#
# spec file for package distribution-logos-openSUSE
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Summary:        Logos for openSUSE Distros
License:        CC-BY-SA-4.0
Version:        20220322
Release:        0
Url:            https://github.com/openSUSE/distribution-logos
Source:         distribution-logos-main.zip
BuildRequires:  unzip
BuildRequires:  hicolor-icon-theme
BuildArch:      noarch

%description
Logos for openSUSE Distributions

%if 0%{?sle_version}

%package Leap
Summary:        Logos for openSUSE Leap

Obsoletes:      distribution-logos
Provides:       distribution-logos
Conflicts:      distribution-logos

RemovePathPostfixes: .Leap
BuildArch:      noarch

%description Leap
Logos for openSUSE Leap

%package LeapMicro
Summary:        Logos for openSUSE Leap Micro

Obsoletes:      distribution-logos
Provides:       distribution-logos
Conflicts:      distribution-logos

RemovePathPostfixes: .LeapMicro
BuildArch:      noarch

%description LeapMicro
Logos for openSUSE Leap Micro

%else

%package Tumbleweed
Summary:        Logos for openSUSE Tumbleweed

Obsoletes:      distribution-logos
Provides:       distribution-logos
Conflicts:      distribution-logos

RemovePathPostfixes: .Tumbleweed
BuildArch:      noarch

%description Tumbleweed
Logos for openSUSE Tumbleweed

%package Kubic
Summary:        Logos for openSUSE Kubic

Obsoletes:      distribution-logos
Provides:       distribution-logos
Conflicts:      distribution-logos

RemovePathPostfixes: .Kubic
BuildArch:      noarch

%description Kubic
Logos for openSUSE Kubic

%package MicroOS
Summary:        Logos for openSUSE MicroOS

Obsoletes:      distribution-logos
Provides:       distribution-logos
Conflicts:      distribution-logos

RemovePathPostfixes: .MicroOS
BuildArch:      noarch

%description MicroOS
Logos for openSUSE MicroOS

%endif

%package icons
Summary:        Icons with distribution logos

Requires:       distribution-logos
Provides:       systemd-icon-branding
Obsoletes:      systemd-icon-branding-openSUSE < 84.87.20210910
Provides:       systemd-icon-branding-openSUSE = 84.87.20210910
Conflicts:      systemd-icon-branding-openSUSE

BuildArch:      noarch

%description icons
Icons with openSUSE distribution logos.

%prep
%setup -qn distribution-logos-main

%build
# Skip build

%install
export NO_BRP_STALE_LINK_ERROR=yes
mkdir -p %{buildroot}%{_datadir}/pixmaps/distribution-logos
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/{scalable,symbolic}/apps
%if 0%{?sle_version}
for distro in Leap LeapMicro; do \
%else
for distro in Tumbleweed Kubic MicroOS; do \
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

%if 0%{?sle_version}

%files Leap
%{_datadir}/pixmaps/distribution-logos/*.Leap

%files LeapMicro
%{_datadir}/pixmaps/distribution-logos/*.LeapMicro

%else

%files Tumbleweed
%{_datadir}/pixmaps/distribution-logos/*.Tumbleweed

%files Kubic
%{_datadir}/pixmaps/distribution-logos/*.Kubic

%files MicroOS
%{_datadir}/pixmaps/distribution-logos/*.MicroOS

%endif

%files icons
%{_datadir}/icons/hicolor/*

%changelog
