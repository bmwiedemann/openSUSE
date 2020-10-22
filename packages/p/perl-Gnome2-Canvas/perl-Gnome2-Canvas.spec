#
# spec file for package perl-Gnome2-Canvas
#
# Copyright (c) 2020 SUSE LLC
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


Name:           perl-Gnome2-Canvas
Version:        1.004
Release:        0
#Upstream: CHECK(Artistic-1.0 or GPL-1.0-or-later)
%define cpan_name Gnome2-Canvas
Summary:        Gnome2::Canvas Perl module
License:        GPL-2.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/X/XA/XAOC/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::Depends) >= 0.2
BuildRequires:  perl(ExtUtils::PkgConfig) >= 1.030000
BuildRequires:  perl(Glib) >= 1.120
BuildRequires:  perl(Gtk2) >= 1.100
Requires:       perl(ExtUtils::Depends) >= 0.200
Requires:       perl(ExtUtils::PkgConfig) >= 1.030000
Requires:       perl(Glib) >= 1.040
Requires:       perl(Gtk2) >= 1.040
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  libgnomecanvas-devel
# MANUAL END

%description
Gnome2::Canvas Perl module

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc AUTHORS canvas.typemap ChangeLog maps NEWS README TODO
%license LICENSE

%changelog
