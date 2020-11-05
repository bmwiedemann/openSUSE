#
# spec file for package python-pyqt-rpm-macros
#
# Copyright (c) 2020 SUSE LLC
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


Name:           python-pyqt-rpm-macros
Version:        0.0.3
Release:        0
Summary:        RPM macros for building PyQt packages
License:        WTFPL
URL:            https://en.opensuse.org/openSUSE:Packaging_PyQt5_and_SIP
Source0:        macros.pyqt
Source1:        LICENSE
Requires:       fdupes
Requires:       python-rpm-macros
# this is not a singlespec package
Requires:       (python-sip-devel or python3-sip-devel)
BuildArch:      noarch

%description
This package provides some macros for using SIP4 or SIP5 to build PyQt5 packages

%prep
cp %{SOURCE1} .

%build

%install
mkdir -p %{buildroot}%{_rpmconfigdir}/macros.d/
install -m 644 %{SOURCE0} %{buildroot}%{_rpmconfigdir}/macros.d/

%files
%license LICENSE
%{_rpmconfigdir}/macros.d/macros.pyqt

%changelog
