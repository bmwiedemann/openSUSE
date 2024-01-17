#
# spec file for package python-jaraco.versioning
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


%{?sle15_python_module_pythons}
Name:           python-jaraco.versioning
Version:        1.1.0
Release:        0
Summary:        More sophisticated version manipulation (than packaging)
License:        MIT
URL:            https://github.com/jaraco/jaraco.versioning
Source:         https://files.pythonhosted.org/packages/source/j/jaraco.versioning/jaraco.versioning-1.1.0.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module setuptools >= 56}
BuildRequires:  %{python_module setuptools_scm >= 3.4.1}
# SECTION test requirements
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Requires:       python-packaging
Suggests:       python-jaraco.packaging >= 9
BuildArch:      noarch
%python_subpackages

%description
More sophisticated version manipulation (than packaging)

%prep
%autosetup -p1 -n jaraco.versioning-%{version}

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
%{python_sitelib}/jaraco/versioning.py
%{python_sitelib}/jaraco.versioning-%{version}.dist-info
%dir %{python_sitelib}/jaraco/__pycache__
%pycache_only %{python_sitelib}/jaraco/__pycache__/versioning.*.py*

%changelog
