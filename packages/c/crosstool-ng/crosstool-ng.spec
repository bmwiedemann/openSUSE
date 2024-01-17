#
# spec file for package crosstool-ng
#
# Copyright (c) 2022 SUSE LLC
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


Name:           crosstool-ng
Version:        1.25.0
Release:        0
Summary:        Toolchain building framework
License:        GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-or-later AND LGPL-2.1-only AND LGPL-3.0-or-later
Group:          Development/Tools/Building
URL:            http://crosstool-ng.org
Source0:        http://crosstool-ng.org/download/crosstool-ng/%{name}-%{version}.tar.xz
Source1:        http://crosstool-ng.org/download/crosstool-ng/%{name}-%{version}.tar.xz.sig
# Alexey Neyman's public key. See http://crosstool-ng.github.io/docs/install/.
Source98:       %{name}.keyring
Source99:       %{name}.rpmlintrc
BuildRequires:  bison
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  gperf
BuildRequires:  help2man
BuildRequires:  libtool
BuildRequires:  makeinfo
BuildRequires:  ncurses-devel
BuildRequires:  unzip
BuildRequires:  wget
Requires:       bzip2
Requires:       gcc
Requires:       gcc-c++
Requires:       glibc-devel-static
Requires:       gzip
Requires:       m4
Requires:       wget
Requires:       xz

%description
crosstool-NG aims at building toolchains. Toolchains are an essential component
in a software development project. It will compile, assemble and link the code
that is being developed. Some pieces of the toolchain will eventually end up
in the resulting binary/ies: static libraries are but an example.

%prep
%setup -q

%build
%configure \
    --docdir=%{_docdir}/%{name}
make %{?_smp_mflags}

%install
%make_install
%fdupes %{buildroot}%{_datadir}/%{name}
# from legal team
# "Distribution and use is free, also for commercial purposes" (no modification permission)
find %{buildroot} -name '*-new-valencian-locale.patch' -type f -delete -print

%files
%license COPYING
%{_bindir}/ct-ng
%{_datadir}/%{name}
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions/
%{_datadir}/bash-completion/completions/ct-ng
%{_docdir}/%{name}
%{_libexecdir}/%{name}
%{_mandir}/man1/ct-ng.1.gz

%changelog
