#
# spec file for package swipl
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           swipl
Version:        7.6.4
Release:        0
Summary:        Prolog Compiler
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Development/Languages/Other
Url:            http://www.swi-prolog.org
Source0:        http://www.swi-prolog.org/download/stable/src/swipl-%{version}.tar.gz
Source98:       swipl-rpmlintrc
# For SOURCE_DATE_EPOCH variable- reproducible builds
Source99:       %{name}.changes
# PATCH-FIX-OPENSUSE swipl-ppc64.patch - Fix configure on PowerPC architecture
Patch0:         swipl-ppc64.patch
# PATCH-FIX-UPSTREAM pkgconfig.patch - Fix location of include files in pkgconfig file
Patch1:         pkgconfig.patch
BuildRequires:  db-devel
BuildRequires:  fdupes
BuildRequires:  freetype2-devel
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  java-devel >= 1.7.0
BuildRequires:  libarchive-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libunwind-devel
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
BuildRequires:  unixODBC-devel
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(libedit)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(ossp-uuid)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xt)
# For %%check
BuildRequires:  junit
Provides:       swi-prolog = %{version}
Provides:       swi_pl = %{version}
Obsoletes:      swi-prolog < %{version}
Obsoletes:      swi_pl < %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Edinburgh-style Prolog compiler including modules, autoload, libraries,
Garbage collector, stack expandor, C interface, GNU readline and GNU
Emacs interface, a very fast compiler,and an X11 interface using XPCE.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
export SOURCE_DATE_EPOCH="$(sed -n '/^----/n;s/ - .*$//;p;q' %{SOURCE99} | date -u -f - +%%s)"
%configure --with-world
make %{?_smp_mflags}

%check
make %{?_smp_mflags} check

%install
make DESTDIR=%{buildroot} install-world

# Fix installation of documentation
mkdir -p %{buildroot}%{_docdir}
mv -v %{buildroot}%{_libdir}/%{name}-%{version}/doc  %{buildroot}%{_docdir}/%{name}-%{version}
mv -v %{buildroot}%{_libdir}/%{name}-%{version}/demo %{buildroot}%{_docdir}/%{name}-%{version}
ln -s %{_docdir}/%{name}-%{version} %{buildroot}%{_libdir}/%{name}-%{version}/doc
ln -s %{_docdir}/%{name}-%{version} %{buildroot}%{_libdir}/%{name}-%{version}/demo

# Fix script
chmod +x %{buildroot}%{_libdir}/swipl-%{version}/library/dialect/sicstus/swipl-lfr.pl
sed -i "s@%{_bindir}/../swipl.sh@%{_bindir}/swipl@" %{buildroot}%{_docdir}/%{name}-%{version}/packages/examples/pldoc/man_server.pl

# Create common symlink for "pl"
ln -s swipl %{buildroot}%{_bindir}/pl

%fdupes %{buildroot}/%{_libdir}/%{name}-%{version}
%fdupes %{buildroot}/%{_docdir}/%{name}-%{version}

%files
%defattr(-,root,root,-)
%license LICENSE
%{_bindir}/pl
%{_bindir}/swipl
%{_bindir}/swipl-ld
%{_bindir}/swipl-rc
%{_bindir}/xpce-client
%{_libdir}/%{name}-%{version}
%{_libdir}/pkgconfig/%{name}.pc
%{_mandir}/man1/swipl-ld.1%{ext_man}
%{_mandir}/man1/swipl-rc.1%{ext_man}
%{_mandir}/man1/swipl.1%{ext_man}
%{_mandir}/man1/xpce-client.1%{ext_man}
%doc %{_docdir}/%{name}-%{version}

%changelog
