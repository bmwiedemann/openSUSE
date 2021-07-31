#
# spec file for package python-pyleri
#
# Copyright (c) 2021, Martin Hauke <mardnh@gmx.de>
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-pyleri
Version:        1.3.3
Release:        0
Summary:        Python Left-Right Parser
License:        MIT
URL:            https://github.com/transceptor-technology/pyleri
Source:         https://github.com/transceptor-technology/pyleri/archive/refs/tags/%{version}.tar.gz#/pyleri-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module pytest}
BuildRequires:  fdupes
BuildArch:      noarch
%python_subpackages

%description
Python Left-Right Parser.

%prep
%setup -q -n pyleri-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE.txt
%doc ChangeLog README.md
%{python_sitelib}/pyleri*

%changelog
