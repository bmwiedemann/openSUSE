#
# spec file for package gkrellm-cpupower
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


Name:           gkrellm-cpupower
%define src_name    gkrellm2-cpupower
Version:        0.2
Release:        0
Summary:        Gkrellm plugin - CPU Frequency
License:        GPL-2.0+
Group:          System/GUI/Other
Url:            https://github.com/sainsaar/gkrellm2-cpupower
Source0:        https://github.com/sainsaar/gkrellm2-cpupower/archive/0.2.tar.gz#/gkrellm2-cpupower-%{version}.tar.gz
Requires:       cpupower
BuildRequires:  cpupower-devel
BuildRequires:  gkrellm-devel
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
Obsoletes:      gkrellm-cpufreq
Provides:       gkrellm-cpufreq
Requires:       gkrellm
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A gkrellm2 plugin for displaying and manipulating CPU frequency

%prep
%setup -q -n %{src_name}-%{version}

%build
make CFLAGS="%{optflags}" %{?_smp_mflags}

%install
sed -i "s:/lib/:/%{_lib}/:" Makefile
%make_install

%clean

%files
%defattr(-,root,root)
# INSTALL is packaged on purpose. There are post-install instructions
%doc ChangeLog* INSTALL LICENSE README
%dir %{_libdir}/gkrellm2/
%dir %{_libdir}/gkrellm2/plugins
%{_libdir}/gkrellm2/plugins/cpupower.so

%changelog
