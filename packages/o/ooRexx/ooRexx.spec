#
# spec file for package ooRexx
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Version:        5.2.0
Release:        0
Summary:        Open Object REXX
License:        CPL-1.0
URL:            https://www.rexxla.org
Source0:        https://master.dl.sourceforge.net/project/oorexx/oorexx/5.2.0/oorexx-5.2.0-13156.tar.gz
Source1:        ooRexx-rpmlintrc
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(ncurses)
Requires:       alts
Requires:       liboorexx4 = %{version}
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
BuildArch:      noarch

%package -n liboorexx4
Summary:        Open Object REXX libraries

%description devel
Development files for Open Object Rexx. These are intended for developing REXX extensions only.

%description -n liboorexx4
Library files for Open Object Rexx.

%prep
%autosetup -n oorexx-5.2.0-13156

%build
# Remove cmake4 error due to not setting
# min cmake version - sflees.de
export CMAKE_POLICY_VERSION_MINIMUM=3.5
# reproducible builds: https://sourceforge.net/p/oorexx/bugs/1712/
setarch -R

# disable optimizations that could cause segfaults in REXX threading
export CFLAGS="-Og"
export CXXFLAGS="-Og"

%cmake -DORX_REXXPATH=%{_rexxpath} -DORX_SHEBANG=%{_bindir}/rexx -DBUILD_RPM=1
%cmake_build

%install
%cmake_install

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

Name:           %{name}
Description: Open Object Rexx
Version:        %{version}
Libs: -L\${libdir} -lrexx -lrexxapi
Cflags: -I\${includedir}
EOF

mkdir -p %{buildroot}%{_sysconfdir}/rpm
cat > %{buildroot}%{_sysconfdir}/rpm/oorexx.macros << EOF
%{_ooRexx}        $(echo %{version} | cut -d. -f1)
%{_rexxclassdir}  %{_rexxpath}
%{_rexxlibdir}    %{_libdir}
EOF

# adding libalternatives support (boo#1083875)
# rexxc and rxsubcom need to be renamed upstream! rexx and rxqueue are okay already.
mv %{buildroot}/%{_bindir}/rexx %{buildroot}/%{_bindir}/rexx-oorexx
mv %{buildroot}/%{_bindir}/rexxc %{buildroot}/%{_bindir}/rexxc-oorexx
mv %{buildroot}/%{_bindir}/rxsubcom %{buildroot}/%{_bindir}/rxsubcom-oorexx
mv %{buildroot}/%{_bindir}/rxqueue %{buildroot}/%{_bindir}/rxqueue-oorexx

# rexx and rxqueue form a group: rxqueue is the queue client of the very
# interpreter that serves the queue, so it should follow the selected rexx.
# libalternatives switches a group according to the group declared by the
# *selected* alternative, so this becomes effective for a switch away from
# ooRexx once Regina-REXX -- the other provider of these two commands --
# declares group=rexx,rxqueue as well. Until then it is simply inert.
for b in rexx rxqueue; do
    ln -s %{_bindir}/alts %{buildroot}%{_bindir}/$b
    install -d %{buildroot}%{_datadir}/libalternatives/$b
    cat > %{buildroot}%{_datadir}/libalternatives/$b/20.conf <<EOF
binary=%{_bindir}/$b-oorexx
man=$b.1
group=rexx,rxqueue
EOF
done

# rexxc and rxsubcom have no competing provider, so they stay ungrouped:
# a group bigger than any other provider can offer would only advertise
# members that can never be switched along.
for b in rexxc rxsubcom; do
    ln -s %{_bindir}/alts %{buildroot}%{_bindir}/$b
    install -d %{buildroot}%{_datadir}/libalternatives/$b
    cat > %{buildroot}%{_datadir}/libalternatives/$b/20.conf <<EOF
binary=%{_bindir}/$b-oorexx
man=$b.1
EOF
done

# removing binary samples to avoid OBS warnings
rm %{buildroot}%{_datadir}/ooRexx/samples/api/c++/callsample/{runRexxProgram,stackOverflow}
rm %{buildroot}%{_datadir}/ooRexx/samples/api/c++/external/libexternal*so
rm %{buildroot}%{_datadir}/ooRexx/samples/api/classic/callrexx/callrexx*
rm %{buildroot}%{_datadir}/ooRexx/samples/api/classic/rexxapi*/librexxapi*.so

%check

%post -n liboorexx4 -p /sbin/ldconfig
%postun -n liboorexx4 -p /sbin/ldconfig

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
%{_bindir}/*dtd
%{_bindir}/*xsd
%{_bindir}/*xsl

# libalternatives: plain symlinks to alts. Regina-REXX ships byte-identical
# rexx and rxqueue links, which rpm allows both packages to own.
%{_bindir}/rexx
%{_bindir}/rexxc
%{_bindir}/rxqueue
%{_bindir}/rxsubcom

%dir %{_datadir}/libalternatives
%dir %{_datadir}/libalternatives/rexx
%{_datadir}/libalternatives/rexx/20.conf
%dir %{_datadir}/libalternatives/rexxc
%{_datadir}/libalternatives/rexxc/20.conf
%dir %{_datadir}/libalternatives/rxqueue
%{_datadir}/libalternatives/rxqueue/20.conf
%dir %{_datadir}/libalternatives/rxsubcom
%{_datadir}/libalternatives/rxsubcom/20.conf

%files -n liboorexx4
%{_libdir}/lib*

%files devel
%config %{_sysconfdir}/rpm/*
%{_includedir}/*
%{_datadir}/pkgconfig/*

%dir %{_datadir}/ooRexx/samples
%{_datadir}/ooRexx/samples/*

%changelog
