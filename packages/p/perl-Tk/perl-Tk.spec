#
# spec file for package perl-Tk
#
# Copyright (c) 2025 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define cpan_name Tk
Name:           perl-Tk
Version:        804.36.0
Release:        0
# 804.036 -> normalize -> 804.36.0
%define cpan_version 804.036
#Upstream: SUSE-Public-Domain
License:        (Artistic-1.0 OR GPL-1.0-or-later) AND Zlib
Summary:        Tk - a Graphical User Interface Toolkit
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/S/SR/SREZIC/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Patch0:         Tk-804.029-event.diff
Patch1:         Tk-804.029-macro.diff
Patch2:         Tk-804.029-null.diff
Patch3:         Tk-804.029-refcnt.diff
Patch4:         Tk-804.036-fix-strlen-vs-int-pointer-confusion.patch
# PATCH-FIX-UPSTREAM fix gcc15 build error https://github.com/eserte/perl-tk/issues/112
Patch5:         Tk-804.036-gcc15.patch
# PATCH-FIX-UPSTREAM fix gcc14 build error https://github.com/eserte/perl-tk/issues/98
Patch6:         Tk-804-config-C99.diff
BuildRequires:  perl
BuildRequires:  perl-macros
Provides:       perl(Tie::Watch)
Provides:       perl(Tk) = %{version}
Provides:       perl(Tk::Adjuster) = 4.8.0
Provides:       perl(Tk::After) = 4.8.0
Provides:       perl(Tk::Animation) = 4.8.0
Provides:       perl(Tk::Balloon) = 4.13.0
Provides:       perl(Tk::Bitmap) = 4.4.0
Provides:       perl(Tk::BrowseEntry) = 4.15.0
Provides:       perl(Tk::Button) = 4.10.0
Provides:       perl(Tk::Canvas) = 4.13.0
Provides:       perl(Tk::Checkbutton) = 4.6.0
Provides:       perl(Tk::Clipboard) = 4.9.0
Provides:       perl(Tk::CmdLine) = 4.7.0
Provides:       perl(Tk::ColorDialog) = 4.14.0
Provides:       perl(Tk::ColorEditor) = 4.14.0
Provides:       perl(Tk::ColorSelect) = 4.14.0
Provides:       perl(Tk::Compound) = 4.4.0
Provides:       perl(Tk::Configure) = 4.9.0
Provides:       perl(Tk::Derived) = 4.11.0
Provides:       perl(Tk::Dialog) = 4.5.0
Provides:       perl(Tk::DialogBox) = 4.16.0
Provides:       perl(Tk::DirTree) = 4.22.0
Provides:       perl(Tk::DirTreeDialog)
Provides:       perl(Tk::Dirlist) = 4.4.0
Provides:       perl(Tk::DragDrop) = 4.15.0
Provides:       perl(Tk::DragDrop::Common) = 4.5.0
Provides:       perl(Tk::DragDrop::Local) = 4.4.0
Provides:       perl(Tk::DragDrop::Rect) = 4.12.0
Provides:       perl(Tk::DragDrop::SunConst) = 4.4.0
Provides:       perl(Tk::DragDrop::SunDrop) = 4.6.0
Provides:       perl(Tk::DragDrop::SunSite) = 4.7.0
Provides:       perl(Tk::DragDrop::Win32Drop) = 4.4.0
Provides:       perl(Tk::DragDrop::Win32Site) = 4.9.0
Provides:       perl(Tk::DragDrop::XDNDDrop) = 4.7.0
Provides:       perl(Tk::DragDrop::XDNDSite) = 4.7.0
Provides:       perl(Tk::DropSite) = 4.8.0
Provides:       perl(Tk::DummyEncode) = 4.7.0
Provides:       perl(Tk::DummyEncode::X11ControlChars)
Provides:       perl(Tk::DummyEncode::iso8859_1)
Provides:       perl(Tk::English) = 4.6.0
Provides:       perl(Tk::Entry) = 4.18.0
Provides:       perl(Tk::ErrorDialog) = 4.8.0
Provides:       perl(Tk::Event) = 4.40.0
Provides:       perl(Tk::Event::IO) = 4.9.0
Provides:       perl(Tk::FBox) = 4.21.0
Provides:       perl(Tk::FileSelect) = 4.18.0
Provides:       perl(Tk::FloatEntry) = 4.4.0
Provides:       perl(Tk::Font) = 4.4.0
Provides:       perl(Tk::Frame) = 4.10.0
Provides:       perl(Tk::HList) = 4.15.0
Provides:       perl(Tk::IO) = 4.6.0
Provides:       perl(Tk::IconList) = 4.7.0
Provides:       perl(Tk::Image) = 4.11.0
Provides:       perl(Tk::InputO) = 4.4.0
Provides:       perl(Tk::ItemStyle) = 4.4.0
Provides:       perl(Tk::JPEG) = 4.3.0
Provides:       perl(Tk::LabEntry) = 4.6.0
Provides:       perl(Tk::LabFrame) = 4.10.0
Provides:       perl(Tk::LabRadiobutton) = 4.4.0
Provides:       perl(Tk::Label) = 4.6.0
Provides:       perl(Tk::LabeledEntryLabeledRadiobutton) = 4.4.0
Provides:       perl(Tk::Labelframe) = 4.3.0
Provides:       perl(Tk::Listbox) = 4.15.0
Provides:       perl(Tk::MMtry) = 4.11.0
Provides:       perl(Tk::MMutil) = 4.26.0
Provides:       perl(Tk::MainWindow) = 4.15.0
Provides:       perl(Tk::MakeDepend) = 4.16.0
Provides:       perl(Tk::Menu) = 4.23.0
Provides:       perl(Tk::Menu::Button)
Provides:       perl(Tk::Menu::Cascade)
Provides:       perl(Tk::Menu::Checkbutton)
Provides:       perl(Tk::Menu::Item) = 4.6.0
Provides:       perl(Tk::Menu::Radiobutton)
Provides:       perl(Tk::Menu::Separator)
Provides:       perl(Tk::Menubar) = 4.6.0
Provides:       perl(Tk::Menubutton) = 4.5.0
Provides:       perl(Tk::Message) = 4.6.0
Provides:       perl(Tk::MsgBox) = 4.2.0
Provides:       perl(Tk::Mwm) = 4.4.0
Provides:       perl(Tk::NBFrame) = 4.4.0
Provides:       perl(Tk::NoteBook) = 4.12.0
Provides:       perl(Tk::Optionmenu) = 4.14.0
Provides:       perl(Tk::PNG) = 4.4.0
Provides:       perl(Tk::Pane) = 4.7.0
Provides:       perl(Tk::Panedwindow) = 4.4.0
Provides:       perl(Tk::Photo) = 4.6.0
Provides:       perl(Tk::Pixmap) = 4.4.0
Provides:       perl(Tk::Pretty) = 4.6.0
Provides:       perl(Tk::ProgressBar) = 4.15.0
Provides:       perl(Tk::ROText) = 4.11.0
Provides:       perl(Tk::Radiobutton) = 4.6.0
Provides:       perl(Tk::Region) = 4.6.0
Provides:       perl(Tk::Reindex) = 4.6.0
Provides:       perl(Tk::ReindexedROText) = 4.4.0
Provides:       perl(Tk::ReindexedText) = 4.4.0
Provides:       perl(Tk::Scale) = 4.4.0
Provides:       perl(Tk::Scrollbar) = 4.10.0
Provides:       perl(Tk::Spinbox) = 4.7.0
Provides:       perl(Tk::Stats) = 4.4.0
Provides:       perl(Tk::Submethods) = 4.5.0
Provides:       perl(Tk::TList) = 4.6.0
Provides:       perl(Tk::Table) = 4.16.0
Provides:       perl(Tk::Text) = 4.31.0
Provides:       perl(Tk::Text::Tag) = 4.4.0
Provides:       perl(Tk::TextEdit) = 4.5.0
Provides:       perl(Tk::TextList) = 4.6.0
Provides:       perl(Tk::TextUndo) = 4.15.0
Provides:       perl(Tk::Tiler) = 4.13.0
Provides:       perl(Tk::TixGrid) = 4.10.0
Provides:       perl(Tk::Toplevel) = 4.6.0
Provides:       perl(Tk::Trace) = 4.9.0
Provides:       perl(Tk::Tree) = 4.720.0
Provides:       perl(Tk::Widget) = 4.37.0
Provides:       perl(Tk::WinPhoto) = 4.5.0
Provides:       perl(Tk::Wm) = 4.15.0
Provides:       perl(Tk::X) = 4.5.0
Provides:       perl(Tk::X11Font) = 4.7.0
Provides:       perl(Tk::Xlib) = 4.4.0
Provides:       perl(Tk::Xrm) = 4.5.0
Provides:       perl(Tk::install) = 4.4.0
Provides:       perl(Tk::widgets) = 4.5.0
Provides:       perl(WidgetDemo) = 4.12.0
%undefine       __perllib_provides
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  liberation-fonts
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  xkeyboard-config
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(xt)
%if 0%{?suse_version} >= 01550
BuildRequires:  xvfb-run
BuildRequires:  perl(Devel::Leak)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
%endif
BuildRequires:  xorg-x11-Xnest
BuildRequires:  xorg-x11-Xvfb
BuildRequires:  xorg-x11-fonts
BuildRequires:  xorg-x11-fonts-100dpi
BuildRequires:  xorg-x11-fonts-scalable
BuildRequires:  zlib-devel
BuildRequires:  perl(Encode)
BuildRequires:  perl(ExtUtils::MakeMaker)
%ifnarch s390 s390x
BuildRequires:  xorg-x11-server
%endif
# MANUAL END

