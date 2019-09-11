#
# spec file for package megaglest-data
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


Name:           megaglest-data
Version:        3.13.0
Release:        0
Summary:        Data files for MegaGlest
License:        CC-BY-SA-3.0
Group:          Amusements/Games/Strategy/Real Time
Url:            http://www.megaglest.org/
Source:         https://github.com/MegaGlest/megaglest-data/releases/download/%{version}/%{name}-%{version}.tar.xz
BuildRequires:  xz
Requires:       megaglest >= %{version}
%if 0%{?suse_version}
BuildRequires:  fdupes
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Data files required for playing MegaGlest.

%prep
%setup -q -n megaglest-%{version}

%build

%install
# get rid of unwanted files
  find . -name "*~" -exec rm {} \;
  find . -name "*\.bak" -exec rm {} \;
  for i in $(find . -name "*.G3D"); do
    rename G3D g3d $i
  done
mkdir -p %{buildroot}/%{_datadir}/megaglest
cp -rp * %{buildroot}/%{_datadir}/megaglest/.
find %{buildroot} -name README.txt -exec rm {} \;
find %{buildroot} -name CHANGELOG.txt -exec rm {} \;
find %{buildroot} -name glest.ini -exec rm {} \;
find %{buildroot} -name servers.ini -exec rm {} \;
%if 0%{?suse_version}
%fdupes -s %{buildroot}
%endif

%files
%defattr(-, root, root)
%doc docs/LICENSE.data.txt docs/AUTHORS.data.txt
%{_datadir}/megaglest/

%changelog
