#
# spec file for package perl-Convert-TNEF
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-Convert-TNEF
Version:        0.18
Release:        0
%define cpan_name Convert-TNEF
Summary:        Perl module to read TNEF files
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Convert-TNEF/
Source:         http://www.cpan.org/authors/id/D/DO/DOUGW/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(IO::Wrap)
BuildRequires:  perl(MIME::Body) >= 4.109
#BuildRequires: perl(Convert::TNEF)
Requires:       perl(IO::Wrap)
Requires:       perl(MIME::Body) >= 4.109
%{perl_requires}

%description
 TNEF stands for Transport Neutral Encapsulation Format, and if you've
 ever been unfortunate enough to receive one of these files as an email
 attachment, you may want to use this module.

 read() takes as its first argument any file handle open
 for reading. The optional second argument is a hash reference
 which contains one or more of the following keys:

 output_dir - Path for storing TNEF attribute data kept in files
 (default: current directory).

 output_prefix - File prefix for TNEF attribute data kept in files
 (default: 'tnef').

 output_to_core - TNEF attribute data will be saved in core memory unless
 it is greater than this many bytes (default: 4096). May also be set to
 'NONE' to keep all data in files, or 'ALL' to keep all data in core.

 buffer_size - Buffer size for reading in the TNEF file (default: 1024).

 debug - If true, outputs all sorts of info about what the read() function
 is reading, including the raw ascii data along with the data converted
 to hex (default: false).

 display_after_err - If debug is true and an error is encountered,
 reads and displays this many bytes of data following the error
 (default: 32).

 debug_max_display - If debug is true then read and display at most
 this many bytes of data for each TNEF attribute (default: 1024).

 debug_max_line_size - If debug is true then at most this many bytes of
 data will be displayed on each line for each TNEF attribute
 (default: 64).

 ignore_checksum - If true, will ignore checksum errors while parsing
 data (default: false).

 read() returns an object containing the TNEF 'attributes' read from the
 file and the data for those attributes. If all you want are the
 attachments, then this is mostly garbage, but if you're interested then
 you can see all the garbage by turning on debugging. If the garbage
 proves useful to you, then let me know how I can maybe make it more
 useful.

 If an error is encountered, an undefined value is returned and the
 package variable $errstr is set to some helpful message.

 read_in() is a convienient front end for read() which takes a filename
 instead of a handle.

 read_ent() is another convient front end for read() which can take a
 MIME::Entity object (or any object with like methods, specifically
 open("r"), read($buff,$num_bytes), and close ).

 purge() deletes any on-disk data that may be in the attachments of
 the TNEF object.

 message() returns the message portion of the tnef object, if any.
 The thing it returns is like an attachment, but its not an attachment.
 For instance, it more than likely does not have a name or any
 attachment data.

 attachments() returns a list of the attachments that the given TNEF
 object contains. Returns a list ref if not called in array context.

 data() takes a TNEF attribute name, and returns a string value for that 
 attribute for that attachment. Its your own problem if the string is too
 big for memory. If no argument is given, then the 'AttachData' attribute
 is assumed, which is probably the attachment data you're looking for.

 name() is the same as data(), except the attribute 'AttachTitle' is
 the default, which returns the 8 character + 3 character extension name
 of the attachment.

 longname() returns the long filename and extension of an attachment. This
 is embedded within a MAPI property of the 'Attachment' attribute data, so
 we attempt to extract the name out of that.

 size() takes an TNEF attribute name, and returns the size in bytes for
 the data for that attachment attribute.

 datahandle() is a method for attachments which takes a TNEF attribute
 name, and returns the data for that attribute as a handle which is
 the same as a MIME::Body handle.  See MIME::Body for all the applicable
 methods. If no argument is given, then 'AttachData' is assumed.

%prep
%setup -q -n %{cpan_name}-%{version}

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
%doc Changes README

%changelog
