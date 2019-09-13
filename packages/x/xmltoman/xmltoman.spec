#
# spec file for package xmltoman
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


Name:           xmltoman
Version:        0.4
Release:        0
Summary:        Scripts to convert xml to man pages or html
License:        GPL-2.0-only
Group:          Development/Tools/Doc Generators
URL:            https://github.com/Distrotech/xmltoman
Source:         https://github.com/Distrotech/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  perl(XML::Parser)
BuildArch:      noarch

%description
xmltoman and xmlmantohtml are two very simple scripts for converting xml
to groff or html.

%prep
%setup -q

%build
%make_build PREFIX=%{_prefix}

%install
%make_install PREFIX=%{_prefix}

%files
%license COPYING
%doc ChangeLog README
%{_bindir}/xmlmantohtml
%{_bindir}/xmltoman
%dir %{_datadir}/xmltoman
%{_datadir}/xmltoman/xmltoman.css
%{_datadir}/xmltoman/xmltoman.dtd
%{_datadir}/xmltoman/xmltoman.xsl

%changelog
