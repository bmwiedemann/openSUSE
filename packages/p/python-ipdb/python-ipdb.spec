#
# spec file for package python-ipdb
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-ipdb
Version:        0.12.2
Release:        0
Summary:        IPython-enabled pdb
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/gotcha/ipdb
Source:         https://files.pythonhosted.org/packages/source/i/ipdb/ipdb-%{version}.tar.gz
BuildRequires:  %{python_module ipython >= 5.1}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
Provides:       python-jupyter_ipdb = %{version}
Obsoletes:      python-jupyter_ipdb < %{version}
BuildArch:      noarch
%ifpython3
Provides:       jupyter-ipdb = %{version}
%endif
%python_subpackages

%description
ipdb exports functions to access the IPython_ debugger, which features
tab completion, syntax highlighting, better tracebacks, better
introspection with the same interface as the `pdb` module.

%prep
%setup -q -n ipdb-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
mv -v %{buildroot}%{_bindir}/ipdb{,-%{python2_bin_suffix}}
mv -v %{buildroot}%{_bindir}/ipdb{3,-%{python3_bin_suffix}}
%prepare_alternative ipdb

%post
%python_install_alternative ipdb

%postun
%python_uninstall_alternative ipdb

%check
%python_exec setup.py test

%files %{python_files}
%doc AUTHORS HISTORY.txt README.rst
%license COPYING.txt
%python_alternative %{_bindir}/ipdb
%{python_sitelib}/*

%changelog
