#
# spec file for package python-ipdb
#
# Copyright (c) 2022 SUSE LLC
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


%define         skip_python2 1
Name:           python-ipdb
Version:        0.13.11
Release:        0
Summary:        IPython-enabled pdb
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/gotcha/ipdb
Source:         https://files.pythonhosted.org/packages/source/i/ipdb/ipdb-%{version}.tar.gz
BuildRequires:  %{python_module decorator}
BuildRequires:  %{python_module ipython >= 7.16.3 if %python-base < 3.7}
BuildRequires:  %{python_module ipython >= 7.31.1 if %python-base >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module tomli if %python-base < 3.11}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-decorator
Requires:       (python-ipython >= 7.16.3 if python-base < 3.7)
Requires:       (python-ipython >= 7.31.1 if python-base >= 3.7)
Requires:       (python-tomli if python-base < 3.11)
Requires(post): update-alternatives
Requires(postun):update-alternatives
Provides:       python-jupyter_ipdb = %{version}
Obsoletes:      python-jupyter_ipdb < %{version}
BuildArch:      noarch
%if "%{python_flavor}" == "python3" || "%{?python_provides}"  == "python3"
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
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/ipdb3
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative ipdb3

%postun
%python_uninstall_alternative ipdb3

%check
%pyunittest -v

%files %{python_files}
%doc AUTHORS HISTORY.txt README.rst
%license COPYING.txt
%python_alternative %{_bindir}/ipdb3
%{python_sitelib}/ipdb
%{python_sitelib}/ipdb-%{version}.dist-info

%changelog
