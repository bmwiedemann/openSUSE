#
# spec file
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif

%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif

Name:           python-jsonschema%{psuffix}
Version:        4.17.3
Release:        0
Summary:        An implementation of JSON-Schema validation for Python
License:        MIT
URL:            https://github.com/python-jsonschema/jsonschema
Source:         https://files.pythonhosted.org/packages/source/j/jsonschema/jsonschema-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module hatch-fancy-pypi-readme}
BuildRequires:  %{python_module hatch_vcs}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros >= 20210929
%if %{with test}
BuildRequires:  %{python_module Twisted}
BuildRequires:  %{python_module jsonschema = %{version}}
BuildRequires:  %{python_module jsonschema-format = %{version}}
BuildRequires:  %{python_module jsonschema-format-nongpl = %{version}}
BuildRequires:  git-core
%endif
Requires:       python-attrs >= 17.4.0
Requires:       python-pyrsistent >= 0.14.0
%if 0%{python_version_nodots} < 38
Requires:       python-importlib-metadata
Requires:       python-typing-extensions
%endif
%if 0%{python_version_nodots} < 39
Requires:       python-importlib-resources >= 1.4.0
Requires:       python-pkgutil-resolve-name >= 1.3.10
%endif
%if %{with libalternatives}
Requires:       alts
BuildRequires:  alts
%else
Requires(post): update-alternatives
Requires(preun):update-alternatives
%endif
BuildArch:      noarch
%python_subpackages

%description
jsonschema is an implementation of the JSON Schema specification for Python
The validator can be used as python module and from console:

    $ jsonschema --instance sample.json sample.schema

%package format
Summary:        An implementation of JSON-Schema validation for Python [format] extra
Requires:       python-fqdn
Requires:       python-idna
Requires:       python-isoduration
Requires:       python-jsonpointer > 1.13
Requires:       python-jsonschema = %{version}
Requires:       python-rfc3339-validator
Requires:       python-rfc3987
Requires:       python-uri_template
Requires:       python-webcolors >= 1.11

%description format
jsonschema is an implementation of the JSON Schema specification for Python.

This subpackage provides the [format] extra

%package format-nongpl
Summary:        An implementation of JSON-Schema validation for Python [format-nongpl] extra
Requires:       python-fqdn
Requires:       python-idna
Requires:       python-isoduration
Requires:       python-jsonpointer > 1.13
Requires:       python-jsonschema = %{version}
Requires:       python-rfc3339-validator
Requires:       python-rfc3986-validator > 0.1.0
Requires:       python-uri_template
Requires:       python-webcolors >= 1.11

%description format-nongpl
jsonschema is an implementation of the JSON Schema specification for Python.

This subpackage provides the [format-nongpl] extra

%prep
%setup -q -n jsonschema-%{version}

%if !%{with test}
%build
%pyproject_wheel

%install
%pyproject_install
# Remove benchmark tests
%{python_expand rm -r %{buildroot}%{$python_sitelib}/jsonschema/benchmarks %{buildroot}%{$python_sitelib}/jsonschema/tests
%fdupes %{buildroot}%{$python_sitelib}
}

# Prepare for libalternatives/update-alternatives usage
%python_clone -a %{buildroot}%{_bindir}/jsonschema
%endif

%if %{with test}
%check
export JSON_SCHEMA_TEST_SUITE=$PWD/json
%{python_expand # see tox.ini
export PYTHONPATH=%{buildroot}%{$python_sitelib}
$python -B -m twisted.trial jsonschema
}
%endif

%pre
# If libalternatives is used: Removing old update-alternatives entries.
%python_libalternatives_reset_alternative jsonschema

%post
%python_install_alternative jsonschema

%preun
%python_uninstall_alternative jsonschema

%if !%{with test}
%files %{python_files}
%license COPYING
%doc README.rst
%python_alternative %{_bindir}/jsonschema
%{python_sitelib}/jsonschema
%{python_sitelib}/jsonschema-%{version}*-info

%files %{python_files format}
%license COPYING

%files %{python_files format-nongpl}
%license COPYING
%endif

%changelog
