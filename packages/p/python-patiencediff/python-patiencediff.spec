#
# spec file for package python-patiencediff
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


%bcond_without libalternatives
Name:           python-patiencediff
Version:        0.2.18
Release:        0
Summary:        Python implementation of the patiencediff algorithm
License:        GPL-2.0-or-later
Group:          Development/Languages/Python
URL:            https://github.com/breezy-team/patiencediff
Source0:        https://files.pythonhosted.org/packages/source/p/patiencediff/patiencediff-%{version}.tar.gz
Source1:        vendor.tar.xz
BuildRequires:  %{python_module devel >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module setuptools-rust}
BuildRequires:  %{python_module wheel}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       alts
%python_subpackages

%description
Python implementation of the patiencediff algorithm.

%prep
%setup -q -n patiencediff-%{version} -a1

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}
%python_clone -a %{buildroot}%{_bindir}/patiencediff

%pre
%python_libalternatives_reset_alternative patiencediff

%check
%pytest

%files %{python_files}
%doc AUTHORS README.rst
%license COPYING
%python_alternative %{_bindir}/patiencediff
%{python_sitearch}/patiencediff
%{python_sitearch}/patiencediff-%{version}*-info

%changelog
