#
# spec file for package nanum-fonts
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


%define mono_name       nanum-gothic-coding-fonts
%define mono_version    2.0
%define nanum_version   20110907

Name:           nanum-fonts
Version:        %{nanum_version}
Release:        0
Summary:        Nanum Korean TrueType Fonts
License:        OFL-1.1
Group:          System/X11/Fonts
Url:            http://hangeul.naver.com/download.nhn
#Url:           http://dev.naver.com/projects/nanumfont/download/ (NanumGothicCoding)
Source0:        %{name}.tar.bz2
BuildRequires:  fontpackages-devel
%reconfigure_fonts_prereq
Recommends:     %{mono_name}
Provides:       locale(ko)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Collection of Nanum Korean TrueType fonts: NanumBrush,
NanumGothic, NanumMyeongjo and NanumPen.

%package -n %{mono_name}

Version:        %{mono_version}
Release:        0
Summary:        Nanum Gothic Coding Korean TrueType Fonts
Group:          System/X11/Fonts
Recommends:     %{name}
# FIXME: This causes a rpmlint warning; change <= to < once here's a new upstream version
Obsoletes:      nanum-gothic-coding <= %{mono_version}
Provides:       nanum-gothic-coding = %{mono_version}

%description -n %{mono_name}
Collection of Nanum Gothic Coding Korean TrueType fonts.

%prep
%setup -q -n %{name}

%build

%install
mkdir -p %{buildroot}%{_ttfontsdir}/
install -m 644 *.ttf %{buildroot}%{_ttfontsdir}/
mkdir -p %{buildroot}%{_docdir}/%{name}
install -m 644 {LICENSE,README}.NanumFont %{buildroot}%{_docdir}/%{name}
mkdir %{buildroot}%{_docdir}/%{mono_name}
install -m 644 {LICENSE,README}.NanumGothicCoding %{buildroot}%{_docdir}/%{mono_name}

%reconfigure_fonts_scriptlets

%files
%defattr(-, root, root)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NanumBrush.ttf
%{_ttfontsdir}/NanumGothic.ttf
%{_ttfontsdir}/NanumGothicBold.ttf
%{_ttfontsdir}/NanumGothicExtraBold.ttf
%{_ttfontsdir}/NanumMyeongjo*.ttf
%{_ttfontsdir}/NanumPen.ttf
%{_docdir}/%{name}

%files -n %{mono_name}
%defattr(-, root, root)
%{_ttfontsdir}/NanumGothicCoding*.ttf
%{_docdir}/%{mono_name}

%changelog
