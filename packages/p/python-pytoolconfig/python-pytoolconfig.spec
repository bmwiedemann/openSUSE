#
# spec file for package python-pytoolconfig
#
# Copyright (c) 2022 SUSE LLC
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


Name:           python-pytoolconfig
Version:        1.2.4
Release:        0
Summary:        Python tool configuration
License:        LGPL-3.0-or-later
URL:            https://github.com/bagel897/pytoolconfig
Source:         https://files.pythonhosted.org/packages/source/p/pytoolconfig/pytoolconfig-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module packaging >= 22}
BuildRequires:  %{python_module pdm-pep517 >= 1.0.5}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module tomli >= 2.0.1 if %python-base < 3.11}
BuildRequires:  %{python_module typing-extensions >= 4.4.0 if %python-base < 3.8}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-packaging >= 22
BuildArch:      noarch
%if %{python_version_nodots} < 311
Requires:       python-tomli >= 2.0.1
%endif
%if %{python_version_nodots} < 38
Requires:       python-typing-extensions >= 4.4.0
%endif
# SECTION test
BuildRequires:  %{python_module Sphinx >= 4.5.0}
BuildRequires:  %{python_module platformdirs > 1.4.4}
BuildRequires:  %{python_module pydantic >= 1.7.4}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module tabulate >= 0.8.9}
# /SECTION
%python_subpackages

%description
Python Tool Configuration

The goal of this project is to manage configuration for python tools,
such as black and rope and add support for a pyproject.toml configuration file.

%package global
Summary:        [global] extra for %{python_flavor}-pytoolconfig
Requires:       python-platformdirs >= 1.4.4
Requires:       python-pytoolconfig = %{version}

%description global
Python Tool Configuration - [global] extra

%package validation
Summary:        [validation] extra for %{python_flavor}-pytoolconfig
Requires:       python-pydantic >= 1.7.4
Requires:       python-pytoolconfig = %{version}

%description validation
Python Tool Configuration - [validation] extra

%prep
%setup -q -n pytoolconfig-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/pytoolconfig
%{python_sitelib}/pytoolconfig-%{version}.dist-info

%files %{python_files global}
%license LICENSE

%files %{python_files validation}
%license LICENSE

%changelog
