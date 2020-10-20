#
# spec file for package python-requirementslib
#
# Copyright (c) 2020 SUSE LLC
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
%bcond_without python2
Name:           python-requirementslib
Version:        1.5.13
Release:        0
Summary:        A tool for converting between pip-style and pipfile requirements
License:        MIT
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
Requires:       python-attrs >= 19.2.0
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
Requires:       python-backports.tempfile
Requires:       python-scandir
Requires:       python-typing
%endif
# SECTION test requirements
BuildRequires:  %{python_module Cerberus}
BuildRequires:  %{python_module appdirs}
BuildRequires:  %{python_module attrs >= 19.2.0}
BuildRequires:  %{python_module boltons >= 19.0.0}
BuildRequires:  %{python_module cached-property}
BuildRequires:  %{python_module dateutil}
BuildRequires:  %{python_module distlib >= 0.2.8}
BuildRequires:  %{python_module first}
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module orderedmultidict}
BuildRequires:  %{python_module packaging >= 0.19.0}
BuildRequires:  %{python_module pep517 >= 0.5.0}
BuildRequires:  %{python_module pip-shims}
BuildRequires:  %{python_module plette}
BuildRequires:  %{python_module pytest-timeout}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module six >= 1.11.0}
BuildRequires:  %{python_module tomlkit >= 0.5.3}
BuildRequires:  %{python_module twine}
BuildRequires:  %{python_module vistir >= 0.3.0}
%if %{with python2}
BuildRequires:  python-backports.tempfile
BuildRequires:  python-scandir
BuildRequires:  python-typing
%endif
# /SECTION
%python_subpackages

%description
RequirementsLib provides a simple layer for building and 
interacting with requirements in both the Pipfile format and 
the requirements.txt format. This library was originally built 
for converting between these formats in Pipenv.

%prep
%setup -q -n requirementslib-%{version}
%patch0 -p1
cp %{SOURCE1} .

sed -i '/invoke/d' setup.cfg
rm -r tasks

%build
export LANG=en_US.UTF-8
%python_build

%install
export LANG=en_US.UTF-8
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8

# many tests need internet https://github.com/sarugaku/requirementslib/issues/145
# most tests are marked properly
skip_tests="needs_internet"
# unmarked but need internet
skip_tests+=" or test_get_local_ref"
skip_tests+=" or test_get_requirements"
skip_tests+=" or (test_convert_from_pipfile and requirement10)"
# unknown reason
skip_tests+=" or test_parse_function_call_as_name"
# no packaged test artifact
skip_tests+=" or test_ast_parser_handles_exceptions"
# https://github.com/sarugaku/requirementslib/issues/270
skip_tests+=" or test_no_duplicate_egg_info"
# increase test deadline for slow obs executions architectures (e.g. on s390x)
cat >> tests/conftest.py <<EOF

from hypothesis import settings
try:
    settings.register_profile("obs", deadline=1000)
except TypeError:
    settings.register_profile("obs", settings(deadline=1000))
EOF
%{python_expand PYTHON_VERSION=%{$python_version}
if [[ ${PYTHON_VERSION:0:1} -eq 3 ]]; then
  PYTHONPATH=%{buildroot}%{$python_sitelib} $python -m pytest tests -k "not ($skip_tests)" --hypothesis-profile=obs
fi}

%files %{python_files}
%doc CHANGELOG.rst README.rst docs/quickstart.rst
%license LICENSE LICENSE.boltons
%{python_sitelib}/requirementslib
%{python_sitelib}/requirementslib-%{version}-py*.egg-info

%changelog
