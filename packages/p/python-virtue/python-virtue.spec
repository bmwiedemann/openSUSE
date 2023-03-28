#
# spec file for package python-virtue
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


Name:             python-virtue
Version:          2.5.2
Release:          0
Summary:          After trial comes virtue. A test runner for good
License:          MIT
URL:              https://github.com/Julian/Virtue
Source:           https://files.pythonhosted.org/packages/source/v/virtue/virtue-2.5.2.tar.gz
BuildRequires:    fdupes
BuildRequires:    python-rpm-macros
BuildRequires:    %{python_module hatch_vcs}
BuildRequires:    %{python_module hatchling}
BuildRequires:    %{python_module pip}
BuildRequires:    %{python_module setuptools}
# SECTION test requirements
BuildRequires:    %{python_module attrs >= 19}
BuildRequires:    %{python_module click}
BuildRequires:    %{python_module colorama}
BuildRequires:    %{python_module pyrsistent}
BuildRequires:    %{python_module Twisted}
# /SECTION
Requires(post):   update-alternatives
Requires(postun): update-alternatives
Requires:         python-attrs >= 19
Requires:         python-click
Requires:         python-colorama
Requires:         python-pyrsistent
Requires:         python-Twisted
Suggests:         python-importlib_metadata
Suggests:         python-pkgutil_resolve_name >= 1.3.10
BuildArch:        noarch
%python_subpackages

%description
After trial comes virtue. A test runner for good.

%prep
%setup -q -n virtue-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/virtue
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative virtue

%postun
%python_uninstall_alternative virtue

%files %{python_files}
%doc README.rst
%license COPYING
%python_alternative %{_bindir}/virtue
%{python_sitelib}/virtue
%{python_sitelib}/virtue-%{version}.dist-info/

%changelog
