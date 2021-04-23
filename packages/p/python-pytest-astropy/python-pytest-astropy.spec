#
# spec file for package python-pytest-astropy
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


%define skip_python2 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-pytest-astropy
Version:        0.8.0
Release:        0
Summary:        Meta-package containing dependencies for testing
License:        BSD-3-Clause
URL:            https://github.com/astropy/pytest-astropy
Source:         https://files.pythonhosted.org/packages/source/p/pytest-astropy/pytest-astropy-%{version}.tar.gz
BuildRequires:  %{python_module setuptools >= 30.3.0}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-hypothesis >= 5.1
Requires:       python-pytest >= 4.6
Requires:       python-pytest-arraydiff >= 0.1
Requires:       python-pytest-astropy-header >= 0.1.2
Requires:       python-pytest-cov >= 2.0
Requires:       python-pytest-doctestplus >= 0.2.0
Requires:       python-pytest-filter-subpackage >= 0.1
Requires:       python-pytest-openfiles >= 0.3.1
Requires:       python-pytest-remotedata >= 0.3.1
BuildArch:      noarch
%python_subpackages

%description
This is a meta-package that pulls in the dependencies that are used by
astropy and some affiliated packages for testing. It can also be used for
testing packages that are not affiliated with the Astropy project.

%prep
%setup -q -n pytest-astropy-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc CHANGES.rst README.rst
%license LICENSE.rst
%{python_sitelib}/pytest_astropy-%{version}-py*.egg-info

%changelog
