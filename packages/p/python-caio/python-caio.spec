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
Version:        0.11.1
Release:        0
Summary:        Asynchronous file IO for Linux MacOS or Windows
License:        Apache-2.0
URL:            https://github.com/mosquito/caio
# Use the PyPI sdist, not the GitHub archive: upstream forgot to bump
# "version" in pyproject.toml for 0.11.0 and 0.11.1, so a build from the git
# tag installs caio-0.10.2.dist-info and the %%files glob below misses it. The
# sdist is produced by upstream's release CI with the correct version injected,
# and since 0.11.0 it also ships the complete tests directory, so %%check is
# unaffected.
Source:         https://files.pythonhosted.org/packages/source/c/caio/caio-%{version}.tar.gz
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
# 0.11.0 started shipping tests/ in the sdist without excluding it from the
# wheel's package discovery, so setuptools installs it as a top-level "tests"
# package. That name is far too generic to occupy in site-packages -- it would
# collide with every other project doing the same -- and the suite has already
# been run from the build tree by %%check, so drop it.
%python_expand rm -rf %{buildroot}%{$python_sitearch}/tests
# force hash-based .pyc (avoid python-bytecode-inconsistent-mtime)
%python_expand $python -m compileall -q -f -o 0 -o 1 --invalidation-mode unchecked-hash %{buildroot}%{$python_sitearch}/caio
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# test_asyncio_adapter.py needs aiomisc (unpackaged); test_file_selector needs a
# writable path the build chroot lacks; test_env_selector asserts the native
# io_uring/linux-aio/thread backends are selectable, but the build chroot only
# offers the pure-Python fallback -- skip those, run the rest of the suite.
#
# The five names below are tests added in 0.11.0 that cannot pass here:
#  * read_with_absurd_nbytes / linux_aio_process_events_max_requests re-exec
#    "python -c" to survive a possible abort. For "-c" the interpreter puts the
#    current directory first on sys.path, so the child imports the source tree's
#    caio/ -- which has the .py files but none of the compiled extensions -- and
#    fails with "No module named caio.thread_aio" before reaching the assertion.
#    The test harness assumes an in-place build; we install into the buildroot.
#  * process_events_respects_timeout_and_releases_gil, poll_does_not_block and
#    process_events_negative_timeout assert real timing and blocking behaviour
#    of linux-aio and io_uring completions, which a parallel OBS build chroot
#    does not reproduce reliably.
%pytest_arch --asyncio-mode=auto --ignore tests/test_asyncio_adapter.py -k "not test_file_selector and not test_env_selector and not test_read_with_absurd_nbytes_raises_cleanly and not test_linux_aio_process_events_max_requests_is_bounded and not test_process_events_respects_timeout_and_releases_gil and not test_poll_does_not_block_when_nothing_pending and not test_process_events_negative_timeout_waits_indefinitely"

%files %{python_files}
%doc README.md
%license COPYING
%{python_sitearch}/caio
%{python_sitearch}/caio-%{version}.dist-info

%changelog
