#
# spec file for package upx
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           upx
Version:        3.95
Release:        0
Summary:        The Ultimate Packer for eXecutables
License:        GPL-2.0-or-later
Group:          Development/Tools/Other
URL:            https://upx.github.io/
Source:         https://github.com/upx/upx/releases/download/v%{version}/upx-%{version}-src.tar.xz
Patch0:         upx-aarch64.patch
Patch1:         upx-endiantests.patch
BuildRequires:  gcc-c++
BuildRequires:  libucl1-devel
BuildRequires:  zlib-devel

%description
UPX is a compressor for several different executable formats.
Programs receive a stub that makes them self-runnable. When run,
decompression either happens in memory in-place if possible, or to a
temporary file, the latter of which does not support setuid programs,
or the proper name in argv[0].

%prep
%setup -q -n %{name}-%{version}-src
%patch0 -p1
%patch1 -p1

# BSD-4-Clause licensed file, remove just in case bnc#753791
rm src/stub/src/i386-dos32.djgpp2-stubify.asm

%build
make %{?_smp_mflags} -C src CXXFLAGS_OPTIMIZE="%{optflags}"
make %{?_smp_mflags} -C doc

%install
install -D -m 0755 src/upx.out %{buildroot}%{_bindir}/upx
install -D -m 0644 doc/upx.1 %{buildroot}%{_mandir}/man1/upx.1

%files
%license COPYING LICENSE
%doc BUGS NEWS PROJECTS README README.SRC THANKS
%doc doc/upx.html
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
