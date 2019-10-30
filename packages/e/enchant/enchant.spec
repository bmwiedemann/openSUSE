#
# spec file for package enchant
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


Name:           enchant
Version:        2.2.5
Release:        0
Summary:        Generic Spell Checking Library
License:        LGPL-2.1-or-later
Group:          Productivity/Text/Spell
URL:            https://abiword.github.io/enchant/
Source:         https://github.com/AbiWord/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
%if 0%{?is_opensuse}
BuildRequires:  aspell-devel
%endif
BuildRequires:  dbus-1-glib-devel
BuildRequires:  gcc-c++
BuildRequires:  glib2-devel
BuildRequires:  hunspell-devel
BuildRequires:  libvoikko-devel

%description
A library providing an efficient extensible abstraction for dealing
with different spell checking libraries.

%package tools
Summary:        Command line tools for the Enchant spell checking library
Group:          Productivity/Text/Spell

%description tools
A library providing an efficient extensible abstraction for dealing
with different spell checking libraries.

This package provides command-line tools to interact with enchant.

%package data
Summary:        Data files for libenchant
# enchant up to version 1.6.1 was not packaged properly according the SLPP
Group:          Productivity/Text/Spell
Conflicts:      libenchant1 < 1.6.1

%description data
A library providing an efficient extensible abstraction for dealing
with different spell checking libraries.

This package provides data/configuration files for libenchant.

%if 0%{?is_opensuse}
%package -n enchant-2-backend-aspell
Summary:        Aspell backend for the Enchant spell checking library
Group:          Productivity/Text/Spell
Supplements:    packageand(libenchant-2-2:%(rpm -q --qf "%%{name}" -f $(readlink -f %{_libdir}/libaspell.so))
Provides:       enchant-2-backend

%description -n enchant-2-backend-aspell
Aspell plugin for enchant, a library providing an efficient
extensible abstraction for dealing with different spell checking
libraries.
%endif

%package -n enchant-2-backend-hunspell
Summary:        Hunspell backend for the Enchant spell checking library
Group:          Productivity/Text/Spell
Supplements:    packageand(libenchant-2-2:%(rpm -q --qf "%%{name}" -f $(readlink -f %{_libdir}/libhunspell.so))
Provides:       enchant-2-backend

%description -n enchant-2-backend-hunspell
Hunspell plugin for enchant, a library providing an efficient
extensible abstraction for dealing with different spell checking
libraries.

%package -n enchant-2-backend-voikko
Summary:        Voikko backend for the Enchant spell checking library
Group:          Productivity/Text/Spell
Supplements:    packageand(libenchant-2-2:%(rpm -q --qf "%%{name}" -f $(readlink -f %{_libdir}/libvoikko.so))
Provides:       enchant-2-backend
Provides:       locale(libenchant-2-2:fi)

%description -n enchant-2-backend-voikko
Voikko plugin (Finnish) for enchant, a library providing an efficient
extensible abstraction for dealing with different spell checking
libraries.

%package -n libenchant-2-2
Summary:        Generic Spell Checking Library
Group:          System/Libraries
Requires:       enchant-2-backend
Requires:       enchant-data >= %{version}
Suggests:       enchant-2-backend-hunspell

%description -n libenchant-2-2
A library providing an efficient extensible abstraction for dealing
with different spell checking libraries.

%package devel
Summary:        Development files for the Enchant spell checking library
Group:          Development/Libraries/C and C++
Requires:       glib2-devel
Requires:       libenchant-2-2 = %{version}
Requires:       libstdc++-devel

%description devel
This package contains all necessary include files and libraries needed
to develop applications that require these.

%prep
%setup -q

%build
%configure \
%if 0%{?is_opensuse}
    --disable-static \
    --with-aspell
%else
    --disable-static
%endif
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libenchant-2-2 -p /sbin/ldconfig
%postun -n libenchant-2-2 -p /sbin/ldconfig

%files tools
%{_bindir}/enchant-2
%{_bindir}/enchant-lsmod-2
%{_mandir}/man1/enchant-2.1%{?ext_man}
%{_mandir}/man1/enchant-lsmod-2.1%{?ext_man}

%files -n libenchant-2-2
%license COPYING.LIB
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/*.so.*
%dir %{_libdir}/enchant-2

%if 0%{?is_opensuse}
%files -n enchant-2-backend-aspell
%dir %{_libdir}/enchant-2
%{_libdir}/enchant-2/enchant_aspell.so
%endif

%files -n enchant-2-backend-hunspell
%dir %{_libdir}/enchant-2
%{_libdir}/enchant-2/enchant_hunspell.so

%files -n enchant-2-backend-voikko
%dir %{_libdir}/enchant-2
%{_libdir}/enchant-2/enchant_voikko.so

%files data
# The directories are not versioned, unfortunately. Not good for the SLPP.
%dir %{_datadir}/enchant
%{_datadir}/enchant/enchant.ordering

%files devel
%{_includedir}/enchant-2
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
