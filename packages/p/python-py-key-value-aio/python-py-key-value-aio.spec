#
# spec file for package python-py-key-value-aio
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


Name:           python-py-key-value-aio
Version:        0.4.5
Release:        0
Summary:        Async key-value store abstraction with multiple backends
License:        Apache-2.0
URL:            https://github.com/strawgate/py-key-value
Source:         https://files.pythonhosted.org/packages/source/p/py-key-value-aio/py_key_value_aio-%{version}.tar.gz
BuildRequires:  %{python_module aiofile >= 3.5.0}
BuildRequires:  %{python_module anyio >= 4.4.0}
BuildRequires:  %{python_module beartype >= 0.20.0}
BuildRequires:  %{python_module cachetools >= 5.0.0}
BuildRequires:  %{python_module keyring >= 25.6.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module uv-build}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# uv-backend wheels don't expose deps to pythondistdeps, so require them by hand
Requires:       python-aiofile >= 3.5.0
Requires:       python-anyio >= 4.4.0
Requires:       python-beartype >= 0.20.0
Requires:       python-cachetools >= 5.0.0
Requires:       python-keyring >= 25.6.0
BuildArch:      noarch
%python_subpackages

%description
An async key-value store abstraction for Python with a common interface
over multiple backends (in-memory, filesystem, keyring, and more).

%prep
%autosetup -p1 -n py_key_value_aio-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
# force hash-based .pyc (avoid python-bytecode-inconsistent-mtime)
%python_expand $python -m compileall -q -f -o 0 -o 1 --invalidation-mode unchecked-hash %{buildroot}%{$python_sitelib}/key_value
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python -B -c "import key_value.aio"

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/key_value
%{python_sitelib}/py_key_value_aio-%{version}.dist-info

%changelog
