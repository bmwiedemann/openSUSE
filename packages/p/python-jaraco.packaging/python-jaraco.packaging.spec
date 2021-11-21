#
# spec file for package python-jaraco.packaging
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           python-jaraco.packaging
Version:        8.1.0
Release:        0
Summary:        Supplement packaging Python releases
License:        MIT
URL:            https://github.com/jaraco/jaraco.packaging
Source:         https://files.pythonhosted.org/packages/source/j/jaraco.packaging/jaraco.packaging-%{version}.tar.gz
BuildRequires:  %{python_module jaraco.base >= 6.1}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module toml}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-jaraco.base >= 6.1
Requires:       python-six
Requires(post): update-alternatives
Requires(preun):update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Tools to supplement packaging Python releases.

%prep
%setup -q -n jaraco.packaging-%{version}
sed -i 's/--flake8//' pytest.ini
sed -i 's/--black --cov//' pytest.ini
rm -rf jaraco.packaging.egg-info

%build
%python_build

%install
%python_install
# We will package the namespace __init__.py separately
%{python_expand rm %{buildroot}%{$python_sitelib}/jaraco/__init__.py*
rm -rf %{buildroot}%{$python_sitelib}/jaraco/__pycache__/
%fdupes %{buildroot}%{$python_sitelib}
}

%python_clone -a %{buildroot}%{_bindir}/dependency-tree

%post
%python_install_alternative dependency-tree upload-package

%postun
%python_uninstall_alternative dependency-tree

%check
# the test depends on accessing PyPI
%pytest -k 'not test_revived_distribution'

%files %{python_files}
%license LICENSE
%doc docs/*.rst CHANGES.rst README.rst
%python_alternative %{_bindir}/dependency-tree
%{python_sitelib}/jaraco.packaging-%{version}-py*.egg-info
%{python_sitelib}/jaraco/packaging/

%changelog
