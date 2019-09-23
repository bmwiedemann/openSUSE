#
# spec file for package docbook-toys
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           docbook-toys
BuildRequires:  automake
BuildRequires:  docbook-dsssl-stylesheets
BuildRequires:  openjade
%define sysconfdir %{_sysconfdir}
Provides:       docbook-tools
Requires:       docbook-dsssl-stylesheets
Requires:       docbook_3
Requires:       docbook_4
Requires:       iso_ent
Requires:       openjade
Requires:       texlive-jadetex
Version:        1.51.0
Release:        0
Summary:        DocBook Tools
License:        GPL-2.0+
Group:          Productivity/Publishing/DocBook
Source:         http://www.suse.de/~ke/docbook-toys/docbook-toys-%{version}.tar.bz2
Source1:        %{name}-README.SUSE
Patch0:         docbook-toys-suffix.diff
Patch1:         docbook-toys-outdir.diff
Patch2:         docbook-toys-1.51.0-pdf-exit.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
Url:            http://www.suse.de/~ke/docbook-toys/

%description
A shell script to convert SGML documents based on the DocBook DTD.

For usage information read:

/usr/share/doc/packages/docbook-toys/README

%define INSTALL install -m755 -s
%define INSTALL_DIR install -d -m755
%define INSTALL_DATA install -m644
%define INSTALL_SCRIPT install -m755

%prep
%setup -q -n docbook-toys-%{version}
%{INSTALL_DATA} %{SOURCE1} README.SUSE
%patch -p 1 -P 0
%patch -p 0 -P 1
%patch -p 1 -P 2

%build
autoreconf -i -f
%configure
make %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT install
make DESTDIR=$RPM_BUILD_ROOT mk_links
mkdir -p $RPM_BUILD_ROOT%sysconfdir/%{name}
# move config files to _sysconfdir
pushd $RPM_BUILD_ROOT%{_datadir}/sgml/docbook/docbook-toys
for f in suse-*.dsl gdp-both.dsl docbook-sloppy.dcl; do
  mv $f $RPM_BUILD_ROOT%sysconfdir/%{name}
  ln -s %sysconfdir/%{name}/$f $f
done
popd

%files
%defattr(-, root, root)
%doc README.SUSE
%doc AUTHORS COPYING NEWS README THANKS TODO
%doc texmf.conf.diff
%{_bindir}/*
%{_datadir}/sgml/docbook/docbook-toys
%config %{sysconfdir}/%{name}

%changelog
