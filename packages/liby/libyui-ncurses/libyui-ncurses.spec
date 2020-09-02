#
# spec file for package libyui-ncurses
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


Name:           libyui-ncurses
Version:        2.56.2
Release:        0
Source:         %{name}-%{version}.tar.bz2

%define so_version 13
%define bin_name %{name}%{so_version}

%if 0%{?suse_version} > 1325
BuildRequires:  libboost_headers-devel
%else
BuildRequires:  boost-devel
%endif
BuildRequires:  cmake >= 2.8
BuildRequires:  gcc-c++
BuildRequires:  pkg-config

# YLabel::setAutoWrap()
%define libyui_devel_version libyui-devel >= 3.10.0
BuildRequires:  %{libyui_devel_version}
BuildRequires:  ncurses-devel

URL:            http://github.com/libyui/
Summary:        Libyui - Character Based User Interface
License:        LGPL-2.1-only OR LGPL-3.0-only
Group:          System/Libraries

%description
This package contains the character based (ncurses) user interface
component for libYUI.


%package -n %{bin_name}

Requires:       glibc-locale
Requires:       libyui%{so_version}
Provides:       %{name} = %{version}
Provides:       yast2-ncurses = 2.42.0
Obsoletes:      yast2-ncurses < 2.42.0
Provides:       yui_backend = %{so_version}

URL:            http://github.com/libyui/
Summary:        Libyui - Character Based User Interface
Group:          System/Libraries

%description -n %{bin_name}
This package contains the character based (ncurses) user interface
component for libYUI.



%package devel

Requires:       %{libyui_devel_version}
%if 0%{?suse_version} > 1325
Requires:       libboost_headers-devel
%else
Requires:       boost-devel
%endif
Requires:       %{bin_name} = %{version}
Requires:       glibc-devel
Requires:       libstdc++-devel
Requires:       ncurses-devel

URL:            http://github.com/libyui/
Summary:        Libyui-ncurses header files
Group:          Development/Languages/C and C++

%description devel
This package contains the character based (ncurses) user interface
component for libYUI.


This can be used independently of YaST for generic (C++) applications.
This package has very few dependencies.

%package tools

URL:            http://github.com/libyui/
Summary:        Libyui-ncurses tools
# conflict with libyui-ncurses8, /usr/bin/libyui-terminal was originally there
Group:          System/Libraries
Conflicts:      %{name}8

Requires:       screen

%description tools
Character based (ncurses) user interface component for libYUI.

libyui-terminal - useful for testing on headless machines

%prep
%setup -q -n %{name}-%{version}

%build

export CFLAGS="$RPM_OPT_FLAGS -DNDEBUG"
export CXXFLAGS="$RPM_OPT_FLAGS -DNDEBUG"

./bootstrap.sh %{_prefix}

mkdir build
cd build

%if %{?_with_debug:1}%{!?_with_debug:0}
cmake .. \
        -DYPREFIX=%{_prefix} \
        -DDOC_DIR=%{_docdir} \
        -DLIB_DIR=%{_lib} \
        -DCMAKE_BUILD_TYPE=RELWITHDEBINFO
%else
cmake .. \
        -DYPREFIX=%{_prefix} \
        -DDOC_DIR=%{_docdir} \
        -DLIB_DIR=%{_lib} \
        -DCMAKE_BUILD_TYPE=RELEASE
%endif

make %{?jobs:-j%jobs}

%install
cd build
make install DESTDIR="$RPM_BUILD_ROOT"
install -m0755 -d $RPM_BUILD_ROOT/%{_docdir}/%{bin_name}/
install -m0755 -d $RPM_BUILD_ROOT/%{_libdir}/yui
install -m0644 ../COPYING* $RPM_BUILD_ROOT/%{_docdir}/%{bin_name}/

%clean
rm -rf "$RPM_BUILD_ROOT"

%post -n %{bin_name} -p /sbin/ldconfig

%postun -n %{bin_name} -p /sbin/ldconfig

%files -n %{bin_name}
%defattr(-,root,root)
%dir %{_libdir}/yui
%{_libdir}/yui/lib*.so.*
%doc %dir %{_docdir}/%{bin_name}
%license %{_docdir}/%{bin_name}/COPYING*

%files devel
%defattr(-,root,root)
%dir %{_docdir}/%{bin_name}
%{_libdir}/yui/lib*.so
%{_prefix}/include/yui
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/cmake/%{name}
%{_datadir}/libyui

%files tools
%defattr(-,root,root)
%{_bindir}/libyui-terminal

%changelog
