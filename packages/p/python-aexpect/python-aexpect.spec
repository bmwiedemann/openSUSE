#
# spec file for package python-aexpect
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
%global         pkgname aexpect
Name:           python-%{pkgname}
Version:        1.5.1
Release:        0
Summary:        Python library to control interactive applications
License:        GPL-2.0-only
Group:          Development/Languages/Python
URL:            http://avocado-framework.readthedocs.org/
Source:         https://github.com/avocado-framework/aexpect/archive/%{version}.tar.gz#/%{pkgname}-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python2-subprocess32 >= 3.2.6
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%ifpython2
Requires:       python2-subprocess32 >= 3.2.6
%endif
%python_subpackages

%description
Aexpect is a Python library used to control interactive applications, very
similar to pexpect. It can be used to control applications such as ssh, scp
sftp, telnet, among others.

%prep
%setup -q -n %{pkgname}-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/aexpect-helper
%fdupes %{buildroot}

%check
export PATH=$PATH:%{buildroot}%{_bindir}
%python_exec setup.py test

%post
%python_install_alternative aexpect-helper

%postun
%python_uninstall_alternative aexpect-helper

%files %{python_files}
%license LICENSE
%doc README.rst
%python_alternative %{_bindir}/aexpect-helper
%{python_sitelib}/*

%changelog
