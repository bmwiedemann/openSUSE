#
# spec file for package klp-build
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


%{!?python_sitelib: %global python_sitelib %(python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
Name:           klp-build
Version:        0~20240622.445505a
Release:        0
Summary:        The kernel livepatching creation tool
License:        GPL-2.0-only
URL:            https://github.com/SUSE/klp-build
Source:         %{name}-%{version}.tar.xz
BuildRequires:  python3-setuptools
BuildRequires:  fdupes
Requires:       python3-GitPython
Requires:       python3-Mako
Requires:       python3-MarkupSafe
Requires:       python3-cached-property
Requires:       python3-lxml
Requires:       python3-natsort
Requires:       python3-osc-tiny
Requires:       python3-requests
BuildArch:      noarch

%description
The kernel livepatching creation tool.

%prep
%autosetup -p1

%build
%python3_build

%install
%python3_install
rm -rf %{buildroot}/%{python_sitelib}/scripts/
# Lets install the script to bindir so we can call it
# {python_sitelib}/scripts is not specific enough
cp scripts/run-kgr-test.sh %{buildroot}%{_bindir}/
%fdupes  %{buildroot}

%files
%license LICENSE
%doc README.md
%{_bindir}/klp-build
%{python_sitelib}/klpbuild
%{python_sitelib}/klp_build-0.0.1-py3.11.egg-info/
%{_bindir}/run-kgr-test.sh

%changelog
