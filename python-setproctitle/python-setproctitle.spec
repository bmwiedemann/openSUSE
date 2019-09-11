#
# spec file for package python-setproctitle
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
Name:           python-setproctitle
Version:        1.1.10
Release:        0
Summary:        Python module to allow customization of the process title
License:        BSD-3-Clause
Group:          Development/Libraries/Python
URL:            http://pypi.python.org/pypi/setproctitle/
Source:         https://files.pythonhosted.org/packages/source/s/setproctitle/setproctitle-%{version}.tar.gz
Patch:          skip-failing-tests.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
BuildRequires:  python3-tools
%python_subpackages

%description
Changing the title is mostly useful in multi-process systems, for example when
a master process is forked: changing the children's title allows to identify
the task each process is busy with. The technique is used by PostgreSQL  and
the OpenSSH Server for example.

%prep
%setup -q -n setproctitle-%{version}
%autopatch -p1

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install

%check
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitearch}
make PYTHON=$python check
}

%files %{python_files}
%doc COPYRIGHT HISTORY.rst README.rst
%{python_sitearch}/*

%changelog
