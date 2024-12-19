#
# spec file for package python-taskgroup
#
# Copyright (c) 2024 SUSE LLC
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


Name:           python-taskgroup
Version:        0.2.1
Release:        0
Summary:        Backport of asyncio.TaskGroup, asyncio.Runner and asynciotimeout
License:        MIT
URL:            https://github.com/graingert/taskgroup
Source:         https://files.pythonhosted.org/packages/source/t/taskgroup/taskgroup-%{version}.tar.gz
BuildRequires:  %{python_module flit-core >= 3.2}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-exceptiongroup
Requires:       python-typing_extensions >= 4.12.2
BuildArch:      noarch
%python_subpackages

%description
This is a backport of the TaskGroup, Runner and timeout code from
Python 3.12a1 to Python 3.9, Python 3.10 and Python 3.11.

This project works by temporarily swapping the current task of a coroutine to a
subclass of asyncio.Task with uncancel and context setting support.
The advantage of this approach means that most of the operation of
asyncio.Task will continue to be c-accelerated.

%prep
%autosetup -p1 -n taskgroup-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# There is no testsuite

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/taskgroup
%{python_sitelib}/taskgroup-%{version}.dist-info

%changelog
