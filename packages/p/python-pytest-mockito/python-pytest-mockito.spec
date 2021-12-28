#
# spec file for package python-pytest-mockito
#
# Copyright (c) 2021 SUSE LLC
# Copyright (c) 2021 Fabrice Bauzac-Stehly
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

# python-mockito is not available for Python 3.6
%define skip_python36 1

Name:           python-pytest-mockito
Version:        0.0.4
Release:        0
Summary:        Convenience plugin on top of mockito
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/kaste/pytest-mockito
Source:         https://github.com/kaste/pytest-mockito/archive/refs/tags/%{version}.tar.gz
BuildRequires:  %{python_module mockito}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       ca-certificates
Requires:       python
Requires:       python-mockito
Requires:       python-pytest
BuildArch:      noarch
%python_subpackages

%description
Integration of Mockito functionality into Pytest.

For example:
  def test_foo(when):
      when(os.path).exists('/foo').thenReturn(False)

%prep
%autosetup -n pytest-mockito-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %python_files
%license LICENSE
%doc README.rst
%{python_sitelib}/pytest_mockito/
%{python_sitelib}/pytest_mockito-*

%changelog
