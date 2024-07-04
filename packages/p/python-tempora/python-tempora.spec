#
# spec file for package python-tempora
#
# Copyright (c) 2024 SUSE LLC
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
Name:           python-tempora
Version:        5.6.0
Release:        0
Summary:        Objects and routines pertaining to date and time (tempora)
License:        MIT
URL:            https://github.com/jaraco/tempora
Source:         https://files.pythonhosted.org/packages/source/t/tempora/tempora-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module freezegun}
BuildRequires:  %{python_module jaraco.functools >= 1.20}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest > 4.6}
BuildRequires:  %{python_module pytest-freezegun}
BuildRequires:  %{python_module setuptools  >= 56}
BuildRequires:  %{python_module setuptools_scm >= 3.4.1}
BuildRequires:  %{python_module toml}
BuildRequires:  %{python_module tzdata}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros >= 20210929
Requires:       python-jaraco.functools >= 1.20
Requires:       python-tzdata
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
Objects and routines pertaining to date and time (tempora)

Modules include:
* tempora (top level package module) contains miscellaneous utilities and constants.
* timing contains routines for measuring and profiling.
* schedule contains an event scheduler.

%prep
%setup -q -n tempora-%{version}
sed -i '/--mypy/d' pytest.ini

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/calc-prorate
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
sed -i -e 's:--black::' -e 's:--cov::' -e 's/--flake8//g' pytest.ini
# https://github.com/jaraco/tempora/issues/22
donttest="tempora.parse_timedelta"
%pytest -k "not $donttest"

%pre
# If libalternatives is used: Removing old update-alternatives entries.
%python_libalternatives_reset_alternative calc-prorate

%post
%python_install_alternative calc-prorate

%postun
%python_uninstall_alternative calc-prorate

%files %{python_files}
%license LICENSE
%doc NEWS.rst README.rst docs/*rst
%python_alternative %{_bindir}/calc-prorate
%{python_sitelib}/tempora
%{python_sitelib}/tempora-%{version}.dist-info

%changelog
