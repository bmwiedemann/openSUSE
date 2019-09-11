#
# spec file for package liberation-fonts
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           liberation-fonts
Version:        1.07.4
Release:        0
Summary:        Liberation Fonts
License:        SUSE-Liberation
Group:          System/X11/Fonts
Url:            https://fedorahosted.org/liberation-fonts/
Source:         https://fedorahosted.org/releases/l/i/liberation-fonts/liberation-fonts-ttf-%{version}.tar.gz
Source100:      %{name}-rpmlintrc
%reconfigure_fonts_prereq
BuildRequires:  fontpackages-devel
Provides:       locale(bg;el;ru;bg)
Obsoletes:      liberation2-fonts
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

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
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog License.txt README
%{_ttfontsdir}

%changelog
