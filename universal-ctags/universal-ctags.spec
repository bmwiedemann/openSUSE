#
# spec file for package universal-ctags
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


Name:           universal-ctags
Version:        0+git~befcb88
Release:        0
Summary:        A program to generate language tag files used with various editors
License:        GPL-2.0-only
Group:          Development/Tools/Navigators
URL:            https://github.com/universal-ctags/ctags
Source:         universal-ctags.tar.gz
Patch1:         0001-Use-pandoc-instead-of-rst2pdf.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gzip
BuildRequires:  make
BuildRequires:  pandoc
BuildRequires:  pkgconfig
BuildRequires:  python3-Pygments
BuildRequires:  python3-docutils
BuildRequires:  texlive-fancyvrb
BuildRequires:  texlive-latex-bin-bin

%description
Universal ctags, a maintained fork from Darren Hieberts project, generates tag
files from source code for various languages to be used with Editors like
Emacs, Vim and several others.

%prep
%setup -q -n ctags-master
%patch1 -p1

%build
./autogen.sh

%configure
make %{?_smp_mflags}
make -C man %{?_smp_mflags}

%install
install -D -m 755 ctags %{buildroot}/%{_bindir}/universal-ctags
install -D -m 644 man/ctags.1 %{buildroot}/%{_mandir}/man1/universal-ctags.1
install -D -m 644 man/ctags-incompatibilities.7 %{buildroot}/%{_mandir}/man7/universal-ctags-incompatibilities.7
install -D -m 644 man/ctags-optlib.7 %{buildroot}/%{_mandir}/man7/universal-ctags-optlib.7

%files
%license COPYING
%{_bindir}/universal-ctags
%{_mandir}/man1/universal-ctags.1%{?ext_man}
%{_mandir}/man7/universal-ctags-incompatibilities.7%{?ext_man}
%{_mandir}/man7/universal-ctags-optlib.7%{?ext_man}

%changelog
