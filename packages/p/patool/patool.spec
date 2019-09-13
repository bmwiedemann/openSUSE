# vim: set ts=4 sw=4 et:
#
# spec file for package patool
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2012 Pascal Bleser <pascal.bleser@opensuse.org>
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


Name:           patool
Version:        1.12
Release:        0
Summary:        Portable Command Line Archive File Manager
License:        GPL-3.0+
Group:          Productivity/Archiving/Compression
URL:            https://github.com/wummel/patool
Source:         https://github.com/wummel/patool/archive/upstream/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  bash-completion
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildArch:      noarch

%description
patool is a portable command line archive file manager. Various archive types
can be created, extracted, tested and listed by patool.
The advantage of patool is its simplicity in handling archive files without
having to remember a myriad of programs and options.
The archive format is determined by the file(1) program and as a fallback by
the archive file extension.

patool supports 7z (.7z), ACE (.ace), ALZIP (.alz), AR (.a), ARC (.arc), ARJ
(.arj), BZIP2 (.bz2), CAB (.cab), compress (.Z), CPIO (.cpio), DEB (.deb), GZIP
(.gz), LRZIP (.lrz), LZH (.lha, .lzh), LZIP (.lz), LZMA (.lzma), LZOP (.lzo),
RPM (.rpm), RAR (.rar), TAR (.tar), XZ (.xz), and ZIP (.zip, .jar) formats.

It relies on helper applications to handle those archive formats.

%package bash-completion
Summary:        Bash Completion for patool
Group:          Productivity/Archiving/Compression
Requires:       bash-completion
Supplements:    packageand(bash:patool)

%description bash-completion
This package contains bash completion for patool, a portable command line
archive file manager.

%prep
%setup -q -n patool-upstream-%{version}

%build
%python3_build

%install
%python3_install
%fdupes %{buildroot}
install -Dpm 0644 patool.bash-completion \
  %{buildroot}%{_datadir}/bash-completion/completions/%{name}

%files
%doc COPYING doc/*.txt
%{_bindir}/patool
%{python3_sitelib}/*
%{_mandir}/man1/patool.1%{ext_man}

%files bash-completion
%{_datadir}/bash-completion/completions/%{name}

%changelog
