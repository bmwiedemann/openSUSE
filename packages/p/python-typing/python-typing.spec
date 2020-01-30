#
# spec file for package python-typing
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
%if 0%{?suse_version} >= 1500 || %{python3_version_nodots} > 34
%define skip_python3 1
%endif
Name:           python-typing
Version:        3.7.4.1
Release:        0
Summary:        Type Hints for Python
License:        Python-2.0
Group:          Development/Languages/Python
URL:            https://docs.python.org/3.5/library/typing.html
Source:         https://files.pythonhosted.org/packages/source/t/typing/typing-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
BuildRequires:  python3-testsuite
%python_subpackages

%description
Backport of the standard library typing module for Python versions older than 3.5.

%prep
%setup -q -n typing-%{version}
ln -s python2 python_%{python2_bin_suffix}
ln -s src python_%{python3_bin_suffix}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
export PYTHONDONTWRITEBYTECODE=1
%python_expand pushd python_%{$python_bin_suffix} ; $python -m unittest test_typing ; popd

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
