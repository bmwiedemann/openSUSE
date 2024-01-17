#
# spec file for package zypp-plugin
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


%define singlespec_py3 ( 0%{?suse_version} > 1330 )

Name:           zypp-plugin
Version:        0.6.3
Release:        0
Summary:        Helper that makes writing ZYpp plugins easier
License:        GPL-2.0-only
Group:          System/Packages
URL:            https://github.com/openSUSE/zypp-plugin
Source0:        %{name}-%{version}.tar.bz2
BuildArch:      noarch

%if %{singlespec_py3}
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
BuildRequires:  %{python_module devel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-base
# provide old names for py2 package
%if "%{python_flavor}" == "python2"
Obsoletes:      zypp-plugin-python < %{version}-%{release}
Provides:       zypp-plugin-python = %{version}-%{release}
%endif
%python_subpackages
### ----------------------------------------
### SLE-12* and even older
%else
%define have_python2 1
%if ( 0%{?suse_version} == 1315 )
%define have_python3 1
%else
%define have_python3 0
%endif
%endif
### ----------------------------------------

%description
This API allows writing ZYpp plugins by just subclassing from a python class
and implementing the commands you want to respond to as python methods.

%prep
%setup -q -n zypp-plugin

%build
:

%install
%if %{singlespec_py3}
%{python_expand #
mkdir -p %{buildroot}%{$python_sitelib}
install -m 0644 python/zypp_plugin.py %{buildroot}%{$python_sitelib}/zypp_plugin.py
# TODO: replace by $python_compileall as soon as it is available sr#843481
$python -m compileall %{buildroot}%{$python_sitelib}
$python -O -m compileall %{buildroot}%{$python_sitelib}
%fdupes %{buildroot}%{$python_sitelib}
}
%else
%if 0%{?have_python2}
mkdir -p %{buildroot}%{python_sitelib}
install -m 0644 python/zypp_plugin.py %{buildroot}%{python_sitelib}/zypp_plugin.py
%py_compile -O %{buildroot}/%{python_sitelib}
%endif
%if 0%{?have_python3}
mkdir -p %{buildroot}%{python3_sitelib}
install -m 0644 python/zypp_plugin.py %{buildroot}%{python3_sitelib}/zypp_plugin.py
%py3_compile -O %{buildroot}/%{python3_sitelib}
%endif
%endif

%if %{singlespec_py3}
%files %{python_files}
%doc COPYING
%{python_sitelib}/zypp_plugin*
%pycache_only %{python_sitelib}/__pycache__/*

### ----------------------------------------
### SLE-12* and even older
%else
%package -n %{name}-python
Summary:        Helper that makes writing ZYpp plugins in python easier
Group:          System/Packages
Provides:       python2-%{name} = %{version}-%{release}
BuildRequires:  python-devel
Requires:       python

%files -n %{name}-python
%defattr(-,root,root)
%doc COPYING
%{python_sitelib}/*

%description -n %{name}-python
This API allows writing ZYpp plugins by just subclassing from a python class
and implementing the commands you want to respond to as python methods.

%if 0%{?have_python3}
%package -n python3-%{name}
Summary:        Helper that makes writing ZYpp plugins in python easier
Group:          System/Packages
Requires:       python3
BuildRequires:  python3-devel

%files -n python3-%{name}
%defattr(-,root,root)
%doc COPYING
%{python3_sitelib}/*

%description -n python3-%{name}
This API allows writing ZYpp plugins by just subclassing from a python class
and implementing the commands you want to respond to as python methods.
%endif
%endif
### ----------------------------------------

%changelog
