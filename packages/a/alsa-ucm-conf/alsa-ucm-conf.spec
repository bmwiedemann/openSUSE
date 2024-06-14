#
# spec file for package alsa-ucm-conf
#
# Copyright (c) 2024 SUSE LLC
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


Name:           alsa-ucm-conf
Version:        1.2.12
Release:        0
Summary:        ALSA UCM Profiles
License:        BSD-3-Clause
URL:            https://www.alsa-project.org
Source:         %{url}/files/pub/lib/alsa-ucm-conf-%{version}.tar.bz2
Source1:        %{url}/files/pub/lib/alsa-ucm-conf-%{version}.tar.bz2.sig
# from https://www.alsa-project.org/files/pub/gpg-release-key-v1.txt
Source2:        alsa-ucm-conf.keyring
BuildRequires:  fdupes
BuildArch:      noarch
Requires:       libasound2 >= 1.2.6.1

%description
This package contains the profiles files for ALSA UCM (Use Case Manager).

%prep
%autosetup -p1
find . -name ".gitignore" -delete

%build

%install
mkdir -p %{buildroot}%{_datadir}/alsa
cp -a ucm %{buildroot}%{_datadir}/alsa/
cp -a ucm2 %{buildroot}%{_datadir}/alsa/
%fdupes -s %{buildroot}

%files
%doc README.md
%license LICENSE
%{_datadir}/alsa

%changelog
