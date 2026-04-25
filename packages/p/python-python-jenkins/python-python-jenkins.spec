#
# spec file for package python-python-jenkins
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Version:        1.8.3
Release:        0
Summary:        Python bindings for the remote Jenkins API
License:        BSD-3-Clause
URL:            https://opendev.org/jjb/python-jenkins
Source:         https://files.pythonhosted.org/packages/source/p/python-jenkins/python_jenkins-%{version}.tar.gz
BuildRequires:  %{python_module cmd2}
BuildRequires:  %{python_module multi_key_dict}
BuildRequires:  %{python_module multiprocess}
BuildRequires:  %{python_module pbr >= 0.8.2}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module requests-mock >= 1.11}
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
%autosetup -p1 -n python_jenkins-%{version}

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
%{python_sitelib}/python_jenkins-%{version}.dist-info

%changelog
