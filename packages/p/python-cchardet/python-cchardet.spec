#
# spec file for package python-cchardet
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
%define skip_python2 1
Name:           python-cchardet
Version:        2.1.6
Release:        0
Summary:        cChardet is high speed universal character encoding detector
License:        MPL-1.1 OR LGPL-2.1-or-later OR GPL-2.0-or-later
URL:            https://github.com/PyYoshi/cChardet
Source:         https://files.pythonhosted.org/packages/source/c/cchardet/cchardet-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(uchardet)
Requires(post): update-alternatives
Requires(postun): update-alternatives
%python_subpackages

%description
cChardet is high speed universal character encoding detector. - binding to `uchardet`_.

%prep
%setup -q -n cchardet-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/cchardetect
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%post
%python_install_alternative cchardetect

%postun
%python_uninstall_alternative cchardetect

%files %{python_files}
%license COPYING
%doc README.rst
%python_alternative %{_bindir}/cchardetect
%{python_sitearch}/*

%changelog
