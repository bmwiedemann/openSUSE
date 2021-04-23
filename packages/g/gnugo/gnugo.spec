#
# spec file for package gnugo
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


Name:           gnugo
Version:        1371149103.84a32e9c
Release:        0
Summary:        Chinese Board Game "Go"
License:        GPL-3.0-or-later
Group:          Amusements/Games/Board/Other
URL:            https://savannah.gnu.org/projects/gnugo
Source:         %{name}-%{version}.tar.xz
Source1:        suse-start-gnugo.el
Source2:        xemacs-auto-autoloads.el
Patch:          xemacs.patch
Patch1:         mouse-2-dont-insert-junk.patch
BuildRequires:  emacs-x11
BuildRequires:  fdupes
BuildRequires:  ncurses-devel
BuildRequires:  xemacs
BuildRequires:  xz
Requires(pre):	info
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Chinese ancient board game.

%prep
%setup -q
%patch -p1
%patch1 -p1

%build
export CFLAGS="%{optflags} -fcommon"
export CXXFLAGS="%{optflags} -fcommon"
%configure --prefix=%{_prefix}
make %{?_smp_mflags}
pushd  interface/xpms
    emacs -batch --no-site-file \
    -l ../make-xpms-file.el -f make-xpms-file gnugo-xpms.el *.xpm
popd

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
rm -f %{buildroot}%{_infodir}/dir*
# GNU Emacs:
mkdir -p %{buildroot}%{_datadir}/emacs/site-lisp/gnugo
for i in $(find . -name "*.el")
do
    emacs -no-site-file -q -batch -f batch-byte-compile $i
    install -m 644 ${i} ${i}c \
                   %{buildroot}%{_datadir}/emacs/site-lisp/gnugo
done
install -m 644 %{SOURCE1} \
	%{buildroot}%{_datadir}/emacs/site-lisp
# XEmacs:
find . -name "*.elc" | xargs rm
mkdir -p %{buildroot}%{_datadir}/xemacs/site-packages/lisp/gnugo
for i in $(find . -name "*.el")
do
    xemacs -no-site-file -q -batch -f batch-byte-compile $i
    install -m 644 ${i} ${i}c \
            %{buildroot}%{_datadir}/xemacs/site-packages/lisp/gnugo
done
install -m 644 %{SOURCE2} \
	%{buildroot}%{_datadir}/xemacs/site-packages/lisp/gnugo/auto-autoloads.el

%fdupes %{buildroot}%{_prefix}/share

%post
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%postun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%files
%defattr(-,root,root)
%doc AUTHORS THANKS ChangeLog TODO README NEWS
%license COPYING
%{_bindir}/%{name}
%{_infodir}/gnugo.info*.gz
%{_mandir}/man6/gnugo.6.gz
%dir %{_datadir}/emacs/site-lisp/gnugo/
%{_datadir}/emacs/site-lisp/gnugo/*
%{_datadir}/emacs/site-lisp/suse-start-gnugo.el
%dir %{_datadir}/xemacs/site-packages/
%dir %{_datadir}/xemacs/site-packages/lisp/
%dir %{_datadir}/xemacs/site-packages/lisp/gnugo/
%{_datadir}/xemacs/site-packages/lisp/gnugo/*

%changelog
