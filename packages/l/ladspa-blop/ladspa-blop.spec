#
# spec file for package ladspa-blop
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           ladspa-blop
Version:        0.2.8
Release:        0
Summary:        LADSPA blop plugins
License:        GPL-2.0+
Group:          Productivity/Multimedia/Sound/Utilities
Url:            http://blop.sourceforge.net/
Source:         blop-%{version}.tar.bz2
Patch1:         blop-automake-fix.dif
Patch2:         blop-shlib.diff
Patch3:         blop-ladspa_dir.diff
Patch4:         blop-wdautil-fix.diff
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  ladspa-devel
BuildRequires:  libtool
Supplements:    ladspa
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package provides a LADSPA (Linux Audio Developer's Simple Plug-in API)
plugins to implement bandlimited sawtooth, square, variable pulse and
slope-variable triangle waves.

%prep
%setup -q -n blop-%{version}
%patch1
%patch2
%patch3
%patch4

%build
# This package failed when testing with -Wl,-as-needed being default.
# So we disable it here, if you want to retest, just delete this comment and the line below.
export SUSE_ASNEEDED=0
autoreconf --install --force
%configure --with-ladspa-plugin-dir=%{_libdir}/ladspa
make %{?_smp_mflags} CFLAGS="%{optflags} -DNO_DEBUG -DPIC -fPIC -ggdb"

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
install -c -m 0644 -D doc/blop.rdf %{buildroot}%{_datadir}/ladspa/rdf/blop.rdf
%find_lang %{name} --all-name

%files -f %{name}.lang
%defattr(-,root,root)
%{_libdir}/ladspa
%{_datadir}/ladspa
%doc COPYING README ChangeLog NEWS THANKS TODO

%changelog
