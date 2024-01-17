#
# spec file for package amavisd-milter
#
# Copyright (c) 2022 SUSE LLC
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


Name:           amavisd-milter
Version:        1.7.2
Release:        0
Summary:        Sendmail milter for amavisd-new using the AM.PDP protocol
License:        BSD-3-Clause
Group:          Productivity/Networking/Security
URL:            https://github.com/prehor/amavisd-milter
Source0:        https://github.com/prehor/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.service
BuildRequires:  sendmail-devel >= 8.12.0
Requires:       amavisd-new
Supplements:    (amavisd-new and sendmail)
Conflicts:      %{name} < %{version}
%{?systemd_ordering}

%description
The amavisd-milter is a sendmail milter (mail filter) for amavisd-new
2.4.3 (and above) and sendmail 8.12 (and above) which use the new AM.PDP
protocol.

%prep
%setup -q

%build
%configure --localstatedir=%{_localstatedir}/spool/amavis
%make_build

%install
%make_install
mkdir -p %{buildroot}%{_unitdir}
install -m 644 %{SOURCE1} %{buildroot}%{_unitdir}
ln -s service %{buildroot}%{_sbindir}/rc%{name}

%pre
%service_add_pre %{name}.service

%preun
%service_del_preun %{name}.service

%post
%service_add_post %{name}.service

%postun
%service_del_postun %{name}.service

%files
%license LICENSE
%doc CHANGES AMAVISD-MILTER.md
%{_sbindir}/*
%{_unitdir}/*
%{_mandir}/man8/%{name}.8%{?ext_man}

%changelog
