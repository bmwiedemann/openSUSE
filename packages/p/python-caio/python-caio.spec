#
# spec file for package python-caio
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


Name:           python-caio
Version:        0.10.2
Release:        0
Summary:        Asynchronous file IO for Linux MacOS or Windows
License:        Apache-2.0
URL:            https://github.com/mosquito/caio
Source:         https://github.com/mosquito/caio/archive/refs/tags/%{version}.tar.gz#/caio-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools >= 77}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  python-rpm-macros
%python_subpackages

%description
Asynchronous file IO for Linux (libaio and POSIX AIO), with a thread-pool
based fallback. Provides a small, fast async file-IO layer.

%prep
%autosetup -p1 -n caio-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
# drop the bundled C sources/headers that the wheel ships alongside the .so
find %{buildroot} -name '*.c' -delete
find %{buildroot} -name '*.h' -delete
# force hash-based .pyc (avoid python-bytecode-inconsistent-mtime)
%python_expand $python -m compileall -q -f -o 0 -o 1 --invalidation-mode unchecked-hash %{buildroot}%{$python_sitearch}/caio
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# test_asyncio_adapter.py needs aiomisc (unpackaged); test_file_selector needs a
# writable path the build chroot lacks; test_env_selector asserts the native
# io_uring/linux-aio/thread backends are selectable, but the build chroot only
# offers the pure-Python fallback -- skip those, run the rest of the suite
%pytest_arch --asyncio-mode=auto --ignore tests/test_asyncio_adapter.py -k "not test_file_selector and not test_env_selector"

%files %{python_files}
%doc README.md
%license COPYING
%{python_sitearch}/caio
%{python_sitearch}/caio-%{version}.dist-info

%changelog
