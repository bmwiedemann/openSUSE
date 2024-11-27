#
# spec file for package python-wheel
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


%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif

%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%{?sle15_python_module_pythons}
Name:           python-wheel%{psuffix}
Version:        0.45.1
Release:        0
Summary:        A built-package format for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/pypa/wheel
Source:         https://github.com/pypa/wheel/archive/%{version}.tar.gz#/wheel-%{version}.tar.gz
# Bootstrap: Don't BuildRequire setuptools or pip here!
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module flit-core}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros >= 20210929
%if %{with libalternatives}
Requires:       alts
BuildRequires:  alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pytest >= 3.0.0}
BuildRequires:  %{python_module wheel >= %{version}}
%endif
%python_subpackages

%description
A built-package format for Python.

A wheel is a ZIP-format archive with a specially formatted filename
and the .whl extension. It is designed to contain all the files for a
PEP 376 compatible install in a way that is very close to the on-disk
format. Many packages will be properly installed with only the "Unpack"
step (simply extracting the file onto sys.path), and the unpacked archive
preserves enough information to "Spread" (copy data and scripts to their
final locations) at any later time.

%prep
%autosetup -p1 -n wheel-%{version}

%build
%if !%{with test}
%{python_expand # bootstrap with built-in pip
$python -m venv build/env
build/env/bin/python -m ensurepip
export PYTHONPATH=build/env/lib/python%{$python_bin_suffix}/site-packages
%{$python_pyproject_wheel}
}
%endif

%install
%if !%{with test}
%{python_expand # use pip bootstrapped above
export PYTHONPATH=build/env/lib/python%{$python_bin_suffix}/site-packages
%{$python_pyproject_install}
}
%python_clone -a %{buildroot}%{_bindir}/wheel
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
export LC_ALL=en_US.utf8
export PYTHONDONTWRITEBYTECODE=1
%pytest
%endif

%if !%{with test}

%pre
# If libalternatives is used: Removing old update-alternatives entries.
%python_libalternatives_reset_alternative wheel

%post
%python_install_alternative wheel

%postun
%python_uninstall_alternative wheel

%files %{python_files}
%doc docs/news.rst README.rst
%license LICENSE.txt
%python_alternative %{_bindir}/wheel
%{python_sitelib}/wheel-%{version}*-info
%{python_sitelib}/wheel/
%endif

%changelog
