#
# spec file for package speedtest-cli
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define oname   speedtest_cli
Name:           speedtest-cli
Version:        2.1.1
Release:        0
Summary:        Command line interface for testing internet bandwidth
License:        Apache-2.0
Group:          System/Benchmark
Url:            https://github.com/sivel/speedtest-cli
Source0:        https://github.com/sivel/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  python3-base
BuildRequires:  python3-setuptools
Requires:       python3-setuptools
BuildArch:      noarch

%description
Command line interface for testing internet bandwidth using
speedtest.net

%prep
%setup -q

%build
%python3_build

%install
%python3_install
install -Dpm 0644 %{name}.1 \
  %{buildroot}%{_mandir}/man1/%{name}.1
ln -s %{_mandir}/man1/%{name}.1 \
  %{buildroot}%{_mandir}/man1/speedtest.1

%files
%doc LICENSE README.rst
%{_bindir}/speedtest
%{_bindir}/%{name}
%{_mandir}/man1/speedtest.1%{ext_man}
%{_mandir}/man1/%{name}.1%{ext_man}
%{python3_sitelib}/*

%changelog
