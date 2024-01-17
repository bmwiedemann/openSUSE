#
# spec file for package xmlstarlet
#
# Copyright (c) 2023 SUSE LLC
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


Name:           xmlstarlet
Version:        1.6.1
Release:        0
Summary:        Command Line Tool to Process XML Documents
License:        MIT
Group:          Productivity/Publishing/XML
URL:            https://sourceforge.net/projects/xmlstar/
Source:         http://prdownloads.sourceforge.net/xmlstar/xmlstarlet-%{version}.tar.gz
Source1:        %{name}-rpmlintrc
Patch2:         %{name}-xml_depyx.c.diff
BuildRequires:  libxml2-devel >= 2.6.27
BuildRequires:  libxslt-devel >= 1.1.9
BuildRequires:  pkgconfig
BuildRequires:  sgml-skel

%description
XMLStarlet (xml) is a command line XML toolkit which can be used to
transform, query, validate, and edit XML documents and files using simple
set of shell commands in similar way it is done for plain text files using
'grep', 'sed', 'awk', 'tr', 'diff', or 'patch'.

%prep
%autosetup -p0

%build
export CFLAGS="%{optflags} -W -Wall"
%configure \
  --disable-static-libs \
  --disable-silent-rules
%make_build

%check
%make_build tests

%install
%make_install

install -d _docs
mv "%{buildroot}%{_datadir}/doc"/* _docs/
rm -rf "%{buildroot}%{_datadir}/doc"

cd %{buildroot}%{_bindir}
ln -s xml %{name}

cd %{buildroot}%{_mandir}/man1/
ln -s %{name}.1%{ext_man} xml.1%{ext_man}

%files
%license Copyright
%doc AUTHORS ChangeLog NEWS README TODO
%doc _docs/*
%{_bindir}/xml
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_mandir}/man1/xml.1%{?ext_man}

%changelog
