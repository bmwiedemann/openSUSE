#
# spec file for package perl-HTTP-Message
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


%define cpan_name HTTP-Message
Name:           perl-HTTP-Message
Version:        6.460.0
Release:        0
# 6.46 -> normalize -> 6.460.0
%define cpan_version 6.46
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        HTTP style message (base class)
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/O/OA/OALDERS/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Clone) >= 0.46
BuildRequires:  perl(Compress::Raw::Bzip2)
BuildRequires:  perl(Compress::Raw::Zlib) >= 2.062
BuildRequires:  perl(Encode) >= 3.01
BuildRequires:  perl(Encode::Locale) >= 1
BuildRequires:  perl(HTTP::Date) >= 6
BuildRequires:  perl(IO::Compress::Bzip2) >= 2.021
BuildRequires:  perl(IO::Compress::Deflate)
BuildRequires:  perl(IO::Compress::Gzip)
BuildRequires:  perl(IO::HTML)
BuildRequires:  perl(IO::Uncompress::Inflate)
BuildRequires:  perl(IO::Uncompress::RawInflate)
BuildRequires:  perl(LWP::MediaTypes) >= 6
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Needs)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(URI) >= 1.10
BuildRequires:  perl(URI::URL)
BuildRequires:  perl(parent)
Requires:       perl(Clone) >= 0.46
Requires:       perl(Compress::Raw::Bzip2)
Requires:       perl(Compress::Raw::Zlib) >= 2.062
Requires:       perl(Encode) >= 3.01
Requires:       perl(Encode::Locale) >= 1
Requires:       perl(HTTP::Date) >= 6
Requires:       perl(IO::Compress::Bzip2) >= 2.021
Requires:       perl(IO::Compress::Deflate)
Requires:       perl(IO::Compress::Gzip)
Requires:       perl(IO::HTML)
Requires:       perl(IO::Uncompress::Inflate)
Requires:       perl(IO::Uncompress::RawInflate)
Requires:       perl(LWP::MediaTypes) >= 6
Requires:       perl(URI) >= 1.10
Requires:       perl(parent)
Provides:       perl(HTTP::Config) = %{version}
Provides:       perl(HTTP::Headers) = %{version}
Provides:       perl(HTTP::Headers::Auth) = %{version}
Provides:       perl(HTTP::Headers::ETag) = %{version}
Provides:       perl(HTTP::Headers::Util) = %{version}
Provides:       perl(HTTP::Message) = %{version}
Provides:       perl(HTTP::Request) = %{version}
Provides:       perl(HTTP::Request::Common) = %{version}
Provides:       perl(HTTP::Response) = %{version}
Provides:       perl(HTTP::Status) = %{version}
%undefine       __perllib_provides
Recommends:     perl(IO::Compress::Brotli) >= 0.4.1
Recommends:     perl(IO::Uncompress::Brotli) >= 0.4.1
%{perl_requires}

%description
An 'HTTP::Message' object contains some headers and a content body. The
following methods are available:

* $mess = HTTP::Message->new

* $mess = HTTP::Message->new( $headers )

* $mess = HTTP::Message->new( $headers, $content )

This constructs a new message object. Normally you would want construct
'HTTP::Request' or 'HTTP::Response' objects instead.

The optional $header argument should be a reference to an 'HTTP::Headers'
object or a plain array reference of key/value pairs. If an 'HTTP::Headers'
object is provided then a copy of it will be embedded into the constructed
message, i.e. it will not be owned and can be modified afterwards without
affecting the message.

The optional $content argument should be a string of bytes.

* $mess = HTTP::Message->parse( $str )

This constructs a new message object by parsing the given string.

* $mess->headers

Returns the embedded 'HTTP::Headers' object.

* $mess->headers_as_string

* $mess->headers_as_string( $eol )

Call the as_string() method for the headers in the message. This will be
the same as

    $mess->headers->as_string

but it will make your program a whole character shorter :-)

* $mess->content

* $mess->content( $bytes )

