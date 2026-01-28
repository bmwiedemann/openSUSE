#
# spec file for package python-sysv_ipc
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


%{?sle15allpythons}
Name:           python-sysv_ipc
Version:        1.2.0
Release:        0
Summary:        System V IPC primitives for Python
License:        BSD-3-Clause
# URL:          http://semanchuk.com/philip/sysv_ipc/
URL:            https://github.com/osvenskan/sysv_ipc
Source:         https://files.pythonhosted.org/packages/source/s/sysv-ipc/sysv_ipc-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%python_subpackages

%description
System V IPC primitives (semaphores, shared memory and message queues) for Python

%prep
%autosetup -p1 -n sysv_ipc-%{version}

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pyunittest_arch -v

%files %{python_files}
%{python_sitearch}/sysv_ipc*.so
%{python_sitearch}/sysv_ipc-%{version}.dist-info

%changelog
