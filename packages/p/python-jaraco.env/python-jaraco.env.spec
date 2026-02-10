#
# spec file for package python-jaraco.env
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           python-jaraco.env
Version:        1.0.0
Release:        0
Summary:        Facilities for environment variables
License:        MIT
URL:            https://github.com/jaraco/jaraco.env
Source:         https://files.pythonhosted.org/packages/source/j/jaraco.env/jaraco.env-1.0.0.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools >= 56}
BuildRequires:  %{python_module setuptools_scm >= 3.4.1}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Facilities for environment variables

%prep
%autosetup -p1 -n jaraco.env-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc CHANGES.rst README.rst
%license LICENSE
%dir %{python_sitelib}/jaraco
%{python_sitelib}/jaraco/env.py
%pycache_only %{python_sitelib}/jaraco/__pycache__
%pycache_only %{python_sitelib}/jaraco/__pycache__/env.*.pyc
%{python_sitelib}/jaraco_env-%{version}.dist-info

%changelog
