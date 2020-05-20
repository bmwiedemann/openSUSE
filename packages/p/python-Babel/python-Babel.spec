#
# spec file for package python-Babel
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
%define oldpython python
Name:           python-Babel
Version:        2.8.0
Release:        0
Summary:        Internationalization utilities
License:        BSD-3-Clause
URL:            http://babel.pocoo.org/
Source:         https://files.pythonhosted.org/packages/source/B/Babel/Babel-%{version}.tar.gz
Patch0:         python383.patch
BuildRequires:  %{python_module freezegun}
BuildRequires:  %{python_module py >= 1.4.14}
BuildRequires:  %{python_module pytest >= 2.3.5}
BuildRequires:  %{python_module pytz >= 2015.7}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pytz >= 2015.7
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%ifpython2
Obsoletes:      %{oldpython}-babel < %{version}
Provides:       %{oldpython}-babel = %{version}
%endif
%ifpython3
Provides:       python3-babel = %{version}
Obsoletes:      python3-babel < %{version}
%endif
%python_subpackages

%description
A collection of tools for internationalizing Python applications.

%prep
%setup -q -n Babel-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/pybabel
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%pre
# Since /usr/bin/pybabel became ghosted to be used with update-alternatives, we have to get rid
# of the old binary resulting from the non-update-alternativies-ified package:
[ -h %{_bindir}/pybabel ] || rm -f %{_bindir}/pybabel

%post
%python_install_alternative pybabel

%postun
%python_uninstall_alternative pybabel

%files %{python_files}
%license LICENSE
%doc CHANGES
%python_alternative %{_bindir}/pybabel
%{python_sitelib}/babel
%{python_sitelib}/Babel-%{version}-py%{python_version}.egg-info

%changelog
