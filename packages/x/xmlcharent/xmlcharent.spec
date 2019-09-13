#
# spec file for package xmlcharent
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


Name:           xmlcharent
Version:        0.3
Release:        0
Summary:        XML Character Entities
License:        BSD-3-Clause
Group:          Productivity/Publishing/XML
Url:            http://www.oasis-open.org/docbook/xmlcharent/
Source0:        xmlcharent-0.3.tar.bz2
Source1:        xmlcharent.xml
Source2:        xmlcharent.sgml
Requires:       sgml-skel >= 0.7
Requires(post): sgml-skel >= 0.7
Requires(postun): sgml-skel >= 0.7
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
XML encodings for the 19 standard character entity sets defined in
non-normative Annex D of [ISO 8879:1986].

%prep
%setup -q -n %{name}-%{version}
sed 's|__DIR__|%{_datadir}/%{name}|' %{SOURCE1} > xmlcharent.xml
sed 's|__DIR__|%{_datadir}/%{name}|' %{SOURCE2} > xmlcharent.sgml

%build

%install
%{__mkdir} -p %{buildroot}%{_datadir}/%{name}/entities/
%{__install} -m 0664 -D *.ent %{buildroot}%{_datadir}/%{name}/entities/
%{__install} -m 0644 -D xmlcharent.xml %{buildroot}%{_sysconfdir}/xml/catalog.d/%{name}.xml
%{__install} -m 0644 -D xmlcharent.sgml %{buildroot}%{_datadir}/%{name}/%{name}.sgml

%post
update-xml-catalog
sgml-register-catalog -a %{_datadir}/%{name}/%{name}.sgml

%postun
update-xml-catalog
sgml-register-catalog -r %{_datadir}/%{name}/%{name}.sgml

%files
%defattr(-, root, root)
%{_datadir}/%{name}
%{_sysconfdir}/xml/catalog.d/%{name}.xml

%changelog
