#
# spec file for package terminus-ttf-fonts
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


%define fontname terminus-ttf
Name:           terminus-ttf-fonts
Version:        4.49.3
Release:        0
Summary:        Terminus Truetype Fonts
License:        OFL-1.1
Group:          System/X11/Fonts
URL:            https://files.ax86.net/terminus-ttf
Source:         https://files.ax86.net/%{fontname}/files/%{version}/%{fontname}-%{version}.zip
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
Terminus TTF is a TrueType version of the great Terminus Font, a
fixed-width bitmap font optimised for long work with computers.

%prep
%setup -q -n %{fontname}-%{version}

%build
# Nothing to build.

%install
mkdir -p %{buildroot}%{_ttfontsdir}/
install -m 0644 TerminusTTF*-%{version}.ttf %{buildroot}%{_ttfontsdir}/

%reconfigure_fonts_scriptlets

%files
%defattr(-,root,root)
%doc COPYING
%dir %{_ttfontsdir}/
%{_ttfontsdir}/TerminusTTF*-%{version}.ttf

%changelog
