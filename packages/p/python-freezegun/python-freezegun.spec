#
# spec file for package python-freezegun
#
# Copyright (c) 2024 SUSE LLC
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
Name:           python-freezegun
Version:        1.5.1
Release:        0
Summary:        Mock time date for Python
License:        Apache-2.0
URL:            https://github.com/spulec/freezegun
Source:         https://files.pythonhosted.org/packages/source/f/freezegun/freezegun-%{version}.tar.gz
# PATCH-FIX-UPSTREAM: https://github.com/spulec/freezegun/commit/1777174bb97c0b514033a09b820078b0d117f4a8
Patch1:         py313-support.patch
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dateutil > 2.7}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{pythons}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python
Requires:       python-python-dateutil > 2.7
BuildArch:      noarch
%python_subpackages

%description
FreezeGun is a library that allows your python tests to travel through
time by mocking the datetime module.

%prep
%autosetup -p1 -n freezegun-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/freezegun
%{python_sitelib}/freezegun-%{version}.dist-info

%changelog
