#
# spec file for package python-python-jenkins
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2014 Thomas Bechtold <thomasbechtold@jpberlin.de>
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


Name:           python-python-jenkins
Version:        1.8.0
Release:        0
Summary:        Python bindings for the remote Jenkins API
License:        BSD-3-Clause
URL:            https://opendev.org/jjb/python-jenkins
Source:         https://files.pythonhosted.org/packages/source/p/python-jenkins/python-jenkins-%{version}.tar.gz
# https://bugs.launchpad.net/python-jenkins/+bug/1971524
Patch0:         python-python-jenkins-no-mock.patch
# PATCH-FIX-OPENSUSE Upstream are arguing about version parsing, use the
# underlying parts of LegacyVersion from packaging pre-removal
Patch1:         use-parts-of-legacy-version.patch
BuildRequires:  %{python_module cmd2}
BuildRequires:  %{python_module multi_key_dict}
BuildRequires:  %{python_module pbr >= 0.8.2}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module requests-mock >= 1.4}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module testscenarios}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(krb5-gssapi)
Requires:       python-multi_key_dict
Requires:       python-pbr
Requires:       python-requests
Requires:       python-six >= 1.3.0
Provides:       python-jenkins = %{version}
Obsoletes:      python-jenkins < %{version}
BuildArch:      noarch
%python_subpackages

%description
This package provides Python bindings for the Jenkins Remote
API. It currently supports management of:
 * Project configuration
 * Build control
 * Slave node configuration

%prep
%autosetup -p1 -n python-jenkins-%{version}

sed -i '1{\@^#!%{_bindir}/env python@d}' jenkins/__init__.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest discover -v tests

%files %{python_files}
%license COPYING
%doc README.rst
%{python_sitelib}/jenkins
%{python_sitelib}/python_jenkins-%{version}*-info

%changelog
