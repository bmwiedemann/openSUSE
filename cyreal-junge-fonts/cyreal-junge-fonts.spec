#
# spec file for package cyreal-junge-fonts
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


Name:           cyreal-junge-fonts
Version:        1.002
Release:        0
License:        OFL-1.1
Summary:        Junge Font
Url:            http://cyreal.org/archives/784
Group:          System/X11/Fonts
#Source0:       wget http://www.google.com/webfonts/download?kit=XcOKr8oZPCeQezxUcCjjyg -O cyreal-junge-fonts.zip
Source0:        cyreal-junge-fonts.zip
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
Junge is an elegant and slim text typeface inspired by the calligraphy
of Günther Junge. Thanks to a combination of features it performs
equally well in most ranges. At small sizes it builds the impression of
flittering strokes. In large headlines its refined detailing become
visible. It is not as strictly structured as a text typeface, and has
subtle irregularities reminiscent of its calligraphic origin.

%prep
%setup -cqn %{name}-%{version}
sed -i 's/\r$//g' OFL.txt

%build

%install
install -Dm 644 Junge-Regular.ttf \
    %{buildroot}%{_ttfontsdir}/Junge-Regular.ttf

%reconfigure_fonts_scriptlets

%files
%defattr(-,root,root,-)
%doc OFL.txt
%dir %{_ttfontsdir}
%{_ttfontsdir}/Junge-Regular.ttf

%changelog
