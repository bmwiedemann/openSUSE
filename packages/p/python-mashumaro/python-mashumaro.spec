#
# spec file for package python-mashumaro
#
# Copyright (c) 2024 SUSE LLC
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
Name:           python-mashumaro
Version:        3.15
Release:        0
Summary:        Fast and well tested serialization library
License:        Apache-2.0
URL:            https://github.com/Fatal1ty/mashumaro
Source:         https://github.com/Fatal1ty/mashumaro/archive/refs/tags/v%{version}.tar.gz#/mashumaro-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# Add (optional) runtime dependencies as BuildRequires,
# so this only builds if all dependencies are met
BuildRequires:  %{python_module typing_extensions >= 4.1.0}
BuildRequires:  %{python_module PyYAML >= 3.13}
BuildRequires:  %{python_module msgpack >= 0.5.6}
BuildRequires:  %{python_module orjson >= 3.10.10}
BuildRequires:  %{python_module tomli >= 1.1.0 if %python-base < 3.11}
BuildRequires:  %{python_module tomli-w >= 1.0}
# SECTION test requirements
BuildRequires:  %{python_module pytest >= 6.2.1}
BuildRequires:  %{python_module ciso8601 >= 2.1.3}
BuildRequires:  %{python_module pendulum >= 2.1.2 if %python-base < 3.13}
BuildRequires:  %{python_module pytest-mock >= 3.5.1}
BuildRequires:  %{python_module pytest-xdist >= 3.5.0}
# /SECTION
BuildRequires:  fdupes
Requires:       python-typing_extensions >= 4.1.0
Suggests:       python-msgpack >= 0.5.6
Suggests:       python-orjson >= 3.10.10
Suggests:       python-tomli >= 1.1.0
Suggests:       python-tomli-w >= 1.0
Suggests:       python-PyYAML >= 3.13
BuildArch:      noarch
%python_subpackages

%description
Fast and well tested serialization library

%prep
%autosetup -p1 -n mashumaro-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest tests

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/mashumaro
%{python_sitelib}/mashumaro-%{version}.dist-info

%changelog
