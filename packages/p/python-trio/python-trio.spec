#
# spec file for package python-trio
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
Name:           python-trio%{psuffix}
Version:        0.25.1
Release:        0
Summary:        Python async/await-native I/O library
License:        Apache-2.0 OR MIT
URL:            https://github.com/python-trio/trio
Source:         https://files.pythonhosted.org/packages/source/t/trio/trio-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  netcfg
BuildRequires:  python-rpm-macros
Requires:       python-attrs >= 20.1.0
Requires:       python-idna
Requires:       python-outcome
Requires:       python-sniffio >= 1.3.0
Requires:       python-sortedcontainers
BuildArch:      noarch
%if 0%{?python_version_nodots} < 311
Requires:       python-exceptiongroup
%endif
%if %{with test}
BuildRequires:  %{python_module astor >= 0.8}
BuildRequires:  %{python_module async_generator >= 1.9}
BuildRequires:  %{python_module pyOpenSSL}
BuildRequires:  %{python_module pytest >= 5.0}
BuildRequires:  %{python_module trio = %{version}}
BuildRequires:  %{python_module trustme}
BuildRequires:  %{python_module yapf >= 0.27.0}
%endif
%python_subpackages

%description
The Trio project produces an async/await-native I/O library for
Python. Like all async libraries, its main purpose is to help write
programs that do multiple things at the same time with parallelized
I/O, such as a web spider that wants to fetch lots of pages in
parallel, a web server that needs to juggle lots of downloads and
websocket connections at the same time, a process supervisor
monitoring multiple subprocesses. Compared to other libraries, Trio
has an obsessive focus on usability and correctness.

%prep
%autosetup -p1 -n trio-%{version}

%build
%pyproject_wheel

%install
%if %{without test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
# test_static_tool_sees_all_symbols uses jedi/pylint for static analysis,
#   pointless for us.
donttest="test_static_tool_sees_all_symbols"
# test_SSLStream_generic deadlocks in OBS
donttest+=" or test_SSLStream_generic"
# test_close_at_bad_time_for_send_all fails on PPC https://github.com/python-trio/trio/issues/1753
donttest+=" or test_close_at_bad_time_for_send_all"
# test_local_address_real fails on qemu_linux_user targets
donttest+=" or test_local_address_real"
# Don't run lint tests
donttest+=" or run_black or run_ruff or lint_failure or test_process"
%pytest -m 'not redistributors_should_skip' -k "not ($donttest)" --pyargs trio -p trio._tests.pytest_plugin --skip-optional-imports
%endif

%if %{without test}
%files %{python_files}
%doc README.rst
%license LICENSE LICENSE.APACHE2 LICENSE.MIT
%{python_sitelib}/trio
%{python_sitelib}/trio-%{version}.dist-info
%endif

%changelog
