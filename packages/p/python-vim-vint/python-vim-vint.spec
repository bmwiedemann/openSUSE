#
# spec file for package python-vim-vint
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
%bcond_without python2
Name:           python-vim-vint
Version:        0.3.21
Release:        0
Summary:        Lint tool for Vim script Language
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Kuniwak/vint
Source:         https://github.com/Kuniwak/vint/archive/v%{version}.tar.gz
Patch0:         test-sys-executable.patch
BuildRequires:  %{python_module PyYAML >= 3.11}
BuildRequires:  %{python_module ansicolor >= 0.2.4}
BuildRequires:  %{python_module chardet >= 2.3.0}
BuildRequires:  %{python_module coverage >= 3.7.1}
BuildRequires:  %{python_module pathlib}
BuildRequires:  %{python_module pytest >= 2.6.4}
BuildRequires:  %{python_module pytest-cov >= 1.8.1}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML >= 3.11
Requires:       python-ansicolor >= 0.2.4
Requires:       python-chardet >= 2.3.0
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%if %{with python2}
BuildRequires:  python-enum34 >= 1.0.4
BuildRequires:  python-mock >= 1.0.1
BuildRequires:  python-typing >= 3.6.2
%endif
%ifpython2
Requires:       python-enum34 >= 1.0.4
Requires:       python-pathlib >= 1.0.1
Requires:       python-typing >= 3.6.2
%endif
%python_subpackages

%description
A lint tool for the Vim script Language.

%prep
%setup -q -n vint-%{version}
%patch0 -p1
sed -e 's/==/>=/g' \
    -e 's/\~=/>=/g' \
    -i setup.py \
    -i test-requirements.txt \
    -i requirements.txt
sed -i -e '/^#!\//, 1d' vint/_bundles/vimlparser.py

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/vint
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python setup.py test

%post
%python_install_alternative vint

%postun
%python_uninstall_alternative vint

%files %{python_files}
%license LICENSE.txt
%doc README.rst
%python_alternative %{_bindir}/vint
%{python_sitelib}/*

%changelog
