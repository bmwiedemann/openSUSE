#
# spec file for package python-jaraco.classes
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
Name:           python-jaraco.classes
Version:        3.2.3
Release:        0
Summary:        Tools to work with classes
License:        MIT
URL:            https://github.com/jaraco/jaraco.classes
Source0:        https://files.pythonhosted.org/packages/source/j/jaraco.classes/jaraco.classes-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module more-itertools}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools >= 56}
BuildRequires:  %{python_module setuptools_scm >= 3.4.1}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-more-itertools
BuildArch:      noarch
%python_subpackages

%description
jaraco.classes Tools for working with classes.

%prep
%setup -q -n jaraco.classes-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc docs/*.rst README.rst CHANGES.rst
%dir %{python_sitelib}/jaraco
%{python_sitelib}/jaraco/classes
%{python_sitelib}/jaraco.classes-%{version}*-info

%changelog
