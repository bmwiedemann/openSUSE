#
# spec file for package diffmk
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
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



Name:           diffmk
Url:            http://wwws.sun.com/software/xml/developers/diffmk/
License:        BSD-3-Clause
Group:          Productivity/Publishing/XML
Requires:       perl = %{perl_version}
Requires:       perl-Algorithm-Diff perl-XML-DOM perl-XML-Parser
BuildRequires:  unzip
Summary:        Compute Differences between XML Documents
Version:        1.0
Release:        139
Provides:       perl-diffmk
Obsoletes:      perl-diffmk
Source:         http://wwws.sun.com/software/xml/developers/diffmk/diffmk-1.0.zip
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Using DiffMk, you can build an automated comparison of two XML
documents. The output format for viewing is HTML.

%prep
%setup -T -D -c
unzip -a %{S:0}
%define perl_site %(TMP=%{perl_sitearch}; echo ${TMP%/*})

%build
cp diffmk diffmk.tmp
sed "s|\(\"/\.diffmk\.xml\",\)|\1 \"%{_datadir}/xml/diffmk/dtd/diffmk.xml\",|" \
  diffmk.tmp > diffmk

%install
install -d -m 755 $RPM_BUILD_ROOT%{_bindir} \
  $RPM_BUILD_ROOT%{_datadir}/xml/diffmk/{dtd,xsd,xml}
install -m 755 diffmk $RPM_BUILD_ROOT%{_bindir}
install -m 755 diffmk.dtd $RPM_BUILD_ROOT%{_datadir}/xml/diffmk/dtd
install -m 755 diffmk.xsd $RPM_BUILD_ROOT%{_datadir}/xml/diffmk/xsd
install -m 755 diffmk.xml $RPM_BUILD_ROOT%{_datadir}/xml/diffmk/xml
pushd $RPM_BUILD_ROOT%{_datadir}/xml/diffmk/dtd \
  && ln -sf ../xml/diffmk.xml . \
  && popd

%files
%defattr(-,root,root)
%doc diff.* diffmk.* README.html diff.txt
%doc frames.html out.html out.xml refentry.html refentry.xml test1.html
%doc test1.xml test2.html test2.xml
%{_bindir}/*
%{_datadir}/xml/diffmk

%changelog
