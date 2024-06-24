#
# spec file for package perl-XML-LibXSLT
#
# Copyright (c) 2024 SUSE LLC
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


%define cpan_name XML-LibXSLT
Name:           perl-XML-LibXSLT
Version:        2.003000
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Interface to GNOME libxslt library
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(File::Path) >= 2.06
BuildRequires:  perl(XML::LibXML) >= 1.70
Requires:       perl(File::Path) >= 2.06
Requires:       perl(XML::LibXML) >= 1.70
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  libxslt-devel
# MANUAL END

%description
This module is an interface to the GNOME project's libxslt. This is an
extremely good XSLT engine, highly compliant and also very fast. I have
tests showing this to be more than twice as fast as Sablotron.

%prep
%autosetup  -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes example README
%license LICENSE

%changelog
