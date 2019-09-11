#
# spec file for package python-cx_Freeze
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
# Missing sample files
%bcond_with     test
Name:           python-cx_Freeze
Version:        5.1.1
Release:        0
Summary:        Create standalone executables from Python scripts
License:        Python-2.0
Group:          Development/Languages/Python
Url:            https://github.com/anthony-tuininga/cx_Freeze
Source:         https://files.pythonhosted.org/packages/source/c/cx_Freeze/cx_Freeze-%{version}.tar.gz
Source10:       https://raw.githubusercontent.com/anthony-tuininga/cx_Freeze/%{version}/doc/license.rst
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  chrpath
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if %{with test}
BuildRequires:  %{python_module nose}
BuildRequires:  python-mock
%endif
Requires(post):   update-alternatives
Requires(postun):  update-alternatives

%python_subpackages

%description
CX_Freeze is a set of scripts and modules for turning Python scripts
into executables in much the same way that py2exe and py2app do.

It works by bundling Python executables and libraries from the local
Python installation. As such, the distribution produced by CX_Freeze
shares the very same dependencies. System libraries are not bundled
however, so additional dependencies may need to be manually installed
before being able to run "cx-frozen" executables that were created by
other systems.

%prep
%setup -q -n cx_Freeze-%{version}
cp %{SOURCE10} .
sed -i -e '/^#!\//, 1d' cx_Freeze/samples/*/*.py
chmod a-x cx_Freeze/initscripts/*.py

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand chrpath -d %{buildroot}%{$python_sitearch}/cx_Freeze/bases/Console*
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%python_clone -a %{buildroot}%{_bindir}/cxfreeze
%python_clone -a %{buildroot}%{_bindir}/cxfreeze-quickstart

%if %{with test}
%check
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitearch}
nosetests-%{$python_bin_suffix}
}
%endif

%post
%{python_install_alternative cxfreeze cxfreeze-quickstart}

%postun
%python_uninstall_alternative cxfreeze

%files %{python_files}
%defattr(-,root,root,-)
%doc README.md
%license license.rst
%python_alternative %{_bindir}/cxfreeze
%python_alternative %{_bindir}/cxfreeze-quickstart
%{python_sitearch}/*

%changelog
