#
# spec file for package prelude-lml-rules
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           prelude-lml-rules
Version:        5.1.0
Release:        0
Summary:        Prelude LML community ruleset
License:        GPL-2.0-or-later
Group:          System/Daemons
Url:            https://www.prelude-siem.org
Source0:        https://www.prelude-siem.org/pkg/src/%{version}/%{name}-%{version}.tar.gz
Patch0:         prelude-lml-rules-fix_shebang.patch
Requires:       prelude-lml
BuildArch:      noarch

%description
Rules for Prelude LML contributed by the community.

%prep
%setup -q
%patch0

%build

%install
mkdir -p %{buildroot}/%{_sysconfdir}/prelude-lml/ruleset
mkdir -p %{buildroot}/%{_bindir}
cp -R $RPM_BUILD_DIR/%{name}-%{version}/ruleset/* %{buildroot}/%{_sysconfdir}/prelude-lml/ruleset/
cp $RPM_BUILD_DIR/%{name}-%{version}/src/%{name}* %{buildroot}/%{_bindir}

%files
%defattr(-,root,root,-)
%doc COPYING NEWS README AUTHORS
%dir %attr(0770,-,-) %{_sysconfdir}/prelude-lml
%dir %attr(0770,-,-) %{_sysconfdir}/prelude-lml/ruleset
%config(noreplace) %attr(0660,-,-) %{_sysconfdir}/prelude-lml/ruleset/*
%attr(775,-,-) %{_bindir}/*

%changelog
