#
# spec file for package python-python-on-whales
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

Name:           python-python-on-whales
Version:        0.67.0
Release:        0
Summary:        A Docker client for Python, designed to be fun and intuitive!
License:        MIT
URL:            https://github.com/gabrieldemarmiesse/python-on-whales
Source:         https://files.pythonhosted.org/packages/source/p/python-on-whales/python-on-whales-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pydantic >= 1.9
Requires:       python-requests
Requires:       python-tqdm
Requires:       python-typer >= 0.4.1
Requires:       python-typing_extensions
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pydantic >= 1.9}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module tqdm}
BuildRequires:  %{python_module typer >= 0.4.1}
BuildRequires:  %{python_module typing_extensions}
# /SECTION
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
%python_subpackages

%description
A Docker client for Python, designed to be fun and intuitive!

%prep
%autosetup -p1 -n python-on-whales-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/python-on-whales

# avoid installing tests
%python_expand rm -rf %{buildroot}%{$python_sitelib}/tests/python_on_whales  %{buildroot}%{$python_sitelib}/docs
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# tests require a running docker instance
#pytest

%pre
%python_reset_alternative python-on-whales

%post
%python_install_alternative python-on-whales

%postun
%python_uninstall_alternative python-on-whales

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/python-on-whales
%{python_sitelib}/python_on_whales
%{python_sitelib}/python_on_whales-%{version}.dist-info

%changelog
