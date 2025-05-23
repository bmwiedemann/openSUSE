#
# spec file for package python-jaraco.collections
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
Name:           python-jaraco.collections
Version:        5.1.0
Release:        0
Summary:        Tools to work with collections
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/jaraco/jaraco.collections
Source0:        https://files.pythonhosted.org/packages/source/j/jaraco.collections/jaraco_collections-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module jaraco.classes}
BuildRequires:  %{python_module jaraco.text}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools >= 56}
BuildRequires:  %{python_module setuptools_scm >= 3.4.1}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-jaraco.classes
Requires:       python-jaraco.text
BuildArch:      noarch
%python_subpackages

%description
jaraco.collections Tools for working with collections.
Models and classes to supplement the stdlib ‘collections’ module.

%prep
%setup -q -n jaraco_collections-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest --doctest-modules -k "not (dummyprefix or read_newlines or report_newlines)"

%files %{python_files}
%license LICENSE
%doc docs/*.rst README.rst NEWS.rst
%{python_sitelib}/jaraco/collections
%{python_sitelib}/jaraco[_.]collections-%{version}.dist-info

%changelog
