#
# spec file for package optipng
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           optipng
Version:        0.7.7
Release:        0
Summary:        A PNG File Compressor
License:        Zlib
Group:          Productivity/Archiving/Compression
Url:            http://optipng.sourceforge.net/
Source0:        http://downloads.sourceforge.net/project/optipng/OptiPNG/optipng-%{version}/optipng-%{version}.tar.gz
Source1:        macros.optipng
BuildRequires:  libpng-devel
BuildRequires:  zlib-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
OptiPNG is a PNG optimizer that recompresses image files to a smaller
size, without losing any information. This program also converts
external formats (BMP, GIF, PNM; TIFF support is coming up) to
optimized PNG, and performs PNG integrity checks and corrections.

%prep
%setup -q

%build
# not autotools generated configure
export CFLAGS="%{optflags}"
./configure \
	-with-system-zlib \
	-with-system-libpng \
	-prefix=%{_prefix} \
	-mandir=%{_mandir}

#don't strip binaries
sed -i "s:\(LDFLAGS = \)-s:\1:" src/optipng/Makefile
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
install -D -m644 %{SOURCE1} %{buildroot}%{_sysconfdir}/rpm/macros.optipng

%check
make %{?_smp_mflags} check

%files
%defattr(-,root,root)
%doc README.txt doc
%{_bindir}/optipng
%{_mandir}/man1/optipng.1.gz
%config %{_sysconfdir}/rpm/macros.optipng

%changelog
