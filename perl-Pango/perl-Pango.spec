#
# spec file for package perl-Pango
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


%bcond_with Gtk2

Name:           perl-Pango
Version:        1.226
Release:        0
%define cpan_name Pango
Summary:        Pango Perl module
License:        LGPL-2.1+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Pango/
Source:         http://www.cpan.org/authors/id/X/XA/XAOC/%{cpan_name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM fix-pangocairo_libs.patch https://rt.cpan.org/Public/Bug/Display.html?id=111117
Patch0:         fix-pangocairo_libs.patch
#
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  update-desktop-files
BuildRequires:  xorg-x11
BuildRequires:  xorg-x11-Xvfb
BuildRequires:  xorg-x11-server
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(pango)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{perl_requires}
%if %{with Gtk2}
BuildRequires:  perl(Gtk2) >= 1.220
%endif
#
BuildRequires:  perl(Cairo) >= 1.000
BuildRequires:  perl(ExtUtils::Depends) >= 0.300
BuildRequires:  perl(ExtUtils::MakeMaker)
#BuildRequires:  perl(ExtUtils::PkgConfig) >= 1.030
BuildRequires:  perl(ExtUtils::PkgConfig) >= 1.03
BuildRequires:  perl(Glib) >= 1.220
#
Requires:       perl(Cairo) >= 1.000
Requires:       perl(ExtUtils::Depends) >= 0.300
#Requires:       perl(ExtUtils::PkgConfig) >= 1.030
Requires:       perl(ExtUtils::PkgConfig) >= 1.03
Requires:       perl(Glib) >= 1.220

%description
Pango is a library for laying out and rendering text, with an emphasis on
internationalization. Pango can be used anywhere that text layout is
needed, but using Pango in conjunction with L<Cairo> and/or L<Gtk2>
provides a complete solution with high quality text handling and graphics
rendering.

Dynamically loaded modules handle text layout for particular
combinations of script and font backend. Pango provides a wide selection
of modules, including modules for Hebrew, Arabic, Hangul, Thai, and a
number of Indic scripts. Virtually all of the world's major scripts are
supported.

In addition to the low level layout rendering routines, Pango includes
Pango::Layout, a high level driver for laying out entire blocks of text,
and routines to assist in editing internationalized text.

%prep
%setup -q -n %{cpan_name}-%{version}
%patch0

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%check
%if %{with Gtk2}
#### FIXME
#### failing with:
## (EE) XKB: Couldn't open rules file /usr/share/X11/xkb/rules/base
## XKB: Failed to compile keymap
## Keyboard initialization failed. This could be a missing or incorrect setup of xkeyboard-config
#
Xvfb -fp /usr/share/fonts/misc -extension RANDR :95 &
trap "kill $! || true" EXIT
sleep 5
DISPLAY=:95 make test
%else
make test
%endif

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%clean
rm -rf %{buildroot}

%files -f %{name}.files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog.pre-git doctypes LICENSE maps-1.0 maps-1.10 maps-1.16 maps-1.18 maps-1.4 maps-1.6 maps-1.8 NEWS pango.exports pango.typemap README xs_files-1.0 xs_files-1.10 xs_files-1.16 xs_files-1.6

%changelog
