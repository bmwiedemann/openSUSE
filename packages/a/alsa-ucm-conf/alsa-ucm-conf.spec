#
# spec file for package alsa-ucm-conf
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        1.2.2
Release:        0
Summary:        ALSA UCM Profiles
License:        BSD-3-Clause
Url:            http://www.alsa-project.org/
Source:         ftp://ftp.alsa-project.org/pub/lib/alsa-ucm-conf-%{version}.tar.bz2
Patch1:         0001-sof-bdw-rt5677-initial-port-to-UCM2.patch
Patch2:         0002-ucm2-treewide-JackHWMute-fixes.patch
Patch3:         0003-sof-hda-dsp-Support-systems-without-integrated-graph.patch
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package contains the profiles files for ALSA UCM (Use Case Manager).

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build

%install
mkdir -p %{buildroot}%{_datadir}/alsa
cp -a ucm %{buildroot}%{_datadir}/alsa/
cp -a ucm2 %{buildroot}%{_datadir}/alsa/

%files
%defattr(-, root, root)
%doc README.md
%license LICENSE
%{_datadir}/alsa

%changelog
