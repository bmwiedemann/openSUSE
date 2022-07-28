#
# spec file for package python-mailman-hyperkitty
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


%if 0%{?suse_version} >= 1550
# Newest python supported by mailman is Python 3.9 -- https://gitlab.com/mailman/mailman/-/issues/936
%define pythons python39
%else
%{?!python_module:%define python_module() python3-%{**}}
%define pythons python3
%endif
Name:           python-mailman-hyperkitty
Version:        1.2.0
Release:        0
Summary:        Mailman archiver plugin for HyperKitty
License:        GPL-3.0-only
URL:            https://gitlab.com/mailman/mailman-hyperkitty/
Source:         https://files.pythonhosted.org/packages/source/m/mailman-hyperkitty/mailman-hyperkitty-%{version}.tar.gz
# https://gitlab.com/mailman/mailman-hyperkitty/-/issues/28
Patch0:         python-mailman-hyperkitty-no-mock.patch
Patch1:         python-mailman-hyperkitty-fix-archiver-test.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-mailman
Requires:       python-requests
Requires:       python-setuptools
Requires:       python-zope.interface
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  mailman3 >= 3.3.5
BuildRequires:  %{python_module nose2}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module zope.interface}
# /SECTION
%python_subpackages

%description
Mailman archiver plugin for HyperKitty

%prep
%autosetup -n mailman-hyperkitty-%{version} -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python -m nose2 -v

%files %{python_files}
%doc README.rst mailman-hyperkitty.cfg
%license LICENSE.txt
%{python_sitelib}/mailman_hyperkitty
%{python_sitelib}/mailman_hyperkitty-%{version}*-info

%changelog
