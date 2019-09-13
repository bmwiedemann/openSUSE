#
# spec file for package python-Durus
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define oldpython python
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-Durus
Version:        3.9
Release:        0
Summary:        A Python Object Database
License:        CNRI-Python
Group:          Development/Languages/Python
Url:            http://www.mems-exchange.org/software/durus/
Source:         https://files.pythonhosted.org/packages/source/D/Durus/Durus-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module nose}
BuildRequires:  python-rpm-macros
%ifpython2
Provides:       %{oldpython}-durus = %{version}
Obsoletes:      %{oldpython}-durus < %{version}
%endif
Requires(post):   update-alternatives
Requires(postun):  update-alternatives
%python_subpackages

%description
Serves and manages changes to persistent objects being used in
multiple client processes.

%prep
%setup -q -n Durus-%{version}
sed -i "1d" {db_renumber,__main__}.py # Fix non-executable scripts

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/durus

%post
%python_install_alternative durus

%postun
%python_uninstall_alternative durus

%check
%python_expand nosetests-%{$python_bin_suffix}

%files %{python_files}
%defattr(-,root,root,-)
%doc ACKS.txt CHANGES.txt LICENSE.txt README.txt doc/FAQ.txt
%python_alternative %{_bindir}/durus
%{python_sitearch}/*

%changelog
