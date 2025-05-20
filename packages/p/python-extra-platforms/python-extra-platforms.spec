#
# spec file for package python-extra-platforms
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


%{?sle15_python_module_pythons}
Name:           python-extra-platforms
Version:        3.2.1
Release:        0
Summary:        Detect platforms and group them by family
License:        GPL-2.0-or-later
URL:            https://github.com/kdeldycke/extra-platforms
Source:         https://files.pythonhosted.org/packages/source/e/extra-platforms/extra_platforms-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.11}
BuildRequires:  %{python_module boltons >= 25.0.0}
BuildRequires:  %{python_module distro >= 1.9.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pytest >= 8.3.1}
BuildRequires:  %{python_module pytest-randomly >= 3.16.0}
BuildRequires:  %{python_module pytest-xdist >= 3.6.1}
BuildRequires:  %{python_module requests >= 2.32.3 with %python-requests < 2.33}
# /SECTION
BuildRequires:  fdupes
Requires:       python-boltons >= 25.0.0
Requires:       python-distro >= 1.9.0
BuildArch:      noarch
%python_subpackages

%description
Detect platforms and group them by family

%prep
%autosetup -p1 -n extra_platforms-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# remove coverage configuration
sed -i '/cov=/d' pyproject.toml
sed -i '/cov-report=/d' pyproject.toml
sed -i '/--cov-branch/d' pyproject.toml
sed -i '/--cov-precision=2/d' pyproject.toml
# do not run tests that try to connect to websites
rm -f tests/test_platform_data.py
%pytest

%files %{python_files}
%{python_sitelib}/extra_platforms
%{python_sitelib}/extra_platforms-%{version}.dist-info

%changelog
