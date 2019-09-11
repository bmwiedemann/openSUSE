#
# spec file for package sffview
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


Name:           sffview
BuildRequires:  SDL-devel
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_headers-devel
%else
BuildRequires:  boost-devel
%endif
BuildRequires:  gcc-c++
BuildRequires:  libtiff-devel
BuildRequires:  update-desktop-files
BuildRequires:  wxWidgets-3_0-devel
BuildRequires:  xorg-x11
Version:        0.5
Release:        0
Summary:        Simple viewer for Structured Fax Files (.sff) used by ISDN applications
License:        MIT
Group:          Hardware/ISDN
Source:         %{name}-%{version}.tar.xz
Source2:        %{name}.1
Url:            http://sfftools.sourceforge.net/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Patch0:         %{name}-%{version}.diff
%define _use_internal_dependency_generator 0
%define __find_requires %wx_requires

%description
The CAPI interface for programming ISDN hardware expects and gives you
faxes in the "Structured Fax File" (SFF) format.

SffView is a viewer for SFF-files. SffView is written in C++ using the
wxWidgets/wxGTK toolkit and is therefore available for Linux and
Windows (wxWidgets is a platform independent toolkit and wxGTK is a
unix implementation based on GTK+, see wxWidgets homepage).

%prep
%setup
%patch0 -p1

%build
make %{?_smp_mflags}

%install
install -d "%buildroot/%_bindir"
install sffview "%buildroot/%_bindir/"
install -d "%buildroot/%_defaultdocdir/sffview"
install -pm0644 doc/readme doc/copying testfax.sff "%buildroot/%_defaultdocdir/sffview/"
install -d "%{buildroot}/%{_mandir}/man1"
install -pm0644 %{S:2} "%{buildroot}/%{_mandir}/man1/"

%files
%defattr(-,root,root,-)
/usr/bin/sffview
%doc %{_defaultdocdir}/sffview
%doc %{_mandir}/man1/sffview.1.gz

%changelog
