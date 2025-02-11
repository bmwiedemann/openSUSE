#
# spec file for package perl-Text-BibTeX
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


%define cpan_name Text-BibTeX
Name:           perl-Text-BibTeX
Version:        0.910.0
Release:        0
# 0.91 -> normalize -> 0.910.0
%define cpan_version 0.91
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Interface to read and parse BibTeX files
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/A/AM/AMBS/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Patch0:         manual-pages-for-libbtparse.patch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Capture::Tiny) >= 0.06
BuildRequires:  perl(Config::AutoConf) >= 0.320
BuildRequires:  perl(ExtUtils::CBuilder) >= 0.27
BuildRequires:  perl(ExtUtils::LibBuilder) >= 0.90.0
BuildRequires:  perl(Module::Build) >= 0.3603
BuildRequires:  perl(Scalar::Util) >= 1.42
Requires:       perl(Scalar::Util) >= 1.42
Provides:       perl(Text::BibTeX) = %{version}
Provides:       perl(Text::BibTeX::BibEntry) = 0.88
Provides:       perl(Text::BibTeX::BibFormat) = 0.88
Provides:       perl(Text::BibTeX::BibSort) = 0.88
Provides:       perl(Text::BibTeX::BibStructure) = 0.88
Provides:       perl(Text::BibTeX::Entry) = 0.88
Provides:       perl(Text::BibTeX::File) = 0.88
Provides:       perl(Text::BibTeX::Name) = 0.88
Provides:       perl(Text::BibTeX::NameFormat) = 0.88
Provides:       perl(Text::BibTeX::SimpleValue) = 0.88
Provides:       perl(Text::BibTeX::Structure) = 0.88
Provides:       perl(Text::BibTeX::StructuredEntry) = 0.88
Provides:       perl(Text::BibTeX::Value) = 0.88
%undefine       __perllib_provides
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  glibc-devel

%package        devel
Summary:        C library for parsing and processing BibTeX files
Group:          Development/Libraries/Other
Provides:       %{name}:%{_libdir}/libbtparse.so

%description    devel
The libbtparse is a C library for parsing and processing BibTeX files.
Note that the interface provided by libbtparse, while complete, is fairly
low-level.  If you have more sophisticated needs, you might be interested
the "Text::BibTeX" module for Perl.


# MANUAL END
%description
The 'Text::BibTeX' module serves mainly as a high-level introduction to the
'Text::BibTeX' library, for both code and documentation purposes. The code
loads the two fundamental modules for processing BibTeX files
('Text::BibTeX::File' and 'Text::BibTeX::Entry'), and this documentation
gives a broad overview of the whole library that isn't available in the
documentation for the individual modules that comprise it.

In addition, the 'Text::BibTeX' module provides a number of miscellaneous
functions that are useful in processing BibTeX data (especially the kind
that comes from bibliographies as defined by BibTeX 0.99, rather than
generic database files). These functions don't generally fit in the
object-oriented class hierarchy centred around the 'Text::BibTeX::Entry'
class, mainly because they are specific to bibliographic data and operate
on generic strings (rather than being tied to a particular BibTeX entry).
These are also documented here, in "MISCELLANEOUS FUNCTIONS".

Note that every module described here begins with the 'Text::BibTeX'
prefix. For brevity, I have dropped this prefix from most class and module
names in the rest of this manual page (and in most of the other manual
pages in the library).

%prep
%autosetup  -n %{cpan_name}-%{cpan_version} -p1

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Build.PL --installdirs=vendor optimize="%{optflags}"
./Build build --flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%doc Changes examples README README.OLD THANKS
%exclude %{_mandir}/man3/*.3.gz

%files devel
%defattr(-,root,root,755)
%{_libdir}/libbtparse.so
%{_mandir}/man3/*.3%{?ext_man}
%{_includedir}/btparse.h

%post devel -p /sbin/ldconfig
%postun devel -p /sbin/ldconfig

%changelog
