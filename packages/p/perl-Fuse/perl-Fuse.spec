#
# spec file for package perl-Fuse
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-Fuse
Summary:        Write filesystems in Perl using FUSE
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Version:        0.16.1
Release:        0.1
Url:            http://search.cpan.org/dist/Fuse/
Source:         http://www.cpan.org/modules/by-module/Fuse/DPATES/Fuse-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  fuse-devel
BuildRequires:  fuse-devel-static
BuildRequires:  module-init-tools
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  pkg-config
BuildRequires:  sudo
#BuildRequires:  perl-Filesys::Statvfs, perl-File-lchown, perl-Unix-Mknod
Requires:       perl = %{perl_version}, fuse

%description
This lets you implement filesystems in perl, through the FUSE (Filesystem
in USErspace) kernel/lib interface.

%prep
%setup -q -n Fuse-%{version}

find . -type f -name '*.pm' -exec %__chmod 0644 {} \;

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
%{__make} %{?_smp_mflags}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.files
%defattr(-,root,root,-)
%doc AUTHORS Changes README

%changelog
