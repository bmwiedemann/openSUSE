#
# spec file for package cyreal-alice-fonts
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


Name:           cyreal-alice-fonts
Version:        1.010
Release:        0
License:        OFL-1.1
Summary:        Alice Font
Url:            http://cyreal.org/archives/842
Group:          System/X11/Fonts
#Source0:       wget http://www.google.com/webfonts/download?kit=nVDICQAe6IAM-XidgBCu9Q -O cyreal-alice-fonts.zip
Source0:        cyreal-alice-fonts.zip
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
Ksenia Erulevich, designer of the Alice typeface, was inspired by Lewis
Carrol’s novel and decided to make a typeface that will be suitable for
typesetting that book.

It came out eclectic and quaint, old-fashioned, having widened
proportions, open aperture, and soft rounded features; perfect for long
meditative text-setting and headlines.

%prep
%setup -cqn %{name}-%{version}
sed -i 's/\r$//g' OFL.txt

%build

%install
install -Dm 644 Alice-Regular.ttf \
    %{buildroot}%{_ttfontsdir}/Alice-Regular.ttf

%reconfigure_fonts_scriptlets

%files
%defattr(-,root,root,-)
%doc OFL.txt
%dir %{_ttfontsdir}
%{_ttfontsdir}/Alice-Regular.ttf

%changelog