The content() method sets the raw content if an argument is given. If no
argument is given the content is not touched. In either case the original
raw content is returned.

If the 'undef' argument is given, the content is reset to its default
value, which is an empty string.

Note that the content should be a string of bytes. Strings in perl can
contain characters outside the range of a byte. The 'Encode' module can be
used to turn such strings into a string of bytes.

* $mess->add_content( $bytes )

The add_content() methods appends more data bytes to the end of the current
content buffer.

* $mess->add_content_utf8( $string )

The add_content_utf8() method appends the UTF-8 bytes representing the
string to the end of the current content buffer.

* $mess->content_ref

* $mess->content_ref( \$bytes )

The content_ref() method will return a reference to content buffer string.
It can be more efficient to access the content this way if the content is
huge, and it can even be used for direct manipulation of the content, for
instance:

  ${$res->content_ref} =~ s/\bfoo\b/bar/g;

This example would modify the content buffer in-place.

If an argument is passed it will setup the content to reference some
external source. The content() and add_content() methods will automatically
dereference scalar references passed this way. For other references
content() will return the reference itself and add_content() will refuse to
do anything.

* $mess->content_charset

This returns the charset used by the content in the message. The charset is
either found as the charset attribute of the 'Content-Type' header or by
guessing.

See http://www.w3.org/TR/REC-html40/charset.html#spec-char-encoding for
details about how charset is determined.

* $mess->decoded_content( %options )

Returns the content with any 'Content-Encoding' undone and, for textual
content ('Content-Type' values starting with 'text/', exactly matching
'application/xml', or ending with '+xml'), the raw content's character set
decoded into Perl's Unicode string format. Note that this at
https://github.com/libwww-perl/HTTP-Message/pull/99 attempt to decode
declared character sets for any other content types like 'application/json'
or 'application/javascript'. If the 'Content-Encoding' or 'charset' of the
message is unknown, this method will fail by returning 'undef'.

The following options can be specified.

  * 'charset'

This overrides the charset parameter for text content. The value 'none' can
used to suppress decoding of the charset.

  * 'default_charset'

This overrides the default charset guessed by content_charset() or if that
fails "ISO-8859-1".

  * 'alt_charset'

If decoding fails because the charset specified in the Content-Type header
isn't recognized by Perl's Encode module, then try decoding using this
charset instead of failing. The 'alt_charset' might be specified as 'none'
to simply return the string without any decoding of charset as alternative.

  * 'charset_strict'

Abort decoding if malformed characters is found in the content. By default
you get the substitution character ("\x{FFFD}") in place of malformed
characters.

  * 'raise_error'

If TRUE then raise an exception if not able to decode content. Reason might
be that the specified 'Content-Encoding' or 'charset' is not supported. If
this option is FALSE, then decoded_content() will return 'undef' on errors,
but will still set $@.

  * 'ref'

If TRUE then a reference to decoded content is returned. This might be more
efficient in cases where the decoded content is identical to the raw
content as no data copying is required in this case.

* $mess->decodable

* HTTP::Message::decodable()

This returns the encoding identifiers that decoded_content() can process.
In scalar context returns a comma separated string of identifiers.

This value is suitable for initializing the 'Accept-Encoding' request
header field.

* $mess->decode

This method tries to replace the content of the message with the decoded
version and removes the 'Content-Encoding' header. Returns TRUE if
successful and FALSE if not.

If the message does not have a 'Content-Encoding' header this method does
nothing and returns TRUE.

Note that the content of the message is still bytes after this method has
been called and you still need to call decoded_content() if you want to
process its content as a string.

* $mess->encode( $encoding, ... )

Apply the given encodings to the content of the message. Returns TRUE if
successful. The "identity" (non-)encoding is always supported; other
currently supported encodings, subject to availability of required
additional modules, are "gzip", "deflate", "x-bzip2", "base64" and "br".

A successful call to this function will set the 'Content-Encoding' header.

Note that 'multipart/*' or 'message/*' messages can't be encoded and this
method will croak if you try.

