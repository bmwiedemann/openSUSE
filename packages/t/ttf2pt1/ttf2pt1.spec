#
# spec file for package ttf2pt1
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           ttf2pt1
Version:        3.4.4
Release:        0
Summary:        True Type Font to PostScript Type 1 font converter
License:        BSD-3-Clause
Group:          Productivity/Publishing/PS
Url:            http://ttf2pt1.sourceforge.net/
Source0:        http://download.sourceforge.net/ttf2pt1/ttf2pt1-%{version}.tgz
Source1:        http://download.sourceforge.net/ttf2pt1/ttf2pt1-chinese-3.4.0.tgz
Source2:        README.SUSE
Patch0:         %{name}.diff
Patch1:         ttf2pt1-3.4.1-freetype2.diff
Patch2:         freetype-2.1.7.patch
Patch3:         ttf2pt1-3.4.4-fix-convert.patch
BuildRequires:  fdupes
BuildRequires:  freetype2-devel
Requires:       t1utils

%description
This is a collection of tools and scripts that allow to convert True
Type Fonts (as used by MS Wind*ws) to be converted to Postscript Type 1
fonts, so they can be used in X11 and Ghostscript.

%prep
%setup -q -a 1
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
make %{?_smp_mflags} CFLAGS_SYS="%{optflags} -fno-strict-aliasing"

%install
make INSTDIR=%{buildroot}%{_prefix} MANDIR=%{buildroot}/%{_mandir} install
mkdir -p %{buildroot}%{_sysconfdir}/%{name}
cp -ai %{buildroot}%{_datadir}/%{name}/scripts/convert.cfg.sample \
       %{buildroot}%{_sysconfdir}/%{name}/convert.cfg
cp -a ttf2pt1-chinese-*/*.map %{buildroot}%{_datadir}/%{name}/maps/
rm -f  %{buildroot}%{_datadir}/%{name}/scripts/{inst_dir,inst_file,mkrel,html2man}
rm -rf  %{buildroot}%{_datadir}/%{name}/app/{RPM,X11}
mkdir -p %{buildroot}%{_defaultdocdir}/%{name}/{app,encodings,other}
for i in COPYRIGHT FONTS* README* CHANGES* app encodings other
do
    ln -s %{_datadir}/%{name}/$i %{buildroot}%{_defaultdocdir}/%{name}/$i
done
cp -a %{SOURCE2} %{buildroot}%{_defaultdocdir}/%{name}
sed -i -e 's!%{buildroot}!!' %{buildroot}/%{_mandir}/man1/*
%fdupes -s %{buildroot}

%files
%doc %{_defaultdocdir}/%{name}
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/*
%{_bindir}/*
%{_prefix}/lib/ttf2pt1
%{_datadir}/%{name}
%{_mandir}/man1/*

%changelog
