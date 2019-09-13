#
# spec file for package python-Flask-Gravatar
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-Flask-Gravatar
Version:        0.5.0
Release:        0
Summary:        Small extension for Flask to make usage of Gravatar service
License:        BSD-3-Clause
Group:          Development/Languages/Python
Url:            https://github.com/zzzsochi/Flask-Gravatar/
Source:         https://files.pythonhosted.org/packages/source/F/Flask-Gravatar/Flask-Gravatar-%{version}.tar.gz
Patch0:         fix-requirements.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# Test requirements
BuildRequires:  %{python_module Flask >= 0.10}
BuildRequires:  %{python_module Pygments}
BuildRequires:  %{python_module check-manifest >= 0.25}
BuildRequires:  %{python_module coverage >= 4.0}
BuildRequires:  %{python_module isort >= 4.2.2}
BuildRequires:  %{python_module pydocstyle >= 1.0.0}
BuildRequires:  %{python_module pytest >= 2.8.0}
BuildRequires:  %{python_module pytest-runner >= 2.6.2}
# End of test requirements
BuildRequires:  fdupes
Requires:       python-Flask >= 0.10
BuildArch:      noarch

%python_subpackages

%description
Small extension for Flask to make usage of the Gravatar service.

%prep
%setup -q -n Flask-Gravatar-%{version}
%patch0 -p1
rm pytest.ini

%build
export LC_CTYPE=en_US@UTF-8
%python_build

%install
export LC_CTYPE=en_US@UTF-8
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LC_CTYPE=en_US@UTF-8
%python_exec setup.py test

%files %{python_files}
%doc AUTHORS CHANGES.rst README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
