#
# spec file for package linux-libertine-fonts
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


%define fontname LinuxLibertine

Name:           linux-libertine-fonts
Version:        5.3.0
Release:        0
Summary:        Free Serif Fonts
License:        GPL-2.0-with-font-exception or OFL-1.1
Group:          System/X11/Fonts
Url:            http://www.linuxlibertine.org/
Source0:        http://downloads.sourceforge.net/linuxlibertine/LinLibertineOTF_%{version}_2012_07_02.tgz
Source1:        31-linux-libertine.conf
BuildRequires:  fontconfig
BuildRequires:  fontpackages-devel
%reconfigure_fonts_prereq
# LinuxLibertine was last used at openSUSE 12.1 (version 5.1.3)
Obsoletes:      %{fontname} < %{version}
Provides:       %{fontname} = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Free serif fonts from the LinuxLibertine project. These might be useful
when exchanging documents using Times fonts.

%prep
%setup -c -q -n %{fontname}
chmod a-x *.txt

# Fix rpmlint warning "wrong-file-end-of-line-encoding"
sed -i 's/\r$//' OFL-1.1.txt

%build

%install
mkdir -p %{buildroot}%{_ttfontsdir}/
install -m 0644 *.otf %{buildroot}%{_ttfontsdir}
%install_fontsconf %{SOURCE1}

%reconfigure_fonts_scriptlets

%files
%defattr(-,root,root,-)
%doc Bugs.txt ChangeLog.txt GPL.txt LICENCE.txt OFL-1.1.txt README ToDo.txt
%{_ttfontsdir}
%files_fontsconf_availdir
%files_fontsconf_file -l 31-linux-libertine.conf

%changelog
