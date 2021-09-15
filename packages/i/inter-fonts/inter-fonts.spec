#
# spec file for package inter-fonts
#
# Copyright (c) 2021 SUSE LLC
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


Name:           inter-fonts
Version:        3.19
Release:        0
Summary:        The Inter font family
License:        OFL-1.1
Group:          System/X11/Fonts
URL:            https://rsms.me/inter/
Source0:        https://github.com/rsms/inter/releases/download/v%{version}/Inter-%{version}.zip
Source1:        https://github.com/rsms/inter/raw/v%{version}/README.md
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
Inter is a typeface specially designed for user interfaces with focus on high
legibility of small-to-medium sized text on computer screens.

%prep
%autosetup -cT -a0
cp %{SOURCE1} .

%build
:

%install
install -d %{buildroot}%{_ttfontsdir}
install -m0644 -t %{buildroot}%{_ttfontsdir} 'Inter Desktop'/*.otf

%reconfigure_fonts_scriptlets

%files
%license LICENSE.txt
%{_ttfontsdir}
%doc README.md

%changelog
