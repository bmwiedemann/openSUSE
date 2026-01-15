#
# spec file for package python-prance
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


%define openapispec_version 3.2.0
Name:           python-prance
Version:        25.4.8.0
Release:        0
Summary:        Resolving Swagger/OpenAPI parser
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/jfinkhaeuser/prance
Source0:        https://files.pythonhosted.org/packages/source/p/prance/prance-%{version}.tar.gz
Source1:        https://github.com/OAI/OpenAPI-Specification/archive/refs/tags/%{openapispec_version}.tar.gz#/OpenAPI-Specification-%{openapispec_version}.tar.gz
Source99:       python-prance.rpmlintrc
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML >= 5.1
Requires:       python-chardet >= 4.0
Requires:       python-requests >= 2.25
Requires:       python-semver >= 2.9
Requires:       python-six >= 1.15
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     python-click >= 7.0
Recommends:     python-openapi-spec-validator > 0.2
Recommends:     python-ruamel.yaml
Suggests:       python-PyICU >= 2.2
Suggests:       python-flex >= 6.13
Suggests:       python-swagger-spec-validator >= 2.4
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module PyICU}
BuildRequires:  %{python_module PyYAML >= 5.1}
BuildRequires:  %{python_module chardet >= 4.0}
BuildRequires:  %{python_module click >= 7.0}
BuildRequires:  %{python_module openapi-spec-validator > 0.2}
BuildRequires:  %{python_module pytest >= 4.2}
BuildRequires:  %{python_module requests >= 2.25}
BuildRequires:  %{python_module ruamel.yaml}
BuildRequires:  %{python_module semver >= 2.9}
BuildRequires:  %{python_module six >= 1.15}
BuildRequires:  %{python_module swagger-spec-validator >= 2.4}
# /SECTION
%python_subpackages

%description
Resolving Swagger/OpenAPI 2.0 and 3.0 Parser.

%prep
%setup -q -n prance-%{version}

# Add version metadata so egg-info is correct
sed -i 's/name = prance/name = prance\nversion = %{version}/' setup.cfg

# Remove pin on chardet
sed -i 's/,<5.0//' setup.cfg

# https://github.com/jfinkhaeuser/prance/issues/85
sed -i 's/~=/>=/' setup.cfg

# Avoid pytest-cov
sed -i '/addopts/d' setup.cfg

# Ignore prance.ValidationError: Version mismatch: selected backend "flex" does not support specified version 3.0.x!
# because it breaks other packages such as openapi3-fuzzer
sed -i 's/if parsed.0. not in versions:/if False:/' prance/__init__.py

cd tests
mkdir OpenAPI-Specification
cd OpenAPI-Specification
tar --strip-components=1 -xf %{SOURCE1}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/prance
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative prance

%postun
%python_uninstall_alternative prance

%check
%pytest -rs -k 'not requires_network'

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%python_alternative %{_bindir}/prance
%{python_sitelib}/prance
%{python_sitelib}/prance-%{version}*-info

%changelog
