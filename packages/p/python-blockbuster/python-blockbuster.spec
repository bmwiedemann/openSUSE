#
# spec file for package python-blockbuster
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


Name:           python-blockbuster
Version:        1.5.25
Release:        0
Summary:        Utility to detect blocking calls in the async event loop
License:        Apache-2.0
URL:            https://github.com/cbornet/blockbuster
Source:         https://files.pythonhosted.org/packages/source/b/blockbuster/blockbuster-%{version}.tar.gz
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module forbiddenfruit >= 0.1.4}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module sqlite3}
# /SECTION
BuildRequires:  fdupes
Requires:       python-forbiddenfruit >= 0.1.4
BuildArch:      noarch
%python_subpackages

%description
Blockbuster is a Python package designed to detect and prevent blocking calls within an asynchronous event loop.
It is particularly useful when executing tests to ensure that your asynchronous code does not inadvertently call blocking operations,
which can lead to performance bottlenecks and unpredictable behavior.

In Python, the asynchronous event loop allows for concurrent execution of tasks without the need for multiple threads or processes.
This is achieved by running tasks cooperatively, where tasks yield control back to the event loop when they are waiting for I/O operations or other long-running tasks to complete.

However, blocking calls, such as file I/O operations or certain networking operations, can halt the entire event loop, preventing other tasks from running.
This can lead to increased latency and reduced performance, defeating the purpose of using asynchronous programming.

The difficulty with blocking calls is that they are not always obvious, especially when working with third-party libraries or legacy code.
This is where Blockbuster comes in: it helps you identify and eliminate blocking calls in your codebase during testing, ensuring that your asynchronous code runs smoothly and efficiently.
It does this by wrapping common blocking functions and raising an exception when they are called within an asynchronous context.

Notes:
- Blockbuster currently only detects `asyncio` event loops.
- Blockbuster is tested only with CPython. It may work with other Python implementations if it's possible to monkey-patch the functions with `setattr`.

%prep
%autosetup -p1 -n blockbuster-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test_ssl_socket needs internet connection
%pytest -k "not test_ssl_socket"

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/blockbuster
%{python_sitelib}/blockbuster-%{version}.dist-info

%changelog
