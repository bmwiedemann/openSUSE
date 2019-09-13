#
# spec file for package enlightenment-branding-openSUSE
#
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           enlightenment-branding-openSUSE
Version:        0.1
Release:        0
Summary:        Enlightenment openSUSE branding
License:        GPL-2.0
Group:          System/GUI/Other
Url:            https://en.opensuse.org/Portal:Enlightenment
Source:         def-ibar.txt
Source2:        AUTHORS
Source3:        COPYING
Provides:       enlightenment-branding = %version
Supplements:    packageand(enlightenment:branding-openSUSE)
Conflicts:      otherproviders(enlightenment-branding)
Requires:       enlightenment-profiles-openSUSE
#provides default elementary theme
Requires:       enlightenment-theme-openSUSE
Recommends:     enlightenment-theme-dark
Recommends:     enlightenment-theme-openSUSE-bluegreen
Recommends:     enlightenment-theme-openSUSE-ice
Recommends:     enlightenment-theme-openSUSE-oliveleaf
Requires:       enlightenment-profiles-openSUSE
# recommend terminology to make xdg-open look better
Recommends:     terminology
Conflicts:      terminology-theme-upstream
Conflicts:      e-branding-openSUSE
Conflicts:      otherproviders(e17-branding)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
# At recomendation of DimStar, add obsoletes but not Provides, this way people being
#  auto upgraded by the enlightenment pattern will be upgraded without any issues and
#  people who have manually installed e17 will be able to keep it
Obsoletes:      e17-branding-openSUSE
Obsoletes:      e-branding-openSUSE

%description
openSUSE specific files as specific branding.

%prep

%build

%install
install -m 0755 -d %{buildroot}%{_libdir}/enlightenment/modules/wizard/
install -m 0644 -t %{buildroot}%{_libdir}/enlightenment/modules/wizard/ %SOURCE0
install -m 0755 -d %{buildroot}%{_docdir}/%{name}
install -m 0644 -t %{buildroot}%{_docdir}/%{name} %SOURCE2 $SOURCE3

%files
%defattr(-,root,root)
%{_docdir}/*
%{_libdir}/enlightenment/

%changelog
