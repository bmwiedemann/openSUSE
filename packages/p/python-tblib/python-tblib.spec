#
# spec file for package python
#
# Copyright (c) 2020 SUSE LLC
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
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%bcond_without  test
%bcond_without  test_twisted
%define psuffix -test
%else
%bcond_without  test
%bcond_with     test_twisted
%endif
Name:           python-tblib%{?psuffix}
Version:        1.7.0
Release:        0
Summary:        Traceback serialization library
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/ionelmc/python-tblib
Source:         https://files.pythonhosted.org/packages/source/t/tblib/tblib-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if %{with test_twisted}
BuildRequires:  %{python_module Twisted}
BuildRequires:  %{python_module tblib == %{version}}
%endif
%if %{with test}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module six}
%endif
Requires:       python-six
BuildArch:      noarch

%python_subpackages

%description
Traceback serialization library.

It allows you to:

* Pickle  tracebacks and raise exceptions with pickled tracebacks in
  different processes. This allows better error handling when running
  code over multiple processes (imagine multiprocessing, billiard,
  futures, celery etc).
* Create traceback objects from strings (the ``from_string`` method).
  *No pickling is used*.
* Serialize tracebacks to/from plain dicts (the ``from_dict`` and
  ``to_dict`` methods). *No pickling is used*.
* Raise the tracebacks created from the aforementioned sources.

Again, note that using the pickle support is completely optional. You
are solely responsible for security problems should you decide to use
the pickle support.

%prep
%setup -q -n tblib-%{version}

%build
%python_build

%install
%if "%{flavor}" != "test"
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
%pytest
%endif

%if "%{flavor}" != "test"
%files %{python_files}
%doc AUTHORS.rst CHANGELOG.rst README.rst
%license LICENSE
%{python_sitelib}/*
%endif

%changelog
