#
# spec file for package python-humanfriendly
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
%define psuffix test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%{?sle15_python_module_pythons}
Name:           python-humanfriendly%{psuffix}
Version:        10.0
Release:        0
Summary:        Human friendly input/output for text interfaces using Python
License:        MIT
URL:            https://github.com/xolox/python-humanfriendly
Source:         https://files.pythonhosted.org/packages/source/h/humanfriendly/humanfriendly-%{version}.tar.gz
# https://github.com/xolox/python-humanfriendly/issues/62
Patch0:         python-humanfriendly-no-mock.patch
# PATCH-FIX-UPSTREAM gh#xolox/python-humanfriendly#65
Patch1:         pytest-7-support.patch
# PATCH-FIX-UPSTREAM gh#xolox/python-humanfriendly#75
Patch2:         support-python-313.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module capturer >= 2.1}
BuildRequires:  %{python_module coloredlogs >= 2}
BuildRequires:  %{python_module docutils}
BuildRequires:  %{python_module pytest >= 3.0.7}
BuildRequires:  %{python_module pytest-cov >= 2.4.0}
BuildRequires:  %{pythons}
%endif
%python_subpackages

%description
The functions and classes in the humanfriendly package can be used to make
text interfaces more user friendly.

 Some example features:
  * Parsing and formatting numbers, file sizes, pathnames and timespans in
    simple, human friendly formats.
  * Easy to use timers for long running operations, with human friendly
    formatting of the resulting timespans.
  * Prompting the user to select a choice from a list of options by typing
    the option’s number or a unique substring of the option.
  * Terminal interaction including text styling (ANSI escape sequences), user
    friendly rendering of usage messages and querying the terminal for its size.

%prep
%autosetup -p1 -n humanfriendly-%{version}

%build
%pyproject_wheel

%install
%if !%{with test}
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/humanfriendly
%{python_expand chmod a+x %{buildroot}%{$python_sitelib}/humanfriendly/tests.py
sed -i "s|#!%{_bindir}/env python|#!%__$python|" %{buildroot}%{$python_sitelib}/humanfriendly/tests.py
$python -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitelib}/humanfriendly/
$python -O -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitelib}/humanfriendly/
%fdupes %{buildroot}%{$python_sitelib}
}
%endif

%if %{with test}
%check
%pytest humanfriendly/tests.py
%endif

%if !%{with test}
%post
%python_install_alternative humanfriendly

%postun
%python_uninstall_alternative humanfriendly

%files %{python_files}
%license LICENSE.txt
%doc README.rst
%python_alternative %{_bindir}/humanfriendly
%{python_sitelib}/humanfriendly
%{python_sitelib}/humanfriendly-%{version}.dist-info
%endif

%changelog
