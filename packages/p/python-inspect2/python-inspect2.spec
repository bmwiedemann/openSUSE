#
# spec file for package python-inspect2
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
%if %{python3_version_nodots} > 35
%define skip_python3 1
%endif
Name:           python-inspect2
Version:        0.1.2
Release:        0
Summary:        Backport of the Python 3.6 inspect module to Python 2.7-3.5
License:        Python-2.0
Group:          Development/Languages/Python
URL:            https://github.com/JelleZijlstra/inspect2
Source:         https://files.pythonhosted.org/packages/source/i/inspect2/inspect2-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python2-devel
BuildRequires:  python3-testsuite
BuildArch:      noarch
%python_subpackages

%description
Backport of the Python 3.6 inspect module to Python 2.7-3.5.

%prep
%setup -q -n inspect2-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
#%pytest
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
