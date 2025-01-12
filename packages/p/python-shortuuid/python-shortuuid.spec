#
# spec file for package python-shortuuid
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


%{?sle15_python_module_pythons}
Name:           python-shortuuid
Version:        1.0.13
Release:        0
Summary:        A generator library for concise, unambiguous and URL-safe UUIDs
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/stochastic-technologies/shortuuid/
Source:         https://files.pythonhosted.org/packages/source/s/shortuuid/shortuuid-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
Requires:       python-base
BuildArch:      noarch
%python_subpackages

%description
A library that generates short, pretty, unambiguous unique IDs
by using an extensive, case-sensitive alphabet and omitting
similar-looking letters and numbers.

%prep
%setup -q -n shortuuid-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/shortuuid
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative shortuuid

%postun
%python_uninstall_alternative shortuuid

%files %{python_files}
%doc README.md
%license COPYING
%python_alternative %{_bindir}/shortuuid
%{python_sitelib}/shortuuid
%{python_sitelib}/shortuuid-%{version}.dist-info

%changelog
