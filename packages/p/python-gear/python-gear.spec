#
# spec file for package python-gear
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


Name:           python-gear
Version:        0.16.0
Release:        0
Summary:        Pure Python Async Gear Protocol Library
License:        Apache-2.0
URL:            https://opendev.org/opendev/gear
Source:         https://files.pythonhosted.org/packages/source/g/gear/gear-%{version}.tar.gz
BuildRequires:  %{python_module extras}
BuildRequires:  %{python_module fixtures >= 0.3.12}
BuildRequires:  %{python_module pbr >= 1.8.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pyOpenSSL}
BuildRequires:  %{python_module python-daemon >= 2.0.4}
BuildRequires:  %{python_module python-subunit}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six >= 1.5.2}
BuildRequires:  %{python_module testrepository >= 0.0.13}
BuildRequires:  %{python_module testresources}
BuildRequires:  %{python_module testscenarios}
BuildRequires:  %{python_module testtools >= 0.9.27}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-extras
Requires:       python-pbr >= 1.8.0
Requires:       python-python-daemon >= 2.0.4
Requires:       python-six >= 1.5.2
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
A pure-Python asynchronous library to interface with Gearman.

%prep
%setup -q -n gear-%{version}
%if 0%{?sle_version} <= 150600
# Remove project url in setup.cfg, this conf fails with old python
sed -i '9,13d' setup.cfg
%endif

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/geard

%check
%pyunittest discover -v

%post
%python_install_alternative geard

%postun
%python_uninstall_alternative geard

%files %{python_files}
%license LICENSE
%doc README.rst ChangeLog AUTHORS
%{python_sitelib}/gear
%{python_sitelib}/gear-%{version}.dist-info
%python_alternative %{_bindir}/geard

%changelog
