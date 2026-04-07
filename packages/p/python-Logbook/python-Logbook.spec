#
# spec file for package python-Logbook
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
Name:           python-Logbook
Version:        1.9.2
Release:        0
Summary:        A logging replacement for Python
License:        BSD-3-Clause
URL:            https://github.com/getlogbook/logbook
Source:         https://files.pythonhosted.org/packages/source/l/logbook/logbook-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  %{python_module Brotli >= 1.1.0}
BuildRequires:  %{python_module Jinja2 >= 2.11.3}
BuildRequires:  %{python_module SQLAlchemy >= 1.4}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module execnet >= 1.5}
BuildRequires:  %{python_module gevent >= 25.5.1}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest >= 8.4.0}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest-rerunfailures >= 15.1}
BuildRequires:  %{python_module pyzmq >= 27.0.2}
BuildRequires:  %{python_module redis >= 4.6.0}
BuildRequires:  %{python_module setuptools-rust >= 1.11.1}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module typing-extensions >= 4.14.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  redis
BuildRequires:  util-linux
BuildRequires:  zstd
Requires:       python-typing-extensions >= 4.14.0
Recommends:     python-Brotli >= 1.1.0
Recommends:     python-Jinja2 >= 2.11.3
Recommends:     python-SQLAlchemy >= 1.4
Recommends:     python-execnet >= 1.5
Recommends:     python-gevent >= 25.5.1
Recommends:     python-pyzmq >= 27.0.2
Recommends:     python-redis >= 4.6.0
%python_subpackages

%description
An alternative logging implementation for python.

%prep
%autosetup -p1 -a1 -n logbook-%{version}
dos2unix LICENSE

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
export CFLAGS="%{optflags}"
%{_sbindir}/redis-server &
# test_asyncio_context_management seems to fail in OBS
%pytest_arch -k 'not test_asyncio_context_management'
kill %%1

%files %{python_files}
%license LICENSE
%doc README.md CHANGES
%{python_sitearch}/logbook
%{python_sitearch}/[Ll]ogbook-%{version}.dist-info

%changelog
