#
# spec file for package python-cangjie
#
# Copyright (c) 2023 SUSE LLC
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


%global src_name cangjie
Name:           python-cangjie
Version:        1.3
Release:        0
Summary:        A python wrapper to libcangjie
License:        LGPL-3.0-or-later
URL:            http://cangjians.github.io/projects/pycangjie
Source:         https://github.com/Cangjians/pycangjie/releases/download/v%{version}/%{src_name}-%{version}.tar.xz
Source99:       python-cangjie-rpmlintrc
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel}
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  libcangjie-data
BuildRequires:  libcangjie-devel
BuildRequires:  libtool
BuildRequires:  python-rpm-macros
Requires:       libcangjie-data
%python_subpackages

%description
Python wrapper to libcangjie, the library implementing the Cangjie input method.

%prep
%setup -q -n %{src_name}-%{version}
sed -i '/.\/configure/ d' autogen.sh

%build
./autogen.sh
%define _configure ../configure
%{python_expand #
mkdir -p build
pushd build
%configure --prefix=%{_prefix}/ PYTHON=%{_bindir}/$python
%make_build
popd
}

%install
%{python_expand #
pushd build
%make_install
popd
find %{buildroot} -type f -name "*.la" -delete -print

fdupes %{buildroot}/%{$python_sitearch}
}

# check
%pyunittest_arch discover tests

%files %{python_files}
%defattr(-,root,root)
%doc AUTHORS COPYING README.md docs/*
%{python_sitearch}/%{src_name}

%changelog
