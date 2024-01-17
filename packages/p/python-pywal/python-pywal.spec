#
# spec file for package python-pywal
#
# Copyright (c) 2021 SUSE LLC
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
Name:           python-pywal
Version:        3.3.0
Release:        0
Summary:        Generate and change color-schemes on the fly
License:        MIT
URL:            https://github.com/dylanaraps/pywal
Source:         https://files.pythonhosted.org/packages/source/p/pywal/pywal-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  ImageMagick
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Recommends:     ImageMagick
BuildArch:      noarch
%python_subpackages

%description
Generate and change color-schemes on the fly

%prep
%setup -q -n pywal-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/wal
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest

%post
%python_install_alternative wal

%postun
%python_uninstall_alternative wal

%files %{python_files}
%doc README.md
%license LICENSE.md
%python_alternative %{_bindir}/wal
%{python_sitelib}/*

%changelog
