#
# spec file for package TreeMaker
#
# Copyright (c) 2023 Aaron Puchert <aaronpuchert@alice-dsl.net>
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


Name:           TreeMaker
Version:        5.0.1
Release:        0
Summary:        Tool for the Design of Origami Bases
License:        GPL-2.0-only
Group:          Productivity/Graphics/CAD
URL:            https://www.langorigami.com/article/treemaker
Source:         https://www.langorigami.com/wp-content/uploads/2015/09/TreeMaker_src.zip
Source1:        com.langorigami.TreeMaker.desktop
Source2:        com.langorigami.TreeMaker.metainfo.xml
Source3:        treemaker.xml
Source4:        https://github.com/wxWidgets/wxWidgets/raw/v3.2.1/utils/hhp2cached/hhp2cached.cpp
# Patches are kept in https://github.com/aaronpuchert/TreeMaker.
Patch1:         Allow-building-with-system-wxWidgets.patch
Patch2:         Use-explicit-this-for-dependent-base-members.patch
Patch3:         Fix-missing-declaration-of-wxPageSetupData-in-tmwxAp.patch
Patch4:         Replace-call-to-protected-wxWindow-ProcessEvent-by-H.patch
Patch5:         Stop-using-wxT-with-non-literals.patch
Patch6:         Explicitly-cast-argument-to-wxConfigBase-Write.patch
Patch7:         Let-tmwxTextCtrl-constructor-take-a-wxString.patch
Patch8:         Replace-tmwxDoc-GetPrintableName-call-by-GetDocument.patch
Patch9:         Inline-private-wxDocChildFrameAny-OnActivate.patch
Patch10:        Fix-flag-arguments-to-wxFileDialog-constructor.patch
Patch11:        Try-to-resolve-missing-members-in-tmwxHtmlHelpFrame.patch
Patch12:        Don-t-set-private-wxDialog-m_modalShowing.patch
Patch13:        Resolve-ambiguous-call-to-tmOnAssert.patch
Patch14:        Let-tmwxHtmlHelpController-CreateHelpWindow-match-wi.patch
Patch15:        Link-with-GTK-libraries.patch
Patch16:        Internalize-g_openDialogs-in-tmwxOptimizerDialog_gtk.patch
Patch17:        Fix-annoying-warning-about-suspiciuos-cast.patch
Patch18:        Fix-popups-about-ignored-flags-at-startup.patch
Patch19:        Fix-crash-on-opening-help.patch
Patch20:        Make-some-build-options-configurable.patch
BuildRequires:  c++_compiler
BuildRequires:  update-desktop-files
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  unzip
BuildRequires:  wxGTK3-devel
BuildRequires:  zip

%description
TreeMaker is a program for the design of origami bases. You draw a stick figure
of the base on the screen; each stick in the stick figure (the “tree”) will be
represented by a flap on the base. You can also place various constraints on
the flaps, forcing them to be corner, edge, or middle flaps, and/or setting up
various symmetry relationships (forcing pairs of flaps to be symmetric about a
line of symmetry of the paper, for example). Once you have defined the tree,
TreeMaker computes the full crease pattern for a base which, when folded, will
have a projection (roughly speaking, its “shadow”) equivalent to that specified
by the defining tree. The crease pattern can be printed out, or copied and
pasted into another graphics program for further processing.

%prep
# Using -T and manually unzipping because zip archive overwrites files.
%setup -c -T -n TreeMaker
unzip -uo %{SOURCE0} -d ..
%autopatch -p1

%build
pushd linux/
OPTIONS="%{optflags}" make %{?_smp_mflags} INSTALL_PREFIX=%{_prefix}

c++ %{optflags} $(wx-config --cxxflags) %{SOURCE4} $(wx-config --libs) -o hhp2cached
make %{?_smp_mflags} help WXHLPCACHEDIR=.
popd

%install
pushd linux/
make install INSTALL_PREFIX=%{buildroot}%{_prefix} WXHLPCACHEDIR=.
popd

rm %{buildroot}%{_datadir}/TreeMaker\ 5/{Icon_app.ppm,LICENSE.txt.gz,uninstall}

%suse_update_desktop_file -i %{SOURCE1}
install -D -m 644 %{SOURCE1} %{buildroot}%{_datadir}/applications/com.langorigami.TreeMaker.desktop
install -D -m 644 %{SOURCE2} %{buildroot}%{_datadir}/metainfo/com.langorigami.TreeMaker.metainfo.xml
install -D -m 644 %{SOURCE3} %{buildroot}%{_datadir}/mime/packages/treemaker.xml
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/{48x48,128x128}/{apps,mimetypes}
ln %{buildroot}%{_datadir}/TreeMaker\ 5/Icon_app_48.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/treemaker.png
ln %{buildroot}%{_datadir}/TreeMaker\ 5/Icon_doc_48.png %{buildroot}%{_datadir}/icons/hicolor/48x48/mimetypes/model-x-tmd5.png
install -D -m 644 linux/resources/Icon_app.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/treemaker.png
install -D -m 644 linux/resources/Icon_doc.png %{buildroot}%{_datadir}/icons/hicolor/128x128/mimetypes/model-x-tmd5.png

%files
%license LICENSE.txt
%{_bindir}/TreeMaker
"%{_datadir}/TreeMaker 5"
%{_datadir}/applications/com.langorigami.TreeMaker.desktop
%{_datadir}/icons/hicolor/{48x48,128x128}/{apps/treemaker.png,mimetypes/model-x-tmd5.png}
%{_datadir}/metainfo/com.langorigami.TreeMaker.metainfo.xml
%{_datadir}/mime/packages/treemaker.xml

%changelog
