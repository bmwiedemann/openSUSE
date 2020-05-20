#
# spec file for package python-technicolor
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
Name:           python-technicolor
Version:        2017.1.16.1544
Release:        0
Summary:        Python package for logging in colour
License:        GPL-3.0-only
Group:          Development/Languages/Python
URL:            https://github.com/wdbm/technicolor
Source:         https://files.pythonhosted.org/packages/source/t/technicolor/technicolor-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-setuptools
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Technicolor provides logging in colour and logging of function usage by
means of a decorator.

%prep
%setup -q -n technicolor-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/technicolor
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# no testsuite found

%post
%python_install_alternative technicolor

%postun
%python_uninstall_alternative technicolor

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/technicolor
%{python_sitelib}/*

%changelog
