#
# spec file for package kde-oxygen-fonts
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


%define fontname oxygen-fonts
Name:           kde-oxygen-fonts
Version:        0.4.0
Release:        0
Summary:        A desktop/gui font family for integrated use with the KDE desktop
License:        OFL-1.1 and SUSE-GPL-3.0+-with-font-exception
Group:          System/X11/Fonts
Url:            https://projects.kde.org/projects/playground/artwork/oxygen-fonts
Source:         http://download.kde.org/stable/plasma/5.0.0/%{fontname}-%{version}.tar.xz
BuildRequires:  extra-cmake-modules >= 0.0.11
BuildRequires:  fontforge
BuildRequires:  fontpackages-devel
BuildRequires:  kf5-filesystem
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%reconfigure_fonts_prereq

%description
‘Oxygen Font’ is a project to design a desktop/gui font 
for integrated use with the KDE desktop. The design is 
based on interpolations between ‘Muli’ and ‘FontOne’ 
that have been further shaped to reach a clear, legible 
font to use within the KDE gui.

The basic concept for ‘Oxygen Font’ was to design a clear,
legible, sans serif, that would be rendered with Freetype 
on Linux-based devices. The idea was to not quite follow 
a ‘purist’ line of sans serif typeface formulae, but to 
allow some juxtapositioning of font forms to give 
familiarity but also a sense of newness. A version of the 
font is also under development that is aimed to be a 
branding typeface for the desktop.


%prep
%setup -n %{fontname}-%{version}

%build
  %cmake_kf5 -d build
  %make_jobs

%install
  %kf5_makeinstall -C build

  # yes, cmake config files can be used, but that's maddness
  rm -rfv %{buildroot}%{_libdir}/

  %reconfigure_fonts_scriptlets

%files
%defattr(-,root,root)
%doc README* *.txt COPYING*
%dir %{_ttfontsdir}
%{_ttfontsdir}/oxygen/

%changelog
