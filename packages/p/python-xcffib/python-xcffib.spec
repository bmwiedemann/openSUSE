#
# spec file
#
# Copyright (c) 2023 SUSE LLC
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

Name:           python-xcffib%{?psuffix}
Version:        1.2.0
Release:        0
Summary:        A drop in replacement for xpyb, an XCB python binding
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/tych0/xcffib
Source:         https://files.pythonhosted.org/packages/source/x/xcffib/xcffib-%{version}.tar.gz
# https://github.com/tych0/xcffib/commit/8a488867d30464913706376ca3a9f4c98ca6c5cf
Patch0:         python-xcffib-six-leftover.patch
# fix ffi import [bsc#1209570c4]
Patch1:         python-xcffib-ffi-import.patch
BuildRequires:  %{python_module cffi >= 1.1.0}
BuildRequires:  %{python_module setuptools}
%if %{with test}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module xcffib}
%endif
BuildRequires:  fdupes
BuildRequires:  libxcb-devel
BuildRequires:  python-rpm-macros
BuildRequires:  xeyes
BuildRequires:  xvfb-run
Requires:       python-cffi >= 1.1.0
BuildArch:      noarch
%python_subpackages

%description
The xcffib package is intended to be a (mostly) drop-in
replacement for xpyb.

%prep
%autosetup -p1 -n xcffib-%{version}

%build
%if !%{with test}
%python_build
%endif

%install
%if !%{with test}
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
%pytest
%endif

%if !%{with test}
%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/xcffib/
%{python_sitelib}/xcffib-%{version}-py*.egg-info
%endif

%changelog
