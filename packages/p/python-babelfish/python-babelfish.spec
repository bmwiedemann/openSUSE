#
# spec file for package python-babelfish
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2015 LISA GmbH, Bingen, Germany.
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


Name:           python-babelfish
Version:        0.6.1
Release:        0
Summary:        A Python library to work with countries and languages
License:        BSD-3-Clause
URL:            https://github.com/Diaoul/babelfish
Source:         https://github.com/Diaoul/babelfish/archive/refs/tags/%{version}.tar.gz#/babelfish-%{version}-gh.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core >= 1.0.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       (python-importlib-metadata if python-base < 3.10)
Requires:       (python-importlib-resources if python-base < 3.9)
BuildArch:      noarch
%python_subpackages

%description
BabelFish is a Python library to work with countries and languages.

%prep
%autosetup -p1 -n babelfish-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/babelfish
%{python_sitelib}/babelfish-%{version}.dist-info

%changelog
