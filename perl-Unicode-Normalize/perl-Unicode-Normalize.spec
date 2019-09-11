#
# spec file for package perl-Unicode-Normalize
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


Name:           perl-Unicode-Normalize
Version:        1.25
Release:        0
%define cpan_name Unicode-Normalize
Summary:        Unicode Normalization Forms
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Unicode-Normalize/
Source0:        https://cpan.metacpan.org/authors/id/K/KH/KHW/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
Patch0:         perl526.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
Parameters:

'$string' is used as a string under character semantics (see
_perlunicode_).

'$code_point' should be an unsigned integer representing a Unicode code
point.

Note: Between XSUB and pure Perl, there is an incompatibility about the
interpretation of '$code_point' as a decimal number. XSUB converts
'$code_point' to an unsigned integer, but pure Perl does not. Do not use a
floating point nor a negative sign in '$code_point'.

%prep
%setup -q -n %{cpan_name}-%{version}
%patch0 -p1

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
%doc Changes disableXS enableXS MANIFEST.N mkheader Normalize.pmN README
%license LICENSE

%changelog
