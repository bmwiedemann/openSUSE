#
# spec file for package python-wheezy.template
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
Name:           python-wheezy.template
Version:        0.1.195
Release:        0
Summary:        A lightweight template library
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/akornatskyy/wheezy.template
Source:         https://files.pythonhosted.org/packages/source/w/wheezy.template/wheezy.template-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Suggests:       python-mock
Suggests:       python-pytest
Suggests:       python-pytest-cov
Suggests:       python-pytest-pep8
BuildArch:      noarch
%python_subpackages

%description
A lightweight template library written in pure python.

%prep
%setup -q -n wheezy.template-%{version}

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/wheezy.template
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative wheezy.template

%postun
%python_uninstall_alternative wheezy.template

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/wheezy.template
%dir %{python_sitelib}/wheezy
%{python_sitelib}/wheezy/template
%{python_sitelib}/wheezy.template-%{version}*.pth
%{python_sitelib}/wheezy.template-%{version}*-info

%changelog
