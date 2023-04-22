#
# spec file for package python-pysendfile
#
# Copyright (c) 2023 SUSE LLC
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
%define mod_name pysendfile
Name:           python-pysendfile
Version:        2.0.1
Release:        0
Summary:        A Python interface to sendfile(2)
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/giampaolo/pysendfile
Source:         https://files.pythonhosted.org/packages/source/p/pysendfile/pysendfile-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
%python_subpackages

%description
A python interface to sendfile(2) system call.

%prep
%setup -q -n %{mod_name}-%{version}

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitearch}/sendfile.*.so
%{python_sitearch}/pysendfile-%{version}*-info

%changelog
