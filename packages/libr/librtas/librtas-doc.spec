#
# spec file for package librtas-doc
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           librtas-doc
Version:        2.0.2
Release:        0
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  libtool
Summary:        Documents for librtas
License:        LGPL-2.1-or-later
Group:          Documentation/Other
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExclusiveArch:  ppc ppc64 ppc64le
Url:            https://github.com/ibm-power-utilities/librtas
Source0:        https://github.com/ibm-power-utilities/librtas/archive/v%{version}.tar.gz#/librtas-%{version}.tar.gz
Patch0:         librtas.fix_doc_path.patch

%description
This package provides librtas documentation

%prep
%setup -n librtas-%{version}
%patch0 -p1

%build
./autogen.sh
%configure
make CFLAGS="%optflags -fPIC -g -I $PWD/librtasevent_src" LIB_DIR="%{_libdir}" %{?_smp_mflags}

%install
rm -rf doc/*/latex
make install DESTDIR=%buildroot LIB_DIR="%{_libdir}"
rm -rf %buildroot/%_libdir
rm -rf %buildroot/%_includedir
%fdupes %buildroot/%_docdir

%files
%defattr(-, root, root)
%doc %{_docdir}/librtas

%changelog
