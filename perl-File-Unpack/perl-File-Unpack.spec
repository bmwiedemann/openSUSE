#
# spec file for package perl-File-Unpack
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


Name:           perl-File-Unpack
Version:        0.70
Release:        0%{?dist}
Summary:        An strong archive file unpacker, based on mime-types
License:        GPL-1.0-or-later OR Artistic-1.0
Group:          Development/Libraries/Perl
Source:         http://search.cpan.org/CPAN/authors/id/J/JN/JNW/File-Unpack-%{version}.tar.gz
Patch0:         fix-xml-test.diff
Patch1:         https://patch-diff.githubusercontent.com/raw/jnweiger/perl-File-Unpack/pull/5.diff
Patch2:         https://patch-diff.githubusercontent.com/raw/jnweiger/perl-File-Unpack/pull/6.diff
Patch3:         https://patch-diff.githubusercontent.com/raw/jnweiger/perl-File-Unpack/pull/9.diff
Patch4:         https://patch-diff.githubusercontent.com/raw/jnweiger/perl-File-Unpack/pull/10.diff
Patch5:         https://patch-diff.githubusercontent.com/raw/jnweiger/perl-File-Unpack/pull/11.diff
Url:            https://github.com/jnweiger/perl-File-Unpack
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  perl(Test::CheckManifest)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)

BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Compare)
BuildRequires:  perl(File::LibMagic)
BuildRequires:  perl(File::MimeInfo::Magic)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Temp)

# SLES11 does does not have this:
BuildRequires:  perl(Compress::Raw::Lzma)
# (provider perl-Compress-Raw-Zlib is obsoleted by installed perl)
BuildRequires:  perl(BSD::Resource)
BuildRequires:  perl(Compress::Raw::Bzip2)
BuildRequires:  perl(Compress::Raw::Zlib) >= 2.024
BuildRequires:  perl(Filesys::Statvfs)
BuildRequires:  perl(IPC::Run)
BuildRequires:  perl(JSON)
BuildRequires:  perl(String::ShellQuote)
BuildRequires:  perl(Text::Sprintf::Named)
# shared-mime-info is a dependency of perl-File-MimeInfo
# file is a dependency of perl-File-LibMagic
BuildRequires:  fdupes
BuildRequires:  file >= 5.03
BuildRequires:  shared-mime-info >= 0.60

Requires:       perl(Carp)
Requires:       perl(Cwd)
Requires:       perl(File::LibMagic)
Requires:       perl(File::MimeInfo::Magic)
Requires:       perl(File::Path)
Requires:       perl(File::Temp)

%if 0%{?suse_version} >= 1110
# SLES11 does does not have this:
Requires:       perl(Compress::Raw::Lzma)
%endif
Requires:       perl(Compress::Raw::Bzip2)
Requires:       perl(Compress::Raw::Zlib)
# 2.024 is provided by perl-5.12.1 in 11.3
Requires:       file >= 5.03
Requires:       shared-mime-info >= 0.60
Requires:       perl(BSD::Resource)
Requires:       perl(Compress::Raw::Zlib) >= 2.024
Requires:       perl(Filesys::Statvfs)
Requires:       perl(IPC::Run)
Requires:       perl(JSON)
Requires:       perl(Text::Sprintf::Named)
# App-cpanminus provides a bogus String::ShellQuote. We need to go by package name here.
# Requires:       perl(String::ShellQuote)
Requires:       perl-String-ShellQuote

## refer to Unpack.pm:@builtin_mime_handlers and to the helper subdirectory
## to see what we might need:
# grep '# Requires: ' Unpack.pm helper/*

%if 0%{?suse_version} > 1110
# 11.1 and SLES11 say: unresolvable: nothing provides xz
BuildRequires:  xz
Requires:       xz
%else
Recommends:     xz
%endif

%if 0%{?suse_version} > 1320
BuildRequires:  lzip
Requires:       lzip
%else
Recommends:     lzip
%endif

BuildRequires:  poppler-tools
Requires:       poppler-tools

