#
# spec file for package python-gear
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-gear
Version:        0.14.0
Release:        0
Summary:        Pure Python Async Gear Protocol Library
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/openstack-infra/gear
Source:         https://files.pythonhosted.org/packages/source/g/gear/gear-%{version}.tar.gz
BuildRequires:  %{python_module extras}
BuildRequires:  %{python_module fixtures >= 0.3.12}
BuildRequires:  %{python_module pbr >= 1.8.0}
BuildRequires:  %{python_module pyOpenSSL}
BuildRequires:  %{python_module python-daemon >= 2.0.4}
BuildRequires:  %{python_module python-subunit}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six >= 1.5.2}
BuildRequires:  %{python_module testrepository >= 0.0.13}
BuildRequires:  %{python_module testresources}
BuildRequires:  %{python_module testscenarios}
BuildRequires:  %{python_module testtools >= 0.9.27}
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

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/geard

%check
%python_expand $python -m unittest discover

%post
%python_install_alternative geard

%postun
%python_uninstall_alternative geard

%files %{python_files}
%license LICENSE
%doc README.rst ChangeLog AUTHORS
%{python_sitelib}/*
%python_alternative %{_bindir}/geard

%changelog
