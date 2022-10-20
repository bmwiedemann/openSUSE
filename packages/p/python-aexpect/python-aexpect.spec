#
# spec file
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define         skip_python2 1
%global         pkgname aexpect
Name:           python-%{pkgname}
Version:        1.6.4
Release:        0
Summary:        Python library to control interactive applications
License:        GPL-2.0-only
URL:            http://avocado-framework.readthedocs.org/
Source:         https://github.com/avocado-framework/aexpect/archive/%{version}.tar.gz#/%{pkgname}-%{version}.tar.gz
Patch0:         helper-version-in-cmdline.patch
# PATCH-FIX-UPSTREAM 0001-Remove-six-dependency.patch gh#avocado-framework/aexpect#102
Patch1:         0001-Remove-six-dependency.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Aexpect is a Python library used to control interactive applications, very
similar to pexpect. It can be used to control applications such as ssh, scp
sftp, telnet, among others.

%prep
%autosetup -p1 -n %{pkgname}-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/aexpect_helper
%fdupes %{buildroot}

%check
export PATH=$PATH:%{buildroot}%{_bindir}
%pytest -k 'not pass_fds_spawn and not share_remote_objects'

%post
%python_install_alternative aexpect_helper

%postun
%python_uninstall_alternative aexpect_helper

%files %{python_files}
%license LICENSE
%doc README.rst
%python_alternative %{_bindir}/aexpect_helper
%{python_sitelib}/aexpect
%{python_sitelib}/aexpect-%{version}*-info

%changelog
