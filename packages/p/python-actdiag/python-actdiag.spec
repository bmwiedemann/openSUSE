#
# spec file for package python-actdiag
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


%bcond_without libalternatives
%{?sle15_python_module_pythons}
Name:           python-actdiag
Version:        3.0.0
Release:        0
Summary:        Text to activity-diagram image generator
License:        Apache-2.0
URL:            http://blockdiag.com/
Source:         https://files.pythonhosted.org/packages/source/a/actdiag/actdiag-%{version}.tar.gz
# PATCH-FIX-UPSTREAM gh#blockdiag/actdiag#25
Patch0:         clean-up-assertions.patch
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module blockdiag >= 3}
BuildRequires:  %{python_module docutils}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       alts
Requires:       python-blockdiag >= 3
BuildArch:      noarch
%python_subpackages

%description
actdiag generates activity-diagram image files from spec-text files.

%prep
%autosetup -p1 -n actdiag-%{version}
# python-blockdiag-nose-to-pytest.patch of python-blockdiag changed the function name
sed -i 's/testcase_generator/_testcase_generator/' src/actdiag/tests/test_generate_diagram.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/actdiag
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest src/actdiag/tests

%pre
%python_libalternatives_reset_alternative actdiag

%files %{python_files}
%license LICENSE
%doc README.rst
%python_alternative %{_bindir}/actdiag
%{python_sitelib}/actdiag
%{python_sitelib}/actdiag-%{version}.dist-info

%changelog
