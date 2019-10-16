#
# spec file for package python-venusian
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2013-2019 LISA GmbH, Bingen, Germany.
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-venusian
Version:        1.2.0
Release:        0
Summary:        A library for deferring decorator actions
License:        SUSE-Repoze AND ZPL-2.1
URL:            https://github.com/Pylons/venusian
Source:         https://files.pythonhosted.org/packages/source/v/venusian/venusian-%{version}.tar.gz
Patch0:         fix-pylons-sphinx-theme.diff
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module nose-exclude}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest}
# /SECTION
# SECTION documentation requirements
BuildRequires:  python3-Sphinx
BuildRequires:  python3-pylons-sphinx-themes
# /SECTION
%python_subpackages

%description
Venusian is a library which allows framework authors to defer
decorator actions.  Instead of taking actions when a function (or
class) decorator is executed at import time, you can defer the action
usually taken by the decorator until a separate "scan" phase.

See the "docs" directory of the package or the online documentation at
http://docs.pylonsproject.org/projects/venusian/dev/.

%package doc
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}

%description doc
This package contains documentation files for %{name}.

%prep
%setup -q -n venusian-%{version}
%patch0 -p1
rm -rf venusian.egg-info

%build
%python_build
python3 setup.py build_sphinx && rm -v build/sphinx/html/{.buildinfo,objects.inv}

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest venusian

%files %{python_files}
%license LICENSE.txt
%doc CHANGES.rst README.rst
%{python_sitelib}/venusian
%{python_sitelib}/venusian-%{version}-py%{python_version}.egg-info

%files %{python_files doc}
%license LICENSE.txt
%doc build/sphinx/html/

%changelog
