#
# spec file for package libstfl
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


%define sover 0
Name:           libstfl
Version:        0.24
Release:        0
Summary:        Structured Terminal Forms Library
License:        LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            http://www.clifford.at/stfl/
Source:         http://www.clifford.at/stfl/stfl-%{version}.tar.gz
Source99:       libstfl-rpmlintrc
Patch1:         stfl-optflags.patch
BuildRequires:  ncurses-devel
BuildRequires:  pkg-config

%description
STFL is a library which implements a curses-based widget set for text
terminals. The STFL API can be used from C, SPL, Python, Perl and Ruby.

%package -n libstfl%{sover}
Summary:        Structured Terminal Forms Library
Group:          System/Libraries

%description -n libstfl%{sover}
STFL is a library which implements a curses-based widget set for text
terminals. The STFL API can be used from C, SPL, Python, Perl and Ruby.

A special language (the Structured Terminal Forms Language) is used to
describe STFL GUIs.

%package -n libstfl-devel
Summary:        Structured Terminal Forms Library
Group:          Development/Libraries/C and C++
Requires:       libstfl%{sover} = %{version}
Requires:       ncurses-devel

%description -n libstfl-devel
STFL is a library which implements a curses-based widget set for text
terminals. The STFL API can be used from C, SPL, Python, Perl and Ruby.
The API has only 14 function calls and generic SWIG bindings exist
already for porting STFL to other scripting languages.

A special language (the Structured Terminal Forms Language) is used to
describe STFL GUIs.

%prep
%autosetup -p0 -n "stfl-%{version}"

%build
%make_build \
	CC="gcc" \
	OPTFLAGS="%{optflags}"\
	FOUND_SPL=0 \
	FOUND_SWIG=0 \
	FOUND_RUBY=0 \
	FOUND_PERL=0 \
	FOUND_PYTHON=0

%install
%make_install \
	libdir="%{_lib}" \
	prefix="%{_prefix}"

if ! [ -e "%{buildroot}/%{_libdir}/libstfl.so.%{sover}" ]; then
    pushd "%{buildroot}%{_libdir}/"
    ln -s libstfl.so.*.* libstfl.so.%{sover}
    popd
fi
rm -fv "%{buildroot}/%{_libdir}"/*.a

%ldconfig_scriptlets -n libstfl%{sover}

%files -n libstfl%{sover}
%license COPYING
%doc README
%{_libdir}/libstfl.so.%{sover}
%{_libdir}/libstfl.so.%{sover}.*

%files -n libstfl-devel
%{_includedir}/stfl.h
%{_libdir}/libstfl.so
%{_libdir}/pkgconfig/stfl.pc

%changelog
