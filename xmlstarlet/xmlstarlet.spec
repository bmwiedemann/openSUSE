#
# spec file for package xmlstarlet
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


Name:           xmlstarlet
Version:        1.6.1
Release:        0
Summary:        Command Line Tool to Process XML Documents
License:        MIT
Group:          Productivity/Publishing/XML
Url:            http://sourceforge.net/projects/xmlstar/
Source:         http://prdownloads.sourceforge.net/xmlstar/xmlstarlet-%{version}.tar.gz
Source1:        %{name}-rpmlintrc
Patch2:         %{name}-xml_depyx.c.diff
BuildRequires:  libxml2-devel >= 2.6.27
BuildRequires:  libxslt-devel >= 1.1.9
BuildRequires:  pkgconfig
BuildRequires:  sgml-skel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
XMLStarlet (xml) is a command line XML toolkit which can be used to
transform, query, validate, and edit XML documents and files using simple
set of shell commands in similar way it is done for plain text files using
'grep', 'sed', 'awk', 'tr', 'diff', or 'patch'.

%prep
%setup -q
%patch2

%build
export CFLAGS="%{optflags} -W -Wall"
%configure \
  --disable-static-libs \
  --disable-silent-rules
make %{?_smp_mflags}

%check
make %{?_smp_mflags} tests

%install
make %{?_smp_mflags} DESTDIR=%{buildroot} install

install -d _docs
mv "%{buildroot}%{_datadir}/doc"/* _docs/
rm -rf "%{buildroot}%{_datadir}/doc"

cd %{buildroot}%{_bindir}
ln -s xml %{name}

cd %{buildroot}%{_mandir}/man1/
ln -s %{name}.1%{ext_man} xml.1%{ext_man}

%files
%defattr(-, root, root)
%doc AUTHORS ChangeLog NEWS README Copyright TODO
%doc _docs/*
%{_bindir}/xml
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{ext_man}
%{_mandir}/man1/xml.1%{ext_man}

%changelog
