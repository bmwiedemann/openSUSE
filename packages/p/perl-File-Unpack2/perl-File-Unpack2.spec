#
# spec file for package perl-File-Unpack2
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define cpan_name File-Unpack2
Name:           perl-File-Unpack2
Version:        2.30.0
Release:        0
# 2.03 -> normalize -> 2.30.0
%define cpan_version 2.03
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Aggressively unpack any archive, recursively, by mime type
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/K/KR/KRAIH/%{cpan_name}-%{cpan_version}.tar.gz
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(BSD::Resource)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 7.12
BuildRequires:  perl(File::LibMagic)
BuildRequires:  perl(File::MimeInfo::Magic)
BuildRequires:  perl(Filesys::Statvfs)
BuildRequires:  perl(IPC::Run)
BuildRequires:  perl(JSON)
BuildRequires:  perl(String::ShellQuote)
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(Text::Sprintf::Named)
Requires:       perl(BSD::Resource)
Requires:       perl(File::LibMagic)
Requires:       perl(File::MimeInfo::Magic)
Requires:       perl(Filesys::Statvfs)
Requires:       perl(IPC::Run)
Requires:       perl(JSON)
Requires:       perl(String::ShellQuote)
Requires:       perl(Text::Sprintf::Named)
Provides:       perl(File::Unpack2) = %{version}
%undefine       __perllib_provides
Recommends:     perl(Compress::Raw::Bzip2)
Recommends:     perl(Compress::Raw::Lzma)
Recommends:     perl(Compress::Raw::Zlib) >= 2.024
%{perl_requires}

%description
File::Unpack2 unpacks archives and compressed files of essentially any
common type - 'bz2', 'gz', 'xz'/'lzma', 'zip', 'tar', 'cpio', 'iso', 'rpm',
'deb', 'cab', '7z', 'rar', and more, down to 'pdf' and 'odf' - and it does
so _aggressively_: it identifies each file by its *mime type* rather than
its name, and it recursively descends into everything it produces, so a
tar-inside-zip-inside-rpm is peeled apart to the last layer without being
fooled by misleading (or absent) file suffixes.

It was built for, and is primarily developed as a dependency of, at
https://github.com/openSUSE/cavil, openSUSE's legal review system, whose
job is to extract every scrap of readable text from a source package so it
can be scanned for license information. That goal - _expose as much
readable payload as possible_ - shapes the whole design: unpacking
continues as deep as it can, and individual failures are logged and stepped
over rather than aborting the run.

Unpacking is dispatched to per-mime-type *helpers*. Many are built in
(wrapping the usual command line tools such as 'tar', 'unzip' and
'rpm2cpio'). Support for further formats is an optional extension: register
a helper command programmatically with 'mime_helper', or point
'mime_helper_dir' (or the 'FILE_UNPACK2_HELPER_DIR' environment variable)
at a directory of executable helper scripts named after the mime types they
handle. File::Unpack2 itself ships no external helpers. See unpack for the
helper calling protocol.

Because Cavil feeds it whole distributions - including binaries,
deliberately malformed samples and archive "bombs" - File::Unpack2 is
hardened against hostile input: it enforces optional caps on file count,
total bytes and per-helper runtime, watches helpers for stalls, and passes
memory limits to the 'xz'/'lzma' decoders. See new for the relevant knobs.

A logfile (JSON, or a plain listing) precisely records every mime type
detected and every unpack action taken.

See the 'docs/Architecture.md' document in the distribution for a prose
overview of how it all fits together.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

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
%doc Changes docs README.md

%changelog
