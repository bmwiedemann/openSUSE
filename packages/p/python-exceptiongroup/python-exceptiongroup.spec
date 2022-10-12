#
# spec file for package python-exceptiongroup
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


%define pyversion 1.0.0rc9
%define skip_python311 1
Name:           python-exceptiongroup
Version:        1.0.0~rc9
Release:        0
Summary:        Backport of PEP 654 (exception groups)
License:        MIT AND Python-2.0
URL:            https://github.com/agronholm/exceptiongroup
Source:         https://github.com/agronholm/exceptiongroup/archive/refs/tags/%{pyversion}.tar.gz#/exceptiongroup-%{pyversion}-gh.tar.gz
BuildRequires:  %{python_module base >= 3.7 with %python-base < 3.11}
BuildRequires:  %{python_module flit-scm}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
This is a backport of the ``BaseExceptionGroup`` and ``ExceptionGroup`` classes from
Python 3.11.

It contains the following:

* The  ``exceptiongroup.BaseExceptionGroup`` and ``exceptiongroup.ExceptionGroup``
  classes
* A utility function (``exceptiongroup.catch()``) for catching exceptions possibly
  nested in an exception group
* Patches to the ``TracebackException`` class that properly formats exception groups
  (installed on import)
* An exception hook that handles formatting of exception groups through
  ``TracebackException`` (installed on import)
* Special versions of some of the functions from the ``traceback`` module, modified to
  correctly handle exception groups even when monkey patching is disabled, or blocked by
  another custom exception hook:

  * ``traceback.format_exception()``
  * ``traceback.format_exception_only()``
  * ``traceback.print_exception()``
  * ``traceback.print_exc()``

If this package is imported on Python 3.11 or later, the built-in implementations of the
exception group classes are used instead, ``TracebackException`` is not monkey patched
and the exception hook won't be installed.

%prep
%setup -q -n exceptiongroup-%{pyversion}

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{pyversion}
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/exceptiongroup
%{python_sitelib}/exceptiongroup-%{pyversion}*-info

%changelog
