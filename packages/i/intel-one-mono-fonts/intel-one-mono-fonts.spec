#
# spec file for package intel-one-mono-fonts
#
# Copyright (c) 2024 SUSE LLC
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


Name:           intel-one-mono-fonts
Version:        1.4.0
Release:        0
Summary:        An expressive monospaced font family
License:        OFL-1.1-RFN
Group:          System/X11/Fonts
URL:            https://github.com/intel/intel-one-mono
Source:         %{url}/releases/download/V%{version}/ttf.zip#/%{name}-%{version}.zip
Source100:      https://raw.githubusercontent.com/intel/intel-one-mono/V%{version}/README.md
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
BuildArch:      noarch

%reconfigure_fonts_prereq

%description
Intel One Mono is an expressive monospaced font family.

Identifying the typographically underserved low-vision developer
audience, Frere-Jones Type designed the Intel One Mono typeface in
partnership with the Intel Brand Team and VMLY&R, for maximum
legibility to address developers' fatigue and eyestrain and reduce
coding errors. A panel of low-vision and legally blind developers
provided feedback at each stage of design.

%prep
%autosetup -n ttf

%build

%install
cp %{S:100} .
mkdir -p %{buildroot}%{_ttfontsdir}
install -m644 *.ttf %{buildroot}%{_ttfontsdir}

%reconfigure_fonts_scriptlets

%files
%doc README.md
%license OFL.txt
%{_ttfontsdir}

%changelog
