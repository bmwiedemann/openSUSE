#
# spec file for package python-scikits.example
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
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-scikits.example
Version:        0.1
Release:        0
Summary:        Scikits example and base package
License:        MIT
Group:          Development/Languages/Python
Url:            http://projects.scipy.org/scipy/scikits
Source:         https://files.pythonhosted.org/packages/source/s/scikits.example/scikits.example-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numpy-devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch

%python_subpackages

%description
Example package on how to organize scikits. This is a do
nothing package, to show how to organize a scikit.

It also includes the base scikit and scikits namespaces, so
other packages using these namespaces must depend on this
package.


%prep
%setup -q -n scikits.example-%{version}

%build
%python_build

%install
%python_install
%python_expand cp scikits/__init__.py %{buildroot}%{$python_sitelib}/scikits/__init__.py
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %have_python2
%py_compile %{buildroot}%{python2_sitelib}/scikits/
%endif
%if %have_python3
%py3_compile %{buildroot}%{python3_sitelib}/scikits/
%endif

%files %{python_files}
%doc README
%dir %{python_sitelib}/scikits/
%{python_sitelib}/scikits/example/
%{python_sitelib}/scikits/__init__.py*
%pycache_only %dir %{python_sitelib}/scikits/__pycache__/
%pycache_only %{python_sitelib}/scikits/__pycache__/__init__*.py*
%{python_sitelib}/scikits.example-%{version}-py*.egg-info
%{python_sitelib}/scikits.example-%{version}-py*-nspkg.pth

%changelog
