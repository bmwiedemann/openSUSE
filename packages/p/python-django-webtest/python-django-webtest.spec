#
# spec file for package python-django-webtest
#
# Copyright (c) 2023 SUSE LLC
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
Name:           python-django-webtest
Version:        1.9.10
Release:        0
Summary:        Django integration for WebTest
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/django-webtest/django-webtest
Source:         https://files.pythonhosted.org/packages/source/d/django-webtest/django-webtest-%{version}.tar.gz
BuildRequires:  %{python_module Django}
BuildRequires:  %{python_module WebTest >= 1.3.3}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django
Requires:       python-WebTest >= 1.3.3
%python_subpackages

%description
Instant integration of Ian Bicking's WebTest with django's testing framework.

%prep
%setup -q -n django-webtest-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
pushd django_webtest_tests
%python_exec runtests.py
popd

%files %{python_files}
%license LICENSE.txt
%doc AUTHORS.txt CHANGES.rst README.rst
%{python_sitelib}/*[Ww]ebtest*/

%changelog
