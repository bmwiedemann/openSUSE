#
# spec file for package python-gscholar
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


Name:           python-gscholar
Version:        2.1.0
Release:        0
Summary:        Python library to query Google Scholar
License:        MIT
URL:            https://github.com/venthur/gscholar
Source0:        https://files.pythonhosted.org/packages/source/g/gscholar/gscholar-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
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
This package provides a python package and CLI to query google scholar
and get references in various formats (e.g. bibtex, endnote, etc.)

%prep
%setup -q -n gscholar-%{version}

sed -i -e '/^#!\//, 1d' gscholar/gscholar.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/gscholar
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# only 3 tests are available on the github tar-ball
# but most need a network connection to google scholar
# so we skip the tests here.

%post
%python_install_alternative gscholar

%postun
%python_uninstall_alternative gscholar

%files %{python_files}
%license LICENSE
%doc README.md CHANGELOG.md
%{python_sitelib}/gscholar
%{python_sitelib}/gscholar-%{version}.dist-info
%python_alternative %{_bindir}/gscholar

%changelog
