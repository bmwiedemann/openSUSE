#
# spec file for package python-unsync
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


%{?sle15_python_module_pythons}
%define modname unsync
Name:           python-unsync
Version:        1.4.0
Release:        0
Summary:        Unsynchronize asyncio
License:        MIT
URL:            https://github.com/alex-sherman/unsync
Source:         https://github.com/alex-sherman/%{modname}/archive/v%{version}.tar.gz#/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
# unsync
Unsynchronize `asyncio` by using an ambient event loop in a separate thread.

# Rules for unsync
1. Mark all async functions with `@unsync`. May also mark regular
   functions to execute in a separate thread.
    * All `@unsync` functions, async or not, return an `Unfuture`
2. All `Futures` must be `Unfutures` which includes the result of an
   `@unsync` function call, or wrapping `Unfuture(asyncio.Future)` or
   `Unfuture(concurrent.Future)`. `Unfuture` combines the behavior of
   `asyncio.Future` and `concurrent.Future`:
   * `Unfuture.set_value` is threadsafe unlike `asyncio.Future`
   * `Unfuture` instances can be awaited, even if made from
     `concurrent.Future`
   * `Unfuture.result()` is a blocking operation *except* in
     `unsync.loop`/`unsync.thread` where it behaves like
     `asyncio.Future.result` and will throw an exception if the future
     is not done
3. Functions will execute in different contexts:
   * `@unsync` async functions will execute in an event loop in
     `unsync.thread`
   * `@unsync` regular functions will execute in
     `unsync.thread_executor`, a `ThreadPoolExecutor`
   * `@unsync(cpu_bound=True)` regular functions will execute in
     `unsync.process_executor`, a `ProcessPoolExecutor`

%prep
%setup -q -n unsync-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest -v

%files %{python_files}
%{python_sitelib}/*

%changelog
