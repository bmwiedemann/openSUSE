#
# spec file for package python-Babel
#
# Copyright (c) 2025 SUSE LLC
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


#
%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif

%define oldpython python
%{?sle15_python_module_pythons}
Name:           python-Babel
Version:        2.17.0
Release:        0
Summary:        Internationalization utilities
License:        BSD-3-Clause
URL:            https://babel.pocoo.org/
Source:         https://files.pythonhosted.org/packages/source/b/babel/babel-%{version}.tar.gz
BuildRequires:  %{python_module freezegun >= 1.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest >= 6.0}
BuildRequires:  %{python_module tzdata}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros >= 20210929
Requires:       python-tzdata
%if %{with libalternatives}
Requires:       alts
BuildRequires:  alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
BuildArch:      noarch
%ifpython2
Obsoletes:      %{oldpython}-babel < %{version}
Provides:       %{oldpython}-babel = %{version}
%endif
%if "%{python_flavor}" == "python3" || "%{?python_provides}" == "python3"
Provides:       python3-babel = %{version}
Obsoletes:      python3-babel < %{version}
%endif
%python_subpackages

%description
A collection of tools for internationalizing Python applications.

%prep
%autosetup -p1 -n babel-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/pybabel
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%pre
# Since /usr/bin/pybabel became ghosted to be used with update-alternatives, we have to get rid
# of the old binary resulting from the non-update-alternativies-ified package:
[ -h %{_bindir}/pybabel ] || rm -f %{_bindir}/pybabel
# If libalternatives is used: Removing old update-alternatives entries.
%python_libalternatives_reset_alternative pybabel

%post
%python_install_alternative pybabel

%postun
%python_uninstall_alternative pybabel

%files %{python_files}
%license LICENSE
%doc CHANGES.rst
%python_alternative %{_bindir}/pybabel
%{python_sitelib}/babel
%{python_sitelib}/babel-%{version}.dist-info

%changelog
