#
# spec file for package python-pytest-fixture-config
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-pytest-fixture-config
Version:        1.7.0
Release:        0
Summary:        Fixture configuration utils for pytest
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/manahl/pytest-plugins
Source:         https://files.pythonhosted.org/packages/source/p/pytest-fixture-config/pytest-fixture-config-%{version}.tar.gz
# https://github.com/man-group/pytest-plugins/issues/209
Patch0:         python-pytest-fixture-config-no-six.patch
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools-git}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pytest
BuildArch:      noarch
%python_subpackages

%description
Fixture configuration utilities for pytest

%prep
%setup -q -n pytest-fixture-config-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md CHANGES.md
%license LICENSE
%{python_sitelib}/*

%changelog
