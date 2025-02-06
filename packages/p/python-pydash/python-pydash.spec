#
# spec file for package python-pydash
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
Name:           python-pydash
Version:        8.0.5
Release:        0
Summary:        The kitchen sink of Python functional utility libraries
License:        MIT
URL:            https://github.com/dgilland/pydash
Source:         https://files.pythonhosted.org/packages/source/p/pydash/pydash-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module invoke}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest-mypy-testing}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module typing_extensions >= 3.10}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-typing_extensions >= 3.10
BuildArch:      noarch
%python_subpackages

%description
The kitchen sink of Python utility libraries for doing "stuff" in a functional way.
Based on the Lo-Dash Javascript library.

%prep
%autosetup -p1 -n pydash-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Avoid weird type reveal issue with pytest-mypy-testing
donttest="test_mypy_tap or test_mypy_assign or test_mypy_assign_with or "
donttest+="test_mypy_callables or test_mypy_clone_with or "
donttest+="test_mypy_clone_deep or test_mypy_clone_deep_with or "
donttest+="test_mypy_defaults or test_mypy_defaults_deep or "
donttest+="test_mypy_for_in or test_mypy_invert_by or "
donttest+="test_mypy_map_keys or test_mypy_map_values or "
donttest+="test_mypy_merge or test_mypy_omit or test_mypy_omit_by or "
donttest+="test_mypy_pick or test_mypy_pick_by or "
donttest+="test_mypy_rename_keys or test_mypy_set_with or "
donttest+="test_mypy_to_dict or test_mypy_transform or "
donttest+="test_mypy_update or test_mypy_update_with or "
donttest+="test_mypy_apply_if or test_mypy_apply_catch"
%pytest -k "not ($donttest)"

%files %{python_files}
%doc AUTHORS.rst CHANGELOG.rst README.rst
%license LICENSE.rst
%{python_sitelib}/pydash
%{python_sitelib}/pydash-%{version}.dist-info

%changelog
