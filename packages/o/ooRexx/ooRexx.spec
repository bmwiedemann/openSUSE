#
# spec file for package oorexx
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

%define _rexxpath %{_datadir}/ooRexx
Name:           ooRexx
Version:        5.0.0
Release:        0
Summary:        Open Object REXX
License:        CPL-1.0
Group:          Development/Languages/Other
URL:            https://www.rexxla.org
Source:         https://master.dl.sourceforge.net/project/oorexx/oorexx/5.0.0/oorexx-5.0.0-12583.tar.gz
Source1:        %{name}-rpmlintrc
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ncurses-devel
Requires(post): %{_sbindir}/update-alternatives
Requires(postun): %{_sbindir}/update-alternatives
Obsoletes:      ooRexx <= 4.2.0
Provides:       ooRexx = %{version}

%description
Open Object Rexx is an object-oriented scripting language. The language is designed for both beginners and experienced Rexx programmers. It is easy to learn and use, and provides an excellent vehicle to enter the
world of object-oriented programming without much effort.

It extends the procedural way of Rexx programming with object-oriented features that allow you to gradually change your programming style as you learn more about objects.

For more information on ooRexx, visit http://www.oorexx.org/
For more information on Rexx, visit http://www.rexxla.org/

%package devel
Summary:        Open Object REXX development files
Group:          Development/Languages/Other
BuildArch:      noarch

%package -n liboorexx4
Summary:        Open Object REXX libraries
Group:          Development/Languages/Other

%description devel
Development files for Open Object Rexx. These are intended for developing REXX extensions only.

%description -n liboorexx4
Library files for Open Object Rexx.

%prep
mkdir -p src build
tar -C src -xvzf %{SOURCE0}

%build
cd build

# reproducible builds: https://sourceforge.net/p/oorexx/bugs/1712/
setarch -R

# FIXME: you should use the %%cmake macros
cmake -S ../src -DORX_REXXPATH=%{_rexxpath} -DORX_SHEBANG=%{_bindir}/rexx -DBUILD_RPM=1 -DCMAKE_INSTALL_PREFIX=%{_prefix}
%make_build -O -j 2

%install
cd build
%make_install

# create a pkgconfig file
mkdir -p %{buildroot}%{_datadir}/pkgconfig
cat > %{buildroot}%{_datadir}/pkgconfig/%{name}.pc << EOF
prefix=%{_prefix}
exec_prefix=%{_prefix}
libdir=%{_libdir}
includedir=%{_includedir}

%{name}_binary_version=%{version}
%{name}_major=$(echo %{version} | cut -d. -f1)
%{name}_minor=$(echo %{version} | cut -d. -f2)

Name: %{name}
Description: Open Object Rexx
Version: %{version}
Libs: -L\${libdir} -lrexx -lrexxapi
Cflags: -I\${includedir}
EOF

mkdir -p %{buildroot}%{_sysconfdir}/rpm
cat > %{buildroot}%{_sysconfdir}/rpm/oorexx.macros << EOF
%{_ooRexx}        $(echo %{version} | cut -d. -f1)
%{_rexxclassdir}  %{_rexxpath}
%{_rexxlibdir}    %{_libdir}
EOF

# adding update-alternatives support (boo#1083875)
mkdir -p %{buildroot}%{_sysconfdir}/alternatives

# rexxc and rxsubcom need to be renamed upstream! rexx and rxqueue are okay already.
mv %{buildroot}/%{_bindir}/rexx %{buildroot}/%{_bindir}/rexx-oorexx
mv %{buildroot}/%{_bindir}/rexxc %{buildroot}/%{_bindir}/rexxc-oorexx
mv %{buildroot}/%{_bindir}/rxsubcom %{buildroot}/%{_bindir}/rxsubcom-oorexx
mv %{buildroot}/%{_bindir}/rxqueue %{buildroot}/%{_bindir}/rxqueue-oorexx

