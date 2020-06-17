#
# spec file for package python-python-dotenv
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
Name:           python-python-dotenv
Version:        0.13.0
Release:        0
Summary:        Python library for .env support
License:        BSD-3-Clause
URL:            https://github.com/theskumar/python-dotenv
Source:         https://github.com/theskumar/python-dotenv/archive/v%{version}.tar.gz#/python-dotenv-%{version}.tar.gz
BuildRequires:  %{python_module click >= 5.0}
BuildRequires:  %{python_module jupyter_ipython}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest >= 3.0.5}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module sh >= 1.09}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-click >= 5.0
# rubygem-dotenv also provides executable dotenv
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     python-jupyter_ipython
# There is a very similar Python package which also used `dotenv` namespace
Conflicts:      python-dotenv
BuildArch:      noarch
%python_subpackages

%description
Add .env support to your Fjango/Flask apps in development and deployments.

%prep
%setup -q -n python-dotenv-%{version}

%build
export LANG=C.UTF-8
%python_build

%install
export LANG=C.UTF-8
%python_install
%python_clone -a %{buildroot}%{_bindir}/dotenv
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=C.UTF-8
mv %{buildroot}%{_bindir}/dotenv %{buildroot}%{_bindir}/dotenv.orig
# CLI tests require distribution to be found, and the correct executable installed
export PATH=%{buildroot}%{_bindir}:$PATH
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitelib}
cp %{buildroot}%{_bindir}/dotenv-%{$python_bin_suffix} %{buildroot}%{_bindir}/dotenv
$python -m pytest -v
}
mv %{buildroot}%{_bindir}/dotenv.orig %{buildroot}%{_bindir}/dotenv

%post
%python_install_alternative dotenv

%postun
%python_uninstall_alternative dotenv

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/dotenv
%{python_sitelib}/*

%changelog
