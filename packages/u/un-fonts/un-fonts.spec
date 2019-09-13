#
# spec file for package un-fonts
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           un-fonts
%define date	080608
%define ver     1.0.2
Version:        1.0.20%{date}
Release:        0
Summary:        Korean TrueType fonts
License:        GPL-2.0+
Group:          System/X11/Fonts
Url:            http://kldp.net/projects/unfonts/download
Source0:        %{name}-core-%{ver}-%{date}.tar.bz2
Source1:        %{name}-extra-%{ver}-%{date}.tar.bz2
Source10:       update-archive
BuildRequires:  fontpackages-devel
%reconfigure_fonts_prereq
Provides:       scalable-font-ko
Provides:       locale(ko)
# FIXME: This causes a rpmlint warning; change <= to < once here's a new upstream version
Obsoletes:      unfonts <= %{version}
Provides:       unfonts = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Collection of Korean TrueType fonts.

%prep
%setup -q -n %{name} -b 1

%build

%install
mkdir -p %{buildroot}%{_ttfontsdir}/
install -c -m 644 *.ttf %{buildroot}%{_ttfontsdir}/

%reconfigure_fonts_scriptlets -c

%files
%defattr(-, root,root)
%doc README COPYING
%{_ttfontsdir}

%changelog
