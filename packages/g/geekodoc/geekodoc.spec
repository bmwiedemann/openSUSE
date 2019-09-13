#
# spec file for package geekodoc
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


%bcond_without  tests

#
Name:           geekodoc
Version:        1.0.2.1
Release:        0
Summary:        DocBook based RNG Schema for SUSE Documentation
License:        GPL-3.0
Group:          Productivity/Publishing/DocBook
Url:            https://github.com/openSUSE/geekodoc/archive/%{name}-%{version}.tar.gz
Source:         %{name}-%{version}.tar.gz
BuildRequires:  docbook_5 >= 5.1
BuildRequires:  jing
BuildRequires:  libxml2-tools
BuildRequires:  make
BuildRequires:  python3-rnginline
BuildRequires:  python3-setuptools
BuildRequires:  trang
Requires:       sgml-skel >= 0.7
Requires(post): sgml-skel >= 0.7
Requires(postun): sgml-skel >= 0.7
Conflicts:      suse-xsl-stylesheets < 2.0.6
BuildArch:      noarch

%description
GeekoDoc is a RELAX NG schema used for current SUSE documentation.

%package -n novdoc
Version:        1.0_%{version}
Release:        0
Summary:        DocBook based Schema for older SUSE Documentation
Group:          Productivity/Publishing/DocBook
Conflicts:      suse-xsl-stylesheets < 2.0.6

%description -n novdoc
NovDoc is a DTD/RELAX NG schema used for older SUSE documentation.

%prep
%setup -q

%build
touch geekodoc/rng/geekodoc5.rnc
# GeekoDoc
make %{?_smp_mflags} VERBOSE=1 -C geekodoc/rng
make %{?_smp_mflags} VERBOSE=1 -C geekodoc/rng geekodoc5-flat.rng

# Novdoc
make %{?_smp_mflags} VERBOSE=1 -C novdoc/rng

%install
install -d %{buildroot}%{_datadir}/xml/{geekodoc/rng,novdoc/rng} \
           %{buildroot}%{_sysconfdir}/xml/catalog.d

# Install GeekoDoc:
cp geekodoc/rng/geekodoc5-flat.rn? %{buildroot}%{_datadir}/xml/geekodoc/rng

# Install Novdoc:
cp -a novdoc/dtd %{buildroot}%{_datadir}/xml/novdoc
cp novdoc/rng/novdocxi-flat.rn? novdoc/rng/novell.ent %{buildroot}%{_datadir}/xml/novdoc/rng

# Install catalogs:
cp catalog.d/* %{buildroot}%{_sysconfdir}/xml/catalog.d/

# Fixup catalog paths
sed -i 's#"\.\./#"%{_datadir}/xml/#' %{buildroot}%{_sysconfdir}/xml/catalog.d/*

%post
update-xml-catalog

%postun
update-xml-catalog

%post -n novdoc
update-xml-catalog

if [ ! -f %{_sysconfdir}/xml/suse-catalog.xml -a -x %{_bindir}/edit-xml-catalog ] ; then
    # susexsl entry
    edit-xml-catalog --group --catalog %{_sysconfdir}/xml/suse-catalog.xml \
       --del suse_schemas
    edit-xml-catalog --group --catalog %{_sysconfdir}/xml/suse-catalog.xml \
       --del novdoc-1.0
fi
exit 0

%postun -n novdoc
update-xml-catalog

%if 0%{with tests}
%check
cd geekodoc/tests
./run-tests.sh -V xmllint
./run-tests.sh -V jing
%endif

%files
%license LICENSE ChangeLog
%config %{_sysconfdir}/xml/catalog.d/geekodoc.xml
%{_datadir}/xml/geekodoc
%{_datadir}/xml/geekodoc/*

%files -n novdoc
%license LICENSE
%config %{_sysconfdir}/xml/catalog.d/novdoc.xml
%{_datadir}/xml/novdoc
%{_datadir}/xml/novdoc/*

%changelog