* $mess->parts

* $mess->parts( @parts )

* $mess->parts( \@parts )

Messages can be composite, i.e. contain other messages. The composite
messages have a content type of 'multipart/*' or 'message/*'. This method
give access to the contained messages.

The argumentless form will return a list of 'HTTP::Message' objects. If the
content type of $msg is not 'multipart/*' or 'message/*' then this will
return the empty list. In scalar context only the first object is returned.
The returned message parts should be regarded as read-only (future versions
of this library might make it possible to modify the parent by modifying
the parts).

If the content type of $msg is 'message/*' then there will only be one part
returned.

If the content type is 'message/http', then the return value will be either
an 'HTTP::Request' or an 'HTTP::Response' object.

If a @parts argument is given, then the content of the message will be
modified. The array reference form is provided so that an empty list can be
provided. The @parts array should contain 'HTTP::Message' objects. The
@parts objects are owned by $mess after this call and should not be
modified or made part of other messages.

When updating the message with this method and the old content type of
$mess is not 'multipart/*' or 'message/*', then the content type is set to
'multipart/mixed' and all other content headers are cleared.

This method will croak if the content type is 'message/*' and more than one
part is provided.

* $mess->add_part( $part )

This will add a part to a message. The $part argument should be another
'HTTP::Message' object. If the previous content type of $mess is not
'multipart/*' then the old content (together with all content headers) will
be made part #1 and the content type made 'multipart/mixed' before the new
part is added. The $part object is owned by $mess after this call and
should not be modified or made part of other messages.

There is no return value.

* $mess->clear

Will clear the headers and set the content to the empty string. There is no
return value

* $mess->protocol

* $mess->protocol( $proto )

Sets the HTTP protocol used for the message. The protocol() is a string
like 'HTTP/1.0' or 'HTTP/1.1'.

* $mess->clone

Returns a copy of the message object.

* $mess->as_string

* $mess->as_string( $eol )

Returns the message formatted as a single string.

The optional $eol parameter specifies the line ending sequence to use. The
default is "\n". If no $eol is given then as_string will ensure that the
returned string is newline terminated (even when the message content is
not). No extra newline is appended if an explicit $eol is passed.

* $mess->dump( %opt )

Returns the message formatted as a string. In void context print the
string.

This differs from '$mess->as_string' in that it escapes the bytes of the
content so that it's safe to print them and it limits how much content to
print. The escapes syntax used is the same as for Perl's double quoted
strings. If there is no content the string "(no content)" is shown in its
place.

Options to influence the output can be passed as key/value pairs. The
following options are recognized:

  * maxlength => $num

How much of the content to show. The default is 512. Set this to 0 for
unlimited.

If the content is longer then the string is chopped at the limit and the
string "...\n(### more bytes not shown)" appended.

  * no_content => $str

Replaces the "(no content)" marker.

  * prefix => $str

A string that will be prefixed to each line of the dump.

All methods unknown to 'HTTP::Message' itself are delegated to the
'HTTP::Headers' object that is part of every message. This allows
convenient access to these methods. Refer to HTTP::Headers for details of
these methods:

    $mess->header( $field => $val )
    $mess->push_header( $field => $val )
    $mess->init_header( $field => $val )
    $mess->remove_header( $field )
    $mess->remove_content_headers
    $mess->header_field_names
    $mess->scan( \&doit )

    $mess->date
    $mess->expires
    $mess->if_modified_since
    $mess->if_unmodified_since
    $mess->last_modified
    $mess->content_type
    $mess->content_encoding
    $mess->content_length
    $mess->content_language
    $mess->title
    $mess->user_agent
    $mess->server
    $mess->from
    $mess->referer
    $mess->www_authenticate
    $mess->authorization
    $mess->proxy_authorization
    $mess->authorization_basic
    $mess->proxy_authorization_basic

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

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
%doc Changes CONTRIBUTING.md CONTRIBUTORS README.md
%license LICENSE

%changelog
