#
# spec file for package python-backports.shutil_get_terminal_size
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
%if %{python3_version_nodots} >=33
%define skip_python3 1
%endif
Name:           python-backports.shutil_get_terminal_size
Version:        1.0.0
Release:        0
Summary:        A backport of the get_terminal_size function from Python 3.3's shutil
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/chrippa/backports.shutil_get_terminal_size
Source:         https://files.pythonhosted.org/packages/source/b/backports.shutil_get_terminal_size/backports.shutil_get_terminal_size-%{version}.tar.gz
# NOTE:
# %%{python_sitelib}/backports is a namespace package, and so under python 2 it must have a proper namespace __init__.py
# python-backports provides this __init__.py to prevent backports packages from conflicting.
# Please see:
#    https://pypi.python.org/pypi/backports/
#    https://www.python.org/dev/peps/pep-0420/%23namespace-packages-today
# If you need to link, the python-backports package is built as a subpackage of python-configparser
BuildRequires:  %{python_module backports}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-backports
BuildArch:      noarch
%python_subpackages

%description
A backport of the `get_terminal_size`_ function from Python 3.3's shutil.
Unlike the original version it is written in pure Python rather than C,
so it might be a tiny bit slower.

%prep
%setup -q -n backports.shutil_get_terminal_size-%{version}

%build
%python_build

%install
%python_install
%python_expand rm %{buildroot}%{$python_sitelib}/backports/__init__.py*
%python_expand rm -rf %{buildroot}%{$python_sitelib}/backports/__pycache__/
%python_expand %fdupes %{buildroot}%{$python_sitelib}/backports/shutil_get_terminal_size/

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/backports/shutil_get_terminal_size/
%{python_sitelib}/backports.shutil_get_terminal_size-%{version}-py*.egg-info

%changelog
