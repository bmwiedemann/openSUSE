#
# spec file for package python-testrepository
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


%{?sle15_python_module_pythons}
Name:           python-testrepository
Version:        0.0.21
Release:        0
Summary:        A repository of test results
License:        Apache-2.0 OR BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/testing-cabal/testrepository
Source:         https://files.pythonhosted.org/packages/source/t/testrepository/testrepository-%{version}.tar.gz
BuildRequires:  %{python_module extras}
BuildRequires:  %{python_module fixtures}
BuildRequires:  %{python_module hatch_vcs}
BuildRequires:  %{python_module python-mimeparse}
BuildRequires:  %{python_module python-subunit}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module testresources}
BuildRequires:  %{python_module testscenarios}
BuildRequires:  %{python_module testtools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-dbm
Requires:       python-extras
Requires:       python-fixtures
Requires:       python-python-subunit >= 0.0.11
Requires:       python-testscenarios
Requires:       python-testtools >= 0.9.30
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%if "%python_flavor" != "python2"
Requires:       python-dbm
%endif
%python_subpackages

%description
This project provides a database of test results which can be used as part of
developer workflow to ensure/check things like:

* No commits without having had a test failure, test fixed cycle.
* No commits without new tests being added.
* What tests have failed since the last commit (to run just a subset).
* What tests are currently failing and need work.

Test results are inserted using subunit (and thus anything that can output
subunit or be converted into a subunit stream can be accepted).

%prep
%setup -q -n testrepository-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/testr

%check
#mv .testr.conf .testr.conf.orig
#%%{python_expand # first line can't be empty
#rm -rf .testrepository
#sed 's/python/$python/' .testr.conf.orig >| .testr.conf
#$python ./testr init
#$python ./testr run --parallel
#}

%post
%python_install_alternative testr

%preun
%python_uninstall_alternative testr

%files %{python_files}
%license COPYING Apache-2.0 BSD
%doc NEWS README.rst
%python_alternative %{_bindir}/testr
%{python_sitelib}/*

%changelog
