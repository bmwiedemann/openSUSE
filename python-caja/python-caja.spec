#
# spec file for package python-caja
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


%define _name   caja-python
%define _version 1.23
Name:           python-caja
Version:        1.23.0
Release:        0
Summary:        Python bindings for Caja
License:        GPL-2.0-or-later
Group:          System/GUI/Other
URL:            https://mate-desktop.org/
Source:         https://pub.mate-desktop.org/releases/%{_version}/%{name}-%{version}.tar.xz
# set to _version when mate-common has an equal release
BuildRequires:  mate-common >= 1.22
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libcaja-extension) >= %{_version}
BuildRequires:  pkgconfig(pygobject-3.0)
BuildRequires:  pkgconfig(python)
%if 0%{?suse_version} < 1500
Requires:       python-gobject
# We can't have automatic typelib() Requires here: it's C code: PyImport_ImportModule("gi.repository.Mate").
Requires:       typelib(Caja)
Recommends:     %{name}-lang
# python-mate-file-manager was last used in openSUSE 13.1.
Provides:       python-mate-file-manager = %{version}
Obsoletes:      python-mate-file-manager < %{version}
%endif

%description
This package contains bindings to write Caja extensions with Python.
It allows writing menu, property pages and column providers
extensions, so that Caja functionality can be easily extended.

%if 0%{?suse_version} >= 1500
%package -n python2-caja
Summary:        Python bindings for Caja
Group:          System/GUI/Other
Requires:       python2-gobject
# We can't have automatic typelib() Requires here: it's C code: PyImport_ImportModule("gi.repository.Mate").
Requires:       typelib(Caja)
Recommends:     %{name}-lang
Provides:       %{name} = %{version}
# python-mate-file-manager was last used in openSUSE 13.1.
Provides:       python-mate-file-manager = %{version}
Obsoletes:      python-mate-file-manager < %{version}
# python-caja was last used in openSUSE Leap 42.3.
Provides:       python-caja = %{version}
Obsoletes:      python-caja < %{version}

%description -n python2-caja
This package contains bindings to write Caja extensions with Python.
It allows writing menu, property pages and column providers
extensions, so that Caja functionality can be easily extended.
%endif

%lang_package

%package devel
Summary:        Python bindings for Caja - Development Files
# python-mate-file-manager-devel was last used in openSUSE 13.1.
Group:          Development/Libraries/Other
Provides:       python-mate-file-manager-devel = %{version}
Obsoletes:      python-mate-file-manager-devel < %{version}
%if 0%{?suse_version} >= 1500
Requires:       python2-caja = %{version}
%else
Requires:       %{name} = %{version}
%endif

%description devel
Development files needed for writing Caja Python extensions.

This package contains bindings to write Caja extensions with Python.
It allows writing menu, property pages and column providers
extensions, so that Caja functionality can be easily extended.

%prep
%setup -q

%build
NOCONFIGURE=1 mate-autogen
export PYTHON=python2
%configure \
  --disable-static
make %{?_smp_mflags} V=1

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

%if 0%{?suse_version} >= 1500
%files -n python2-caja
%else
%files
%endif
%license COPYING
%doc AUTHORS NEWS README
%doc %{_docdir}/%{name}/
%{_libdir}/caja/extensions-2.0/lib%{_name}.so
%{_datadir}/caja/extensions/lib%{_name}.caja-extension
%{_datadir}/%{_name}/

%files devel
%{_libdir}/pkgconfig/%{_name}.pc

%files lang -f %{name}.lang

%changelog
