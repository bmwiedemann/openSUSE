#
# spec file for package python-setproctitle
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Name:           python-setproctitle
Version:        1.3.7
Release:        0
Summary:        Python module to allow customization of the process title
License:        BSD-3-Clause
URL:            https://github.com/dvarrazzo/py-setproctitle/
Source:         https://files.pythonhosted.org/packages/source/s/setproctitle/setproctitle-%{version}.tar.gz
# PATCH-FIX-UPSTREAM gh#dvarrazzo/py-setproctitle#158
Patch0:         support-python315.patch
BuildRequires:  %{python_module devel >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  procps
BuildRequires:  python-rpm-macros
%python_subpackages

%description
Changing the title is mostly useful in multi-process systems, for example when
a master process is forked: changing the children's title allows to identify
the task each process is busy with. The technique is used by PostgreSQL  and
the OpenSSH Server for example.

%prep
%autosetup -p1 -n setproctitle-%{version}

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# This is incompatible with qemu emulation
%if !0%{?qemu_user_space_build}
%pytest_arch
%endif

%files %{python_files}
%doc HISTORY.rst README.rst
%license LICENSE
%{python_sitearch}/setproctitle
%{python_sitearch}/setproctitle-%{version}.dist-info

%changelog
