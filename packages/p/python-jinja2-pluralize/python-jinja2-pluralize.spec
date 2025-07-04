#
# spec file for package python-jinja2-pluralize
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


Name:           python-jinja2-pluralize
Version:        0.3.0
Release:        0
Summary:        Jinja2 pluralize filters
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/audreyr/jinja2_pluralize
Source:         https://files.pythonhosted.org/packages/source/j/jinja2_pluralize/jinja2_pluralize-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Jinja2 >= 2.4
Requires:       python-inflect >= 0.2.4
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Jinja2 >= 2.4}
BuildRequires:  %{python_module inflect >= 0.2.4}
# /SECTION
%python_subpackages

%description
Jinja2 pluralize filters.

%prep
%setup -q -n jinja2_pluralize-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest discover -v

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/jinja2[-_]pluralize
%{python_sitelib}/jinja2[-_]pluralize-%{version}*-info

%changelog
