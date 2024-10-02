#
# spec file for package python-async-wrapper
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


Name:           python-async-wrapper
Version:        0.10.0
Release:        0
Summary:        Library for improving async programming
License:        MIT
URL:            https://github.com/phi-friday/async-wrapper
# Using GitHub tarball, because it contains tests
Source:         https://github.com/phi-friday/async-wrapper/archive/refs/tags/v%{version}.tar.gz#/async-wrapper-%{version}.tar.gz
# PATCH-FEATURE-OPENSUSE fix-version.patch gh#phi-friday/async-wrapper#1 mcepl@suse.com
# We cannot use dynamic version number
Patch0:         fix-version.patch
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-anyio >= 4.0.0
Requires:       python-sniffio >= 1.3.1
Requires:       python-typing-extensions >= 4.4.0
Requires:       (python-exceptiongroup if python-base < 3.11)
Suggests:       python-greenlet
Suggests:       python-readthedocs-sphinx-search >= 0.3.2
Suggests:       python-sphinx >= 7.1.0
Suggests:       python-sphinx-mdinclude >= 0.5.3
Suggests:       python-sphinx-rtd-theme >= 2.0.0
Suggests:       python-sqlalchemy
Suggests:       python-uvloop
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module aiosqlite >= 0.20.0}
BuildRequires:  %{python_module anyio >= 4.0.0}
BuildRequires:  %{python_module pytest >= 8.0.0}
BuildRequires:  %{python_module pytest-xdist >= 3.6.1}
BuildRequires:  %{python_module sniffio >= 1.3.1}
BuildRequires:  %{python_module sqlalchemy}
BuildRequires:  %{python_module trio >= 0.24.0}
BuildRequires:  %{python_module typing-extensions >= 4.4.0}
BuildRequires:  %{python_module uvloop}
# /SECTION
%python_subpackages

%description
Package with helping functions for async programming.

%prep
%autosetup -p1 -n async-wrapper-%{version}

# We have to use fixed version of the package and we don't need to run test coverage analysis
sed -i -E -e 's/@VERSION@/%{version}/' -e '/^addopts/s/ --cov.*/"/' pyproject.toml

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%{python_sitelib}/async_wrapper
%{python_sitelib}/async_wrapper-%{version}.dist-info

%changelog
