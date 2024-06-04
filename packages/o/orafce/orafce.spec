#
# spec file for package orafce
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


%define		pgname @BUILD_FLAVOR@
%define		realname orafce

Name:           %{pgname}-orafce
Version:        4.10.3+git0.e050dd6
Release:        0
Summary:        Implementation of some Oracle functions into PostgreSQL
Group:          Productivity/Databases/Tools
License:        MIT
URL:            https://github.com/orafce/orafce
Source0:        %{realname}-%{version}.tar.gz
BuildRequires:  %{pgname}-server-devel
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  krb5-devel
BuildRequires:  libicu-devel
BuildRequires:  openssl-devel
%requires_eq    %{pgname}-server
Provides:       orafce = %{version}-%{release}
%if "%{pgname}" == ""
ExclusiveArch:  do_not_build
Name:           %{realname}
%endif

%description
The goal of this project is implementation some functions from Oracle database.
Some date functions (next_day, last_day, trunc, round, ...) are implemented
now. Functionality was verified on Oracle 10g and module is useful
for production work.

%prep
%setup -q -n %{realname}-%{version}

%build
export PATH="$PATH:/usr/lib/%{pgname}/bin"
make USE_PGXS=1 %{?_smp_mflags} FLEX=/usr/bin/flex

%install
export PATH="$PATH:/usr/lib/%{pgname}/bin"
make USE_PGXS=1 install DESTDIR=$RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc COPYRIGHT.orafce INSTALL.orafce README.asciidoc NEWS
%{_prefix}/lib/%{pgname}/%{_lib}
%{_datadir}/%{pgname}/
%exclude %{_docdir}/%{pgname}/

%changelog
