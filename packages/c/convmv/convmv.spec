#
# spec file for package convmv
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


Name:           convmv
Version:        2.05
Release:        0
Summary:        Utility to convert file names between encodings
License:        GPL-2.0-or-later
Group:          Productivity/File utilities
Url:            http://j3e.de/linux/convmv/
Source:         http://j3e.de/linux/convmv/%{name}-%{version}.tar.gz
BuildArch:      noarch

%description
convmv is meant to convert the filenames in a directory tree or a
whole file system into a different encoding, with support for
symlinks.

This is useful for converting from old 8-bit locales to UTF-8. It is
also possible to convert directories to UTF-8 that are already partly
UTF-8 encoded.

convmv can convert names to both the NFC and NFD normalization forms.
NFC is commonly used on Linux and (most?) other Unix-like OSes,
though it does not enforce it. Darwin, the base of Macintosh OS X,
enforces Normalization Form Canonical Decomposition (NFD).

%prep
%setup -q
tar -xf testsuite.tar

%build
make %{?_smp_mflags} PREFIX=%{_prefix}

%install
mkdir -p %{buildroot}%{_bindir} %{buildroot}%{_mandir}/man1
%make_install PREFIX=%{_prefix}

%check
make %{?_smp_mflags} test

%files
%doc GPL2 Changes CREDITS TODO VERSION
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{ext_man}

%changelog
