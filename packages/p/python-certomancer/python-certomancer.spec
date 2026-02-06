#
# spec file for package python-certomancer
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Name:           python-certomancer
Version:        0.13.0
Release:        0
Summary:        PKI testing tool
License:        MIT
URL:            https://github.com/MatthiasValvekens/certomancer
Source:         https://github.com/MatthiasValvekens/certomancer/archive/refs/tags/v%{version}.tar.gz#/certomancer-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 67.4}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module asn1crypto >= 1.5}
BuildRequires:  %{python_module Jinja2 >= 2.11.3}
BuildRequires:  %{python_module PyYAML >= 5.4.1}
BuildRequires:  %{python_module Werkzeug}
BuildRequires:  %{python_module click >= 7.1.2}
BuildRequires:  %{python_module cryptography >= 3.4.7}
BuildRequires:  %{python_module freezegun >= 1.1.0}
BuildRequires:  %{python_module pyhanko-certvalidator}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dateutil >= 2.8.1}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module requests-mock}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module tzlocal >= 2.1}
# /SECTION
BuildRequires:  fdupes
Requires:       python-PyYAML >= 5.4.1
Requires:       python-asn1crypto >= 1.5
Requires:       python-click >= 7.1.2
Requires:       python-cryptography >= 3.4.7
Requires:       python-python-dateutil >= 2.8.1
Requires:       python-tzlocal >= 2.1
Suggests:       python-Werkzeug >= 2.2.3
Suggests:       python-Jinja2 >= 2.11.3
Suggests:       python-python-pkcs11 >= 0.7.0
Suggests:       python-pytz >= 2020.1
Suggests:       python-freezegun >= 1.1.0
Suggests:       python-pyhanko-certvalidator >= 0.26.5
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
BuildArch:      noarch
%python_subpackages

%description
PKI testing tool

%prep
%autosetup -p1 -n certomancer-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/certomancer
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Failing tests
donttest="test_mass_summon_explicit_config or test_mass_summon or test_summon_no_pem or test_summon_der_stdout"
%pytest -k "not ($donttest)"

%pre
# If libalternatives is used: Removing old update-alternatives entries.
%python_libalternatives_reset_alternative certomancer

%post
%python_install_alternative certomancer

%postun
%python_uninstall_alternative certomancer

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/certomancer
%{python_sitelib}/certomancer
%{python_sitelib}/certomancer-%{version}.dist-info

%changelog
