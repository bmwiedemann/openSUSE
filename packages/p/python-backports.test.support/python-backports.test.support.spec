#
# spec file for package python-backports.test.support
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


%define skip_python3 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-backports.test.support
Version:        0.1.1
Release:        0
Summary:        Backport of Python 3's test.support package
License:        Python-2.0
Group:          Development/Languages/Python
URL:            https://github.com/pjdelport/backports.test.support
Source:         https://files.pythonhosted.org/packages/source/b/backports.test.support/backports.test.support-%{version}.tar.gz
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-backports.os
Requires:       python-future
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module backports.os}
BuildRequires:  %{python_module future}
BuildRequires:  python2-mock
# /SECTION
%python_subpackages

%description
Backport of Python 3's test.support package.

%prep
%setup -q -n backports.test.support-%{version}

%build
%python_build

%install
%python_install
# __init__.py belongs in 'python-backports' package
%python_expand rm %{buildroot}%{$python_sitelib}/backports/*.py*
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%{python_expand cp %{$python_sitelib}/backports/__init__.py %{$python_sitelib}/backports/os.py %{buildroot}%{$python_sitelib}/backports/
PYTHONPATH=%{buildroot}%{$python_sitelib} $python -m unittest discover tests
rm %{buildroot}%{$python_sitelib}/backports/*.py*
rm -rf %{buildroot}%{$python_sitelib}/backports/__pycache__/
}

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/backports/test/
%{python_sitelib}/backports.test.support*

%changelog
