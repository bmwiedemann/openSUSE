#
# spec file for package fontpackages
#
# Copyright (c) 2021 SUSE LLC
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


Name:           fontpackages
Version:        0.2
Release:        0
Summary:        Commons for Font Packages
License:        BSD-3-Clause
Group:          System/Base
Source0:        rpm-macros.fonts-config
Source100:      COPYING
BuildArch:      noarch

%description
Commons for font packages.

%package devel
Summary:        Development Commons for Font Packages
Group:          Development/Tools/Building

%description devel
Development commons for font packages.

%prep

%build
cp %{SOURCE100} .

%install
mkdir -p %{buildroot}%{_rpmmacrodir}
cp -a %{SOURCE0} %{buildroot}%{_rpmmacrodir}/macros.fonts-config

%files devel
%license COPYING
%{_rpmmacrodir}/macros.fonts-config

%changelog
