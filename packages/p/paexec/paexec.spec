#
# spec file for package paexec
#
# Copyright (c) 2024 SUSE LLC
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


Name:           paexec
Version:        1.1.6
Release:        0
Summary:        Utility for task distribution over networks or CPUs
License:        MIT
Group:          Productivity/Clustering/Computing
URL:            https://paexec.sourceforge.net/
Source0:        https://sourceforge.net/projects/paexec/files/paexec/paexec-%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}-rpmlintrc
BuildRequires:  libmaa-devel >= 1.5.1
BuildRequires:  mk-configure >= 0.27.0
BuildRequires:  mk-configure-rpm-macros
BuildRequires:  runawk
Requires:       runawk

%description
A program that processes a list of tasks in parallel
on different CPUs, computers in a network or whatever else.

%package examples
Summary:        Examples for paexec
Group:          Documentation/Other
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description examples
A program that processes a list of tasks in parallel
on different CPUs, computers in a network or whatever else.

This package contains examples for paexec.

%prep
%setup -q
sed -i 's|#!/usr/bin/env |#!%{_bindir}/|' examples/*/* paexec/paexec_reorder

%define env export EGDIR=%{_docdir}/%{name}/examples DESTDIR=%{buildroot}
%define _mkcmake %{mkcmake} DOCDIR=%{_docdir}/%{name}

mkdir -p /var/tmp/mkcmake-home/.mkcmake

%build
%{env}
%{_mkcmake} all all-examples all-doc

%install
%{env}
%{_mkcmake} install install-examples install-doc
cp presentation/paexec.pdf %{buildroot}/%{_docdir}/%{name}

%files
%dir %{_docdir}/paexec
%{_bindir}/paargs
%{_bindir}/paexec
%{_bindir}/paexec_reorder
%{_bindir}/pareorder
%{_mandir}/man1/paargs.1%{?ext_man}
%{_mandir}/man1/paexec.1%{?ext_man}
%{_mandir}/man1/paexec_reorder.1%{?ext_man}
%{_mandir}/man1/pareorder.1%{?ext_man}
%{_docdir}/paexec/paexec.pdf
%{_docdir}/paexec/LICENSE
%{_docdir}/paexec/NEWS
%{_docdir}/paexec/README
%{_docdir}/paexec/TODO

%files examples
%dir %{_docdir}/paexec/examples
%{_docdir}/paexec/examples/*

%changelog
