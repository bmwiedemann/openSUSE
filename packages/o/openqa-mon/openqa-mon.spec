#
# spec file for package openqa-mon
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


Name:           openqa-mon
Version:        0.26
Release:        0
Summary:        CLI monitoring utility for openQA
License:        GPL-3.0-or-later
URL:            https://github.com/grisu48/openqa-mon/
Source:         openqa-mon-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go >= 1.14
BuildRequires:  golang-packaging
%{go_nostrip}

%description
openqa-mon is a CLI monitoring client for openqa written in plain go.

%prep
%autosetup -D -a 1

%build
make all GOARGS="-mod vendor -buildmode pie"

%install
# Manual install (for now)
install -Dm 755 openqa-mon %{buildroot}/%{_bindir}/openqa-mon
install -Dm 755 openqa-mq %{buildroot}/%{_bindir}/openqa-mq
install -Dm 755 openqa-revtui %{buildroot}/%{_bindir}/openqa-revtui
install -Dm 644 doc/openqa-mon.8 %{buildroot}/%{_mandir}/man8/openqa-mon.8

%files
%doc README.md
%{_bindir}/openqa-mon
%{_bindir}/openqa-mq
%{_bindir}/openqa-revtui
%{_mandir}/man8/openqa-mon.8%{?ext_man}

%changelog
