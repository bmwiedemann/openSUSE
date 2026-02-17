#
# spec file for package python-baize
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


Name:           python-baize
Version:        0.23.1
Release:        0
Summary:        Powerful and exquisite WSGI/ASGI framework/toolkit
License:        Apache-2.0
URL:            https://github.com/abersheeran/baize
Source:         https://files.pythonhosted.org/packages/source/b/baize/baize-%{version}.tar.gz
BuildRequires:  %{python_module httpx >= 0.28.1}
BuildRequires:  %{python_module pdm-backend}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-asyncio >= 0.24.0}
BuildRequires:  %{python_module pytest-cov >= 5}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module starlette >= 0.44}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%python_subpackages

%description
Powerful and exquisite WSGI/ASGI framework/toolkit.

The minimize implementation of methods required in the Web framework. No redundant implementation means that you can freely customize functions without considering the conflict with baize's own implementation.

Under the ASGI/WSGI protocol, the interface of the request object and the response object is almost the same, only need to add or delete `await` in the appropriate place. In addition, it should be noted that ASGI supports WebSocket but WSGI does not.

%prep
%autosetup -p1 -n baize-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand rm %{buildroot}%{$python_sitearch}/.gitignore
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitearch}/baize
%{python_sitearch}/baize-%{version}.dist-info

%changelog
