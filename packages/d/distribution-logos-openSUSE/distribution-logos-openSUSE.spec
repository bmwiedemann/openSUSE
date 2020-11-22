#
# spec file for package distribution-logos-openSUSE
#
# Copyright (c) 2019 Stasiek Michalski <hellcp@opensuse.org>.
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

Name:           distribution-logos-openSUSE
Summary:        Logos for openSUSE Distros
Version:        20190414
Release:        0
License:        CC-BY-SA-4.0
Group:          System/GUI/Other
Url:            https://github.com/openSUSE/distribution-logos
Source:         distribution-logos-master.zip
BuildRequires:  unzip
BuildArch:      noarch

%description
Logos for openSUSE Distributions

%package Leap
Summary:        Logos for openSUSE Leap

Obsoletes:      distribution-logos
Provides:       distribution-logos
Conflicts:      distribution-logos

RemovePathPostfixes: .Leap
BuildArch:      noarch
%description Leap
Logos for openSUSE Leap

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

%prep
%setup -qn distribution-logos-master

%build
# Skip build

%install
for distro in Leap Tumbleweed Kubic MicroOS; do \
mkdir -p %{buildroot}%{_datadir}/pixmaps/distribution-logos; \
for file in `ls ${distro}`; do \
cp -r ${distro}/${file} %{buildroot}%{_datadir}/pixmaps/distribution-logos/${file}.${distro}; \
done; \
done \

%files
%dir %{_datadir}/pixmaps/distribution-logos

%files Leap
%{_datadir}/pixmaps/distribution-logos/*.Leap

%files Tumbleweed
%{_datadir}/pixmaps/distribution-logos/*.Tumbleweed

%files Kubic
%{_datadir}/pixmaps/distribution-logos/*.Kubic

%files MicroOS
%{_datadir}/pixmaps/distribution-logos/*.MicroOS

%changelog
