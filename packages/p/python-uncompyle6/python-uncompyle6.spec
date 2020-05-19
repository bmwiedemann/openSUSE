#
# spec file for package python-uncompyle6
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
Name:           python-uncompyle6
Version:        3.6.5
Release:        0
Summary:        Python cross-version byte-code decompiler
License:        GPL-3.0-only
Group:          Development/Languages/Python
URL:            https://github.com/rocky/python-uncompyle6/
Source:         https://files.pythonhosted.org/packages/source/u/uncompyle6/uncompyle6-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-hypothesis >= 2.0.0
Requires:       python-setuptools
Requires:       python-spark_parser >= 1.8.7
Requires:       python-xdis >= 4.2.2
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module hypothesis >= 2.0.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module spark_parser >= 1.8.7}
BuildRequires:  %{python_module xdis >= 4.2.2}
# /SECTION
%python_subpackages

%description
A native Python cross-version decompiler and fragment decompiler.
The successor to decompyle, uncompyle, and uncompyle2.

%prep
%setup -q -n uncompyle6-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/pydisassemble
%python_clone -a %{buildroot}%{_bindir}/uncompyle6
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest pytest

%post
%python_install_alternative pydisassemble
%python_install_alternative uncompyle6

%postun
%python_uninstall_alternative pydisassemble
%python_uninstall_alternative uncompyle6

%files %{python_files}
%license COPYING
%doc ChangeLog README README.rst
%python_alternative %{_bindir}/uncompyle6
%python_alternative %{_bindir}/pydisassemble
%{python_sitelib}/*

%changelog
