#
# spec file for package emacs-vterm
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2023 Björn Bidar
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


%global _name    vterm
%global _upstream_name emacs-libvterm

Name:           emacs-%{_name}
Version:        708.99c1f5e
Release:        0
Summary:        An experimental module for libvterm bindings to Emacs
License:        GPL-3.0-or-later
Group:          Productivity/Text/Editors
URL:            https://github.com/akermu/emacs-libvterm
Source0:        %{_upstream_name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  emacs-devel
BuildRequires:  emacs-nox
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(vterm)
Requires:       emacs
Supplements:    emacs

%description
Emacs-libvterm (vterm) is fully-fledged terminal emulator inside GNU Emacs based on libvterm, a C library. As a result of using compiled code (instead of elisp), emacs-libvterm is fully capable, fast, and it can seamlessly handle large outputs.

%prep
%autosetup -p1 -n %{_upstream_name}-%{version}

%build
%cmake \
       -DUSE_SYSTEM_LIBVTERM=ON

%cmake_build

cd ..

emacs -batch -f batch-byte-compile *.el

%install
install -d %{buildroot}/%{_emacs_sitelispdir}/
install -D -m644 %{_name}.el %{_name}.elc %{buildroot}/%{_emacs_sitelispdir}/
install -D -m755 %{_name}-module.so %{buildroot}/%{_libdir}/emacs/site-lisp/%{_name}-module.so

install -dm755 %{buildroot}/%{_emacs_sitestartdir}/
cat << EOF > %{buildroot}/%{_emacs_sitestartdir}/%{_name}-init.el
(add-to-list 'load-path "%{_libdir}/emacs/site-lisp")
EOF

install -d %{buildroot}/%{_emacs_etcdir}/vterm
install -Dm644 etc/* %{buildroot}/%{_emacs_etcdir}/vterm

%files
%doc README.md
%license LICENSE
%{_emacs_sitelispdir}/%{_name}.el*
%{_emacs_sitestartdir}/%{_name}-init.el
%dir %{_libdir}/emacs
%dir %{_emacs_archsitelispdir}
%{_emacs_archsitelispdir}/%{_name}-module.so
%dir %{_emacs_etcdir}
%dir %{_emacs_etcdir}/vterm
%{_emacs_etcdir}/vterm/emacs-vterm-bash.sh
%{_emacs_etcdir}/vterm/emacs-vterm-zsh.sh
%{_emacs_etcdir}/vterm/emacs-vterm.fish

%changelog
