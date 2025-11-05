#
# spec file for package python-sure
#
# Copyright (c) 2025 SUSE LLC and contributors
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
%{?sle15_python_module_pythons}
Name:           python-sure
Version:        2.0.1
Release:        0
Summary:        Utility belt for automated testing in python for python
License:        GPL-3.0-or-later
URL:            https://github.com/gabrielfalcao/sure
Source:         https://files.pythonhosted.org/packages/source/s/sure/sure-%{version}.tar.gz
# Based on https://github.com/gabrielfalcao/sure/pull/161
Patch0:         python-sure-no-mock.patch
# PATCH-FIX-OPENSUSE Support Python 3.14 ast changes
Patch1:         support-python314.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six >= 1.10.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-six >= 1.10.0
BuildArch:      noarch
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
%python_subpackages

%description
A testing library for python with powerful and flexible assertions. Sure is
heavily inspired by should.js

%prep
%autosetup -p1 -n sure-%{version}
sed -i '/^#!/d' sure/*.py
sed -i 's/--cov=sure//' setup.cfg

%build
%pyproject_wheel

%install
%pyproject_install
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

%pre
%python_libalternatives_reset_alternative sure

%files %{python_files}
%license COPYING
%doc README.rst
%python_alternative %{_bindir}/sure
%{python_sitelib}/sure
%{python_sitelib}/sure-%{version}.dist-info

%changelog
