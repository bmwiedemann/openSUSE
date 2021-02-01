#
# spec file for package python-setproctitle
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
%define skip_python2 1
Name:           python-setproctitle
Version:        1.2.2
Release:        0
Summary:        Python module to allow customization of the process title
License:        BSD-3-Clause
URL:            https://github.com/dvarrazzo/py-setproctitle/
Source:         https://files.pythonhosted.org/packages/source/s/setproctitle/setproctitle-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  procps
BuildRequires:  python-rpm-macros
%python_subpackages

%description
Changing the title is mostly useful in multi-process systems, for example when
a master process is forked: changing the children's title allows to identify
the task each process is busy with. The technique is used by PostgreSQL  and
the OpenSSH Server for example.

%prep
%setup -q -n setproctitle-%{version}

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install

%check
%pytest_arch

%files %{python_files}
%doc HISTORY.rst README.rst
%license COPYRIGHT
%{python_sitearch}/setproctitle*.so
%{python_sitearch}/setproctitle-%{version}*-info

%changelog
