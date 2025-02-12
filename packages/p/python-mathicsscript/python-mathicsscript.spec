#
# spec file for package python-mathicsscript
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
%else
%define psuffix %{nil}
%bcond_with test
%endif
%define skip_python313 1
%define modname mathicsscript
Name:           python-mathicsscript%{psuffix}
Version:        8.0.0
Release:        0
Summary:        A command line interface to Mathics
License:        GPL-3.0-or-later
URL:            https://mathics.org/
Source0:        https://github.com/Mathics3/mathicsscript/archive/refs/tags/%{version}.tar.gz#/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module Mathics >= 8.0.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Mathics3 >= 8.0.0
Requires:       python-Mathics-Scanner
Requires:       python-Pygments
Requires:       python-click
Requires:       python-colorama
Requires:       python-columnize
Requires:       python-mathics-pygments
Requires:       python-networkx
Requires:       python-prompt_toolkit
Requires:       python-term-background
Requires(post): update-alternatives
Requires(postun): update-alternatives
%if %{with test}
# SECTION For tests
BuildRequires:  %{python_module colorama}
BuildRequires:  %{python_module columnize}
BuildRequires:  %{python_module mathics-pygments}
BuildRequires:  %{python_module mathicsscript = %{version}}
BuildRequires:  %{python_module networkx}
BuildRequires:  %{python_module prompt_toolkit >= 3.0.18}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module term-background}
# /SECTION
%endif
BuildArch:      noarch
%python_subpackages

%description
Mathicsscript is a feature-rich command line interface to Mathics.

%prep
%autosetup -n %{modname}-%{version}

%build
%if %{without test}
%pyproject_wheel
%endif

%install
%if %{without test}
%pyproject_install
%{python_expand # Miscellaneous fixes
# Clear some unnecessary hashbangs
sed -i "1{\@/usr/bin/env@d}" \
  %{buildroot}%{$python_sitelib}/%{modname}/fake_psviewer.py \
  %{buildroot}%{$python_sitelib}/%{modname}/__main__.py \
  %{buildroot}%{$python_sitelib}/%{modname}/asymptote.py
# Move test dir into main module dir
mv %{buildroot}%{$python_sitelib}/test %{buildroot}%{$python_sitelib}/%{modname}/
%fdupes %{buildroot}%{$python_sitelib}/
}

%python_clone -a %{buildroot}%{_bindir}/fake_psviewer.py
%python_clone -a %{buildroot}%{_bindir}/mathicsscript
%endif

%if %{with test}
%check
export MATHICS_CHARACTER_ENCODING="ASCII"
%pytest
%endif

%if %{without test}
%post
%python_install_alternative fake_psviewer.py
%python_install_alternative mathicsscript

%postun
%python_uninstall_alternative fake_psviewer.py
%python_uninstall_alternative mathicsscript

%files %{python_files}
%license COPYING.txt
%doc README.rst
%python_alternative %{_bindir}/fake_psviewer.py
%python_alternative %{_bindir}/mathicsscript
%{python_sitelib}/%{modname}/
%{python_sitelib}/%{modname}-%{version}*.*-info/
%endif

%changelog
