#
# spec file for package zoo
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           zoo
Version:        2.10
Release:        0
Summary:        Pack Program
License:        SUSE-Public-Domain
Group:          Productivity/Archiving/Compression
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
%setup -q -n zoo
%patch0
%patch1
%patch2
%patch3
%patch4
%patch5
%patch6
%patch7
%patch8

%build
make %{?_smp_mflags} linux OPTIM="%{optflags}"

%install
install -Dpm 0755 zoo \
  %{buildroot}%{_prefix}/bin/zoo
install -Dpm 0755 fiz \
  %{buildroot}%{_prefix}/bin/fiz
install -Dpm 0644 zoo.1 \
  %{buildroot}/%{_mandir}/man1/zoo.1
install -Dpm 0644 fiz.1 \
  %{buildroot}/%{_mandir}/man1/fiz.1

%files
%defattr(-,root,root)
%doc Copyright
%{_bindir}/fiz
%{_bindir}/zoo
%{_mandir}/man1/fiz.1%{ext_man}
%{_mandir}/man1/zoo.1%{ext_man}

%changelog
