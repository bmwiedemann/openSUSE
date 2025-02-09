#
# spec file for package conan
#
# Copyright (c) 2025 SUSE LLC
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


# Note: We only want to build for the default python3
Name:           conan
Version:        2.12.1
Release:        0
Summary:        A C/C++ package manager
License:        MIT
URL:            https://github.com/conan-io/conan
Source:         https://files.pythonhosted.org/packages/source/c/conan/conan-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
Requires:       python3-Jinja2
Requires:       python3-PyYAML >= 6.0
Requires:       python3-colorama >= 0.4.3
Requires:       python3-distro
Requires:       python3-fasteners >= 0.15
Requires:       python3-patch-ng >= 1.17.4
Requires:       python3-python-dateutil >= 2.8.0
Requires:       python3-requests >= 2.25
Requires:       python3-urllib3 >= 1.26.6
BuildArch:      noarch

%description
Conan is a package manager for C and C++ developers. It is specifically
designed and optimized for accelerating the development and Continuous
Integration of C and C++ projects.

%prep
%autosetup -p1 -n conan-%{version}

%build
%python3_pyproject_wheel

%install
%python3_pyproject_install
%fdupes %{buildroot}%{python3_sitelib}
sed -Ei "1{\@/usr/bin/(env )?python@d}" \
  %{buildroot}%{python3_sitelib}/conan/tools/intel/intel_cc.py \
  %{buildroot}%{python3_sitelib}/conan/test/utils/server_launcher.py

%files
%doc README.md
%license LICENSE.md
%{_bindir}/conan
%{python3_sitelib}/conan/
%{python3_sitelib}/conans/
%{python3_sitelib}/conan-%{version}.dist-info

%changelog
