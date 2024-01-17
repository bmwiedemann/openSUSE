#
# spec file for package antijingoist-opendyslexic-fonts
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           antijingoist-opendyslexic-fonts
Version:        0.91.12
Release:        0
Summary:        OpenDyslexic Fonts
License:        OFL-1.1
Group:          System/X11/Fonts
Url:            https://github.com/antijingoist/opendyslexic
Source:         %{name}-%{version}.tar.gz
BuildRequires:  fontpackages-devel
%reconfigure_fonts_prereq
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
OpenDyslexic, a typeface that uses typeface shapes & features to help offset
some visual symptoms of Dyslexia.

%prep
%setup -q -n opendyslexic-%{version}

%build
# Nothing to do here

%install
mkdir -p %{buildroot}%{_ttfontsdir}
install -m 0644 compiled/*.otf %{buildroot}%{_ttfontsdir}

%reconfigure_fonts_scriptlets

%files
%license OFL.txt
%doc OFL-FAQ.txt README.md FONTLOG.txt
%{_ttfontsdir}

%changelog

