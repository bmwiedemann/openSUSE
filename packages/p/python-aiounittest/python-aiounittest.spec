#
# spec file for package python-aiounittest
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2019 Matthias Fehring <buschmann23@opensuse.org>
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


%define skip_python2 1
Name:           python-aiounittest
Version:        1.4.2
Release:        0
Summary:        Test AyncIO Python Code Easily
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/kwarunek/aiounittest
Source:         https://github.com/kwarunek/aiounittest/archive/%{version}.tar.gz#/aiounittest-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wrapt}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-wrapt
BuildArch:      noarch
%python_subpackages

%description
This is a helper library to ease of your pain (and boilerplate), when writing a
test of the asynchronous code (asyncio). You can test:

* synchronous code (same as the unittest.TestCase)
* asynchronous code, it supports syntax with async/await (Python 3.5+) and
  asyncio.coroutine/yield from (Python 3.4)

%prep
%setup -q -n aiounittest-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/aiounittest-%{version}-*.egg-info/
%{python_sitelib}/aiounittest

%changelog
