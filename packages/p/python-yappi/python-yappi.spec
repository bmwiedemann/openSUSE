#
# spec file for package python-yappi
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
%define skip_python36 1
Name:           python-yappi
Version:        1.4.0
Release:        0
Summary:        Yet Another Python Profiler
License:        MIT
URL:            https://github.com/sumerc/yappi
Source:         https://files.pythonhosted.org/packages/source/y/yappi/yappi-%{version}.tar.gz
BuildRequires:  %{python_module contextvars}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module gevent >= 20.6.2}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-setuptools
Requires(post): update-alternatives
Requires(postun):update-alternatives
%python_subpackages

%description
Yet Another Python Profiler

%prep
%setup -q -n yappi-%{version}

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/yappi
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
export PYTHONPATH="tests/"
# Skip two flaky tests
skip_tests="not test_basic_old_style and not test_basic"
%if %{python3_version_nodots} < 37
    # this test relies on asyncio.run method
    skip_tests="$skip_tests and not test_asyncio_context_vars"
%endif
%if 0%{?qemu_user_space_build}
# qemu linux-user emulation always creates an additional thread
skip_tests="$skip_tests and not test_context_cbks_reset_to_default"
%endif
# yappi binary is not available (only yappi-%python_version)
skip_tests="$skip_tests and not test_run_as_script"
%pytest_arch -k "$skip_tests"

%post
%python_install_alternative yappi

%postun
%python_uninstall_alternative yappi

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/yappi
%{python_sitearch}/*

%changelog
