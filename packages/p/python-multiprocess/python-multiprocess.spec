#
# spec file for package python-multiprocess
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


Name:           python-multiprocess
Version:        0.70.19
Release:        0
Summary:        Better multiprocessing and multithreading in Python
License:        BSD-3-Clause
URL:            https://github.com/uqfoundation/multiprocess
Source:         https://files.pythonhosted.org/packages/source/m/multiprocess/multiprocess-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module build}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 42}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module dill >= 0.4.1}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module testsuite}
# /SECTION
BuildRequires:  fdupes
Requires:       python-dill >= 0.4.1
BuildArch:      noarch
%python_subpackages

%description
Better multiprocessing and multithreading in Python

%prep
%autosetup -p1 -n multiprocess-%{version}

%build
# We need to build this multiple times, for each version of Python, as opposed
# to just once, because that will only be compatible for the first version
# of Python built.
%python_exec -m build -wn -o build

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%{python_expand \
subver=$($python --version | cut -d. -f2)
pushd py3.$subver/multiprocess/tests
export PYTHONPATH=%{buildroot}%{$python_sitelib}
export PYTHONDONTWRITEBYTECODE=1
pytest-3.$subver -v -x -k 'not (CmdLineTest or WithThreadsTestProcess or WithThreadsTestQueue or test_repr_lock or test_repr_rlock or sys_path or test_wait or test_resource_tracker_reused or test_empty or test_args_argument or test_child_fd_inflation or test_lose_target_ref)' .
popd
}

%files %{python_files}
%doc README.md
%license COPYING LICENSE
%{python_sitelib}/_multiprocess
%{python_sitelib}/multiprocess
%{python_sitelib}/multiprocess-%{version}.dist-info

%changelog
