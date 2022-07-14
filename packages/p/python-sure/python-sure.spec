#
# spec file for package python-sure
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-sure
Version:        2.0.0
Release:        0
Summary:        Utility belt for automated testing in python for python
License:        GPL-3.0-or-later
URL:            https://github.com/gabrielfalcao/sure
Source:         https://files.pythonhosted.org/packages/source/s/sure/sure-%{version}.tar.gz
# Based on https://github.com/gabrielfalcao/sure/pull/161
Patch0:         python-sure-no-mock.patch
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six >= 1.10.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-six >= 1.10.0
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
%python_subpackages

%description
A testing library for python with powerful and flexible assertions. Sure is
heavily inspired by should.js

%prep
%autosetup -p1 -n sure-%{version}
sed -i '/^#!/d' sure/*.py
sed -i 's/--cov=sure//' setup.cfg

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/sure
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# requires nose
rm tests/test_old_api.py
%pytest

%post
%python_install_alternative sure

%postun
%python_uninstall_alternative sure

%files %{python_files}
%license COPYING
%doc README.rst
%python_alternative %{_bindir}/sure
%{python_sitelib}/sure
%{python_sitelib}/sure-%{version}*-info

%changelog
