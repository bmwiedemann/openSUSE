#
# spec file for package distribution-logos-openSUSE
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2020 Stasiek Michalski <hellcp@opensuse.org>.
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
Version:        20201117
Release:        0
Url:            https://github.com/openSUSE/distribution-logos
Source:         distribution-logos-master.zip
BuildRequires:  unzip
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

%prep
%setup -qn distribution-logos-master

%build
# Skip build

%install
%if 0%{?sle_version}
for distro in Leap; do \
%else
for distro in Tumbleweed Kubic MicroOS; do \
%endif
mkdir -p %{buildroot}%{_datadir}/pixmaps/distribution-logos; \
for file in `ls ${distro}`; do \
cp -r ${distro}/${file} %{buildroot}%{_datadir}/pixmaps/distribution-logos/${file}.${distro}; \
done; \
done \

%files
%dir %{_datadir}/pixmaps/distribution-logos

%if 0%{?sle_version}

%files Leap
%{_datadir}/pixmaps/distribution-logos/*.Leap

%else

%files Tumbleweed
%{_datadir}/pixmaps/distribution-logos/*.Tumbleweed

%files Kubic
%{_datadir}/pixmaps/distribution-logos/*.Kubic

%files MicroOS
%{_datadir}/pixmaps/distribution-logos/*.MicroOS

%endif

%changelog
