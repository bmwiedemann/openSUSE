#
# spec file for package python-Flask-Gravatar
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
Name:           python-Flask-Gravatar
Version:        0.5.0
Release:        0
Summary:        Small extension for Flask to make usage of Gravatar service
License:        BSD-3-Clause
URL:            https://github.com/zzzsochi/Flask-Gravatar/
Source:         https://files.pythonhosted.org/packages/source/F/Flask-Gravatar/Flask-Gravatar-%{version}.tar.gz
# https://github.com/zzzsochi/Flask-Gravatar/issues/27
Patch0:         fix-requirements.patch
# PATCH-FIX-OPENSUSE Remove unused and broken with Flask 3.0 internal imports
Patch1:         remove-connection-stack.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# Test requirements
BuildRequires:  %{python_module Flask >= 0.10}
BuildRequires:  %{python_module Pygments}
BuildRequires:  %{python_module check-manifest >= 0.25}
BuildRequires:  %{python_module coverage >= 4.0}
BuildRequires:  %{python_module isort >= 4.2.2}
BuildRequires:  %{python_module pytest >= 2.8.0}
# End of test requirements
BuildRequires:  fdupes
Requires:       python-Flask >= 0.10
BuildArch:      noarch

%python_subpackages

%description
Small extension for Flask to make usage of the Gravatar service.

%prep
%autosetup -p1 -n Flask-Gravatar-%{version}
rm pytest.ini

%build
export LC_CTYPE=en_US@UTF-8
%pyproject_wheel

%install
export LC_CTYPE=en_US@UTF-8
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LC_CTYPE=en_US@UTF-8
%pyunittest discover -v tests

%files %{python_files}
%doc AUTHORS CHANGES.rst README.rst
%license LICENSE
%{python_sitelib}/flask_gravatar
%{python_sitelib}/[Ff]lask_[Gg]ravatar-%{version}.dist-info

%changelog
