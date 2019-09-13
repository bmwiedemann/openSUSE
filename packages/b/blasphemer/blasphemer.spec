#
# spec file for package blasphemer
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


Name:           blasphemer
Version:        0.1.5
Release:        0
Summary:        Replacement game files for Heretic game engines
License:        BSD-3-Clause
Group:          Amusements/Games/3D/Shoot
Url:            https://github.com/Blasphemer/blasphemer/tree/experimental
#Old Url:       https://code.google.com/archive/p/blasphemer/
Source:         https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/blasphemer/%{name}-%{version}.zip
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
BuildRequires:  unzip

%description
Blasphemer aims to create a free content package for the Heretic engine,
with a theme of metal-inspired dark fantasy.

%prep
%setup -q -c %{name}-%{version}

%build
# Game data files. Nothing to build!

%install
install -Dpm0644 BLASPHEM.WAD %{buildroot}%{_datadir}/doom/blasphem.wad

%files
%defattr(-,root,root)
%doc copying credits story.txt wadinfo.txt
%{_datadir}/doom/

%changelog
