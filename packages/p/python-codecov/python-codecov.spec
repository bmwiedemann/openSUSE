#
# spec file for package python-codecov
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
Name:           python-codecov
Version:        2.1.9
Release:        0
Summary:        Hosted coverage reports
License:        Apache-2.0
URL:            https://github.com/codecov/codecov-python
Source:         https://files.pythonhosted.org/packages/source/c/codecov/codecov-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module requests >= 2.7.9}
# /SECTION
Requires:       python-coverage
Requires:       python-requests >= 2.7.9
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
Requires(post):   update-alternatives
Requires(postun):  update-alternatives

%python_subpackages

%description
Hosted coverage reports for Github, Bitbucket and Gitlab.

%prep
%setup -q -n codecov-%{version}
sed -i -e '/^#!\//, 1d' codecov/__init__.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/codecov

%post
%python_install_alternative codecov

%postun
%python_uninstall_alternative codecov

%files %{python_files}
%defattr(-,root,root,-)
%license LICENSE
%doc README.md
%python_alternative %{_bindir}/codecov
%{python_sitelib}/*

%changelog
