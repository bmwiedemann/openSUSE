#
# spec file for package python-aioeventlet
#
# Copyright (c) 2023 SUSE LLC
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


# versioning fun
%define intver 0.5.1
Name:           python-aioeventlet
Version:        0.5.2
Release:        0
Summary:        Asyncio event loop scheduling callbacks in eventlet
License:        Apache-2.0
URL:            https://pypi.org/project/aioeventlet/
Source:         https://files.pythonhosted.org/packages/source/a/aioeventlet/aioeventlet-%{version}.tar.gz
# pr_1.patch is Python 3.7+ support
Patch0:         pr_1.patch
# PATCH-FIX-OPENSUSE py311.patch Python 3.11+ support
Patch1:         py311.patch
BuildRequires:  %{python_module eventlet}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
Requires:       python-eventlet
BuildArch:      noarch
%ifpython2
Requires:       python-trollius >= 0.3
%endif
%python_subpackages

%description
aioeventlet implements the asyncio API (PEP 3156) on top of eventlet. It makes
possible to write asyncio code in a project currently written for eventlet.

aioeventlet allows to use greenthreads in asyncio coroutines, and to use
asyncio coroutines, tasks and futures in greenthreads: see ``link_future()``
and ``wrap_greenthread()`` functions.

The main visible difference between aioeventlet and trollius is the behaviour
of ``run_forever()``: ``run_forever()`` blocks with trollius, whereas it runs
in a greenthread with aioeventlet. It means that aioeventlet event loop can run
in an greenthread while the Python main thread runs other greenthreads in
parallel.

%prep
%autosetup -p1 -n aioeventlet-%{intver}

%build
%python_build

%install
%python_install

%check
# Python 2 requires trollius which is not in devel project,
# and test setup fails on Python 3.6 as it tries to reach live DNS server
%{python_expand PYTHON_VERSION=%{$python_version_nodots}
if [[ ${PYTHON_VERSION:0:1} -eq 3 && ${PYTHON_VERSION:1:2} -gt 6 ]]; then
  # Some tests in test_eventlet.py halt
  $python -m pytest -k 'EventletTests or test_wrap_invalid_type or test_wrap_greenlet_dead or test_wrap_greenlet_running or test_greenlet'
fi}

%files %{python_files}
%license COPYING
%doc README
%{python_sitelib}/aioeventlet.py
%{python_sitelib}/aioeventlet-%{intver}*-info
%pycache_only %{python_sitelib}/__pycache__

%changelog
