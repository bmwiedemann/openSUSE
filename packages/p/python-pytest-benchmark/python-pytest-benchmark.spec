#
# spec file for package python-pytest-benchmark
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


%define skip_python2 1
Name:           python-pytest-benchmark
Version:        4.0.0
Release:        0
Summary:        A py.test fixture for benchmarking code
License:        BSD-2-Clause
URL:            https://github.com/ionelmc/pytest-benchmark
Source:         https://files.pythonhosted.org/packages/source/p/pytest-benchmark/pytest-benchmark-%{version}.tar.gz
Patch0:         fix-test-fast.patch
BuildRequires:  %{python_module aspectlib}
BuildRequires:  %{python_module elasticsearch}
BuildRequires:  %{python_module freezegun}
BuildRequires:  %{python_module py-cpuinfo}
BuildRequires:  %{python_module pygaljs}
BuildRequires:  %{python_module pygal}
BuildRequires:  %{python_module pytest >= 3.8}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  git-core
BuildRequires:  python-rpm-macros
Requires:       python-py-cpuinfo
Requires:       python-pytest >= 3.8
Requires(post): update-alternatives
Requires(postun):update-alternatives
Recommends:     python-aspectlib
Recommends:     python-elasticsearch
Recommends:     python-pygal
Recommends:     python-pygaljs
BuildArch:      noarch
%python_subpackages

%description
A py.test fixture for benchmarking code. It will group the tests into
rounds that are calibrated to the chosen timer.

%prep
%autosetup -p1 -n pytest-benchmark-%{version}
# skip cli tests as we use update-alternatives
rm -f tests/test_cli.py
# Don't look for a test pass in the wrong place -- https://github.com/ionelmc/pytest-benchmark/issues/214
sed -i -e '/test_fast PASSED/d' -e '/test_fast SKIPPED/d' tests/test_benchmark.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%python_clone -a %{buildroot}%{_bindir}/pytest-benchmark
%python_clone -a %{buildroot}%{_bindir}/py.test-benchmark

%check
%pytest tests

%post
%{python_install_alternative pytest-benchmark py.test-benchmark}

%postun
%python_uninstall_alternative pytest-benchmark

%files %{python_files}
%doc AUTHORS.rst CHANGELOG.rst README.rst
%license LICENSE
%python_alternative %{_bindir}/py.test-benchmark
%python_alternative %{_bindir}/pytest-benchmark
%{python_sitelib}/pytest_benchmark
%{python_sitelib}/pytest_benchmark-%{version}*-info

%changelog
