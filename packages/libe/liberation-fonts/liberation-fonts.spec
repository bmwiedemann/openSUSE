#
# spec file for package liberation-fonts
#
# Copyright (c) 2020 SUSE LLC
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


Name:           liberation-fonts
Version:        2.1.1
Release:        0
Summary:        Liberation Fonts
License:        SUSE-Liberation
Group:          System/X11/Fonts
URL:            https://fedorahosted.org/liberation-fonts/
Source:         https://github.com/liberationfonts/liberation-fonts/files/4743886/liberation-fonts-ttf-2.1.1.tar.gz
Source100:      %{name}-rpmlintrc
BuildRequires:  fontpackages-devel
Provides:       locale(bg;el;ru;bg)
Obsoletes:      liberation2-fonts < 2
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
Free fonts which are metric compatible to "Arial", "Times New Roman"
and "Courier New".

%prep
%setup -q -n %{name}-ttf-%{version}

%build

%install
mkdir -p %{buildroot}%{_ttfontsdir}
install -m 0644 *.ttf %{buildroot}%{_ttfontsdir}/

%reconfigure_fonts_scriptlets

%files
%license LICENSE
%doc AUTHORS ChangeLog README.md
%{_ttfontsdir}

%changelog
