#
# spec file for package opengost-fonts
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


Name:           opengost-fonts
Version:        0.3
Release:        0
Summary:        Open-source Russian GOST Fonts
License:        OFL-1.1
Group:          System/X11/Fonts
Url:            https://bitbucket.org/fat_angel/opengostfont/overview
Source0:        https://bitbucket.org/fat_angel/opengostfont/downloads/opengostfont-otf-%{version}.tar.xz
Source1:        https://bitbucket.org/fat_angel/opengostfont/downloads/opengostfont-ttf-%{version}.tar.xz
BuildRequires:  fontpackages-devel
BuildRequires:  xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
Open-source version of the fonts by Russian standard GOST 2.304-81
«Letters for drawings».

%package -n opengost-otf-fonts
Summary:        Open-source Russian GOST Fonts (OpenType Format)
Group:          System/X11/Fonts

%description -n opengost-otf-fonts
Open-source version of the fonts by Russian standard GOST 2.304-81
«Letters for drawings».

This package contains fonts in OpenType format.

%package -n opengost-ttf-fonts
Summary:        Open-source Russian GOST Fonts (TrueType Format)
Group:          System/X11/Fonts

%description -n opengost-ttf-fonts
Open-source version of the fonts by Russian standard GOST 2.304-81
«Letters for drawings».

This package contains fonts in TrueType format.

%prep
%setup -cqn %{name}-%{version}
xz -dc %{SOURCE1} | tar -xf -

%build

%install
install -dm 0755 %{buildroot}%{_ttfontsdir}
install -m 0644 opengostfont-otf-%{version}/*.otf \
    %{buildroot}%{_ttfontsdir}
install -m 0644 opengostfont-ttf-%{version}/*.ttf \
    %{buildroot}%{_ttfontsdir}

%reconfigure_fonts_scriptlets -n opengost-otf-fonts

%reconfigure_fonts_scriptlets -n opengost-ttf-fonts

%files -n opengost-otf-fonts
%defattr(-,root,root,-)
%doc opengostfont-otf-%{version}/LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/*.otf

%files -n opengost-ttf-fonts
%defattr(-,root,root,-)
%doc opengostfont-ttf-%{version}/LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/*.ttf

%changelog
