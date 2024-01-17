#
# spec file for package python-compizconfig
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


%define skip_python2 1
%define _rev    11bb53f9054e95f715e631a261968e2c
%define _name   compizconfig-python
Name:           python-compizconfig
Version:        0.8.18
Release:        0
Summary:        Python bindings for libraries for compizconfig-settings
License:        GPL-2.0-or-later
URL:            https://gitlab.com/compiz/compizconfig-python
Source:         https://gitlab.com/compiz/compizconfig-python/uploads/%{_rev}/%{_name}-%{version}.tar.xz
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel}
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libcompizconfig) < 0.9
BuildRequires:  pkgconfig(x11)
Requires:       compiz < 0.9
%python_subpackages

%description
Python bindings for libraries/plugins for compizconfig-settings.

%prep
%setup -q -n %{_name}-%{version}

%build
NOCONFIGURE=1 ./autogen.sh
%global _configure ../configure
%{python_expand mkdir -p "build-$python"
pushd "build-$python"
export PYTHON="$python"
%configure \
  --disable-static \
  --with-cython="cython-%{$python_version}"
%make_build
popd
}

%install
%python_expand %make_install -C "build-$python"

find %{buildroot} -type f -name "*.la" -delete -print
rm -r %{buildroot}%{_libdir}/pkgconfig/

%files %{python_files}
%license COPYING
%doc NEWS README.md
%{python_sitearch}/compizconfig*

%changelog
