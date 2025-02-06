#
# spec file for package python-breathe
#
# Copyright (c) 2025 SUSE LLC
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
Name:           python-breathe
Version:        4.35.0
Release:        0
Summary:        Sphinx Doxygen renderer
License:        BSD-3-Clause
URL:            https://github.com/michaeljones/breathe
Source:         https://github.com/michaeljones/breathe/archive/v%{version}.tar.gz#/breathe-%{version}.tar.gz
Patch0:         support-sphinx-7.2.patch
# PATCH-FIX-UPSTREAM support-sphinx-7.4.patch gh#breathe-doc/breathe!1007 mcepl@suse.com
# fix the test suite
Patch1:         support-sphinx-7.4.patch
BuildRequires:  %{python_module Sphinx >= 4.0}
BuildRequires:  %{python_module docutils >= 0.12}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Sphinx >= 4.0
Requires:       python-docutils >= 0.12
Requires(post): update-alternatives
Requires(postun): update-alternatives
Provides:       python-sphinxcontrib-breathe = %{version}
Obsoletes:      python-sphinxcontrib-breathe < %{version}
BuildArch:      noarch
%python_subpackages

%description
Breathe is an extension to reStructuredText and Sphinx to be
able to read and  render Doxygen xml output.

%prep
%autosetup -p1 -n breathe-%{version}

%build
%pyproject_wheel

%check
%pytest

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/breathe-apidoc
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative breathe-apidoc

%postun
%python_uninstall_alternative breathe-apidoc

%files %{python_files}
%doc README.rst
%license LICENSE
%python_alternative %{_bindir}/breathe-apidoc
%{python_sitelib}/breathe
%{python_sitelib}/breathe-%{version}*-info

%changelog
