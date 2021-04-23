#
# spec file for package python-sadisplay
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
Name:           python-sadisplay
Version:        0.4.9
Release:        0
Summary:        SqlAlchemy schema display script
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://bitbucket.org/estin/sadisplay
Source:         https://files.pythonhosted.org/packages/source/s/sadisplay/sadisplay-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-SQLAlchemy >= 0.5
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
SqlAlchemy schema display script

%prep
%setup -q -n sadisplay-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/sadisplay
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative sadisplay

%postun
%python_uninstall_alternative sadisplay

%files %{python_files}
%doc README.rst
%license LICENSE
%python_alternative %{_bindir}/sadisplay
%{python_sitelib}/*

%changelog
