#
# spec file for package qt6-macros
#
# Copyright (c) 2023 SUSE LLC
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


Name:           qt6-macros
Version:        20221130
Release:        0
Summary:        RPM macros for Qt6 packages
License:        MIT
URL:            https://www.opensuse.org
Source0:        macros.qt6
Source1:        LICENSE.MIT
Requires:       cmake
Requires:       ninja

%description
This package provides macros which are used by Qt6 packages.

%prep

%build

%install
install -D -m644 %{SOURCE0} %{buildroot}%{_rpmmacrodir}/macros.qt6
install -D -m644 %{SOURCE1} %{buildroot}%{_defaultlicensedir}/qt6-macros/LICENSE.MIT

%files
%license %{_defaultlicensedir}/qt6-macros/LICENSE.MIT
%dir %{_defaultlicensedir}/qt6-macros
%{_rpmmacrodir}/macros.qt6

%changelog
