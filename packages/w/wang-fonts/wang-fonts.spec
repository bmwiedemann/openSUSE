#
# spec file for package wang-fonts
#
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           wang-fonts
Version:        1.3.0
Release:        0
Summary:        Chinese (Unicode) TrueType fonts by Dr
License:        GPL-2.0+
Group:          System/X11/Fonts
Url:            http://code.google.com/p/wangfonts/
Source0:        http://wangfonts.googlecode.com/files/wangfonts-%{version}.tar.gz
Source1:        gpl-2.0.txt
BuildRequires:  fontpackages-devel
%reconfigure_fonts_prereq
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Chinese (Unicode) TrueType fonts by Dr. Hann-Tzong Wang

%prep
%setup -q -n wangfonts
cp %{SOURCE1} .

%build

%install
mkdir -p %{buildroot}%{_ttfontsdir}/
install -c -m 644 *.ttf %{buildroot}%{_ttfontsdir}

%reconfigure_fonts_scriptlets -c

%files
%defattr(-, root,root)
%doc gpl-2.0.txt
%{_ttfontsdir}

%changelog
