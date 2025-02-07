#
# spec file for package python-DataProperty
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
Name:           python-DataProperty
Version:        1.1.0
Release:        0
Summary:        Python library for extract property from data
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/thombashi/DataProperty
Source:         https://files.pythonhosted.org/packages/source/d/dataproperty/dataproperty-%{version}.tar.gz
BuildRequires:  %{python_module setuptools >= 38.3.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-mbstrdecoder >= 1.0.0
Requires:       python-typepy >= 1.1.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module mbstrdecoder >= 1.0.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dateutil >= 2.8.0}
BuildRequires:  %{python_module pytz >= 2018.9}
BuildRequires:  %{python_module tcolorpy}
BuildRequires:  %{python_module typepy >= 1.1.0}
# /SECTION
%python_subpackages

%description
Python library for extract property from data.

%prep
%setup -q -n dataproperty-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Required by termcolor to have colors in the tests
export FORCE_COLOR=1
%pytest

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/dataproperty*
%{python_sitelib}/DataProperty*

%changelog
