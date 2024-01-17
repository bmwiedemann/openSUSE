#
# spec file for package ladspa-cmt
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


Name:           ladspa-cmt
Version:        1.18
Release:        0
Summary:        LADSPA CMT plugins
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Utilities
URL:            https://www.ladspa.org/cmt/overview.html
Source0:        http://www.ladspa.org/download/cmt_%{version}.tgz
Source1:        cmt.rdf
# PATCH-FEATURE-OPENSUSE no-installation-doc.patch -- There is no need for installation documentation
Patch0:         no-installation-doc.patch
BuildRequires:  gcc-c++
BuildRequires:  ladspa-devel
Supplements:    ladspa

%description
This toolkit is a set of musical sound processing and synthesis tools
presented as a LADSPA (Linux Audio Developer's Simple Plug-in API)
plugin library for CMT (Computer Music Toolkit).
See the %{_docdir}/%{name} directory for documentation.

%prep
%autosetup -p1 -n cmt_%{version}

%build
%make_build -C src CFLAGS="%{optflags}" targets

%install
install -d -m 0755 %{buildroot}%{_libdir}/ladspa
install -d -m 0755 %{buildroot}%{_datadir}/ladspa/rdf
install -D -m 0644 plugins/cmt.so %{buildroot}%{_libdir}/ladspa/cmt.so
install -D -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/ladspa/rdf/cmt.rdf

%files
%doc doc/*.html
%license doc/COPYING
%{_libdir}/ladspa
%{_datadir}/ladspa

%changelog
