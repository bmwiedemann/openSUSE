#
# spec file for package perl-Pango
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Pango
Version:        1.227
Release:        0
%define cpan_name Pango
Summary:        Layout and render international text
License:        LGPL-2.1-or-later
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/X/XA/XAOC/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Cairo) >= 1.000
BuildRequires:  perl(ExtUtils::Depends) >= 0.300
BuildRequires:  perl(ExtUtils::PkgConfig) >= 1.030000
BuildRequires:  perl(Glib) >= 1.220
Requires:       perl(Cairo) >= 1.000
Requires:       perl(ExtUtils::Depends) >= 0.300
Requires:       perl(ExtUtils::PkgConfig) >= 1.030000
Requires:       perl(Glib) >= 1.220
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  xorg-x11
BuildRequires:  xorg-x11-Xvfb
BuildRequires:  xorg-x11-server
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(pango)
%if %{with Gtk2}
BuildRequires:  perl(Gtk2) >= 1.220
%endif
# MANUAL END

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

%files -f %{name}.files
%defattr(-,root,root,755)
%doc AUTHORS ChangeLog.pre-git doctypes examples maps-1.0 maps-1.10 maps-1.16 maps-1.18 maps-1.4 maps-1.6 maps-1.8 NEWS pango.exports pango.typemap perl-Pango.doap README xs_files-1.0 xs_files-1.10 xs_files-1.16 xs_files-1.6
%license LICENSE

%changelog
