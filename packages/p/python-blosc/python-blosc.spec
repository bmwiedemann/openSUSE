#
# spec file for package python-blosc
#
# Copyright (c) 2021 SUSE LLC
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
%define skip_python2 1
# Upstream dropped official support for Python < 3.7 and python36-numpy is being phased out of TW
%define skip_python36 1
Name:           python-blosc
Version:        1.10.2
Release:        0
Summary:        Blosc data compressor for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Blosc/python-blosc
Source:         https://files.pythonhosted.org/packages/source/b/blosc/blosc-%{version}.tar.gz
# PATCH-FEATURE-UPSTREAM use-system-blosc.patch -- gh#Blosc/python-blosc#244
Patch0:         https://github.com/Blosc/python-blosc/pull/244.patch#/use-system-blosc.patch
BuildRequires:  %{python_module devel >= 3.7}
BuildRequires:  %{python_module scikit-build >= 0.11.1}
BuildRequires:  %{python_module setuptools}
BuildRequires:  blosc-devel >= 1.9.0
BuildRequires:  c++_compiler
BuildRequires:  cmake >= 3.14.0
BuildRequires:  fdupes
BuildRequires:  ninja
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module numpy >= 1.16}
BuildRequires:  %{python_module psutil}
# /SECTION
Recommends:     python-numpy
%python_subpackages

%description
Blosc is a high performance compressor optimized for binary data in
Python.

%prep
%autosetup -p1 -n blosc-%{version}

%build
export CFLAGS="%{optflags}"
export USE_SYSTEM_BLOSC=1
%python_build

%install
export USE_SYSTEM_BLOSC=1
# gh#Blosc/python-blosc#222
%python_expand %{$python_install} --install-purelib %{$python_sitearch}
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pyunittest_arch discover -s blosc/ -v 

%files %{python_files}
%doc ANNOUNCE.rst README.rst RELEASE_NOTES.rst
%license LICENSES/*.txt
%{python_sitearch}/blosc-%{version}*-info
%{python_sitearch}/blosc/

%changelog
