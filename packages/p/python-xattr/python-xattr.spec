#
# spec file for package python-xattr
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


Name:           python-xattr
Version:        0.10.1
Release:        0
Summary:        Python wrapper for extended filesystem attributes
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/xattr/xattr
Source:         https://files.pythonhosted.org/packages/source/x/xattr/xattr-%{version}.tar.gz
BuildRequires:  %{python_module cffi}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-cffi >= 1.11
Requires:       python-setuptools
Requires(post): update-alternatives
Requires(postun):update-alternatives
%ifpython2
Provides:       pyxattr = %{version}
Obsoletes:      pyxattr < %{version}
%endif
%python_subpackages

%description
Extended attributes extend the basic attributes of files and directories
in the file system.  They are stored as name:data pairs associated with
file system objects (files, directories, symlinks, etc).

Extended attributes are currently only available on Darwin 8.0+ (Mac OS X 10.4)
and Linux 2.6+. Experimental support is included for Solaris and FreeBSD.

%prep
%setup -q -n xattr-%{version}
sed -i "/#\!\/usr\/bin\/env python/d" xattr/tool.py # Fix executable-bit rpmlint warning

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}
%python_clone -a %{buildroot}%{_bindir}/xattr

%check
export LC_ALL=en_US.utf-8
%pyunittest discover -v

%post
%python_install_alternative xattr

%postun
%python_uninstall_alternative xattr

%files %{python_files}
%license LICENSE.txt
%doc README.rst
%python_alternative %{_bindir}/xattr
%{python_sitearch}/xattr
%{python_sitearch}/xattr-*egg-info

%changelog
