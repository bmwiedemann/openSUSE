#
# spec file for package
#
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           fslint
Version:        2.46
Release:        0
License:        GPL-2.0
Summary:        A utility to find and clean "lint" on a filesystem
Url:            http://www.pixelbeat.org/fslint/
Group:          System/Filesystems
Source0:        http://www.pixelbeat.org/fslint/%{name}-%{version}.tar.xz
Source1:        fslint.desktop
BuildRequires:  desktop-file-utils
BuildRequires:  gettext >= 0.13
Requires:       cpio
Requires:       python >= 2.0
Requires:       python-gtk >= 2.0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%if 0%{?suse_version}
BuildRequires:  update-desktop-files
%endif

%description
FSlint is a utility to find redundant disk usage like duplicate files
for example. It can be used to reclaim disk space and fix other problems
like file naming issues and bad symlinks etc.
It includes a GTK+ GUI as well as a command line interface.

%prep
%setup -q
perl -pi -e 's|^liblocation=.*$|liblocation="%{_datadir}/%{name}" #RPM edit|' fslint-gui
perl -pi -e 's|^locale_base=.*$|locale_base=None #RPM edit|' fslint-gui


%build



%install
install -Dpm 755 fslint-gui %{buildroot}%{_bindir}/fslint-gui
install -dm 755 %{buildroot}%{_datadir}/%{name}/%{name}/{fstool,supprt}
install -dm 755 %{buildroot}%{_datadir}/%{name}/%{name}/supprt/rmlint
install -dm 755 %{buildroot}%{_mandir}/man1
install -pm 644 fslint.glade fslint_icon.png \
  %{buildroot}%{_datadir}/%{name}
install -dm 755 %{buildroot}%{_datadir}/pixmaps
ln -s ../%{name}/fslint_icon.png %{buildroot}%{_datadir}/pixmaps
install -pm 755 fslint/{find*,fslint,zipdir} \
  %{buildroot}%{_datadir}/%{name}/fslint
install -pm 755 fslint/fstool/* \
  %{buildroot}%{_datadir}/%{name}/fslint/fstool
install -pm 644 fslint/supprt/fslver \
  %{buildroot}%{_datadir}/%{name}/fslint/supprt
install -pm 755 fslint/supprt/get* \
  %{buildroot}%{_datadir}/%{name}/fslint/supprt
install -pm 755 fslint/supprt/md5sum_approx \
  %{buildroot}%{_datadir}/%{name}/fslint/supprt
install -pm 755 fslint/supprt/rmlint/* \
  %{buildroot}%{_datadir}/%{name}/fslint/supprt/rmlint

cp -a man/* \
  %{buildroot}%{_mandir}/man1/

make -C po DESTDIR=%{buildroot} LOCALEDIR=%{_datadir}/locale install

install  -pm 755 -D %{SOURCE1}  %{buildroot}%{_datadir}/applications/fslint.desktop


%if 0%{?suse_version}
%suse_update_desktop_file %{buildroot}%{_datadir}/applications/%{name}.desktop
%endif

%find_lang %{name}


%clean
rm -rf %{buildroot}


%files -f %{name}.lang
%defattr(-,root,root,-)
%doc doc/*
%{_mandir}/man1/fslint*
%{_bindir}/fslint-gui
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/fslint_icon.png


%changelog
