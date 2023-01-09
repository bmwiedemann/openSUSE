#
# spec file for package trinity
#
# Copyright (c) 2023 SUSE LLC
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


Name:           trinity
Version:        1.9+git.20230108
Release:        0
Summary:        A Linux System call fuzz tester
License:        GPL-2.0-only
URL:            https://github.com/kernelslacker/trinity
Source0:        %{name}-%{version}.tar.gz

%description
The basic idea is fairly simple. As 'fuzz testing' suggests, we call syscalls
at random, with random arguments.  Not an original idea, and one that has been
done many times before on Linux, and on other operating systems.  Where
Trinity differs is that the arguments it passes are not purely random.

%prep
%autosetup

%build
export CFLAGS="%{optflags}"
# Not autotools configure
./configure
# disable -Werror by setting DEVEL to 0
%make_build DEVEL=0

%install
%make_install DESTDIR=%{buildroot}%{_prefix}
install -Dpm 0644 trinity.1 \
  %{buildroot}%{_mandir}/man1/trinity.1

%files
%license COPYING
%doc README
%{_bindir}/trinity
%{_mandir}/man1/trinity.1%{?ext_man}

%changelog
