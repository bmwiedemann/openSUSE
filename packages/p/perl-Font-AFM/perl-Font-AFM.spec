#
# spec file for package perl-Font-AFM
#
# Copyright (c) 2019 SUSE LLC.
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


Name:           perl-Font-AFM
Version:        1.20
Release:        0
Summary:        Interface to Adobe Font Metrics Files
License:        Artistic-1.0 OR GPL-2.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/pod/Font::AFM
Source:         https://cpan.metacpan.org/authors/id/G/GA/GAAS/Font-AFM-%{version}.tar.gz
BuildArch:      noarch
%{perl_requires}

%description
This module implements the Font::AFM class. Objects of this class are
initialized from an AFM file and allow you to obtain information about
the font and the metrics of the various glyphs in the font.

%prep
%setup -q -n Font-AFM-%{version}

%build
perl Makefile.PL
make %{?_smp_mflags}

%check
make %{?_smp_mflags} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-, root, root)
%doc README Changes

%changelog
