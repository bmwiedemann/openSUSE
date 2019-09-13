#
# spec file for package ladspa-cmt
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


Name:           ladspa-cmt
Version:        1.15
Release:        0
Summary:        LADSPA CMT plugins
License:        GPL-2.0+
Group:          Productivity/Multimedia/Sound/Utilities
Url:            http://www.ladspa.org/cmt/
Source:         http://www.ladspa.org/download/cmt_src_%{version}.tgz
Source1:        cmt.rdf
Patch1:         cmt_src_1.15.diff
BuildRequires:  gcc-c++
BuildRequires:  ladspa-devel
Supplements:    ladspa
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package provides a LADSPA (Linux Audio Developer's Simple Plug-in API)
CMT (Computer Music Toolkit) plugins.

%prep
%setup -q -n cmt
%patch1
chmod 0644 doc/plugins.html

%build
# This package failed when testing with -Wl,-as-needed being default.
# So we disable it here, if you want to retest, just delete this comment and the line below.
export SUSE_ASNEEDED=0
make -C src %{?_smp_mflags} CFLAGS="%{optflags} -fno-strict-aliasing -fPIC -ggdb" targets

%install
mkdir -p %{buildroot}%{_libdir}/ladspa
make -C src INSTALL_PLUGINS_DIR=%{buildroot}%{_libdir}/ladspa install
mkdir -p %{buildroot}%{_datadir}/ladspa/rdf
cp -p %{SOURCE1} %{buildroot}%{_datadir}/ladspa/rdf

%files
%defattr(-,root,root)
%{_libdir}/ladspa
%{_datadir}/ladspa
%doc README
%doc doc/*

%changelog
