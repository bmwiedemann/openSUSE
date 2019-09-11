#
# spec file for package perl-Gnome2
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


Name:           perl-Gnome2
Version:        1.047
Release:        0
%define cpan_name Gnome2
Summary:        Perl interface to the 2.x series of the GNOME libraries
License:        LGPL-2.1+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Gnome2/
Source0:        https://cpan.metacpan.org/authors/id/X/XA/XAOC/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::Depends) >= 0.20
BuildRequires:  perl(ExtUtils::PkgConfig) >= 1.030000
BuildRequires:  perl(Glib) >= 1.04
BuildRequires:  perl(Gnome2::Canvas) >= 1.00
BuildRequires:  perl(Gnome2::VFS) >= 1.00
BuildRequires:  perl(Gtk2) >= 1.00
Requires:       perl(ExtUtils::Depends) >= 0.20
Requires:       perl(ExtUtils::PkgConfig) >= 1.030000
Requires:       perl(Glib) >= 1.04
Requires:       perl(Gnome2::Canvas) >= 1.00
Requires:       perl(Gnome2::VFS) >= 1.00
Requires:       perl(Gtk2) >= 1.00
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  libgnomeui-devel
# MANUAL END

%description
Since this module tries to stick very closely to the C API, the
documentation found at

  http://developer.gnome.org/libgnome

and

  http://developer.gnome.org/libgnomeui

is the canonical reference.

In addition to that, there's also the automatically generated API
documentation: Gnome2::index(3pm).

The mapping described in Gtk2::api(3pm) also applies to this module.

To discuss this module, ask questions and flame/praise the authors, join
gtk-perl-list@gnome.org at lists.gnome.org.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc AUTHORS ChangeLog.pre-git doctypes examples gnome.typemap maps NEWS perl-Gnome2.doap README TODO
%license LICENSE

%changelog
