#
# spec file for package python-pyVows
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
Name:           python-pyVows
Version:        3.0.0
Release:        0
Summary:        BDD test engine based on Vows.js
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/heynemann/pyvows
Source:         https://files.pythonhosted.org/packages/source/p/pyVows/pyVows-%{version}.tar.gz
BuildRequires:  %{python_module Unidecode}
BuildRequires:  %{python_module colorama >= 0.3.7}
BuildRequires:  %{python_module gevent >= 0.13.6}
BuildRequires:  %{python_module preggy >= 0.5.8}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Unidecode
Requires:       python-gevent >= 1.2.2
Requires:       python-preggy >= 1.3.0
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     python-colorama >= 0.3.7
BuildArch:      noarch
%python_subpackages

%description
pyVows is a BDD test engine based on Vows.js <http://vowsjs.org>.

%prep
%setup -q -n pyVows-%{version}
sed -i '/^#!/d' pyvows/__main__.py pyvows/cli.py

%build
export LANG="en_US.UTF-8"
%python_build

%install
export LANG="en_US.UTF-8"
%python_install
%python_clone -a %{buildroot}%{_bindir}/pyvows
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG="en_US.UTF-8"
export PYTHONPATH=.
export PATH=%{buildroot}%{_bindir}:$PATH
%python_exec pyvows/cli.py -x tests/

%post
%python_install_alternative pyvows

%postun
%python_uninstall_alternative pyvows

%files %{python_files}
%python_alternative %{_bindir}/pyvows
%{python_sitelib}/*

%changelog
