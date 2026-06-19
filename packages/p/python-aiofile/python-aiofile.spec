#
# spec file for package python-aiofile
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


Name:           python-aiofile
Version:        3.11.1
Release:        0
Summary:        Asynchronous file operations interface for Python
License:        Apache-2.0
URL:            https://github.com/mosquito/aiofile
Source:         https://files.pythonhosted.org/packages/source/a/aiofile/aiofile-%{version}.tar.gz
BuildRequires:  %{python_module caio >= 0.9.0}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-caio >= 0.9.0
BuildArch:      noarch
%python_subpackages

%description
A high-level asynchronous file-operations interface for Python built on
caio (Linux libaio / POSIX AIO / thread-pool backends).

%prep
%autosetup -p1 -n aiofile-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
# force hash-based .pyc (avoid python-bytecode-inconsistent-mtime)
%python_expand $python -m compileall -q -f -o 0 -o 1 --invalidation-mode unchecked-hash %{buildroot}%{$python_sitelib}/aiofile
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python -B -c "import aiofile"

%files %{python_files}
%doc README.md
%{python_sitelib}/aiofile
%{python_sitelib}/aiofile-%{version}.dist-info

%changelog
