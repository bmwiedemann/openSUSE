#
# spec file for package ladspa-swh-plugins
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define tarname ladspa

Name:           ladspa-swh-plugins
Version:        0.4.17
Release:        0
Summary:        LADSPA SWH plugins
License:        GPL-2.0+
Group:          Productivity/Multimedia/Sound/Utilities
Url:            http://plugin.org.uk/
Source:         https://github.com/swh/ladspa/archive/v%{version}.tar.gz#/%{tarname}-%{version}.tar.gz
Source1:        ladspa-swh.tex
Source2:        ladspa-swh.pdf
Patch1:         swh-uninit-variable.diff
Patch2:         swh-readonly.dif
Patch3:         swh-0.4.13-gcc4-fix.diff
Patch5:         swh-libblo.dif
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fftw3-devel
BuildRequires:  gcc
BuildRequires:  ladspa-devel
BuildRequires:  libtool
BuildRequires:  perl-XML-Parser
BuildRequires:  pkgconfig
Supplements:    ladspa
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package provides a collection of LADSPA (Linux Audio Developer's
Simple Plug-in API) plugins written by Steve Harris.


%prep
%setup -q -n %{tarname}-%{version}
# This creates the .c files from .xml files.
for i in `ls -1 *.xml|cut -f 1 -d .` ;do ./makestub.pl "$i.xml" > "$i.c";done
%patch1
%patch2
%patch3
%patch5
cp gsm/README README-gsm
cp %{SOURCE1} .
cp %{SOURCE2} .

%build
# This replaces the wrong version with the right one in configure.ac
# see https://github.com/swh/ladspa/issues/41.
sed s/0.4.15/%{version}/ configure.ac>configure.ac1
mv configure.ac1 configure.ac

autoreconf -i -I m4
# This package failed when testing with -Wl,-as-needed being default.
# So we disable it here, if you want to retest, just delete this comment and the line below.
export SUSE_ASNEEDED=0
CFLAGS="%{optflags} -fPIC -ggdb -DPIC -fno-strict-aliasing" \
./configure --prefix=%{_prefix} \
              --disable-rpath \
              --enable-shared \
              --enable-dependency-tracking \
              --disable-static
make %{?_smp_mflags} CFLAGS="%{optflags} -fPIC -ggdb -DPIC -fno-strict-aliasing"
#
%install
make DESTDIR=%{buildroot} plugindir=%{_libdir}/ladspa install
%find_lang %{name} --all-name

%files -f %{name}.lang
%defattr(-,root,root)
%{_libdir}/ladspa
%{_datadir}/ladspa
%doc AUTHORS COPYING ChangeLog README TODO README-gsm
%doc ladspa-swh.tex
%doc ladspa-swh.pdf

%changelog
