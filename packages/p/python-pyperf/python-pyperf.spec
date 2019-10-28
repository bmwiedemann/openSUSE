#
# spec file for package python-pyperf
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-pyperf
Version:        1.6.1
Release:        0
License:        MIT
Summary:        Python module to run and analyze benchmarks
Url:            https://github.com/vstinner/pyperf
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/p/pyperf/pyperf-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
# SECTION test requirements
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module six}
BuildRequires:  python2-contextlib2
BuildRequires:  python2-statistics
BuildRequires:  python2-unittest2
# /SECTION
BuildRequires:  fdupes
Requires:       python-six
Recommends:     python-psutil
%ifpython2
Requires:       python2-contextlib2
Requires:       python2-statistics
%endif
BuildArch:      noarch

%python_subpackages

%description
Python module to run and analyze benchmarks.

%prep
%setup -q -n pyperf-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# See https://github.com/vstinner/pyperf/issues/58 for test_collect_metadata failure
%pytest -k 'not test_collect_metadata'

%files %{python_files}
%doc README.rst
%license COPYING
%python3_only %{_bindir}/pyperf
%{python_sitelib}/*

%changelog
