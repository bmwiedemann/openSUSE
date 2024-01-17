#
# spec file for package perl-Image-Size
#
# Copyright (c) 2021 SUSE LLC
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


%define cpan_name Image-Size
Name:           perl-Image-Size
Version:        3.300
Release:        0
#Upstream: Artistic-1.0 or GPL-1.0-or-later
Summary:        Read the dimensions of an image in several popular formats
License:        LGPL-2.1-only OR Artistic-1.0
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJRAY/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
Patch0:         endian.patch
# PATCH-FIX-UPSTREAM do not fail on JPEG files with 0x00XX markers
Patch1:         Image-Size-3.300_Fix_JPEG_00_Markers.patch
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build) >= 0.420000
BuildRequires:  perl(Test::More) >= 0.80
Requires:       perl(Module::Build) >= 0.280000
Requires:       perl(Test::More) >= 0.80
Recommends:     perl(Compress::Zlib) >= 2
%{perl_requires}

%description
The *Image::Size* library is based upon the 'wwwis' script written by Alex
Knowles _(alex@ed.ac.uk)_, a tool to examine HTML and add 'width' and
'height' parameters to image tags. The sizes are cached internally based on
file name, so multiple calls on the same file name (such as images used in
bulleted lists, for example) do not result in repeated computations.

%prep
%autosetup  -n %{cpan_name}-%{version} -p1
find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc ChangeLog ChangeLog.xml imgsize README README.textile

%changelog
