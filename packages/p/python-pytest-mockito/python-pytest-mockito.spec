#
# spec file for package python-pytest-mockito
#
# Copyright (c) 2025 SUSE LLC
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


Name:           python-pytest-mockito
Version:        0.0.5
Release:        0
Summary:        Convenience plugin on top of mockito
License:        MIT
URL:            https://github.com/kaste/pytest-mockito
Source:         https://github.com/kaste/pytest-mockito/archive/refs/tags/%{version}.tar.gz
BuildRequires:  %{python_module mockito}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module wheel}
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
# Replace the dynamic version that's calculated with hatch-vcs without
# as git checkout
sed -i 's/dynamic.*/version="%{version}"/' pyproject.toml

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %python_files
%license LICENSE
%doc README.rst
%{python_sitelib}/pytest_mockito
%{python_sitelib}/pytest_mockito-%{version}.dist-info

%changelog
