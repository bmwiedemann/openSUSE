#
# spec file for package python-requirementslib
#
# Copyright (c) 2021 SUSE LLC
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
# gh#sarugaku/requirementslib#288
%define skip_python39 1
%bcond_without python2
Name:           python-requirementslib
Version:        1.5.16
Release:        0
Summary:        A tool for converting between pip-style and pipfile requirements
License:        MIT
URL:            https://github.com/sarugaku/requirementslib
Source:         https://github.com/sarugaku/requirementslib/archive/%{version}.tar.gz#/requirementslib-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/mahmoud/boltons/master/LICENSE#/LICENSE.boltons
Source2:        https://raw.githubusercontent.com/pyinstaller/pyinstaller/develop/setup.py#/pyinstaller-setup.py
Patch0:         use-boltons.patch
BuildRequires:  %{python_module chardet}
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
Requires:       python-chardet
Requires:       python-distlib >= 0.2.8
Requires:       python-first
Requires:       python-orderedmultidict
Requires:       python-packaging >= 19.0
Requires:       python-pep517 >= 0.5.0
Requires:       python-pip-shims >= 0.5.2
Requires:       python-plette
Requires:       python-requests
Requires:       python-setuptools >= 40.8
Requires:       python-six >= 1.11.0
Requires:       python-tomlkit >= 0.5.3
Requires:       python-vistir >= 0.3.1
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
BuildRequires:  %{python_module chardet}
BuildRequires:  %{python_module dateutil}
BuildRequires:  %{python_module distlib >= 0.2.8}
BuildRequires:  %{python_module first}
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module orderedmultidict}
BuildRequires:  %{python_module packaging >= 0.19.0}
BuildRequires:  %{python_module pep517 >= 0.5.0}
BuildRequires:  %{python_module pip-shims >= 0.5.2}
BuildRequires:  %{python_module plette}
BuildRequires:  %{python_module pytest-timeout}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module six >= 1.11.0}
BuildRequires:  %{python_module tomlkit >= 0.5.3}
BuildRequires:  %{python_module twine}
BuildRequires:  %{python_module vistir >= 0.3.1}
%if %{with python2}
BuildRequires:  python-backports.tempfile
BuildRequires:  python-scandir
BuildRequires:  python-typing
%endif
BuildRequires:  git-core
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

# Avoid failure during build
sed -i '/invoke/d' setup.cfg

# It is unclear whether this modified assertion is sufficient.
# https://github.com/sarugaku/requirementslib/issues/279
cp %{SOURCE2} tests/artifacts/git/pyinstaller/setup.py
sed -i 's/assert "altgraph" in result\["install_requires"\]/assert "setuptools >= 39.2.0" in result["setup_requires"]/' tests/unit/test_setup_info.py

%build
export LANG=en_US.UTF-8
%python_build

%install
export LANG=en_US.UTF-8
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8

# many tests need internet gh#sarugaku/requirementslib#145
# most tests are marked properly
skip_tests="needs_internet"

# depends on access to https://github.com/benjaminp/six.git
skip_tests+=" or test_get_local_ref"

# depends on access to https://github.com/jazzband/tablib/archive/v0.12.1.zip
skip_tests+=" or test_get_requirements"

# Rapptz is marker for https://github.com/Rapptz/discord.py
skip_tests+=" or (test_convert_from_pipfile and Rapptz)"

# gh#sarugaku/requirementslib#280
skip_tests+=" or test_parse_function_call_as_name"

# gh#sarugaku/requirementslib#270
skip_tests+=" or test_no_duplicate_egg_info"

# gh#sarugaku/requirementslib#303
skip_tests+=" or test_parse_function_call_as_name or test_repo_line or test_requirement_line"
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
