#
# spec file for package python-template-remover
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-template-remover
Version:        0.1.9
Release:        0
License:        Apache-2.0
Summary:        Remove the template markup from html files
Url:            http://github.com/deezer/template-remover
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/t/template-remover/template-remover-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/deezer/template-remover/master/LICENSE
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module docopt >= 0.6.1}
BuildRequires:  %{python_module nose >= 1.3}
Requires:       python-docopt >= 0.6.1
BuildArch:      noarch

%python_subpackages

%description
Template remover is a tool to remove the PHP and Jinja markup from HTML files.

Many tools, like html tidy, are designed to parse and analyze html files,
however they do not play well when there is language markup. This projects aims
to be a simple way of getting rid of those markups.

%prep
%setup -q -n template-remover-%{version}
cp %SOURCE1 .

%build
%python_build

%install
%python_install
mv %{buildroot}%{_bindir}/remove_template.py %{buildroot}%{_bindir}/remove_template
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec -R setup.py nosetests

%files %{python_files}
%license LICENSE
%doc README.rst
%python3_only %{_bindir}/remove_template
%{python_sitelib}/*

%changelog
