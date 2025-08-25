#
# spec file for package python-pygal
#
# Copyright (c) 2025 SUSE LLC and contributors
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
Name:           python-pygal
Version:        3.0.5
Release:        0
Summary:        A python svg graph plotting library
License:        LGPL-3.0-or-later
Group:          Development/Languages/Python
URL:            https://pygal.org/
Source:         https://files.pythonhosted.org/packages/source/p/pygal/pygal-%{version}.tar.gz
BuildRequires:  %{python_module CairoSVG}
BuildRequires:  %{python_module Flask}
BuildRequires:  %{python_module importlib-metadata}
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pyquery}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-importlib-metadata
Requires:       python-lxml
Recommends:     python-CairoSVG
BuildArch:      noarch
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Pygal is a dynamic SVG charting library written in python.
It supports various chart types and CSS styling.

%prep
%autosetup -p1 -n pygal-%{version}

# not sure where to report
sed -Ei 's:.pytest-runner.,?::' setup.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

mv %{buildroot}%{_bindir}/pygal_gen.py %{buildroot}%{_bindir}/pygal_gen
%python_clone -a %{buildroot}%{_bindir}/pygal_gen

%check
%pytest

%post
%python_install_alternative pygal_gen

%postun
%python_uninstall_alternative pygal_gen

%pre
%python_libalternatives_reset_alternative pygal_gen

%files %{python_files}
%doc README
%license COPYING
%python_alternative %{_bindir}/pygal_gen
%{python_sitelib}/pygal
%{python_sitelib}/pygal-%{version}.dist-info

%changelog
