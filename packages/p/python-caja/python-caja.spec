#
# spec file for package python-caja
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


%define _name   caja-python
%define _version 1.26

Name:           python-caja
Version:        1.26.0
Release:        0
Summary:        Python bindings for Caja
License:        GPL-2.0-or-later
Group:          Development/Libraries/Python
URL:            https://mate-desktop.org/
Source:         https://pub.mate-desktop.org/releases/%{_version}/%{name}-%{version}.tar.xz
BuildRequires:  mate-common >= %{_version}
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libcaja-extension) >= %{_version}
BuildRequires:  pkgconfig(pygobject-3.0)
BuildRequires:  pkgconfig(python3)
Requires:       python3-gobject
# We can't have automatic typelib() Requires here: it's C code: PyImport_ImportModule("gi.repository.Mate").
Requires:       typelib(Caja)
Recommends:     %{name}-lang
# python2-caja was last used in openSUSE Leap 15.2.
Obsoletes:      python2-caja < %{version}
# python-mate-file-manager was last used in openSUSE 13.1.
Provides:       python-mate-file-manager = %{version}
Obsoletes:      python-mate-file-manager < %{version}

%description
This package contains bindings to write Caja extensions with Python.
It allows writing menu, property pages and column providers
extensions, so that Caja functionality can be easily extended.

%lang_package

%package devel
Summary:        Python bindings for Caja - Development Files
Requires:       %{name} = %{version}
# python-mate-file-manager-devel was last used in openSUSE 13.1.
Provides:       python-mate-file-manager-devel = %{version}
Obsoletes:      python-mate-file-manager-devel < %{version}

%description devel
Development files needed for writing Caja Python extensions.

This package contains bindings to write Caja extensions with Python.
It allows writing menu, property pages and column providers
extensions, so that Caja functionality can be easily extended.

%prep
%setup -q

%build
NOCONFIGURE=1 mate-autogen
export PYTHON=python3
%configure \
  --disable-static
%make_build

%install
%make_install
# New dir where python extensions get installed. It's not created by make install (bgo#638890).
[ ! -d %{buildroot}%{_datadir}/%{_name}/extensions/ ]
mkdir -p %{buildroot}%{_datadir}/%{_name}/extensions/
find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{name}
# Move documentation to a correct directory.
mkdir -p %{buildroot}%{_docdir}/
mv -f %{buildroot}%{_datadir}/doc/%{name}/ %{buildroot}%{_docdir}/%{name}/

%files
%license COPYING
%doc AUTHORS NEWS README
%doc %{_docdir}/%{name}/
%{_libdir}/caja/extensions-2.0/lib%{_name}.so
%{_datadir}/caja/extensions/lib%{_name}.caja-extension
%{_datadir}/%{_name}/

%files lang -f %{name}.lang

%files devel
%{_libdir}/pkgconfig/%{_name}.pc

%changelog
