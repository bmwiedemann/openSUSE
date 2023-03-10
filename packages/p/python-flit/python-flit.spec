#
# spec file for package python-flit
#
# Copyright (c) 2023 SUSE LLC
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


%define skip_python2 1
Name:           python-flit
Version:        3.8.0
Release:        0
Summary:        Simplified packaging of Python modules
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/pypa/flit
Source:         https://files.pythonhosted.org/packages/source/f/flit/flit-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.6}
BuildRequires:  %{python_module docutils}
BuildRequires:  %{python_module flit-core >= 3.8.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module tomli-w}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-docutils
Requires:       python-flit-core >= 3.8.0
Requires:       python-requests
Requires:       python-tomli-w
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest >= 2.7.3}
BuildRequires:  %{python_module responses}
BuildRequires:  %{python_module testpath}
BuildRequires:  %{python_module tomli}
# /SECTION
%python_subpackages

%description
Simplified packaging of Python modules

%prep
%setup -q -n flit-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/flit
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%{python_expand # create python name interpreter for test_find_python_excutable"
mkdir build/testbin
ln -s %{_bindir}/$python build/testbin/python
}
export PATH=$PWD/build/testbin/:$PATH
# test_invalid_classifier requires internet
# https://github.com/takluyver/flit/blob/96751efce651f8bae8ccb9e7f144dac460b3f013/flit/validate.py#L126
# "The error you get on a train, going through Oregon, without wifi"
%pytest -k "not test_invalid_classifier"

%post
%python_install_alternative flit

%postun
%python_uninstall_alternative flit

%files %{python_files}
%doc README.rst
%license LICENSE
%python_alternative %{_bindir}/flit
%{python_sitelib}/flit
%{python_sitelib}/flit-%{version}*-info

%changelog
