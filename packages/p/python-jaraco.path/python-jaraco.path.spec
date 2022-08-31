#
# spec file for package python-jaraco.path
#
# Copyright (c) 2022 SUSE LLC
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


Name:           python-jaraco.path
Version:        3.4.0
Release:        0
Summary:        Miscellaneous path functions for jaraco packages
License:        MIT
URL:            https://github.com/jaraco/jaraco.path
Source:         https://files.pythonhosted.org/packages/source/j/jaraco.path/jaraco.path-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools >= 56}
BuildRequires:  %{python_module setuptools_scm >= 3.4.1}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
jaraco.path provides cross platform hidden file detection
and other miscellaneous path helper functions.

%prep
%setup -q -n jaraco.path-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
#  work around for gh#pytest-dev/pytest#3396 until gh#pytest-dev/pytest#10088 lands in a pytest release
touch jaraco/__init__.py
%pytest

%files %{python_files}
%license LICENSE
%dir %{python_sitelib}/jaraco/
%{python_sitelib}/jaraco/path.py
%{python_sitelib}/jaraco.path-%{version}*-info
%pycache_only %dir %{python_sitelib}/jaraco/__pycache__
%pycache_only %{python_sitelib}/jaraco/__pycache__/path*.py*

%changelog
