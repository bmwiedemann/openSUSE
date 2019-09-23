#
# spec file for package python-posix_ipc
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
Name:           python-posix_ipc
Version:        1.0.4
Release:        0
Summary:        POSIX IPC primitives (semaphores, shared memory and message queues) for Python
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            http://semanchuk.com/philip/posix_ipc/
Source:         https://files.pythonhosted.org/packages/source/p/posix_ipc/posix_ipc-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%python_subpackages

%description
posix_ipc is a Python module (written in C) that permits creation and
manipulation of POSIX inter-process semaphores, shared memory and message
queues on platforms supporting the POSIX Realtime Extensions a.k.a. POSIX
1003.1b-1993. This includes nearly all Unices and Windows + Cygwin 1.7.

%prep
%setup -q -n posix_ipc-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitearch} $python -m unittest discover

%files %{python_files}
%license LICENSE
%doc README ReadMe.html
%{python_sitearch}/*

%changelog
