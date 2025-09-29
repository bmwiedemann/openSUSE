#
# spec file for package python-python-dotenv
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


# rubygem-dotenv also provides executable dotenv
%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif
%{?sle15_python_module_pythons}
Name:           python-python-dotenv
Version:        1.1.1
Release:        0
Summary:        Python library for .env support
License:        BSD-3-Clause
URL:            https://github.com/theskumar/python-dotenv
Source:         https://github.com/theskumar/python-dotenv/archive/v%{version}.tar.gz#/python-dotenv-%{version}.tar.gz
# PATCH-FIX-OPENSUSE Avoid upstream click 8.2 bug -- gh#pallets/click#2913
Patch0:         avoid-click-8.2-bug.patch
BuildRequires:  %{python_module click >= 5.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest >= 3.0.5}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module sh >= 2.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
Requires:       python-click >= 5.0
Suggests:       python-jupyter_ipython
# There is a very similar Python package which also used `dotenv` namespace
Conflicts:      python-dotenv
BuildArch:      noarch
%python_subpackages

%description
Add .env support to your Django/Flask apps in development and deployments.

%prep
%autosetup -p1 -n python-dotenv-%{version}

%build
export LANG=C.UTF-8
%pyproject_wheel

%install
export LANG=C.UTF-8
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/dotenv
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=C.UTF-8
mv %{buildroot}%{_bindir}/dotenv %{buildroot}%{_bindir}/dotenv.orig
# CLI tests require distribution to be found, and the correct executable installed
export PATH=%{buildroot}%{_bindir}:$PATH
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitelib}
cp %{buildroot}%{_bindir}/dotenv-%{$python_bin_suffix} %{buildroot}%{_bindir}/dotenv
# ipython is optional and only available for python >= 3.7 in Tumbleweed
$python -m pytest -v -k "not ipython"
}
mv %{buildroot}%{_bindir}/dotenv.orig %{buildroot}%{_bindir}/dotenv

%pre
%python_libalternatives_reset_alternative dotenv

%post
%python_install_alternative dotenv

%postun
%python_uninstall_alternative dotenv

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/dotenv
%{python_sitelib}/dotenv/
%{python_sitelib}/python_dotenv-%{version}.dist-info

%changelog
