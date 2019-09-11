#
# spec file for package gnome-patch-translation
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           gnome-patch-translation
Version:        15.0
Release:        0
Summary:        Collect and Merge Translations From RPM Patches
License:        GPL-2.0-or-later
Group:          System/GUI/GNOME
Source:         gnome-patch-translation-files.tar.bz2
Source1:        gnome-patch-translation.tar.bz2
Source2:        README
Source3:        gnome-patch-translation-prepare
Source4:        gnome-patch-translation-update
Source5:        gnome-patch-translation-merge
Source6:        HEADER.pot
Source7:        HOWTO
Source8:        update-step1-update-translations-from-lcn
Source9:        update-step2-update-strings-from-packages
Source10:       update-step3-upload-strings-to-lcn
Source11:       update-solve-upload-conflict
Source12:       gnome-patch-translation.conf
Requires:       intltool
BuildArch:      noarch

%description
This package provides scripts for collecting strings changed in RPM
patches and merging them to one translation compendium.

%prep
%setup -q -T -a0 -a1 -c %{name}-%{version}
cp -a %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6} .

%build
sh gnome-patch-translation-merge

%install
mkdir -p %{buildroot}%{_bindir}
install gnome-patch-translation-prepare gnome-patch-translation-update %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/gnome-patch-translation
cp gnome-patch-translation/*.po gnome-patch-translation-merged/*.pot %{buildroot}%{_datadir}/gnome-patch-translation

%files
%doc README
%{_bindir}/*
%{_datadir}/gnome-patch-translation

%changelog
