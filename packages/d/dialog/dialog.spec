#
# spec file for package dialog
#
# Copyright (c) 2024 SUSE LLC
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


%define src_date 20240307
%define somajor 15
Name:           dialog
Version:        1.3
Release:        0
Summary:        Menus and Input Boxes for Shell Scripts
License:        LGPL-2.1-only
Group:          Development/Tools/Other
URL:            http://invisible-island.net/dialog/
Source0:        https://www.invisible-island.net/archives/%{name}/%{name}-%{version}-%{src_date}.tgz
Source1:        https://www.invisible-island.net/archives/%{name}/%{name}-%{version}-%{src_date}.tgz.asc
Source2:        %{name}.keyring
Source4:        dialog-rpmlintrc
# PATCH-FIX-OPENSUSE : fix shadow during resizing terminal
Patch0:         dialog-1.2-20121230.dif
Patch2:         dialog-gcc-warnings.patch
Patch3:         dialog-1.3-usretc.diff
BuildRequires:  libtool
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig
Requires:       terminfo-base
Suggests:       terminfo

%description
This program lets you use menus and dialog boxes in shell scripts.

%package     -n libdialog%{somajor}
Summary:        Menus and Input Boxes for Shell Scripts
Group:          System/Libraries

%description -n libdialog%{somajor}
This program lets you use menus and dialog boxes in shell scripts.

%package        devel
Summary:        Menus and Input Boxes for Shell Scripts
Group:          Development/Libraries/Other
Requires:       libdialog%{somajor} = %{version}

%description    devel
This program lets you use menus and dialog boxes in shell scripts.

%package        examples
Summary:        Examples of using dialog tool
Group:          Development/Libraries/Other
Requires:       %{name} = %{version}
BuildArch:      noarch

%description    examples
Examples of using menus and dialog boxes in shell scripts.

%lang_package

%prep
%autosetup -n %{name}-%{version}-%{src_date}

%build
    CC=gcc
    LIBS=""
    CFLAGS="%{optflags} -pipe -Wall -D_GNU_SOURCE"
    for ncurses_conf in ncursesw6-config ncurstesw5-config ; do
	ncurses_conf=$(type -p $ncurses_conf 2> /dev/null) || continue
	LIBS="${LIBS:+$LIBS }$($ncurses_conf --libs)"
	CFLAGS="${CFLAGS:+$CFLAGS }$($ncurses_conf --cflags)"
	NCURSES_CONFIG=$ncurses_conf
	export NCURSES_CONFIG
	break
    done
    export CC LIBS CFLAGS

%configure \
    --enable-nls \
    --enable-included-msgs \
    --enable-widec \
    --with-ncursesw \
    --with-libtool \
    --disable-rpath-hack \
    --includedir=%{_includedir}/dialog

# libtool seems to be broken in shell function func_lalib_unsafe_p()
exec 0</dev/null
make %{?_smp_mflags}

%install
# libtool seems to be broken in shell function func_lalib_unsafe_p()
exec 0</dev/null
%make_install

rm -rf %{buildroot}%{_libdir}/.libs
find %{buildroot} -type f -name "*.la" -delete -print
find %{buildroot}%{_libdir} -name '*.a' -type f -delete -print

rm -rf %{buildroot}%{_datadir}/locale/mg/ # Malagasy (Malayalam??)
rm -rf %{buildroot}%{_datadir}/locale/rm/ # Rhaeto-Romance

mkdir %{buildroot}/etc
> %{buildroot}%{_sysconfdir}/dialogrc
%find_lang %{name}
xz CHANGES

%post -n libdialog%{somajor} -p /sbin/ldconfig
%postun -n libdialog%{somajor} -p /sbin/ldconfig

%files
%defattr(-,root,root)
%if %{defined license}
%license COPYING
%doc CHANGES.xz README VERSION
%else
%doc CHANGES.xz README VERSION COPYING
%endif
%ghost %config(noreplace) %{_sysconfdir}/dialogrc
%{_bindir}/dialog
%{_mandir}/man1/dialog.1%{ext_man}

%files -n libdialog%{somajor}
%defattr(-,root,root)
%{_libdir}/libdialog.so.%{somajor}*

%files devel
%defattr(-,root,root)
%{_bindir}/dialog-config
%{_libdir}/libdialog.so
%{_includedir}/dialog/
%{_mandir}/man3/dialog.3%{ext_man}

%files examples
%defattr(-,root,root)
%doc samples/*

%files lang -f %{name}.lang
%defattr(-,root,root)

%changelog
