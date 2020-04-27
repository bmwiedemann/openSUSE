#
# spec file for package python-pgmagick
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%bcond_without  python2
Name:           python-pgmagick
Version:        0.7.4
Release:        0
Summary:        Yet Another Python wrapper for GraphicsMagick
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/hhatto/pgmagick/
Source:         https://files.pythonhosted.org/packages/source/p/pgmagick/pgmagick-%{version}.tar.gz
# PATCH-FIX-UPSTREAM https://github.com/hhatto/pgmagick/pull/47
Patch0:         reproducible.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  ghostscript-fonts-std
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(GraphicsMagick++)
%if 0%{?suse_version} >= 1500
BuildRequires:  libboost_python3-devel
%if %{with python2}
BuildRequires:  libboost_python-devel
%endif
%else
BuildRequires:  boost-devel
%endif
%python_subpackages

%description
The pgmagick package is a yet another boost.python based
wrapper for GraphicsMagick.

%prep
%setup -q -n pgmagick-%{version}
%patch0 -p1

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
mkdir tester
pushd tester
cp -r ../test .
%python_expand PYTHONPATH=%{buildroot}%{$python_sitearch} $python -m unittest discover -v
popd
rm -r tester

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitearch}/pgmagick/
%{python_sitearch}/pgmagick-%{version}-py*.egg-info/

%changelog
