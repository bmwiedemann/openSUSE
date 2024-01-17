#
# spec file for package eb-garamond-fonts
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           eb-garamond-fonts
Version:        0.016
Release:        0
Summary:        Claude Garamont's designs go open source
License:        OFL-1.1
Group:          System/X11/Fonts
Url:            http://www.georgduffner.at/ebgaramond/
Source:         http://bitbucket.org/georgd/eb-garamond/downloads/EBGaramond-%{version}.zip
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
Provides:       eb-garamond = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
Garamont’s fonts represent a milestone in the history of type design,
a touchstone to which font designers have been returning ever since. EB Garamond
is an open source project to create a revival of Claude Garamont’s famous
humanist typeface from the mid-16th century. Its design reproduces the original
by Claude Garamont: The source for the letterforms is a scan of a specimen known
as the “Berner specimen”, which, composed in 1592 by Conrad Berner, son-in-law
of Christian Egenolff and his successor at the Egenolff print office, shows
Garamont’s roman and Granjon’s italic fonts at different sizes. Hence the name
of this project: Egenolff-Berner Garamond.

%prep
%setup -q -n EBGaramond-%{version}

%build

%install
mkdir -p %{buildroot}%{_ttfontsdir}/
install -m 0644 ttf/*.ttf %{buildroot}%{_ttfontsdir}/

%reconfigure_fonts_scriptlets

%files
%defattr(-,root,root)
%doc Changes COPYING
%{_ttfontsdir}/

%changelog
