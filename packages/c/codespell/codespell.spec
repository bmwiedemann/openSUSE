#
# spec file for package codespell
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


%define pythons python3
Name:           codespell
Version:        2.3.0
Release:        0
Summary:        Source code checker for common misspellings
License:        GPL-2.0-only
Group:          Development/Tools/Other
URL:            https://github.com/codespell-project/codespell/
Source0:        https://files.pythonhosted.org/packages/source/c/codespell/codespell-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-chardet
BuildRequires:  python3-pip
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-dependency
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-wheel
Requires:       python3-chardet
Requires:       python3-setuptools
BuildArch:      noarch

%description
codespell fixes common misspellings in text files. It primarily checks
misspelled words in source code, but it can be used with other files as well.

%prep
%autosetup -p1

# remove everything coverage-related
sed -i '/\-cov/ d' pyproject.toml

%build
%pyproject_wheel

%install
%pyproject_install
%fdupes %{buildroot}%{python3_sitelib}

%check
# disable command test; does not work in chroot
export PATH=$PATH:%{buildroot}%{_bindir}
%pytest -k 'not test_command'

%files
%license COPYING
%doc README.rst
%{_bindir}/codespell
%{python3_sitelib}/codespell_lib
%{python3_sitelib}/codespell-%{version}.dist-info

%changelog
