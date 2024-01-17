#
# spec file for package python-flake8-polyfill
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
Name:           python-flake8-polyfill
Version:        1.0.2
Release:        0
Summary:        Polyfill package for Flake8 plugins
License:        MIT
Group:          Development/Languages/Python
URL:            https://gitlab.com/pycqa/flake8-polyfill
Source:         https://files.pythonhosted.org/packages/source/f/flake8-polyfill/flake8-polyfill-%{version}.tar.gz
# https://gitlab.com/pycqa/flake8-polyfill/-/merge_requests/8
Patch0:         python-flake8-polyfill-use-unittest-mock.patch
# https://gitlab.com/pycqa/flake8-polyfill/-/issues/3
Patch1:         python-flake8-polyfill-tool-pytest.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-flake8
BuildArch:      noarch
# SECTION test requirements
%if %{suse_version} <= 1500
BuildRequires:  python2-mock
%endif
BuildRequires:  %{python_module flake8}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Flake8-polyfill is a package that provides some compatibility helpers for
Flake8 plugins that intend to support Flake8 2.x and 3.x simultaneously.

%prep
%setup -q -n flake8-polyfill-%{version}
%patch0 -p1
%patch1 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# tests/test_stdin.py: we do not have pep8 module in TW
%pytest tests/test_options.py

%files %{python_files}
%doc AUTHORS.rst CHANGELOG.rst README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
