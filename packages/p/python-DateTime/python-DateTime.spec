#
# spec file for package python-DateTime
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
Name:           python-DateTime
Version:        5.5
Release:        0
Summary:        Zope DateTime data type
License:        ZPL-2.1
Group:          Development/Languages/Python
URL:            https://github.com/zopefoundation/DateTime
Source:         https://files.pythonhosted.org/packages/source/D/DateTime/DateTime-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pytz
Requires:       python-zope.interface
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module zope.interface}
# /SECTION
%python_subpackages

%description
This package provides a DateTime data type, as known from Zope.
Unless you need to communicate with Zope APIs, you're probably
better off using Python's built-in datetime module.

%prep
%setup -q -n DateTime-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc CHANGES.rst README.rst
%license LICENSE.txt
%{python_sitelib}/DateTime
%{python_sitelib}/[Dd]ate[Tt]ime-%{version}*info

%changelog
