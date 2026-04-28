#
# spec file for package python-striprtf
#
# Copyright (c) 2026 SUSE LLC and contributors
# Copyright (c) 2024-2026, Martin Hauke <mardnh@gmx.de>
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


%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif
Name:           python-striprtf
Version:        0.0.32
Release:        0
Summary:        A simple library to convert rtf to text
License:        BSD-3-Clause
URL:            https://github.com/joshy/striprtf
Source:         https://github.com/joshy/striprtf/archive/refs/tags/v%{version}.tar.gz#/striprtf-%{version}.tar.gz
BuildRequires:  %{python_module hatchling >= 1.21.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest >= 7.0.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
%python_subpackages

%description
A simple library to convert rtf to text.

%prep
%autosetup -p1 -n striprtf-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/striprtf
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative striprtf

%postun
%python_uninstall_alternative striprtf

%pre
%python_libalternatives_reset_alternative striprtf

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.md
%python_alternative %{_bindir}/striprtf
%{python_sitelib}/striprtf
%{python_sitelib}/striprtf-%{version}.dist-info

%changelog
