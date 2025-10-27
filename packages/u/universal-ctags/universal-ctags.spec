#
# spec file for package universal-ctags
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif
Name:           universal-ctags
Version:        6.2.0
Release:        0
Summary:        A program to generate language tag files used with various editors
License:        GPL-2.0-only
URL:            https://github.com/universal-ctags/ctags
Source:         https://github.com/universal-ctags/ctags/releases/download/v%{version}/universal-ctags-%{version}.tar.gz
%if %{with libalternatives}
BuildRequires:  alts
Requires(pre):  alts
Requires(post): alts
%else
BuildRequires:  update-alternatives
Requires(pre):  update-alternatives
Requires(post): update-alternatives
%endif
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gzip
BuildRequires:  make
BuildRequires:  pcre2-devel
BuildRequires:  pkgconfig
BuildRequires:  python3-Pygments
BuildRequires:  python3-docutils
BuildRequires:  texlive-fancyvrb
BuildRequires:  texlive-latex-bin-bin
BuildRequires:  pkgconfig(jansson)
BuildRequires:  pkgconfig(libseccomp)
BuildRequires:  pkgconfig(yaml-0.1)

%description
Universal ctags, a maintained fork from Darren Hieberts project, generates tag
files from source code for various languages to be used with Editors like
Emacs, Vim and several others.

%prep
%autosetup -p1

%build
echo '#define CTAGS_REPOINFO "%{version}"' > main/repoinfo.h
autoreconf -fiv

%configure
%make_build
%make_build -C man

%install
install -D -m 755 ctags %{buildroot}/%{_bindir}/universal-ctags
install -D -m 644 man/ctags.1 %{buildroot}/%{_mandir}/man1/universal-ctags.1
install -D -m 644 man/ctags-incompatibilities.7 %{buildroot}/%{_mandir}/man7/universal-ctags-incompatibilities.7
install -D -m 644 man/ctags-optlib.7 %{buildroot}/%{_mandir}/man7/universal-ctags-optlib.7

%if %{with libalternatives}
mkdir -p %{buildroot}%{_datadir}/libalternatives/ctags
ln -sf %{_bindir}/alts %{buildroot}%{_bindir}/ctags
cat > %{buildroot}%{_datadir}/libalternatives/ctags/25.conf <<-EOF
	binary=%{_bindir}/universal-ctags
	man=universal-ctags.1
	group=ctags
	EOF
%else
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
ln -s %{_sysconfdir}/alternatives/ctags %{buildroot}%{_bindir}/ctags
ln -s %{_sysconfdir}/alternatives/ctags.1%{?ext_man}  %{buildroot}%{_mandir}/man1/ctags.1%{?ext_man}
%endif

%if ! %{with libalternatives}
%post
test -L %{_bindir}/ctags || rm -f %{_bindir}/ctags
update-alternatives --install  %{_bindir}/ctags ctags %{_bindir}/universal-ctags 25 \
  --slave %{_mandir}/man1/ctags.1.gz ctags.1 %{_mandir}/man1/universal-ctags.1.gz

%postun
if [ ! -f %{_bindir}/ctags ] ; then
   update-alternatives --remove ctags %{_bindir}/universal-ctags
fi
%endif

%files
%license COPYING
%{_bindir}/ctags
%{_bindir}/universal-ctags
%{_mandir}/man1/universal-ctags.1%{?ext_man}
%{_mandir}/man7/universal-ctags-incompatibilities.7%{?ext_man}
%{_mandir}/man7/universal-ctags-optlib.7%{?ext_man}
%if %{with libalternatives}
%dir %{_datadir}/libalternatives/
%dir %{_datadir}/libalternatives/ctags/
%{_datadir}/libalternatives/ctags/25.conf
%else
%{_mandir}/man1/ctags.1%{ext_man}
%ghost %{_sysconfdir}/alternatives/ctags
%ghost %{_sysconfdir}/alternatives/ctags.1%{?ext_man}
%endif

%changelog
