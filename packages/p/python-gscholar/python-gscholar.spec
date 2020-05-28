#
# spec file for package python-gscholar
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
Name:           python-gscholar
Version:        1.6.1
Release:        0
Summary:        Python library to query Google Scholar
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/venthur/gscholar
Source0:        https://files.pythonhosted.org/packages/source/g/gscholar/gscholar-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
This package provides a python package and CLI to query google scholar
and get references in various formats (e.g. bibtex, endnote, etc.)

%prep
%setup -q -n gscholar-%{version}

sed -i -e '/^#!\//, 1d' gscholar/__main__.py
sed -i -e '/^#!\//, 1d' gscholar/gscholar.py

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/gscholar
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative gscholar

%postun
%python_uninstall_alternative gscholar

%files %{python_files}
%license LICENSE
%doc README.md CHANGELOG.md
%{python_sitelib}/*
%python_alternative %{_bindir}/gscholar

%changelog
