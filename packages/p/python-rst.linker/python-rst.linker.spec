#
# spec file for package python-rst.linker
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define _name   rst.linker
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-rst.linker
Version:        1.11
Release:        0
Summary:        Changelog link and timestamp adding Sphinx plugin
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/jaraco/rst.linker
Source:         https://files.pythonhosted.org/packages/source/r/%{_name}/%{_name}-%{version}.tar.gz
BuildRequires:  %{python_module jaraco.packaging >= 3.2}
BuildRequires:  %{python_module path.py}
BuildRequires:  %{python_module pytest >= 3.5}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-Sphinx
Requires:       python-python-dateutil
Requires:       python-six
BuildArch:      noarch
%python_subpackages

%description
rst.linker is a Sphinx plugin to add links and timestamps to the
changelog.

%prep
%setup -q -n %{_name}-%{version}
sed -i 's/--flake8 --black//' pytest.ini

%build
%python_build
python3 setup.py build_sphinx && rm build/sphinx/html/.buildinfo

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest test_all.py

%files %{python_files}
%license LICENSE
%doc CHANGES.rst README.rst
%doc build/sphinx/html
%{python_sitelib}/*

%changelog
