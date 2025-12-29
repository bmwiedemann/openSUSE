#
# spec file for package python-mailman-hyperkitty
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


# Always only build one flavor
%if 0%{?sle_version} && 0%{?sle_version} < 160000
%{?sle15_python_module_pythons}
%elif %{defined primary_python}
%define pythons %{primary_python}
%else
%define pythons python3
%endif
%global mypython %pythons
%global mypython_sitelib %{expand:%%{%{mypython}_sitelib}}

Name:           python-mailman-hyperkitty
Version:        1.2.1
Release:        0
Summary:        Mailman archiver plugin for HyperKitty
License:        GPL-3.0-only
URL:            https://gitlab.com/mailman/mailman-hyperkitty/
Source:         https://files.pythonhosted.org/packages/source/m/mailman-hyperkitty/mailman-hyperkitty-%{version}.tar.gz
# https://gitlab.com/mailman/mailman-hyperkitty/-/issues/28
Patch0:         python-mailman-hyperkitty-fix-archiver-test.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  (mailman3 >= 3.3.5 with %{mypython}-mailman3)
BuildRequires:  %{python_module nose2}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module zope.interface}
# /SECTION

%description
Mailman archiver plugin for HyperKitty

%package -n %{mypython}-mailman-hyperkitty
Summary:        Mailman archiver plugin for HyperKitty
Requires:       %{mypython}-requests
Requires:       %{mypython}-zope.interface
Requires:       (mailman3 >= 3.3.5 with %{mypython}-mailman3)

%description -n %{mypython}-mailman-hyperkitty
Mailman archiver plugin for HyperKitty

%prep
%autosetup -n mailman-hyperkitty-%{version} -p1

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python -m nose2 -v

%files -n %{mypython}-mailman-hyperkitty
%doc README.rst mailman-hyperkitty.cfg
%license LICENSE.txt
%{mypython_sitelib}/mailman_hyperkitty
%{mypython_sitelib}/mailman_hyperkitty-%{version}.dist-info

%changelog