%description
This a re-port of a perl interface to Tk8.4.
C code is derived from Tcl/Tk8.4.5.
It also includes all the C code parts of Tix8.1.4 from SourceForge.
The perl code corresponding to Tix's Tcl code is not fully implemented.

Perl API is essentially the same as Tk800 series Tk800.025 but has not
been verified as compliant. There ARE differences see pod/804delta.pod.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version} -N

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644
%patch -P0 -p0
%patch -P1 -p0
%patch -P2 -p0
%patch -P3 -p0
%patch -P4 -p0
%patch -P5 -p0
%patch -P6 -p0
# MANUAL BEGIN
find . -type f -name "Tcl-pTk" -print0 | xargs -0 chmod +x
find . -type f -name "mkVFunc" -print0 | xargs -0 chmod +x
# MANUAL END

%build
# Work around boo#1225909, see the bug for more details
%global optflags %{optflags} -fpermissive

find -name "*.orig" -exec rm {} \;
for file in `find -type f` ; do
  grep -q "%{_prefix}/local/bin/perl" $file && \
      sed -i -e "s@%{_prefix}/local/bin/perl@%{_bindir}/perl@g" "$file"
  grep -q "%{_prefix}/local/bin/nperl" $file && \
      sed -i -e "s@%{_prefix}/local/bin/nperl@%{_bindir}/nperl@g" "$file"
  grep -q "#!\s*/bin/perl" $file && \
      sed -i -e "s@/bin/perl@%{_bindir}/perl@g" "$file"
  grep -q "#!\s*/tools/local/perl" $file && \
      sed -i -e "s@/tools/local/perl@%{_bindir}/perl@g" "$file"
  grep -q "%{_prefix}/local/bin/new/perl" $file && \
      sed -i -e "s@%{_prefix}/local/bin/new/perl@%{_bindir}/perl@g" "$file"
done
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" XFT=1
make %{?_smp_mflags} CFLAGS="%{optflags} -Wall -fpic"

%check
%if 0%{?suse_version} >= 01550
xvfb-run -a make test  %{?_smp_mflags} V=1
%else
Xvfb :95 -screen 0 1280x1024x24 & #430569
trap "kill $!" EXIT
sleep 5
DISPLAY=:95 make test %{?_smp_mflags}
%endif

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Change.log Changes examples Funcs.doc PPM-HowTo README README.linux ToDo VERSIONS
%license COPYING
%exclude %{perl_vendorarch}/Tk/pTk
%exclude %{perl_vendorarch}/Tk/*.h

%package devel
Summary:        Development files for perl-Tk
Requires:       %{name} = %{version}

%description devel
Development files for Tk - a graphical user interface toolkit for Perl

%files devel
%{perl_vendorarch}/Tk/pTk
%{perl_vendorarch}/Tk/*.h

%changelog
