#
# spec file for package python-zhon
#
# Copyright (c) 2021 SUSE LLC
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
Name:           python-zhon
Version:        1.1.5
Release:        0
Summary:        Constants used in Chinese text processing
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/tsroten/zhon
Source:         https://github.com/tsroten/zhon/archive/v%{version}.tar.gz#/zhon-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Zhon provides constants used in Chinese text processing.

%prep
%setup -q -n zhon-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
printf "[pytest]\npython_files = test-*.py\n" > pytest.ini
%pytest

%files %{python_files}
%doc AUTHORS.rst CHANGES.rst README.rst
%license LICENSE.txt
%{python_sitelib}/*

%changelog
