#
# spec file for package Regina-REXX
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


%define somajor 3
%define libname libregina%{somajor}
Name:           Regina-REXX
Version:        3.9.1
Release:        0
Summary:        Mark Hessling's implementation of the REXX Interpreter
License:        GFDL-1.1-only AND LGPL-2.1-or-later
Group:          Development/Languages/Other
URL:            http://regina-rexx.sourceforge.net/
Source:         http://downloads.sourceforge.net/project/regina-rexx/regina-rexx/%{version}/Regina-REXX-%{version}.tar.gz
Source1:        http://sourceforge.net/projects/regina-rexx/files/regina-documentation/%{version}/regina.pdf#/Regina-REXX-%{version}-doc.pdf
Source2:        http://sourceforge.net/projects/regina-rexx/files/regina-documentation/%{version}/regutil.pdf#/Regina-REXX-regutil-%{version}-doc.pdf
Source3:        rxstack.service
BuildRequires:  distribution-release
BuildRequires:  flex
BuildRequires:  lsb-release
BuildRequires:  ncurses-devel
BuildRequires:  systemd-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
Provides:       rexx
%{?systemd_ordering}

%description
Mark Hessling's implementation of the REXX language interpreter.

%package devel
Summary:        Header files for the REXX interpreter
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}-%{release}
Requires:       %{name} = %{version}-%{release}
Provides:       regina-devel = %{version}-%{release}
Provides:       regina:%{_includedir}/rexxsaa.h

%description devel
This package contains all necessary include files and libraries needed
to develop applications that require Regina-REXX.

%package -n %{libname}
Summary:        The regina shared library
Group:          System/Libraries

%description -n %{libname}
This package provides the shared library for Mark Hessling's implementation
of the REXX Interpreter.

%package doc
Summary:        Documentation for the Regina REXX interpreter
Group:          Documentation/Other

%description doc
Documentation for both the Regina REXX interpreter and the REXX Utility
Functions (regutil).

%prep
%setup -q

%build
%configure \
  --enable-posix-threads
# parallel build seems to randomly fail
make --jobs=1

%install
%make_install
# The supplied init script isn't sufficient for our needs.
rm -v %{buildroot}%{_sysconfdir}/rxstack
install -D -m 0644 %{SOURCE3} %{buildroot}%{_unitdir}/rxstack.service
cp %{SOURCE1} .
cp %{SOURCE2} .
# Do not ship statical library
rm -f %{buildroot}%{_libdir}/libregina.a

install -m 755 -d %{buildroot}/%{_sbindir}
ln -s %{_sbindir}/service %{buildroot}/%{_sbindir}/rcrxstack
ln -s %{_mandir}/man1/regina.1.gz %{buildroot}/%{_mandir}/man1/rexx.1.gz

# adding update-alternatives support (boo#1083875)
install -d %{buildroot}%{_sysconfdir}/alternatives

touch %{buildroot}%{_sysconfdir}/alternatives/rexx
touch %{buildroot}%{_sysconfdir}/alternatives/rxqueue

mv %{buildroot}%{_bindir}/rexx %{buildroot}%{_bindir}/rexx-%{name}
mv %{buildroot}%{_bindir}/rxqueue %{buildroot}%{_bindir}/rxqueue-%{name}

ln -sf %{_sysconfdir}/alternatives/rexx %{buildroot}%{_bindir}/rexx
ln -sf %{_sysconfdir}/alternatives/rxqueue %{buildroot}%{_bindir}/rxqueue

# Drop not needed examples/addons
rm -rf  %{buildroot}%{_datadir}/Regina-REXX/addons

%pre
%service_add_pre rxstack.service

%post
%service_add_post rxstack.service
update-alternatives --install \
   %{_bindir}/rexx rexx %{_bindir}/rexx-%{name} 15
update-alternatives --install \
   %{_bindir}/rxqueue rxqueue %{_bindir}/rxqueue-%{name} 15

%preun
%service_del_preun rxstack.service

%postun
%service_del_postun rxstack.service
if [ ! -f %{_bindir}/rexx ] ; then
   update-alternatives --remove rexx %{_bindir}/rexx-%{name}
fi
if [ ! -f %{_bindir}/rxqueue ] ; then
   update-alternatives --remove rxqueue %{_bindir}/rxqueue-%{name}
fi

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files
%{_mandir}/man1/*
%doc COPYING-LIB README.*
%ghost %{_sysconfdir}/alternatives/rexx
%ghost %{_sysconfdir}/alternatives/rxqueue
%{_bindir}/regina
%{_bindir}/rexx
%{_bindir}/rexx-%{name}
%{_bindir}/rxqueue
%{_bindir}/rxqueue-%{name}
%{_bindir}/rxstack
%{_datadir}/Regina-REXX
%{_sbindir}/rcrxstack
%{_unitdir}/rxstack.service

%files doc
%doc Regina-REXX-%{version}-doc.pdf Regina-REXX-regutil-%{version}-doc.pdf

%files devel
%{_bindir}/regina-config
%{_includedir}/*
%{_libdir}/libregina.so

%files -n %{libname}
%{_libdir}/libregina.so.%{somajor}*

%changelog
