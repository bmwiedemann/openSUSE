#
# spec file for package perl-LWP-MediaTypes
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


Name:           perl-LWP-MediaTypes
Version:        6.04
Release:        0
%define cpan_name LWP-MediaTypes
Summary:        Guess media type for a file or a URL
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/O/OA/OALDERS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::Fatal)
%{perl_requires}

%description
This module provides functions for handling media (also known as MIME)
types and encodings. The mapping from file extensions to media types is
defined by the _media.types_ file. If the _~/.media.types_ file exists it
is used instead. For backwards compatibility we will also look for
_~/.mime.types_.

The following functions are exported by default:

* guess_media_type( $filename )

* guess_media_type( $uri )

* guess_media_type( $filename_or_object, $header_to_modify )

This function tries to guess media type and encoding for a file or objects
that support the a 'path' or 'filename' method, eg, URI or File::Temp
objects. When an object does not support either method, it will be
stringified to determine the filename. It returns the content type, which
is a string like '"text/html"'. In array context it also returns any
content encodings applied (in the order used to encode the file). You can
pass a URI object reference, instead of the file name.

If the type can not be deduced from looking at the file name, then
guess_media_type() will let the '-T' Perl operator take a look. If this
works (and '-T' returns a TRUE value) then we return _text/plain_ as the
type, otherwise we return _application/octet-stream_ as the type.

The optional second argument should be a reference to a HTTP::Headers
object or any object that implements the $obj->header method in a similar
way. When it is present the values of the 'Content-Type' and
'Content-Encoding' will be set for this header.

* media_suffix( $type, ... )

This function will return all suffixes that can be used to denote the
specified media type(s). Wildcard types can be used. In a scalar context it
will return the first suffix found. Examples:

  @suffixes = media_suffix('image/*', 'audio/basic');
  $suffix = media_suffix('text/html');

The following functions are only exported by explicit request:

* add_type( $type, @exts )

Associate a list of file extensions with the given media type. Example:

    add_type("x-world/x-vrml" => qw(wrl vrml));

* add_encoding( $type, @ext )

Associate a list of file extensions with an encoding type. Example:

 add_encoding("x-gzip" => "gz");

* read_media_types( @files )

Parse media types files and add the type mappings found there. Example:

    read_media_types("conf/mime.types");

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README
%license LICENSE

%changelog
