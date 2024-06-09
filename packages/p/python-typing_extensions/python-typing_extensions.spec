#
# spec file for package python-typing_extensions
#
# Copyright (c) 2024 SUSE LLC
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
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif

%{?sle15_python_module_pythons}
Name:           python-typing_extensions%{psuffix}
Version:        4.12.2
Release:        0
Summary:        Backported and Experimental Type Hints for Python 3.8+
License:        Python-2.0
URL:            https://github.com/python/typing_extensions
Source0:        https://files.pythonhosted.org/packages/source/t/typing_extensions/typing_extensions-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module flit-core >= 3.4 with %python-flit-core < 4}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Provides:       python-typing-extensions = %{version}-%{release}
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module testsuite}
%endif
%python_subpackages

%description
The typing_extensions module serves two related purposes:

  * Enable use of new type system features on older Python versions.
    For example, typing.TypeGuard is new in Python 3.10, but
    typing_extensions allows users on previous Python versions to use
    it too.
  * Enable experimentation with new type system PEPs before they are
    accepted and added to the typing module.

New features may be added to typing_extensions as soon as they are
specified in a PEP that has been added to the python/peps repository.
If the PEP is accepted, the feature will then be added to typing for
the next CPython release. No typing PEP has been rejected so far, so
we haven't yet figured out how to deal with that possibility.

Starting with version 4.0.0, typing_extensions uses Semantic Versioning.
The major version is incremented for all backwards-incompatible changes.
Therefore, it's safe to depend on typing_extensions like this:
typing_extensions >=x.y, <(x+1),
where x.y is the first version that includes all features you need.

typing_extensions supports Python versions 3.7 and higher.
In the future, support for older Python versions will be dropped some time
after that version reaches end of life.

%prep
%autosetup -p1 -n typing_extensions-%{version}

%if !%{with test}
%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
pushd src
%pyunittest -v test_typing_extensions
popd
%endif

%if !%{with test}
%files %{python_files}
%license LICENSE
%doc CHANGELOG.md README.md
%{python_sitelib}/typing_extensions.py*
%pycache_only %{python_sitelib}/__pycache__/typing_extensions*
%{python_sitelib}/typing_extensions-%{version}*-info
%endif

%changelog
