#
# spec file for package python-ytmusicapi
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


%{?sle15_python_module_pythons}
Name:           python-ytmusicapi
Version:        1.10.1
Release:        0
Summary:        Unofficial API for YouTube Music
License:        MIT
URL:            https://github.com/sigma67/ytmusicapi
Source:         https://files.pythonhosted.org/packages/source/y/ytmusicapi/ytmusicapi-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 65}
BuildRequires:  %{python_module setuptools_scm >= 7}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-requests >= 2.22
Requires(post): update-alternatives
Requires(preun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Unofficial API for YouTube Music

%prep
%autosetup -p1 -n ytmusicapi-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/ytmusicapi
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Requires network access
# %%pytest

%post
%python_install_alternative ytmusicapi

%postun
%python_uninstall_alternative ytmusicapi

%files %{python_files}
%doc README.rst
%license LICENSE
%python_alternative %{_bindir}/ytmusicapi
%{python_sitelib}/ytmusicapi
%{python_sitelib}/ytmusicapi-%{version}.dist-info

%changelog
