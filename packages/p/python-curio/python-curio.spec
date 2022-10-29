#
# spec file for package python-curio
#
# Copyright (c) 2022 SUSE LLC
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           python-curio
Version:        1.6
Release:        0
Summary:        Concurrent I/O library for Python 3
License:        BSD-Source-Code
URL:            https://github.com/dabeaz/curio
Source:         https://github.com/dabeaz/curio/archive/%{version}.tar.gz#/curio-%{version}.tar.gz
Patch0:         make-tests-reproducible.patch
BuildRequires:  %{python_module base >= 3.6}
BuildRequires:  %{python_module contextvars}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%if 0%{?python_version_nodots} == 36
Requires:       python-contextvars
%endif
%python_subpackages

%description
Curio is a library for performing concurrent I/O with coroutines in Python 3.

%prep
%setup -q -n curio-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# disabled network tests
skiptest_allpython="test_ssl_outgoing or test_socket_funcs"
# https://github.com/dabeaz/curio/issues/336
# The dependency tree on curio is too large to just define skip_python36.
# Let's hope the python36 flavor will be in Tumbleweed before upstream drops
# Python 3.6 support completely, so that a dedicated staging project can work
# out the skips on all the depending packages.
skiptest_python36_only=" or test_uqueue_asyncio_consumer or test_uevent_get_asyncio or test_universal"
%if 0%{?python3_version_nodots} == 36
skiptest_python3_only="$skiptest_python36_only"
%endif
%pytest -k "not (${skiptest_allpython} ${skiptest_$python_only})"

%files %{python_files}
%license LICENSE
%doc CHANGES README.rst
%{python_sitelib}/curio
%{python_sitelib}/curio-%{version}*-info

%changelog
