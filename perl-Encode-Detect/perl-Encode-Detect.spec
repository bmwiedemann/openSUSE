#
# spec file for package perl-Encode-Detect
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

# norootforbuild


Name:           perl-Encode-Detect
%define cpan_name Encode-Detect
Summary:        An Encode::Encoding subclass that detects the encoding of data
Version:        1.01
Release:        4
License:        MPL-1.1
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Encode-Detect
Source:         %{cpan_name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{perl_requires}
BuildRequires:  gcc-c++
BuildRequires:  perl
%if 0%{?suse_version} && 0%{?suse_version} <= 1210
BuildRequires:  perl-macros
%endif
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(Module::Build)

%description
This Perl module is an Encode::Encoding subclass that uses
Encode::Detect::Detector to determine the charset of the input data and then
decodes it using the encoder of the detected charset.

It is similar to Encode::Guess, but does not require the configuration of a set
of expected encodings. Like Encode::Guess, it only supports decoding--it cannot
encode.

Authors:
--------
    John Gardiner Myers <jgmyers@proofpoint.com>

%prep
%setup -q -n %{cpan_name}-%{version}

%build
export CFLAGS="$RPM_OPT_FLAGS"
export CXXFLAGS="$RPM_OPT_FLAGS"
%{__perl} Build.PL --prefix $RPM_BUILD_ROOT/usr --installdirs vendor
./Build

%check
./Build test

%install
./Build install
%perl_process_packlist
%perl_gen_filelist

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files -f %{name}.files
%defattr(-, root, root)
%doc Changes LICENSE

%changelog
