#
# spec file for package zoo
#
# Copyright (c) 2020 SUSE LLC
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


Name:           zoo
Version:        2.10
Release:        0
Summary:        Pack Program
License:        SUSE-Public-Domain
Group:          Productivity/Archiving/Compression
URL:            https://en.wikipedia.org/wiki/Zoo_(file_format)
Source:         zoo.tar.gz
Patch0:         zoo.patch
Patch1:         zoo-%{version}-tempfile.patch
Patch2:         zoo-gcc.patch
Patch3:         zoo-%{version}-CAN-2005-2349.patch
Patch4:         zoo-return.patch
Patch5:         zoo-security_pathsize.patch
Patch6:         zoo-security_parse.patch
Patch7:         zoo-%{version}-security-infinite_loop.patch
Patch8:         zoo-fclose.patch

%description
Zoo is a packer based on the Lempel-Ziv algorithm. Lots of files on
DOS/AmigaDOS and TOS systems used this packer for their archives. The
compression rate of gzip is not reached, and thus zoo should only be used
for decompressing old archives.

%prep
%autosetup -n zoo -p0

%build
%make_build linux OPTIM="%{optflags}"

%install
install -Dpm 0755 zoo \
  %{buildroot}%{_bindir}/zoo
install -Dpm 0755 fiz \
  %{buildroot}%{_bindir}/fiz
install -Dpm 0644 zoo.1 \
  %{buildroot}/%{_mandir}/man1/zoo.1
install -Dpm 0644 fiz.1 \
  %{buildroot}/%{_mandir}/man1/fiz.1

%files
%license Copyright
%{_bindir}/fiz
%{_bindir}/zoo
%{_mandir}/man1/fiz.1%{?ext_man}
%{_mandir}/man1/zoo.1%{?ext_man}

%changelog
