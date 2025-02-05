#
# spec file for package python-stopit
#
# Copyright (c) 2025 SUSE LLC
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


%define modname stopit
Name:           python-stopit
Version:        1.1.2
Release:        0
Summary:        Timeout control decorator and context managers
License:        MIT
URL:            https://pypi.python.org/pypi/stopit
Source0:        https://files.pythonhosted.org/packages/source/s/stopit/stopit-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/glenfant/stopit/refs/tags/%{version}/tests.py
Source2:        https://raw.githubusercontent.com/glenfant/stopit/refs/tags/%{version}/LICENSE
# PATCH-FIX-UPSTREAM
Patch0:         https://github.com/glenfant/stopit/commit/dda4bd181d1d29ab1fb22314dc9bde0e3c931abc.patch#/python-stopit-ulong-for-thread-id.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
%{name} is a python module that provides:
* a function that raises an exception in another thread, including the main thread.
* two context managers that may stop its inner block activity on timeout.
* two decorators that may stop its decorated callables on timeout.

%prep
%autosetup -p1 -n %{modname}-%{version}
cp %{SOURCE1} %{SOURCE2} ./

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%{python_expand export PYTHONDONTWRITEBYTECODE=1
export PYTHONPATH=%{buildroot}%{$python_sitelib}
$python tests.py
}

%files %{python_files}
%license LICENSE
%doc CHANGES.rst README.rst
%{python_sitelib}/%{modname}/
%{python_sitelib}/%{modname}-%{version}*.*-info

%changelog
