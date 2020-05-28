#
# spec file for package python-pytest-xdist
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
Name:           python-pytest-xdist
Version:        1.32.0
Release:        0
Summary:        Distributed testing and loop-on-failing for py.test
License:        MIT
URL:            https://github.com/pytest-dev/pytest-xdist
Source0:        https://files.pythonhosted.org/packages/source/p/pytest-xdist/pytest-xdist-%{version}.tar.gz
BuildRequires:  %{python_module execnet >= 1.1}
BuildRequires:  %{python_module filelock}
BuildRequires:  %{python_module pytest >= 4.4.0}
BuildRequires:  %{python_module pytest-forked}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-execnet >= 1.1
Requires:       python-pytest >= 4.4.0
Requires:       python-pytest-forked
Requires:       python-six
BuildArch:      noarch
%python_subpackages

%description
The `pytest-xdist`_ plugin extends py.test with some unique
test execution modes:

* test run parallelization_: if you have multiple CPUs or hosts you can use
  those for a combined test run.  This allows to speed up
  development or to use special resources of `remote machines`_.

* ``--boxed``: (not available on Windows) run each test in a boxed_
  subprocess to survive ``SEGFAULTS`` or otherwise dying processes

* ``--looponfail``: run your tests repeatedly in a subprocess.  After each run
  py.test waits until a file in your project changes and then re-runs
  the previously failing tests.  This is repeated until all tests pass
  after which again a full run is performed.

* `Multi-Platform`_ coverage: you can specify different Python interpreters
  or different platforms and run tests in parallel on all of them.

Before running tests remotely, ``py.test`` efficiently "rsyncs" your
program source code to the remote place.  All test results
are reported back and displayed to your local terminal.
You may specify different Python versions and interpreters.

%prep
%setup -q -n pytest-xdist-%{version}
sed -i 's/\r//' README.rst

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc CHANGELOG.rst ISSUES.txt README.rst
%license LICENSE
%{python_sitelib}/xdist
%{python_sitelib}/pytest_xdist-%{version}-py%{python_version}.egg-info

%changelog
