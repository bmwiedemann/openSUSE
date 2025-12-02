#
# spec file for package python-tblib
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -%{flavor}
%bcond_without  test
%else
%define psuffix %{nil}
%bcond_with     test
%endif
%{?sle15_python_module_pythons}
Name:           python-tblib%{?psuffix}
Version:        3.2.2
Release:        0
Summary:        Traceback serialization library
License:        BSD-2-Clause
URL:            https://github.com/ionelmc/python-tblib
Source:         https://files.pythonhosted.org/packages/source/t/tblib/tblib-%{version}.tar.gz
# PATCH-FIX-FEDORA https://src.fedoraproject.org/rpms/python-tblib/blob/rawhide/f/0001-test_pickle_exception-even-harder-location-stripping.patch
Patch1:         test_pickle_exception-even-harder-location-stripping.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module Twisted}
BuildRequires:  %{python_module pytest-benchmark}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module tblib == %{version}}
%endif
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
%autosetup -p1 -n tblib-%{version}

%build
%pyproject_wheel

%install
%if !%{with test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
%pytest
%endif

%if !%{with test}
%files %{python_files}
%doc AUTHORS.rst CHANGELOG.rst README.rst
%license LICENSE
%{python_sitelib}/tblib
%{python_sitelib}/tblib-%{version}.dist-info
%endif

%changelog
