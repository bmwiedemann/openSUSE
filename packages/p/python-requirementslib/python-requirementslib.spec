#
# spec file for package python-requirementslib
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-requirementslib
Version:        1.5.3
Release:        0
Summary:        A tool for converting between pip-style and pipfile requirements
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/sarugaku/requirementslib
Source:         https://github.com/sarugaku/requirementslib/archive/%{version}.tar.gz#/requirementslib-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/mahmoud/boltons/master/LICENSE#/LICENSE.boltons
Patch0:         use-boltons.patch
BuildRequires:  %{python_module parver}
BuildRequires:  %{python_module setuptools >= 40.8}
BuildRequires:  %{python_module vistir}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# Cerberus is suggested by plette, but required by requirementslib
Requires:       python-Cerberus
Requires:       python-appdirs
Requires:       python-attrs >= 18.2
Requires:       python-boltons >= 19.0.0
Requires:       python-cached-property
Requires:       python-distlib >= 0.2.8
Requires:       python-first
Requires:       python-orderedmultidict
Requires:       python-packaging >= 19.0
Requires:       python-pep517 >= 0.5.0
Requires:       python-pip-shims >= 0.3.2
Requires:       python-plette
Requires:       python-requests
Requires:       python-setuptools >= 40.8
Requires:       python-six >= 1.11.0
Requires:       python-tomlkit >= 0.5.3
Requires:       python-vistir >= 0.3.0
BuildArch:      noarch
%ifpython2
Requires:       python-scandir
Requires:       python-typing
%endif
# SECTION test requirements
BuildRequires:  %{python_module Cerberus}
BuildRequires:  %{python_module appdirs}
BuildRequires:  %{python_module attrs >= 18.2}
BuildRequires:  %{python_module boltons >= 19.0.0}
BuildRequires:  %{python_module cached-property}
BuildRequires:  %{python_module distlib >= 0.2.8}
BuildRequires:  %{python_module first}
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module orderedmultidict}
BuildRequires:  %{python_module packaging >= 0.19.0}
BuildRequires:  %{python_module pep517 >= 0.5.0}
BuildRequires:  %{python_module pip-shims}
BuildRequires:  %{python_module plette}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest-timeout}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module six >= 1.11.0}
BuildRequires:  %{python_module tomlkit >= 0.5.3}
BuildRequires:  %{python_module twine}
BuildRequires:  %{python_module vistir >= 0.3.0}
BuildRequires:  python-typing
# /SECTION
%python_subpackages

%description
A tool for converting between pip-style and pipfile requirements.

%prep
%setup -q -n requirementslib-%{version}
%patch0 -p1
cp %{SOURCE1} .

# https://github.com/sarugaku/requirementslib/pull/144 unnecessary in next release
sed -i '/colorama/d' setup.cfg

sed -i '/invoke/d' setup.cfg
rm -r tasks

# This test module is entirely online
rm tests/unit/test_dependencies.py

%build
export LANG=en_US.UTF-8
%python_build

%install
export LANG=en_US.UTF-8
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test_get_local_ref and test_get_requirements need internet, test_local_req is somehow misconfigured
#  The tests actually fail randomly; if you loop them in 100 runs around
#  3-7 tests fail, with no repeated offender most of the time
#%%pytest tests -k "not needs_internet and not test_get_local_ref and not test_get_requirements and not test_local_req"

%files %{python_files}
%doc CHANGELOG.rst README.rst docs/quickstart.rst
%license LICENSE LICENSE.boltons
%{python_sitelib}/*

%changelog