ln -s  %{_sysconfdir}/alternatives/rexx %{buildroot}%{_bindir}/rexx
ln -s  %{_sysconfdir}/alternatives/rexxc %{buildroot}%{_bindir}/rexxc
ln -s  %{_sysconfdir}/alternatives/rxqueue %{buildroot}%{_bindir}/rxqueue
ln -s  %{_sysconfdir}/alternatives/rxsubcom %{buildroot}%{_bindir}/rxsubcom

# removing binary samples to avoid OBS warnings
rm %{buildroot}%{_datadir}/ooRexx/samples/api/c++/callsample/{runRexxProgram,stackOverflow}
rm %{buildroot}%{_datadir}/ooRexx/samples/api/c++/external/libexternal*so
rm %{buildroot}%{_datadir}/ooRexx/samples/api/classic/callrexx/callrexx*
rm %{buildroot}%{_datadir}/ooRexx/samples/api/classic/rexxapi*/librexxapi*.so

%check

%post
update-alternatives --install %{_bindir}/rexx rexx %{_bindir}/rexx-oorexx 20
update-alternatives --install %{_bindir}/rexxc rexxc %{_bindir}/rexxc-oorexx 20
update-alternatives --install %{_bindir}/rxqueue rxqueue %{_bindir}/rxqueue-oorexx 20
update-alternatives --install %{_bindir}/rxsubcom rxsubcom %{_bindir}/rxsubcom-oorexx 20

%postun
if [ ! -f %{_bindir}/rexx-oorexx ] ; then
  update-alternatives --remove rexx %{_bindir}/rexx-oorexx
fi

if [ ! -f %{_bindir}/rexxc-oorexx ] ; then
  update-alternatives --remove rexxc %{_bindir}/rexxc-oorexx
fi

if [ ! -f %{_bindir}/rxqueue-oorexx ] ; then
  update-alternatives --remove rxqueue %{_bindir}/rxqueue-oorexx
fi

if [ ! -f %{_bindir}/rxsubcom-oorexx ] ; then
  update-alternatives --remove rxsubcom %{_bindir}/rxsubcom-oorexx
fi

%post -n liboorexx4 -p /sbin/ldconfig
%postun -n liboorexx4 -p /sbin/ldconfig

%changelog
%files
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/48x48
%dir %{_datadir}/icons/hicolor/48x48/apps
%dir %{_datadir}/ooRexx

%{_mandir}/man1/*
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/48x48/apps/*

%{_libdir}/rexx.img
%{_bindir}/rexxtry.rex
%{_bindir}/rxapi
%{_bindir}/rexx-oorexx
%{_bindir}/rexxc-oorexx
%{_bindir}/rxqueue-oorexx
%{_bindir}/rxsubcom-oorexx
%{_bindir}/*cls

%ghost %{_bindir}/rexx
%ghost %{_bindir}/rexxc
%ghost %{_bindir}/rxqueue
%ghost %{_bindir}/rxsubcom

%ghost %attr(0755,root,root) %{_sysconfdir}/alternatives/rexx
%ghost %attr(0755,root,root) %{_sysconfdir}/alternatives/rexxc
%ghost %attr(0755,root,root) %{_sysconfdir}/alternatives/rxqueue
%ghost %attr(0755,root,root) %{_sysconfdir}/alternatives/rxsubcom
%ghost %attr(0644,root,root) %{_sysconfdir}/alternatives/rexx.1
%ghost %attr(0644,root,root) %{_sysconfdir}/alternatives/rexxc.1
%ghost %attr(0644,root,root) %{_sysconfdir}/alternatives/rxqueue.1
%ghost %attr(0644,root,root) %{_sysconfdir}/alternatives/rxsubcom.1

%files -n liboorexx4
%{_libdir}/lib*

%files devel
%config %{_sysconfdir}/rpm/*
%{_includedir}/*
%{_datadir}/pkgconfig/*

%dir %{_datadir}/ooRexx/samples
%{_datadir}/ooRexx/samples/*

%changelog
