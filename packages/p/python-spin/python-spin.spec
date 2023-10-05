#
# spec file for package python-spin
#
# Copyright (c) 2023 SUSE LLC
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


Name:           python-spin
Version:        0.7
Release:        0
Summary:        Developer tool for scientific Python libraries
License:        BSD-3-Clause
URL:            https://github.com/scientific-python/spin
Source:         https://files.pythonhosted.org/packages/source/s/spin/spin-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
# SECTION test requirements
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Requires:       python-click
%if 0%{?python_version_nodots} < 311
Requires:       python-tomli
%endif
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Developer tool for scientific Python libraries

%prep
%autosetup -p1 -n spin-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/spin
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative spin

%postun
%python_uninstall_alternative spin

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/spin
%{python_sitelib}/spin
%{python_sitelib}/spin-%{version}.dist-info

%changelog
