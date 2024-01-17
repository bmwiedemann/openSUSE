#
# spec file for package cpmono_v07-fonts
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


Name:           cpmono_v07-fonts
Version:        1.0
Release:        0
Summary:        Industrial Monotype Font
License:        CC-BY-3.0
Group:          System/X11/Fonts
Url:            http://www.fontsquirrel.com/fonts/CPMono_v07
# http://www.fontsquirrel.com/fonts/download/CPMono_v07
Source:         CPMono_v07.zip
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
%reconfigure_fonts_prereq
# FIXME: This causes a rpmlint warning; change <= to < once here's a new upstream version
Obsoletes:      cpmono_v07-font <= %{version}
Provides:       cpmono_v07-font = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
CPMono v07 is an industrial / high-tech monospace font.

%prep
%setup -q -c "%{name}-%{version}"

%build

%install
install -d "%{buildroot}%{_ttfontsdir}"
install -m0644 *.otf "%{buildroot}%{_ttfontsdir}/"

%reconfigure_fonts_scriptlets

%files
%defattr(-,root,root)
%doc *.txt
%dir %{_ttfontsdir}
%{_ttfontsdir}/*.otf

%changelog
