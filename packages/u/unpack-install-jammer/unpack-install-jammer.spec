#
# spec file for package unpack-install-jammer
#
# Copyright (c) 2021 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           unpack-install-jammer
Version:        0.2.0
Release:        0
Summary:        Pulls files out of InstallJammer generated executable installers
License:        GPL-3.0
Group:          Productivity/Archiving/Backup
Url:            https://github.com/lod/unpack-install-jammer/
Source:         https://github.com/lod/unpack-install-jammer/archive/%{version}.tar.gz
BuildRequires:  perl-macros
Requires:       perl-Term-ProgressBar
Requires:       perl-Modern-Perl
Requires:       perl-Compress-Raw-Lzma
Requires:       perl-File-HomeDir
Requires:       perl-Data-Dump
BuildArch:      noarch
%{perl_requires}

%description
It will search through your binary install blob, identify and extract the files
buried within and drop them in a local directory. No higher permissions required,
the only thing that is executed is the Perl script which lives up to Perl's
reputation of easy inspection.

%prep
%setup -q

%build

%install
install extract.pl -Dm0755 %{buildroot}%{_bindir}/unpack-install-jammer

%files
%{_bindir}/unpack-install-jammer
%doc README.md
%license LICENSE

%changelog

