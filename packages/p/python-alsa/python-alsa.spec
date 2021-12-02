#
# spec file for package python-alsa
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
Name:           python-alsa
Version:        1.1.6
Release:        0
Summary:        Python ALSA binding
License:        LGPL-2.1-or-later AND GPL-2.0-only
Group:          Development/Libraries/Python
URL:            https://www.alsa-project.org
Source:         %{url}/files/pub/pyalsa/pyalsa-%{version}.tar.bz2
Source1:        COPYING
Source2:        COPYING.LIB
Patch1:         0001-alsaseq-fix-constant-objects-in-Python-3.patch
Patch2:         0002-Fix-PyTuple_SET_ITEM-usage-no-return-value.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  alsa-devel
BuildRequires:  python-rpm-macros
Provides:       pyalsa = %{version}
Obsoletes:      pyalsa < %{version}
%python_subpackages

%description
This package provides the Python binding to ALSA.

%prep
%setup -q -n pyalsa-%{version}
%patch1 -p1
%patch2 -p1
cp %{SOURCE1} %{SOURCE2} .

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%python_build

%install
%python_install

%files %{python_files}
%license COPYING COPYING.LIB
%{python_sitearch}/*

%changelog
