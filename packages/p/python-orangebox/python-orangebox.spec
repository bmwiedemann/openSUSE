#
# spec file for package python-orangebox
#
# Copyright (c) 2022 SUSE LLC
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
%define         skip_python2 1
%define         skip_python36 1
Name:           python-orangebox
Version:        0.2.0
Release:        0
Summary:        Betaflight blackbox flight recorder parser
License:        GPL-3.0-or-later
Group:          Development/Languages/Python
URL:            https://github.com/atomgomba/orangebox
#!RemoteAssetUrl: git+https://github.com/atomgomba/orangebox#v0.2.0
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Betaflight blackbox recording tooling. It provides a CLI tool and
also python modules.

%prep
%autosetup -p1 -n orangebox -c -T

cp -a %{_sourcedir}/orangebox/* .

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/bb2csv
%python_clone -a %{buildroot}%{_bindir}/bbsplit
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative bb2csv
%python_install_alternative bbsplit

%postun
%python_uninstall_alternative bb2csv
%python_uninstall_alternative bbsplit

%files %{python_files}
%python_alternative %{_bindir}/bb2csv
%python_alternative %{_bindir}/bbsplit
%{python_sitelib}/orangebox
%{python_sitelib}/orangebox-%{version}*-info

%changelog
