#
# spec file for package perl-Image-Size
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Image-Size
Version:        3.300
Release:        0
#Upstream: Artistic-1.0 or GPL-1.0+
%define cpan_name Image-Size
Summary:        Read the Dimensions of an Image in Several Popular Formats
License:        LGPL-2.1 or Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Image-Size/
Source0:        http://www.cpan.org/authors/id/R/RJ/RJRAY/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
Patch0:         endian.patch
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build) >= 0.42
BuildRequires:  perl(Test::More) >= 0.80
Requires:       perl(Module::Build) >= 0.28
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
%setup -q -n %{cpan_name}-%{version}
%patch0 -p1
find . -type f -print0 | xargs -0 chmod 644

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc ChangeLog ChangeLog.xml etc ex imgsize README README.textile

%changelog
