#
# spec file for package tetrinet-server
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


Name:           tetrinet-server
BuildRequires:  libadns-devel
%define realname	tetrinetx
%define qirc_version	1.40c
Version:        1.13.16
Release:        0
URL:            http://tetrinetx.sourceforge.net/
Summary:        The GNU TetriNET server
License:        GPL-2.0-or-later
Group:          Amusements/Games/Logic
Source:         %{realname}-%{version}+qirc-%{qirc_version}.tar.bz2
Patch2:         %{realname}.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Tetrinetx-qirc1.40c with Async DNS support for high productivity
server.

%prep
%setup -n %{realname}-%{version}+qirc-%{qirc_version}
%patch2

%build
export CFLAGS="$RPM_OPT_FLAGS"
cd src
sed -e 's@\(^#define [[:alnum:]_]* *"\)\(game\.\)@\1%{_datadir}/%{realname}/\2@' \
config.h >config.h1
mv config.h1 config.h
sed -e 's@\(^pidfile=\)\(game\.pid$\)@\1%{_datadir}/%{realname}/\2@' \
../bin/game.conf >../bin/game.conf1
mv ../bin/game.conf1 ../bin/game.conf
INCLUDE_DIR=$RPM_BUILD_ROOT%{_includedir} \
LIB_DIR=$RPM_BUILD_ROOT%{_libdir} \
./c

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mv bin/tetrix.linux $RPM_BUILD_ROOT%{_bindir}/%{realname}
ln -sf %{_bindir}/%{realname} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -m 755 -d $RPM_BUILD_ROOT%{_datadir}/%{realname}
cp -r bin/* $RPM_BUILD_ROOT%{_datadir}/%{realname}/

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog README README.qirc.spectators
%{_bindir}/*
%{_datadir}/%{realname}/

%changelog
