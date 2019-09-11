#
# spec file for package universal-ctags
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


Name:           universal-ctags
Version:        0+git~c77db554
Release:        0
Summary:        A program to generate language tag files used with various editors
License:        GPL-2.0-only
Group:          Development/Tools/Navigators
URL:            https://github.com/universal-ctags/ctags
Source:         ctags-%{version}.tar.xz
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
BuildRequires:  update-alternatives
Requires(pre):  update-alternatives
Requires(post): update-alternatives

%description
Universal ctags, a maintained fork from Darren Hieberts project, generates tag
files from source code for various languages to be used with Editors like
Emacs, Vim and several others.

%prep
%setup -q -n ctags-%{version}
%patch1 -p1

%build
echo '#define CTAGS_REPOINFO "%{version}"' > main/repoinfo.h
./autogen.sh

%configure
make %{?_smp_mflags}
make -C man %{?_smp_mflags}

%install
install -D -m 755 ctags %{buildroot}/%{_bindir}/universal-ctags
install -D -m 644 man/ctags.1 %{buildroot}/%{_mandir}/man1/universal-ctags.1
install -D -m 644 man/ctags-incompatibilities.7 %{buildroot}/%{_mandir}/man7/universal-ctags-incompatibilities.7
install -D -m 644 man/ctags-optlib.7 %{buildroot}/%{_mandir}/man7/universal-ctags-optlib.7
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
ln -s ctags %{buildroot}%{_bindir}/ctags
ln -s ctags.1%{ext_man} %{buildroot}%{_mandir}/man1/ctags.1%{ext_man}
ln -s ctags %{buildroot}%{_sysconfdir}/alternatives/ctags
ln -s ctags.1%{ext_man} %{buildroot}%{_sysconfdir}/alternatives/ctags.1%{ext_man}

%post
test -L %{_bindir}/ctags || rm -f %{_bindir}/ctags
update-alternatives --install  %{_bindir}/ctags ctags %{_bindir}/universal-ctags 20 \
  --slave %{_mandir}/man1/ctags.1.gz ctags.1 %{_mandir}/man1/universal-ctags.1.gz
update-alternatives --auto ctags

%preun
if [ $1 -eq 0 ]; then
  update-alternatives --remove ctags %{_bindir}/universal-ctags
fi

%files
%license COPYING
%{_bindir}/universal-ctags
%{_mandir}/man1/universal-ctags.1%{?ext_man}
%{_mandir}/man7/universal-ctags-incompatibilities.7%{?ext_man}
%{_mandir}/man7/universal-ctags-optlib.7%{?ext_man}
%ghost %{_bindir}/ctags
%ghost %{_mandir}/man1/ctags.1%{?ext_man}
%ghost %{_sysconfdir}/alternatives/ctags
%ghost %{_sysconfdir}/alternatives/ctags.1%{?ext_man}

%changelog
