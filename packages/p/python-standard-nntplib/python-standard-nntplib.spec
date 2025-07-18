#
# spec file for package python-standard-nntplib
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


%if 0%{?suse_version} >= 1550
# Keep in sync with the main version for mailman
%global pythons python313
%else
%{?sle15_python_module_pythons}
%endif
Name:           python-standard-nntplib
Version:        3.13.0
Release:        0
Summary:        Standard library nntplib redistribution. "dead battery"
License:        PSF-2.0
URL:            https://github.com/youknowone/python-deadlib
Source:         https://files.pythonhosted.org/packages/source/s/standard-nntplib/standard_nntplib-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools >= 75.0}
BuildRequires:  %{python_module testsuite}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Standard library nntplib redistribution. "dead battery".

%prep
%autosetup -p1 -n standard_nntplib-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
donttest="test_starttls"
%pytest -k "not ($donttest)"

%files %{python_files}
%{python_sitelib}/nntplib
%{python_sitelib}/standard_nntplib-%{version}.dist-info

%changelog
