#
# spec file
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
# the test suite on <= 2.3.7.post1 is not compatible with Python 3.10
# it is already fixed in upstream's devel branch
%define skip_python310 1
%else
%define psuffix %{nil}
%bcond_with test
%endif
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-pathlib2%{?psuffix}
Version:        2.3.7.post1
Release:        0
Summary:        Object-oriented filesystem paths
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/jazzband/pathlib2
Source:         https://files.pythonhosted.org/packages/source/p/pathlib2/pathlib2-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-six
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module pathlib2 = %{version}}
BuildRequires:  %{python_module testsuite}
%endif
%ifpython2
Requires:       python-mock
Requires:       python-scandir
Requires:       python-typing
%endif
%python_subpackages

%description
The goal of pathlib2 is to provide a backport of
`standard pathlib <http://docs.python.org/dev/library/pathlib.html>`_
module which tracks the standard library module,
so all the newest features of the standard pathlib can be
used also on older Python versions.

%prep
%autosetup -n pathlib2-%{version}
dos2unix CHANGELOG.rst README.rst

%build
%python_build

%install
%if !%{with test}
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
pushd tests
%pyunittest -v
popd
%endif

%if !%{with test}
%files %{python_files}
%license LICENSE.rst
%doc CHANGELOG.rst README.rst
%{python_sitelib}/pathlib2
%{python_sitelib}/pathlib2-%{version}*-info
%endif

%changelog