## The following BuildRequires is for testing existance only.
## If you cannot provide a package, you may remove it from both BuildRequires 
## and Requires, and move it over to Recommends.
BuildRequires:  binutils
BuildRequires:  bzip2
BuildRequires:  cabextract
BuildRequires:  cpio
%if 0%{?suse_version} >= 1500
BuildRequires:  mkisofs
%else
BuildRequires:  genisoimage
%endif
BuildRequires:  gzip
# Remove when p7zip-full is in all products
%if 0%{suse_version} > 1500
BuildRequires:  p7zip-full
%else
BuildRequires:  p7zip
%endif
BuildRequires:  rpm
BuildRequires:  sharutils
BuildRequires:  tar
BuildRequires:  unzip
Requires:       binutils
Requires:       bzip2
Requires:       cabextract
Requires:       cpio
%if 0%{?suse_version} >= 1500
Requires:       mkisofs
%else
Requires:       genisoimage
%endif
Requires:       gzip
# Remove when p7zip-full is in all products
%if 0%{suse_version} > 1500
Requires:       p7zip-full
%else
Requires:       p7zip
%endif
Requires:       rpm
Requires:       sharutils
Requires:       tar
Requires:       unzip
Recommends:     unrar poppler-tools xz upx antiword xar

%if 0%{?suse_version} < 1140
Requires:       perl = %{perl_version}
%else
%{perl_requires}
%endif
Requires:       file-unpack == %version

%description
File::Unpack is an unpacker for archives and files
(bz2/gz/zip/tar/cpio/iso/rpm/deb/cab/lzma/7z/rar/...).  We call
it strong, because it is not fooled by file suffixes, or multiply wrapped packages.
It reliably detects mime-types and recursivly descends into each archive found
until it finally exposes all unpackable payload contents. 
A precise logfile can be written, describing mimetypes and unpack actions.
Most of the known archive file formats are supported. Shell-script-style
plugins can be added to support additinal formats.

%package -n file-unpack
Summary:        Command line tool to unpack anything
Group:          Productivity/Archiving/Compression
Requires:       perl(File::Unpack) == %version

%description -n file-unpack
/usr/bin/file-unpack is a trivial command line frontend that
ships with the File::Unpack perl module.

%prep
%setup -q -n File-Unpack-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

(cd contrib && %{__make} stringsx)

%install
%{__make} pure_install PERL_INSTALL_ROOT=%{buildroot}
mv $RPM_BUILD_ROOT/usr/bin/{file_unpack,file-unpack} || :
install -d       $RPM_BUILD_ROOT/usr/share/File-Unpack/helper/
install helper/* $RPM_BUILD_ROOT/usr/share/File-Unpack/helper/

%fdupes $RPM_BUILD_ROOT/usr/share/File-Unpack/

ln -s /usr/bin/file-unpack $RPM_BUILD_ROOT/usr/bin/file_unpack
ln -s /usr/bin/file-unpack $RPM_BUILD_ROOT/usr/bin/unpack-file
ln -s /usr/bin/file-unpack $RPM_BUILD_ROOT/usr/bin/unpack-file-deep
ln -s /usr/bin/file-unpack $RPM_BUILD_ROOT/usr/bin/unpack-deep
ln -s /usr/bin/file-unpack $RPM_BUILD_ROOT/usr/bin/file-unpack-deep

## CAUTION: a line beginning with . is a macro-expanded by nroff.
# echo .nf > file-unpack.1
# perl -Iblib/lib file-unpack.pl --help >> file-unpack.1 && true
# rm -rf file-unpack.1

cat <<EOF> file-unpack.pod
=pod

=head1 SYNOPSIS
EOF
perl file-unpack.pl --help >> file-unpack.pod && true
cat <<EOF1>> file-unpack.pod
=head1 REFERENCES

See also C<perldoc File::Unpack>
EOF1
pod2man file-unpack.pod > file-unpack.1
rm file-unpack.pod
echo file-unpack.1 >> MANIFEST

install -m0644 -D file-unpack.1 $RPM_BUILD_ROOT/%_mandir/man1/file-unpack.1
ln -s %_mandir/man1/file-unpack.1 $RPM_BUILD_ROOT/%_mandir/man1/unpack_file.1
install -m0755 -D contrib/stringsx $RPM_BUILD_ROOT/%_bindir/stringsx
rm contrib/stringsx # so that the Manifest in make check is not confused.

# FIXME: use ./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
# maybe then we would not need to remove the .packlist files :-)
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'

find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'

%{_fixperms} %{buildroot}/*
%perl_process_packlist
%perl_gen_filelist

## seperate bin man from the main package 
mv %{name}.files /tmp/%{name}.files
sed -ie '/\/man\?/d' /tmp/%{name}.files
sed -ie '/\/bin\//d' /tmp/%{name}.files

%check
export RELEASE_TESTING=1
#%{__make} test

%files -f /tmp/%{name}.files
%defattr(-,root,root,-)
%doc README Changes
%dir /usr/share/File-Unpack
/usr/share/File-Unpack/*
%doc %_mandir/man3/*

%files -n file-unpack
%defattr(-,root,root)
/usr/bin/*
%doc %_mandir/man1/*

%changelog
