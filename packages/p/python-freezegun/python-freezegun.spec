#
# spec file for package python-freezegun
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%bcond_without python2
Name:           python-freezegun
Version:        0.3.15
Release:        0
Summary:        Mock time date for Python
License:        Apache-2.0
URL:            https://github.com/spulec/freezegun
Source:         https://files.pythonhosted.org/packages/source/f/freezegun/freezegun-%{version}.tar.gz
# gh#spulec/freezegun#259
Patch1:         denose.patch
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dateutil > 2.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  %{pythons}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python
Requires:       python-python-dateutil > 2.0
Requires:       python-six
BuildArch:      noarch
%if %{with python2}
BuildRequires:  python-mock
%endif
%python_subpackages

%description
FreezeGun is a library that allows your python tests to travel through
time by mocking the datetime module.

%prep
%setup -q -n freezegun-%{version}
%autopatch -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec -munittest discover -v

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
