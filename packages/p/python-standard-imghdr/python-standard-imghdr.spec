#
# spec file for package python-standard-imghdr
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

# Removed in 3.13
%define skip_python311 1
%define skip_python312 1
Name:           python-standard-imghdr
Version:        3.13.0
Release:        0
Summary:        Standard library imghdr redistribution
License:        PSF-2.0
URL:            https://github.com/youknowone/python-deadlib
Source:         https://files.pythonhosted.org/packages/source/s/standard-imghdr/standard_imghdr-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 75.0}
BuildRequires:  %{python_module testsuite}
BuildRequires:  fdupes
BuildArch:      noarch
%python_subpackages

%description
Standard library imghdr redistribution. "dead battery".

%prep
%autosetup -p1 -n standard_imghdr-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Not yet available in 3.13.0, should be in the next release
# %%pyunittest -v tests

%files %{python_files}
%{python_sitelib}/imghdr
%{python_sitelib}/standard_imghdr-%{version}.dist-info

%changelog
