#
# spec file for package kanjipad
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


Name:           kanjipad
BuildRequires:  gtk2-devel
BuildRequires:  update-desktop-files
Version:        2.0.0
Release:        0
Url:            http://fishsoup.net/software/kanjipad/
Source0:        http://fishsoup.net/software/kanjipad/kanjipad-2.0.0.tar.bz2
Source1:        %name.desktop
Patch:          kanjipad.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Summary:        Japanese Handwriting Recognition
License:        GPL-2.0+
Group:          System/I18n/Japanese

%description
KanjiPad is a very simple program for handwriting recognition. The user
draws a character into the box, then requests translation. The best
candidates are displayed along the right hand side of the window and
can be selected for pasting into other programs.

It is meant primarily for dictionary purposes for learners of Japanese.
It does not support entering kana, so its usefulness as an input method
is limited. Furthermore, if you already know the reading of a
character, conventional pronunciation-based methods of entering the
character are probably faster.

However, KanjiPad is sometimes useful for entering very unusual
characters, even if the pronunciation is known, because
pronunciation-based input methods often fail for rarely used
characters.

%prep
%setup -q
%patch

%build
make PREFIX=/usr OPTIMIZE="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT;
make PREFIX=$RPM_BUILD_ROOT/usr install
%suse_update_desktop_file -i %name Education Languages

%clean
rm -rf $RPM_BUILD_ROOT;

%files
%defattr(-,root,root)
%doc COPYING README TODO ChangeLog
/usr/bin/*
/usr/share/[^a]*
/usr/share/applications/*

%changelog
