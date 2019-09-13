#
# spec file for package enlightenment-profiles-openSUSE
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           enlightenment-profiles-openSUSE
Version:        20160622
Release:        0
Summary:        Enlightenment openSUSE profiles
License:        BSD-2-Clause
Group:          System/GUI/Other
Url:            https://github.com/simotek/enlightenment-openSUSE-profiles
Source:         enlightenment-profiles-openSUSE-%{version}.tar.xz
BuildRequires:  eet
# The profile needs default.edj, it presumes it is the right default.edj for the theme
Requires:       enlightenment-theme-dft
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
Conflicts:      e-profiles-openSUSE
Conflicts:      e17-profiles-openSUSE
# At recomendation of DimStar, add obsoletes but not Provides, this way people being
#  auto upgraded by the enlightenment pattern will be upgraded without any issues and
#  people who have manually installed e17 will be able to keep it
Obsoletes:      e-profiles-openSUSE
Obsoletes:      e17-profiles-openSUSE

%description
openSUSE variant of profiles for enlightenment.

%prep
%setup -q -n enlightenment-profiles-openSUSE-%{version}

%build
make

%install
make install DESTDIR="%buildroot"

%files
%defattr(-,root,root)
%doc README.md LICENSE AUTHORS
%{_datadir}/enlightenment

%changelog
