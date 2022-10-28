#
# spec file for package sca-patterns-hae
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


%define sca_common sca
%define patdirbase /usr/lib/%{sca_common}
%define patdir %{patdirbase}/patterns
%define patuser root
%define patgrp root
%define mode 544
%define category HAE

Name:           sca-patterns-hae
Version:        1.5.2
Release:        0
Summary:        Supportconfig Analysis Patterns for HAE
License:        GPL-2.0-only
URL:            https://github.com/g23guy/sca-patterns-hae
Group:          System/Monitoring
Source:         %{name}-%{version}.tar.gz
BuildRequires:  fdupes
Requires:       sca-patterns-base >= 1.5.0
Requires:       sca-server-report >= 1.5.1
BuildArch:      noarch

%description
Supportconfig Analysis (SCA) appliance patterns to identify known
issues relating to all versions of High Availability Extension (HAE)
clustering

See %{_docdir}/sca-patterns-base/COPYING.GPLv2

%prep
%setup -q

%build

%install
pwd;ls -la
install -d %{buildroot}/%{patdir}/%{category}
install -d %{buildroot}/%{patdir}/%{category}/hae11all
install -d %{buildroot}/%{patdir}/%{category}/hae11sp0
install -d %{buildroot}/%{patdir}/%{category}/hae11sp1
install -d %{buildroot}/%{patdir}/%{category}/hae11sp2
install -d %{buildroot}/%{patdir}/%{category}/hae11sp3
install -d %{buildroot}/%{patdir}/%{category}/hae11sp4
install -m %{mode} patterns/%{category}/hae11all/* %{buildroot}/%{patdir}/%{category}/hae11all
install -m %{mode} patterns/%{category}/hae11sp0/* %{buildroot}/%{patdir}/%{category}/hae11sp0
install -m %{mode} patterns/%{category}/hae11sp1/* %{buildroot}/%{patdir}/%{category}/hae11sp1
install -m %{mode} patterns/%{category}/hae11sp2/* %{buildroot}/%{patdir}/%{category}/hae11sp2
install -m %{mode} patterns/%{category}/hae11sp3/* %{buildroot}/%{patdir}/%{category}/hae11sp3
install -m %{mode} patterns/%{category}/hae11sp4/* %{buildroot}/%{patdir}/%{category}/hae11sp4

install -d %{buildroot}/%{patdir}/%{category}/hae12all
install -d %{buildroot}/%{patdir}/%{category}/hae12sp0
install -d %{buildroot}/%{patdir}/%{category}/hae12sp1
install -d %{buildroot}/%{patdir}/%{category}/hae12sp2
install -d %{buildroot}/%{patdir}/%{category}/hae12sp3
install -d %{buildroot}/%{patdir}/%{category}/hae12sp4
install -d %{buildroot}/%{patdir}/%{category}/hae12sp5
install -m %{mode} patterns/%{category}/hae12all/* %{buildroot}/%{patdir}/%{category}/hae12all
install -m %{mode} patterns/%{category}/hae12sp0/* %{buildroot}/%{patdir}/%{category}/hae12sp0
install -m %{mode} patterns/%{category}/hae12sp1/* %{buildroot}/%{patdir}/%{category}/hae12sp1
install -m %{mode} patterns/%{category}/hae12sp2/* %{buildroot}/%{patdir}/%{category}/hae12sp2
install -m %{mode} patterns/%{category}/hae12sp3/* %{buildroot}/%{patdir}/%{category}/hae12sp3
install -m %{mode} patterns/%{category}/hae12sp4/* %{buildroot}/%{patdir}/%{category}/hae12sp4
install -m %{mode} patterns/%{category}/hae12sp5/* %{buildroot}/%{patdir}/%{category}/hae12sp5

install -d %{buildroot}/%{patdir}/%{category}/hae15all
install -d %{buildroot}/%{patdir}/%{category}/hae15sp0
install -d %{buildroot}/%{patdir}/%{category}/hae15sp1
install -d %{buildroot}/%{patdir}/%{category}/hae15sp2
install -d %{buildroot}/%{patdir}/%{category}/hae15sp3
install -d %{buildroot}/%{patdir}/%{category}/hae15sp4
install -m %{mode} patterns/%{category}/hae15all/* %{buildroot}/%{patdir}/%{category}/hae15all
install -m %{mode} patterns/%{category}/hae15sp0/* %{buildroot}/%{patdir}/%{category}/hae15sp0
install -m %{mode} patterns/%{category}/hae15sp1/* %{buildroot}/%{patdir}/%{category}/hae15sp1
install -m %{mode} patterns/%{category}/hae15sp2/* %{buildroot}/%{patdir}/%{category}/hae15sp2
install -m %{mode} patterns/%{category}/hae15sp3/* %{buildroot}/%{patdir}/%{category}/hae15sp3
install -m %{mode} patterns/%{category}/hae15sp4/* %{buildroot}/%{patdir}/%{category}/hae15sp4

%fdupes %{buildroot}

%files
%defattr(-,%{patuser},%{patgrp})
%dir %{patdirbase}
%dir %{patdir}
%dir %{patdir}/%{category}
%dir %{patdir}/%{category}/hae11all
%dir %{patdir}/%{category}/hae11sp0
%dir %{patdir}/%{category}/hae11sp1
%dir %{patdir}/%{category}/hae11sp2
%dir %{patdir}/%{category}/hae11sp3
%dir %{patdir}/%{category}/hae11sp4
%dir %{patdir}/%{category}/hae12all
%dir %{patdir}/%{category}/hae12sp0
%dir %{patdir}/%{category}/hae12sp1
%dir %{patdir}/%{category}/hae12sp2
%dir %{patdir}/%{category}/hae12sp3
%dir %{patdir}/%{category}/hae12sp4
%dir %{patdir}/%{category}/hae12sp5
%dir %{patdir}/%{category}/hae15all
%dir %{patdir}/%{category}/hae15sp0
%dir %{patdir}/%{category}/hae15sp1
%dir %{patdir}/%{category}/hae15sp2
%dir %{patdir}/%{category}/hae15sp3
%dir %{patdir}/%{category}/hae15sp4
%attr(%{mode},%{patuser},%{patgrp}) %{patdir}/%{category}/hae11all/*
%attr(%{mode},%{patuser},%{patgrp}) %{patdir}/%{category}/hae11sp0/*
%attr(%{mode},%{patuser},%{patgrp}) %{patdir}/%{category}/hae11sp1/*
%attr(%{mode},%{patuser},%{patgrp}) %{patdir}/%{category}/hae11sp2/*
%attr(%{mode},%{patuser},%{patgrp}) %{patdir}/%{category}/hae11sp3/*
%attr(%{mode},%{patuser},%{patgrp}) %{patdir}/%{category}/hae11sp4/*
%attr(%{mode},%{patuser},%{patgrp}) %{patdir}/%{category}/hae12all/*
%attr(%{mode},%{patuser},%{patgrp}) %{patdir}/%{category}/hae12sp0/*
%attr(%{mode},%{patuser},%{patgrp}) %{patdir}/%{category}/hae12sp1/*
%attr(%{mode},%{patuser},%{patgrp}) %{patdir}/%{category}/hae12sp2/*
%attr(%{mode},%{patuser},%{patgrp}) %{patdir}/%{category}/hae12sp3/*
%attr(%{mode},%{patuser},%{patgrp}) %{patdir}/%{category}/hae12sp4/*
%attr(%{mode},%{patuser},%{patgrp}) %{patdir}/%{category}/hae12sp5/*
%attr(%{mode},%{patuser},%{patgrp}) %{patdir}/%{category}/hae15all/*
%attr(%{mode},%{patuser},%{patgrp}) %{patdir}/%{category}/hae15sp0/*
%attr(%{mode},%{patuser},%{patgrp}) %{patdir}/%{category}/hae15sp1/*
%attr(%{mode},%{patuser},%{patgrp}) %{patdir}/%{category}/hae15sp2/*
%attr(%{mode},%{patuser},%{patgrp}) %{patdir}/%{category}/hae15sp3/*
%attr(%{mode},%{patuser},%{patgrp}) %{patdir}/%{category}/hae15sp4/*

%attr(444,%{patuser},%{patgrp}) %{patdir}/%{category}/hae11sp0/*README
%attr(444,%{patuser},%{patgrp}) %{patdir}/%{category}/hae11sp1/*README
%attr(444,%{patuser},%{patgrp}) %{patdir}/%{category}/hae11sp2/*README
%attr(444,%{patuser},%{patgrp}) %{patdir}/%{category}/hae11sp3/*README
%attr(444,%{patuser},%{patgrp}) %{patdir}/%{category}/hae11sp4/*README
%attr(444,%{patuser},%{patgrp}) %{patdir}/%{category}/hae12all/*README
%attr(444,%{patuser},%{patgrp}) %{patdir}/%{category}/hae12sp0/*README
%attr(444,%{patuser},%{patgrp}) %{patdir}/%{category}/hae12sp1/*README
%attr(444,%{patuser},%{patgrp}) %{patdir}/%{category}/hae12sp2/*README
%attr(444,%{patuser},%{patgrp}) %{patdir}/%{category}/hae12sp3/*README
%attr(444,%{patuser},%{patgrp}) %{patdir}/%{category}/hae12sp4/*README
%attr(444,%{patuser},%{patgrp}) %{patdir}/%{category}/hae12sp5/*README
%attr(444,%{patuser},%{patgrp}) %{patdir}/%{category}/hae15all/*README
%attr(444,%{patuser},%{patgrp}) %{patdir}/%{category}/hae15sp0/*README
%attr(444,%{patuser},%{patgrp}) %{patdir}/%{category}/hae15sp1/*README
%attr(444,%{patuser},%{patgrp}) %{patdir}/%{category}/hae15sp2/*README
%attr(444,%{patuser},%{patgrp}) %{patdir}/%{category}/hae15sp3/*README
%attr(444,%{patuser},%{patgrp}) %{patdir}/%{category}/hae15sp4/*README

%changelog
