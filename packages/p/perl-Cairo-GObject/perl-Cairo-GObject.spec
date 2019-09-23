#
# spec file for package perl-Cairo-GObject
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


Name:           perl-Cairo-GObject
Version:        1.005
Release:        0
%define cpan_name Cairo-GObject
Summary:        Integrate Cairo into the Glib type system
License:        LGPL-2.1-or-later
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/X/XA/XAOC/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Cairo) >= 1.080
BuildRequires:  perl(ExtUtils::Depends) >= 0.2
BuildRequires:  perl(ExtUtils::PkgConfig) >= 1.000000
BuildRequires:  perl(Glib) >= 1.224
Requires:       perl(Cairo) >= 1.080
Requires:       perl(ExtUtils::Depends) >= 0.2
Requires:       perl(ExtUtils::PkgConfig) >= 1.000000
Requires:       perl(Glib) >= 1.224
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  pkgconfig(cairo-gobject)
# MANUAL END

%description
Integrate Cairo into the Glib type system

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
%doc examples NEWS perl-Cairo-GObject.doap README
%license LICENSE

%changelog
