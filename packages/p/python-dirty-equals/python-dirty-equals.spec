#
# spec file for package python-dirty-equals
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


Name:           python-dirty-equals
Version:        0.5.0
Release:        0
Summary:        Doing dirty (but useful) things with equals
License:        MIT
URL:            https://dirty-equals.helpmanual.io
Source:         https://github.com/samuelcolvin/dirty-equals/archive/refs/tags/v%{version}.tar.gz#/dirty-equals-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-typing-extensions >= 4.0.1 if %python-base < 3.8}
BuildRequires:  %{python_module pytz >= 2021.3}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pytz >= 2021.3
%if 0%{?python_version_nodots} < 38
Requires:       python-typing-extensions >= 4.0.1
%endif
BuildArch:      noarch
%python_subpackages

%description
Doing dirty (but extremely useful) things with equals.

%prep
%setup -q -n dirty-equals-%{version}
# https://github.com/samuelcolvin/dirty-equals/issues/45
sed -i 's/version = "0"/version = "%{version}"/' pyproject.toml
sed -i 's/0.0.dev0/%{version}/' dirty_equals/__init__.py

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
%{python_sitelib}/dirty_equals
%{python_sitelib}/dirty_equals-%{version}*-info

%changelog
